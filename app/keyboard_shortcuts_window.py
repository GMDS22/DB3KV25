"""
keyboard_shortcuts_window.py
=============================
Standalone keyboard shortcuts manager window.

This window displays all available keyboard shortcuts and provides:
- Enable/disable toggle for manual control shortcuts
- Display of all menu-accessible windows and their shortcuts
- Reference for all keyboard controls
- Visual organization by category
"""

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTabWidget, QWidget,
    QLabel, QPushButton, QCheckBox, QScrollArea, QGroupBox,
    QGridLayout, QMessageBox
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
import json
import os


class KeyboardShortcutsWindow(QDialog):
    """Window for viewing and managing keyboard shortcuts."""
    
    shortcuts_changed = pyqtSignal(dict)  # Emits config when settings change
    
    def __init__(self, parent=None, main_app=None):
        super().__init__(parent)
        self.main_app = main_app
        self.setWindowTitle("⌨️ Keyboard Shortcuts Manager")
        self.setGeometry(150, 150, 900, 700)
        self.setMinimumSize(700, 500)
        
        # Styling
        self.setStyleSheet("""
            QDialog { background-color: #1e1e1e; color: #ffffff; }
            QLabel { color: #ffffff; }
            QPushButton { 
                background-color: #00aa00; 
                color: #000000; 
                font-weight: bold; 
                padding: 5px;
                border-radius: 3px;
            }
            QPushButton:hover { background-color: #00dd00; }
            QPushButton:pressed { background-color: #007700; }
            QCheckBox { color: #00ff00; }
            QGroupBox { 
                color: #00ff00; 
                border: 1px solid #00ff00; 
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title { 
                subcontrol-origin: margin; 
                left: 10px; 
                padding: 0 3px 0 3px; 
            }
            QTabWidget::pane { border: 1px solid #00ff00; }
            QTabBar::tab { 
                background-color: #2d2d2d; 
                color: #00ff00; 
                padding: 5px;
            }
            QTabBar::tab:selected { 
                background-color: #00aa00; 
                color: #000000;
            }
            QScrollArea { background-color: #1e1e1e; }
        """)
        
        self.load_shortcuts_config()
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        
        # Title
        title = QLabel("⌨️ Keyboard Shortcuts Manager")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet("color: #00ff00;")
        layout.addWidget(title)
        
        # Tab widget for different categories
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Create tabs
        self.manual_control_tab = self.create_manual_control_tab()
        self.menu_shortcuts_tab = self.create_menu_shortcuts_tab()
        self.special_functions_tab = self.create_special_functions_tab()
        
        self.tabs.addTab(self.manual_control_tab, "🎮 Manual Control")
        self.tabs.addTab(self.menu_shortcuts_tab, "📋 Menu & Windows")
        self.tabs.addTab(self.special_functions_tab, "⚡ Special Functions")
        
        # Bottom buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        save_btn = QPushButton("💾 Save Settings")
        save_btn.clicked.connect(self.save_shortcuts_config)
        button_layout.addWidget(save_btn)
        
        reset_btn = QPushButton("🔄 Reset to Defaults")
        reset_btn.clicked.connect(self.reset_to_defaults)
        button_layout.addWidget(reset_btn)
        
        close_btn = QPushButton("✖️ Close")
        close_btn.clicked.connect(self.close)
        button_layout.addWidget(close_btn)
        
        layout.addLayout(button_layout)
    
    def create_manual_control_tab(self) -> QWidget:
        """Create manual control shortcuts tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Enable/Disable toggle at top
        toggle_group = QGroupBox("Manual Control Status")
        toggle_layout = QVBoxLayout(toggle_group)
        
        self.manual_control_enabled = QCheckBox("Enable Manual Control Shortcuts (WASD, Arrow Keys, Space, etc.)")
        self.manual_control_enabled.setChecked(
            self.shortcuts_config.get("manual_control_enabled", True)
        )
        self.manual_control_enabled.stateChanged.connect(self.on_manual_control_toggle)
        toggle_layout.addWidget(self.manual_control_enabled)
        
        info = QLabel(
            "Disable this to prevent accidental turret movement via keyboard.\n"
            "All other shortcuts remain active."
        )
        info.setStyleSheet("color: #aaaaaa; font-size: 9px; margin-top: 5px;")
        toggle_layout.addWidget(info)
        
        layout.addWidget(toggle_group)
        
        # Shortcuts list
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        
        shortcuts = [
            ("Movement", [
                ("W or ↑", "Move Up (Pan +)"),
                ("S or ↓", "Move Down (Pan -)"),
                ("A or ←", "Move Left (Tilt +)"),
                ("D or →", "Move Right (Tilt -)"),
            ]),
            ("Actions", [
                ("Space", "Fire (when enabled)"),
                ("H", "Go to Home Position"),
                ("C", "Center on Target"),
                ("K", "Emergency Stop / Kill"),
            ]),
            ("Modes & Control", [
                ("T", "Toggle Tracking Mode"),
                ("R", "Toggle Rapid Fire"),
                ("E", "Export Rapid Fire Preset"),
            ]),
        ]
        
        for section_name, section_shortcuts in shortcuts:
            section_label = QLabel(f"<h4 style='color: #00ff00;'>{section_name}</h4>")
            scroll_layout.addWidget(section_label)
            
            for key, description in section_shortcuts:
                shortcut_layout = QHBoxLayout()
                key_label = QLabel(f"<b>{key}</b>")
                key_label.setMinimumWidth(100)
                key_label.setStyleSheet("color: #00ff00;")
                desc_label = QLabel(description)
                desc_label.setStyleSheet("color: #ffffff;")
                shortcut_layout.addWidget(key_label)
                shortcut_layout.addWidget(desc_label)
                shortcut_layout.addStretch()
                scroll_layout.addLayout(shortcut_layout)
            
            spacer = QLabel("")
            spacer.setFixedHeight(5)
            scroll_layout.addWidget(spacer)
        
        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)
        
        return widget
    
    def create_menu_shortcuts_tab(self) -> QWidget:
        """Create menu and window shortcuts tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        
        menu_items = [
            ("Main Window", [
                ("F1", "Open Help / Documentation"),
                ("F5", "Refresh Video Feed"),
                ("F11", "Toggle Fullscreen"),
                ("L", "Save Layout Preset"),
            ]),
            ("Tools & Settings", [
                ("Ctrl+Shift+I", "Open Idle Settings Window"),
                ("Ctrl+Shift+K", "Open Keyboard Shortcuts (this window)"),
                ("Ctrl+Shift+P", "Open Presets Manager"),
                ("Ctrl+Shift+L", "Open Layout Manager"),
                ("Ctrl+Shift+S", "Open Serial Console"),
            ]),
            ("Editor & Display", [
                ("Ctrl+S", "Save Current Configuration"),
                ("Ctrl+O", "Open Configuration File"),
                ("Ctrl+N", "New Configuration"),
                ("Alt+Tab", "Switch Between Windows"),
            ]),
        ]
        
        for section_name, section_shortcuts in menu_items:
            section_label = QLabel(f"<h4 style='color: #00ff00;'>{section_name}</h4>")
            scroll_layout.addWidget(section_label)
            
            for key, description in section_shortcuts:
                item_layout = QHBoxLayout()
                key_label = QLabel(f"<b>{key}</b>")
                key_label.setMinimumWidth(150)
                key_label.setStyleSheet("color: #00aaff;")
                desc_label = QLabel(description)
                desc_label.setStyleSheet("color: #ffffff;")
                item_layout.addWidget(key_label)
                item_layout.addWidget(desc_label)
                item_layout.addStretch()
                scroll_layout.addLayout(item_layout)
            
            spacer = QLabel("")
            spacer.setFixedHeight(5)
            scroll_layout.addWidget(spacer)
        
        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)
        
        return widget
    
    def create_special_functions_tab(self) -> QWidget:
        """Create special functions shortcuts tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        
        special = [
            ("Safety & Arming", [
                ("Shift+K", "Toggle Arm/Disarm System"),
                ("Shift+A", "Arm System"),
                ("Shift+D", "Disarm System"),
            ]),
            ("Detection & Tracking", [
                ("Shift+T", "Toggle Detection System"),
                ("Shift+L", "Toggle Lock-On Mode"),
                ("Shift+C", "Cycle Detection Model"),
            ]),
            ("Presets & Scenes", [
                ("1", "Load Preset 1"),
                ("2", "Load Preset 2"),
                ("3", "Load Preset 3"),
                ("Shift+P", "Save As New Preset"),
            ]),
        ]
        
        for section_name, section_shortcuts in special:
            section_label = QLabel(f"<h4 style='color: #00ff00;'>{section_name}</h4>")
            scroll_layout.addWidget(section_label)
            
            for key, description in section_shortcuts:
                item_layout = QHBoxLayout()
                key_label = QLabel(f"<b>{key}</b>")
                key_label.setMinimumWidth(150)
                key_label.setStyleSheet("color: #ffaa00;")
                desc_label = QLabel(description)
                desc_label.setStyleSheet("color: #ffffff;")
                item_layout.addWidget(key_label)
                item_layout.addWidget(desc_label)
                item_layout.addStretch()
                scroll_layout.addLayout(item_layout)
            
            spacer = QLabel("")
            spacer.setFixedHeight(5)
            scroll_layout.addWidget(spacer)
        
        # Add notes section
        notes_label = QLabel("<h4 style='color: #00ff00;'>Notes</h4>")
        scroll_layout.addWidget(notes_label)
        
        notes_text = QLabel(
            "• All shortcuts can be customized (future feature)\n"
            "• Some shortcuts may require the application window to be active\n"
            "• Manual control shortcuts can be disabled to prevent accidents\n"
            "• Emergency Stop (K) works even when manual control is disabled"
        )
        notes_text.setStyleSheet("color: #aaaaaa; font-size: 9px;")
        scroll_layout.addWidget(notes_text)
        
        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)
        
        return widget
    
    def on_manual_control_toggle(self, state):
        """Handle manual control enable/disable toggle."""
        is_enabled = state == 2  # Qt.Checked = 2
        self.shortcuts_config["manual_control_enabled"] = is_enabled
        
        status = "ENABLED" if is_enabled else "DISABLED"
        print(f"[SHORTCUTS] Manual control shortcuts {status}")
    
    def save_shortcuts_config(self):
        """Save shortcuts configuration."""
        try:
            config_file = os.path.join(
                os.path.dirname(__file__),
                "keyboard_shortcuts_config.json"
            )
            
            with open(config_file, 'w') as f:
                json.dump(self.shortcuts_config, f, indent=2)
            
            self.shortcuts_changed.emit(self.shortcuts_config)
            QMessageBox.information(self, "Saved", "Keyboard shortcuts configuration saved!")
            
            # Notify main app if available
            if self.main_app and hasattr(self.main_app, 'apply_shortcuts_config'):
                self.main_app.apply_shortcuts_config(self.shortcuts_config)
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save config: {str(e)}")
    
    def reset_to_defaults(self):
        """Reset shortcuts to default configuration."""
        reply = QMessageBox.question(
            self,
            "Reset to Defaults",
            "Reset all keyboard shortcuts to defaults?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.shortcuts_config = self.get_default_config()
            self.manual_control_enabled.setChecked(
                self.shortcuts_config.get("manual_control_enabled", True)
            )
            QMessageBox.information(self, "Reset", "Shortcuts reset to defaults!")
    
    def load_shortcuts_config(self):
        """Load shortcuts configuration from file."""
        try:
            config_file = os.path.join(
                os.path.dirname(__file__),
                "keyboard_shortcuts_config.json"
            )
            
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    self.shortcuts_config = json.load(f)
            else:
                self.shortcuts_config = self.get_default_config()
        except Exception as e:
            print(f"Could not load shortcuts config: {e}")
            self.shortcuts_config = self.get_default_config()
    
    @staticmethod
    def get_default_config() -> dict:
        """Get default shortcuts configuration."""
        return {
            "manual_control_enabled": True,
            "movement": {
                "up": ["W", "Up"],
                "down": ["S", "Down"],
                "left": ["A", "Left"],
                "right": ["D", "Right"],
            },
            "actions": {
                "fire": "Space",
                "home": "H",
                "center": "C",
                "emergency_stop": "K",
            },
            "modes": {
                "toggle_tracking": "T",
                "toggle_rapid_fire": "R",
                "export_preset": "E",
            },
            "windows": {
                "idle_settings": "Ctrl+Shift+I",
                "keyboard_shortcuts": "Ctrl+Shift+K",
                "presets_manager": "Ctrl+Shift+P",
                "layout_manager": "Ctrl+Shift+L",
                "serial_console": "Ctrl+Shift+S",
            },
        }
