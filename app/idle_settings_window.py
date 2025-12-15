"""
idle_settings_window.py
=======================
Standalone Idle Settings window for configuring all idle modes.

This is a separate window that can be opened independently to configure:
- Rest Mode settings
- Guard Mode patrol points
- Watch Mode sweep parameters
- Search Mode boundaries
"""

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTabWidget, QWidget,
    QLabel, QPushButton, QSpinBox, QDoubleSpinBox, QCheckBox,
    QListWidget, QListWidgetItem, QComboBox, QGridLayout,
    QGroupBox, QScrollArea, QMessageBox, QInputDialog
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont


class IdleSettingsWindow(QDialog):
    """Standalone window for configuring idle modes."""
    
    settings_changed = pyqtSignal(str)  # Emits mode name when settings change
    
    def __init__(self, parent=None, idle_modes=None):
        super().__init__(parent)
        self.idle_modes = idle_modes
        self.setWindowTitle("Idle Settings")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("""
            QDialog { background-color: #1e1e1e; color: #ffffff; }
            QPushButton { background-color: #00aa00; color: #000000; font-weight: bold; padding: 5px; }
            QPushButton:hover { background-color: #00dd00; }
            QPushButton:pressed { background-color: #007700; }
            QGroupBox { color: #00ff00; border: 1px solid #00ff00; margin-top: 10px; }
            QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; }
            QTabWidget::pane { border: 1px solid #00ff00; }
            QTabBar::tab { background-color: #2d2d2d; color: #00ff00; padding: 5px; }
            QTabBar::tab:selected { background-color: #00aa00; color: #000000; }
            QSpinBox, QDoubleSpinBox, QComboBox { background-color: #2d2d2d; color: #00ff00; }
            QListWidget { background-color: #2d2d2d; color: #00ff00; border: 1px solid #00aa00; }
        """)
        
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        layout = QVBoxLayout(self)
        
        # Title
        title = QLabel("⚙️ Idle Mode Settings")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet("color: #00ff00;")
        layout.addWidget(title)
        
        # Tab widget for each mode
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Create tabs
        self.rest_tab = self.create_rest_tab()
        self.guard_tab = self.create_guard_tab()
        self.watch_tab = self.create_watch_tab()
        self.search_tab = self.create_search_tab()
        
        self.tabs.addTab(self.rest_tab, "🛌 Rest Mode")
        self.tabs.addTab(self.guard_tab, "🚔 Guard Mode")
        self.tabs.addTab(self.watch_tab, "👁️ Watch Mode")
        self.tabs.addTab(self.search_tab, "🔍 Search Mode")
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        save_btn = QPushButton("💾 Save Settings")
        save_btn.clicked.connect(self.save_settings)
        button_layout.addWidget(save_btn)
        
        close_btn = QPushButton("✖️ Close")
        close_btn.clicked.connect(self.close)
        button_layout.addWidget(close_btn)
        
        layout.addLayout(button_layout)
    
    def create_rest_tab(self) -> QWidget:
        """Create REST mode settings tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Description box
        desc_group = QGroupBox("How Rest Mode Works")
        desc_layout = QVBoxLayout(desc_group)
        desc_label = QLabel(
            "🛌 REST MODE:\n"
            "• Turret holds its current position\n"
            "• Auto-hides video feed after 3 seconds\n"
            "• No movement or scanning\n"
            "• Consumes minimal power\n"
            "• Perfect for pausing operations\n\n"
            "Save up to 8 positions for quick recall!"
        )
        desc_label.setStyleSheet("color: #00ff00; font-size: 10pt;")
        desc_layout.addWidget(desc_label)
        layout.addWidget(desc_group)
        
        # Settings group
        settings_group = QGroupBox("Rest Mode Settings")
        settings_layout = QGridLayout(settings_group)
        
        # Hold Position checkbox
        self.rest_hold_check = QCheckBox("Hold Current Position")
        self.rest_hold_check.setChecked(True)
        settings_layout.addWidget(self.rest_hold_check, 0, 0, 1, 2)
        
        settings_layout.addWidget(QLabel("Position Memory:"), 1, 0)
        settings_layout.addWidget(QLabel("Stores up to 8 saved positions"), 1, 1)
        
        layout.addWidget(settings_group)
        
        # Position memory group
        memory_group = QGroupBox("Saved Positions")
        memory_layout = QVBoxLayout(memory_group)
        
        self.rest_positions_list = QListWidget()
        memory_layout.addWidget(self.rest_positions_list)
        
        button_layout = QHBoxLayout()
        save_pos_btn = QPushButton("💾 Save Current Position")
        save_pos_btn.clicked.connect(self.rest_save_position)
        button_layout.addWidget(save_pos_btn)
        
        delete_pos_btn = QPushButton("🗑️ Delete Selected")
        delete_pos_btn.clicked.connect(self.rest_delete_position)
        button_layout.addWidget(delete_pos_btn)
        
        clear_all_btn = QPushButton("🗑️ Clear All")
        clear_all_btn.clicked.connect(self.rest_clear_all)
        button_layout.addWidget(clear_all_btn)
        
        memory_layout.addLayout(button_layout)
        layout.addWidget(memory_group)
        
        layout.addStretch()
        self.update_rest_display()
        return widget
    
    def create_guard_tab(self) -> QWidget:
        """Create GUARD mode settings tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Description box
        desc_group = QGroupBox("How Guard Mode Works")
        desc_layout = QVBoxLayout(desc_group)
        desc_label = QLabel(
            "🚔 GUARD MODE (Patrol):\n"
            "• Turret patrols between saved waypoints\n"
            "• Dwells at each point for set duration\n"
            "• Follows waypoints in order (or random)\n"
            "• Continuous scanning pattern\n"
            "• Great for monitoring large areas\n\n"
            "Add up to 8 patrol waypoints. Turret will visit each one!"
        )
        desc_label.setStyleSheet("color: #00ff00; font-size: 10pt;")
        desc_layout.addWidget(desc_label)
        layout.addWidget(desc_group)
        
        # Settings group
        settings_group = QGroupBox("Guard Mode Settings")
        settings_layout = QGridLayout(settings_group)
        
        settings_layout.addWidget(QLabel("Dwell Time (seconds):"), 0, 0)
        self.guard_dwell_spin = QSpinBox()
        self.guard_dwell_spin.setRange(1, 60)
        self.guard_dwell_spin.setValue(5)
        settings_layout.addWidget(self.guard_dwell_spin, 0, 1)
        
        settings_layout.addWidget(QLabel("Movement Speed (%):"), 1, 0)
        self.guard_speed_spin = QSpinBox()
        self.guard_speed_spin.setRange(1, 100)
        self.guard_speed_spin.setValue(50)
        settings_layout.addWidget(self.guard_speed_spin, 1, 1)
        
        self.guard_random_check = QCheckBox("Random Point Order")
        settings_layout.addWidget(self.guard_random_check, 2, 0, 1, 2)
        
        layout.addWidget(settings_group)
        
        # Patrol points group
        points_group = QGroupBox("Patrol Points (Max 8)")
        points_layout = QVBoxLayout(points_group)
        
        self.guard_points_list = QListWidget()
        points_layout.addWidget(self.guard_points_list)
        
        button_layout = QHBoxLayout()
        add_point_btn = QPushButton("➕ Add Current Position as Point")
        add_point_btn.clicked.connect(self.guard_add_point)
        button_layout.addWidget(add_point_btn)
        
        delete_point_btn = QPushButton("🗑️ Remove Selected")
        delete_point_btn.clicked.connect(self.guard_delete_point)
        button_layout.addWidget(delete_point_btn)
        
        points_layout.addLayout(button_layout)
        layout.addWidget(points_group)
        
        layout.addStretch()
        self.update_guard_display()
        return widget
    
    def create_watch_tab(self) -> QWidget:
        """Create WATCH mode settings tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Description box
        desc_group = QGroupBox("How Watch Mode Works")
        desc_layout = QVBoxLayout(desc_group)
        desc_label = QLabel(
            "👁️ WATCH MODE (Sweep):\n"
            "• Turret sweeps back and forth between two limits\n"
            "• Scans horizontally (pan only)\n"
            "• Pauses at each end before reversing\n"
            "• Smooth, continuous sweeping motion\n"
            "• Perfect for corridor/hallway monitoring\n\n"
            "Set left/right pan limits and sweep speed!"
        )
        desc_label.setStyleSheet("color: #00ff00; font-size: 10pt;")
        desc_layout.addWidget(desc_label)
        layout.addWidget(desc_group)
        
        settings_group = QGroupBox("Watch Mode Settings")
        settings_layout = QGridLayout(settings_group)
        
        settings_layout.addWidget(QLabel("Left Limit (Pan):"), 0, 0)
        self.watch_left_spin = QSpinBox()
        self.watch_left_spin.setRange(5, 180)
        self.watch_left_spin.setValue(45)
        settings_layout.addWidget(self.watch_left_spin, 0, 1)
        
        settings_layout.addWidget(QLabel("Right Limit (Pan):"), 1, 0)
        self.watch_right_spin = QSpinBox()
        self.watch_right_spin.setRange(5, 180)
        self.watch_right_spin.setValue(135)
        settings_layout.addWidget(self.watch_right_spin, 1, 1)
        
        settings_layout.addWidget(QLabel("Sweep Speed (%):"), 2, 0)
        self.watch_speed_spin = QSpinBox()
        self.watch_speed_spin.setRange(1, 100)
        self.watch_speed_spin.setValue(50)
        settings_layout.addWidget(self.watch_speed_spin, 2, 1)
        
        settings_layout.addWidget(QLabel("Pause Time at End (sec):"), 3, 0)
        self.watch_pause_spin = QSpinBox()
        self.watch_pause_spin.setRange(1, 10)
        self.watch_pause_spin.setValue(2)
        settings_layout.addWidget(self.watch_pause_spin, 3, 1)
        
        layout.addWidget(settings_group)
        layout.addStretch()
        
        if self.idle_modes:
            cfg = self.idle_modes.get_watch_config()
            self.watch_left_spin.setValue(cfg.get('left_limit', 45))
            self.watch_right_spin.setValue(cfg.get('right_limit', 135))
            self.watch_speed_spin.setValue(cfg.get('sweep_speed', 50))
            self.watch_pause_spin.setValue(cfg.get('pause_time', 2))
        
        return widget
    
    def create_search_tab(self) -> QWidget:
        """Create SEARCH mode settings tab."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Description box
        desc_group = QGroupBox("How Search Mode Works")
        desc_layout = QVBoxLayout(desc_group)
        desc_label = QLabel(
            "🔍 SEARCH MODE (Area Scanning):\n"
            "• Turret searches entire defined area\n"
            "• Can use random, spiral, or grid patterns\n"
            "• Varies speed to look more natural\n"
            "• Covers pan and tilt ranges\n"
            "• Great for thorough area scanning\n\n"
            "Define search boundaries and pick a movement pattern!"
        )
        desc_label.setStyleSheet("color: #00ff00; font-size: 10pt;")
        desc_layout.addWidget(desc_label)
        layout.addWidget(desc_group)
        
        settings_group = QGroupBox("Search Mode Settings")
        settings_layout = QGridLayout(settings_group)
        
        settings_layout.addWidget(QLabel("Pan Min:"), 0, 0)
        self.search_pan_min = QSpinBox()
        self.search_pan_min.setRange(5, 180)
        self.search_pan_min.setValue(5)
        settings_layout.addWidget(self.search_pan_min, 0, 1)
        
        settings_layout.addWidget(QLabel("Pan Max:"), 0, 2)
        self.search_pan_max = QSpinBox()
        self.search_pan_max.setRange(5, 180)
        self.search_pan_max.setValue(185)
        settings_layout.addWidget(self.search_pan_max, 0, 3)
        
        settings_layout.addWidget(QLabel("Tilt Min:"), 1, 0)
        self.search_tilt_min = QSpinBox()
        self.search_tilt_min.setRange(18, 110)
        self.search_tilt_min.setValue(20)
        settings_layout.addWidget(self.search_tilt_min, 1, 1)
        
        settings_layout.addWidget(QLabel("Tilt Max:"), 1, 2)
        self.search_tilt_max = QSpinBox()
        self.search_tilt_max.setRange(18, 110)
        self.search_tilt_max.setValue(110)
        settings_layout.addWidget(self.search_tilt_max, 1, 3)
        
        settings_layout.addWidget(QLabel("Movement Style:"), 2, 0)
        self.search_style_combo = QComboBox()
        self.search_style_combo.addItems(["Random", "Spiral", "Grid"])
        settings_layout.addWidget(self.search_style_combo, 2, 1, 1, 3)
        
        self.search_variation_check = QCheckBox("Enable Speed Variation")
        self.search_variation_check.setChecked(True)
        settings_layout.addWidget(self.search_variation_check, 3, 0, 1, 4)
        
        layout.addWidget(settings_group)
        layout.addStretch()
        
        if self.idle_modes:
            cfg = self.idle_modes.get_search_config()
            area = cfg.get('search_area', {})
            self.search_pan_min.setValue(area.get('pan_min', 5))
            self.search_pan_max.setValue(area.get('pan_max', 185))
            self.search_tilt_min.setValue(area.get('tilt_min', 20))
            self.search_tilt_max.setValue(area.get('tilt_max', 110))
            self.search_style_combo.setCurrentText(cfg.get('movement_style', 'random').capitalize())
            self.search_variation_check.setChecked(cfg.get('speed_variation', True))
        
        return widget
    
    def update_rest_display(self):
        """Update rest mode position list display."""
        if not self.idle_modes:
            return
        self.rest_positions_list.clear()
        for pos in self.idle_modes.rest_get_positions():
            item_text = f"{pos['label']} - Pan: {pos['pan']}, Tilt: {pos['tilt']}"
            self.rest_positions_list.addItem(item_text)
    
    def update_guard_display(self):
        """Update guard mode points list display."""
        if not self.idle_modes:
            return
        self.guard_points_list.clear()
        for point in self.idle_modes.guard_get_points():
            item_text = f"{point['label']} - Pan: {point['pan']}, Tilt: {point['tilt']}"
            self.guard_points_list.addItem(item_text)
    
    def rest_save_position(self):
        """Save current position to rest mode."""
        if not self.idle_modes:
            return
        label, ok = QInputDialog.getText(self, "Save Position", "Position Label:", text="Position")
        if ok and label:
            # Get actual current angles from parent app
            pan = getattr(self.parent(), 'target_pan', 90)
            tilt = getattr(self.parent(), 'target_tilt', 50)
            self.idle_modes.rest_save_position(pan, tilt, label)
            self.update_rest_display()
            QMessageBox.information(self, "Success", f"Position '{label}' saved at Pan:{pan}° Tilt:{tilt}°!")
    
    def rest_delete_position(self):
        """Delete selected rest position."""
        if not self.idle_modes:
            return
        current_row = self.rest_positions_list.currentRow()
        if current_row >= 0:
            self.idle_modes.rest_get_positions().pop(current_row)
            self.idle_modes.save_config()
            self.update_rest_display()
    
    def rest_clear_all(self):
        """Clear all rest positions."""
        if not self.idle_modes:
            return
        reply = QMessageBox.question(self, "Clear All", "Delete all saved positions?")
        if reply == QMessageBox.Yes:
            self.idle_modes.rest_clear_positions()
            self.update_rest_display()
    
    def guard_add_point(self):
        """Add current position as guard patrol point."""
        if not self.idle_modes:
            return
        points = self.idle_modes.guard_get_points()
        if len(points) >= 8:
            QMessageBox.warning(self, "Max Reached", "Maximum 8 patrol points allowed!")
            return
        label, ok = QInputDialog.getText(self, "Add Point", "Point Label:", text="Point")
        if ok and label:
            # Get actual current angles from parent app
            pan = getattr(self.parent(), 'target_pan', 90)
            tilt = getattr(self.parent(), 'target_tilt', 50)
            self.idle_modes.guard_add_point(pan, tilt, label)
            self.update_guard_display()
            QMessageBox.information(self, "Success", f"Point '{label}' added at Pan:{pan}° Tilt:{tilt}°!")
    
    def guard_delete_point(self):
        """Delete selected guard patrol point."""
        if not self.idle_modes:
            return
        current_row = self.guard_points_list.currentRow()
        if current_row >= 0:
            self.idle_modes.guard_remove_point(current_row)
            self.update_guard_display()
    
    def save_settings(self):
        """Save all idle mode settings."""
        if not self.idle_modes:
            return
        
        # Save REST settings
        self.idle_modes.set_rest_hold_position(self.rest_hold_check.isChecked())
        
        # Save GUARD settings
        self.idle_modes.guard_set_dwell_time(self.guard_dwell_spin.value())
        self.idle_modes.guard_set_movement_speed(self.guard_speed_spin.value())
        self.idle_modes.guard_set_random_order(self.guard_random_check.isChecked())
        
        # Save WATCH settings
        self.idle_modes.watch_set_limits(self.watch_left_spin.value(), self.watch_right_spin.value())
        self.idle_modes.watch_set_sweep_speed(self.watch_speed_spin.value())
        self.idle_modes.watch_set_pause_time(self.watch_pause_spin.value())
        
        # Save SEARCH settings
        self.idle_modes.search_set_area(
            self.search_pan_min.value(),
            self.search_pan_max.value(),
            self.search_tilt_min.value(),
            self.search_tilt_max.value()
        )
        self.idle_modes.search_set_movement_style(self.search_style_combo.currentText().lower())
        self.idle_modes.search_set_speed_variation(self.search_variation_check.isChecked())
        
        self.idle_modes.save_config()
        QMessageBox.information(self, "Saved", "All idle mode settings saved!")
        self.settings_changed.emit("all_modes")
