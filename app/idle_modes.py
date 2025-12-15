"""
idle_modes.py
=============
Idle mode implementations for the Auto Turret system.

Supported Modes:
1. Rest Mode - System stays at current position
2. Guard Mode - Automated patrol between preset positions (up to 8)
3. Watch Mode - Sweep between two positions
4. Search Mode - Random movement within defined area

Each mode has configurable settings and can be enabled/disabled independently.
"""

import json
import random
import time
from pathlib import Path
from typing import List, Tuple, Dict, Any


class IdleModes:
    """Manages idle mode configurations and state."""
    
    MODES = {
        'rest': 'Rest Mode',
        'guard': 'Guard Mode',
        'watch': 'Watch Mode',
        'search': 'Search Mode'
    }
    
    def __init__(self, config_file: str = None):
        """Initialize idle modes with configuration file."""
        self.config_file = config_file or str(Path(__file__).parent / "idle_modes_config.json")
        self.active_mode = None
        self.config = self._load_config()
        self.guard_current_point = 0
        self.watch_direction = 1  # 1 for right, -1 for left
        self.search_last_position = (90, 40)
        
    def _load_config(self) -> Dict:
        """Load configuration from file or return defaults."""
        try:
            if Path(self.config_file).exists():
                with open(self.config_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
        
        return self._default_config()
    
    def _default_config(self) -> Dict:
        """Return default idle modes configuration."""
        return {
            'rest': {
                'enabled': False,
                'hold_position': True,
                'position_memory': [],  # Empty - user adds positions
            },
            'guard': {
                'enabled': False,
                'patrol_points': [
                    {'label': 'Home', 'pan': 90, 'tilt': 50},
                    {'label': 'Left', 'pan': 30, 'tilt': 50},
                    {'label': 'Right', 'pan': 150, 'tilt': 50},
                    {'label': 'Top Left', 'pan': 40, 'tilt': 25},
                    {'label': 'Top Right', 'pan': 140, 'tilt': 25},
                    {'label': 'Bottom Left', 'pan': 40, 'tilt': 75},
                    {'label': 'Bottom Right', 'pan': 140, 'tilt': 75},
                    {'label': 'Center Top', 'pan': 90, 'tilt': 25},
                ],
                'dwell_time': 5,  # seconds
                'movement_speed': 50,  # 1-100%
                'random_order': False,
            },
            'watch': {
                'enabled': False,
                'left_limit': 45,
                'right_limit': 135,
                'sweep_speed': 50,  # 1-100%
                'pause_time': 2,  # seconds at each end
            },
            'search': {
                'enabled': False,
                'search_area': {
                    'pan_min': 5,
                    'pan_max': 185,
                    'tilt_min': 20,
                    'tilt_max': 110,
                },
                'movement_style': 'random',  # 'random', 'spiral', 'grid'
                'speed': 50,  # Bug #7 FIX: Add speed configuration (1-100%) for search mode movement
                'speed_variation': True,
                'direction_changes': 5,  # seconds between direction changes
            }
        }
    
    def save_config(self):
        """Save current configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
    
    def set_mode(self, mode: str):
        """Set active idle mode."""
        if mode in self.MODES or mode is None:
            self.active_mode = mode
            if mode:
                print(f"[IDLE-MODE] Switched to {self.MODES.get(mode, 'Unknown')}")
            else:
                print(f"[IDLE-MODE] Mode cleared (OFF)")
            return True
        return False
    
    def get_mode(self) -> str:
        """Get currently active idle mode."""
        return self.active_mode
    
    def is_mode_enabled(self, mode: str) -> bool:
        """Check if a specific mode is enabled."""
        return self.config.get(mode, {}).get('enabled', False)
    
    def enable_mode(self, mode: str):
        """Enable a specific mode."""
        if mode in self.config:
            self.config[mode]['enabled'] = True
            self.set_mode(mode)
            self.save_config()
    
    def disable_mode(self, mode: str):
        """Disable a specific mode."""
        if mode in self.config:
            self.config[mode]['enabled'] = False
            if self.active_mode == mode:
                self.active_mode = None
            self.save_config()
    
    # ===== REST MODE =====
    def get_rest_config(self) -> Dict:
        """Get rest mode configuration."""
        return self.config.get('rest', {})
    
    def set_rest_hold_position(self, hold: bool):
        """Set rest mode position lock."""
        self.config['rest']['hold_position'] = hold
        self.save_config()
    
    def rest_save_position(self, pan: int, tilt: int, label: str = None):
        """Save current position to rest mode memory."""
        memory = self.config['rest']['position_memory']
        if len(memory) < 8:  # Limit to 8 saved positions
            memory.append({
                'label': label or f"Position {len(memory) + 1}",
                'pan': pan,
                'tilt': tilt
            })
            self.save_config()
            return True
        return False
    
    def rest_get_positions(self) -> List[Dict]:
        """Get all saved rest positions."""
        return self.config['rest']['position_memory']
    
    def rest_clear_positions(self):
        """Clear all saved rest positions."""
        self.config['rest']['position_memory'] = []
        self.save_config()
    
    # ===== GUARD MODE =====
    def get_guard_config(self) -> Dict:
        """Get guard mode configuration."""
        return self.config.get('guard', {})
    
    def guard_add_point(self, pan: int, tilt: int, label: str = None) -> bool:
        """Add patrol point to guard mode."""
        points = self.config['guard']['patrol_points']
        if len(points) < 8:  # Max 8 points
            points.append({
                'label': label or f"Point {len(points) + 1}",
                'pan': pan,
                'tilt': tilt
            })
            self.save_config()
            return True
        return False
    
    def guard_remove_point(self, index: int) -> bool:
        """Remove patrol point from guard mode."""
        points = self.config['guard']['patrol_points']
        if 0 <= index < len(points):
            points.pop(index)
            self.guard_current_point = min(self.guard_current_point, len(points) - 1)
            self.save_config()
            return True
        return False
    
    def guard_get_points(self) -> List[Dict]:
        """Get all guard mode patrol points."""
        return self.config['guard']['patrol_points']
    
    def guard_get_next_point(self) -> Tuple[int, int]:
        """Get next patrol point for guard mode."""
        points = self.config['guard']['patrol_points']
        if not points:
            return (90, 40)
        
        if self.config['guard']['random_order']:
            idx = random.randint(0, len(points) - 1)
        else:
            idx = self.guard_current_point
            self.guard_current_point = (idx + 1) % len(points)
        
        point = points[idx]
        return (point['pan'], point['tilt'])
    
    def guard_set_dwell_time(self, seconds: int):
        """Set dwell time for guard mode."""
        self.config['guard']['dwell_time'] = max(1, min(60, seconds))
        self.save_config()
    
    def guard_set_movement_speed(self, speed: int):
        """Set movement speed for guard mode (1-100%)."""
        self.config['guard']['movement_speed'] = max(1, min(100, speed))
        self.save_config()
    
    def guard_set_random_order(self, random: bool):
        """Enable/disable random order for guard patrol."""
        self.config['guard']['random_order'] = random
        self.save_config()
    
    # ===== WATCH MODE =====
    def get_watch_config(self) -> Dict:
        """Get watch mode configuration."""
        return self.config.get('watch', {})
    
    def watch_set_limits(self, left: int, right: int):
        """Set sweep limits for watch mode."""
        self.config['watch']['left_limit'] = max(5, min(180, left))
        self.config['watch']['right_limit'] = max(5, min(180, right))
        self.save_config()
    
    def watch_set_sweep_speed(self, speed: int):
        """Set sweep speed for watch mode (1-100%)."""
        self.config['watch']['sweep_speed'] = max(1, min(100, speed))
        self.save_config()
    
    def watch_set_pause_time(self, seconds: int):
        """Set pause time at each end of sweep."""
        self.config['watch']['pause_time'] = max(1, min(10, seconds))
        self.save_config()
    
    def watch_get_next_position(self, current_pan: int) -> int:
        """Get next pan position for watch mode sweep."""
        left = self.config['watch']['left_limit']
        right = self.config['watch']['right_limit']
        
        # Determine direction
        if current_pan <= left:
            self.watch_direction = 1
        elif current_pan >= right:
            self.watch_direction = -1
        
        if self.watch_direction == 1:
            return right
        else:
            return left
    
    # ===== SEARCH MODE =====
    def get_search_config(self) -> Dict:
        """Get search mode configuration."""
        return self.config.get('search', {})
    
    def search_set_area(self, pan_min: int, pan_max: int, tilt_min: int, tilt_max: int):
        """Set search area boundaries."""
        area = self.config['search']['search_area']
        area['pan_min'] = max(5, min(185, pan_min))
        area['pan_max'] = max(5, min(185, pan_max))
        area['tilt_min'] = max(18, min(110, tilt_min))
        area['tilt_max'] = max(18, min(110, tilt_max))
        self.save_config()
    
    def search_set_movement_style(self, style: str):
        """Set search movement style (random, spiral, grid)."""
        if style in ['random', 'spiral', 'grid']:
            self.config['search']['movement_style'] = style
            self.save_config()
    
    def search_set_speed_variation(self, enabled: bool):
        """Enable/disable speed variation in search mode."""
        self.config['search']['speed_variation'] = enabled
        self.save_config()
    
    def search_get_next_position(self) -> Tuple[int, int]:
        """Get next random position for search mode."""
        area = self.config['search']['search_area']
        pan = random.randint(area['pan_min'], area['pan_max'])
        tilt = random.randint(area['tilt_min'], area['tilt_max'])
        self.search_last_position = (pan, tilt)
        return (pan, tilt)
    
    def get_search_speed(self) -> int:
        """Get movement speed for search mode with optional variation."""
        base_speed = self.config['search'].get('speed', 50)
        if self.config['search']['speed_variation']:
            return base_speed + random.randint(-20, 20)
        return base_speed
    
    def search_get_speed(self) -> int:
        """Alias for get_search_speed() - returns search mode movement speed."""
        return self.get_search_speed()
    
    # ===== IDLE DISENGAGEMENT PROTOCOL =====
    def disengage_immediately(self):
        """
        STANDARD PROTOCOL: Immediately stop idle mode and clear all state.
        
        This is called when:
        1. A target is detected during idle mode
        2. User manually disables idle mode
        3. User enables tracking/aiming during idle mode
        
        Effect: All idle mode state is cleared, resuming normal tracking.
        """
        # Clear all idle state variables
        self.active_mode = None
        self.guard_current_point = 0
        self.watch_direction = 1
        self.search_last_position = (90, 40)
        
        return True
    
    def is_idle_mode_active(self) -> bool:
        """Check if any idle mode is currently active."""
        return self.active_mode is not None


# Example usage / testing
if __name__ == "__main__":
    idle = IdleModes()
    
    # Test REST mode
    print("\n=== REST MODE ===")
    idle.rest_save_position(90, 40, "Center")
    idle.rest_save_position(45, 50, "Left")
    print("Saved positions:", idle.rest_get_positions())
    
    # Test GUARD mode
    print("\n=== GUARD MODE ===")
    idle.guard_add_point(90, 40, "Front")
    idle.guard_add_point(45, 40, "Left")
    idle.guard_add_point(135, 40, "Right")
    print("Patrol points:", idle.guard_get_points())
    print("Next point:", idle.guard_get_next_point())
    
    # Test WATCH mode
    print("\n=== WATCH MODE ===")
    idle.watch_set_limits(30, 150)
    print("Watch limits: 30-150 pan")
    print("Next position:", idle.watch_get_next_position(90))
    
    # Test SEARCH mode
    print("\n=== SEARCH MODE ===")
    idle.search_set_area(5, 185, 20, 110)
    print("Search position:", idle.search_get_next_position())
    
    # Test mode switching
    print("\n=== MODE SWITCHING ===")
    idle.enable_mode('rest')
    print("Active mode:", idle.MODES.get(idle.get_mode()))
    idle.enable_mode('guard')
    print("Active mode:", idle.MODES.get(idle.get_mode()))
