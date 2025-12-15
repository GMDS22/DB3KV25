"""
Manages user-created behavior presets for the auto-turret system.
Works alongside turret_presets.py which contains factory presets.
"""
import os
import json
import time
from pathlib import Path

PRESETS_FILE = "behavior_presets.json"

class BehaviorPresets:
    def __init__(self, settings_dir=None):
        self.settings_dir = settings_dir or os.path.dirname(os.path.abspath(__file__))
        self.presets_path = os.path.join(self.settings_dir, PRESETS_FILE)
        self._presets = {}
        self.load_presets()

    def load_presets(self):
        """Load saved presets from JSON file."""
        try:
            if os.path.exists(self.presets_path):
                with open(self.presets_path, 'r') as f:
                    self._presets = json.load(f)
        except Exception as e:
            print(f"Error loading behavior presets: {e}")
            self._presets = {}

    def save_presets(self):
        """Save presets to JSON file."""
        try:
            with open(self.presets_path, 'w') as f:
                json.dump(self._presets, f, indent=4)
        except Exception as e:
            print(f"Error saving behavior presets: {e}")

    def add_preset(self, name: str, settings: dict) -> bool:
        """Add or update a preset with the given name and settings."""
        try:
            clean_name = name.strip()
            if not clean_name:
                return False

            settings['created_at'] = time.time()
            settings['last_modified'] = time.time()
            self._presets[clean_name] = settings
            self.save_presets()
            return True
        except Exception:
            return False

    def delete_preset(self, name: str) -> bool:
        """Delete a preset by name."""
        try:
            if name in self._presets:
                del self._presets[name]
                self.save_presets()
                return True
        except Exception:
            pass
        return False

    def get_preset(self, name: str) -> dict:
        """Get a preset's settings by name."""
        return self._presets.get(name, {})

    def list_presets(self) -> list[str]:
        """Get a sorted list of preset names."""
        try:
            return sorted(self._presets.keys())
        except Exception:
            return []

    def get_all_presets(self) -> dict:
        """Get the full presets dictionary."""
        return dict(self._presets)  # Return a copy