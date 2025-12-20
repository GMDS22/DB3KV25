"""
UI Builder Components for Color Detection
==========================================

This module provides UI building functions for the color detection settings.
These functions should be called from ui_builder.py during integration.

The color settings panel includes:
- Color preset dropdown
- Custom HSV sliders
- Min/Max area controls
- Blur and morphology settings
"""

from PyQt5.QtWidgets import (
    QGroupBox, QGridLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QComboBox, QSlider, QSpinBox, QPushButton,
    QCheckBox, QFrame
)
from PyQt5.QtCore import Qt


def build_color_detection_panel(app, parent_layout):
    """
    Build the color detection settings panel.
    
    Args:
        app: Main application instance
        parent_layout: Layout to add the panel to
        
    Returns:
        QGroupBox: The color settings group box
    """
    color_group = QGroupBox("Color Detection Settings")
    color_layout = QGridLayout(color_group)
    color_layout.setSpacing(6)
    row = 0

    # Lists of widgets for compact mode-aware visibility control
    # (managed by MAIN_FILE_SINGLE_CAM.py advanced toggle + mode selection)
    app._color_basic_widgets = []
    app._color_advanced_widgets = []
    app._color_hybrid_widgets = []
    app._color_custom_hsv_widgets = []
    
    # =========================================================================
    # COLOR PRESET DROPDOWN
    # =========================================================================
    preset_label = QLabel("Color Preset:")
    color_layout.addWidget(preset_label, row, 0)
    
    if not hasattr(app, "color_preset_combo") or app.color_preset_combo is None:
        app.color_preset_combo = QComboBox()
    
    presets = [
        "red", "orange", "yellow", "green", "cyan", 
        "blue", "purple", "pink", "neon_green", "laser_red",
        "white", "black", "custom"
    ]
    
    if app.color_preset_combo.count() == 0:
        app.color_preset_combo.addItems(presets)
    
    app.color_preset_combo.setToolTip(
        "Select a predefined color to track, or 'custom' to use the HSV sliders below."
    )
    color_layout.addWidget(app.color_preset_combo, row, 1)
    app._color_basic_widgets.extend([preset_label, app.color_preset_combo])
    row += 1
    
    # =========================================================================
    # CUSTOM HSV SLIDERS (visible when "custom" selected)
    # =========================================================================
    
    # Separator
    separator = QFrame()
    separator.setFrameShape(QFrame.HLine)
    separator.setFrameShadow(QFrame.Sunken)
    color_layout.addWidget(separator, row, 0, 1, 2)
    app._color_advanced_widgets.append(separator)
    row += 1
    
    custom_label = QLabel("Custom HSV Range:")
    custom_label.setStyleSheet("font-weight: bold;")
    color_layout.addWidget(custom_label, row, 0, 1, 2)
    app._color_advanced_widgets.append(custom_label)
    app._color_custom_hsv_widgets.append(custom_label)
    row += 1
    
    # H Min
    hmin_label = QLabel("Hue Min (0-179):")
    color_layout.addWidget(hmin_label, row, 0)
    app.color_h_min = QSlider(Qt.Horizontal)
    app.color_h_min.setRange(0, 179)
    app.color_h_min.setValue(0)
    app.color_h_min.setToolTip("Minimum hue value (0-179). Red is 0/179, Green ~60, Blue ~120.")
    color_layout.addWidget(app.color_h_min, row, 1)
    app._color_advanced_widgets.extend([hmin_label, app.color_h_min])
    app._color_custom_hsv_widgets.extend([hmin_label, app.color_h_min])
    row += 1
    
    # H Max
    hmax_label = QLabel("Hue Max (0-179):")
    color_layout.addWidget(hmax_label, row, 0)
    app.color_h_max = QSlider(Qt.Horizontal)
    app.color_h_max.setRange(0, 179)
    app.color_h_max.setValue(10)
    app.color_h_max.setToolTip("Maximum hue value (0-179).")
    color_layout.addWidget(app.color_h_max, row, 1)
    app._color_advanced_widgets.extend([hmax_label, app.color_h_max])
    app._color_custom_hsv_widgets.extend([hmax_label, app.color_h_max])
    row += 1
    
    # S Min
    smin_label = QLabel("Saturation Min:")
    color_layout.addWidget(smin_label, row, 0)
    app.color_s_min = QSlider(Qt.Horizontal)
    app.color_s_min.setRange(0, 255)
    app.color_s_min.setValue(100)
    app.color_s_min.setToolTip("Minimum saturation (0-255). Higher = more vibrant colors only.")
    color_layout.addWidget(app.color_s_min, row, 1)
    app._color_advanced_widgets.extend([smin_label, app.color_s_min])
    app._color_custom_hsv_widgets.extend([smin_label, app.color_s_min])
    row += 1
    
    # S Max
    smax_label = QLabel("Saturation Max:")
    color_layout.addWidget(smax_label, row, 0)
    app.color_s_max = QSlider(Qt.Horizontal)
    app.color_s_max.setRange(0, 255)
    app.color_s_max.setValue(255)
    app.color_s_max.setToolTip("Maximum saturation (0-255).")
    color_layout.addWidget(app.color_s_max, row, 1)
    app._color_advanced_widgets.extend([smax_label, app.color_s_max])
    app._color_custom_hsv_widgets.extend([smax_label, app.color_s_max])
    row += 1
    
    # V Min
    vmin_label = QLabel("Value Min:")
    color_layout.addWidget(vmin_label, row, 0)
    app.color_v_min = QSlider(Qt.Horizontal)
    app.color_v_min.setRange(0, 255)
    app.color_v_min.setValue(100)
    app.color_v_min.setToolTip("Minimum brightness value (0-255). Higher = brighter colors only.")
    color_layout.addWidget(app.color_v_min, row, 1)
    app._color_advanced_widgets.extend([vmin_label, app.color_v_min])
    app._color_custom_hsv_widgets.extend([vmin_label, app.color_v_min])
    row += 1
    
    # V Max
    vmax_label = QLabel("Value Max:")
    color_layout.addWidget(vmax_label, row, 0)
    app.color_v_max = QSlider(Qt.Horizontal)
    app.color_v_max.setRange(0, 255)
    app.color_v_max.setValue(255)
    app.color_v_max.setToolTip("Maximum brightness value (0-255).")
    color_layout.addWidget(app.color_v_max, row, 1)
    app._color_advanced_widgets.extend([vmax_label, app.color_v_max])
    app._color_custom_hsv_widgets.extend([vmax_label, app.color_v_max])
    row += 1
    
    # =========================================================================
    # DETECTION PARAMETERS
    # =========================================================================
    
    separator2 = QFrame()
    separator2.setFrameShape(QFrame.HLine)
    separator2.setFrameShadow(QFrame.Sunken)
    color_layout.addWidget(separator2, row, 0, 1, 2)
    app._color_advanced_widgets.append(separator2)
    row += 1
    
    params_label = QLabel("Detection Parameters:")
    params_label.setStyleSheet("font-weight: bold;")
    color_layout.addWidget(params_label, row, 0, 1, 2)
    app._color_advanced_widgets.append(params_label)
    row += 1
    
    # Min Area
    min_area_label = QLabel("Min Color Area:")
    color_layout.addWidget(min_area_label, row, 0)
    app.color_min_area_input = QSpinBox()
    app.color_min_area_input.setRange(0, 100000)
    app.color_min_area_input.setValue(300)
    app.color_min_area_input.setSingleStep(50)
    app.color_min_area_input.setToolTip(
        "Minimum contour area in pixels. Increase to ignore small noise."
    )
    color_layout.addWidget(app.color_min_area_input, row, 1)
    app._color_advanced_widgets.extend([min_area_label, app.color_min_area_input])
    row += 1
    
    # Max Area
    max_area_label = QLabel("Max Color Area:")
    color_layout.addWidget(max_area_label, row, 0)
    app.color_max_area_input = QSpinBox()
    app.color_max_area_input.setRange(0, 1000000)
    app.color_max_area_input.setValue(500000)
    app.color_max_area_input.setSingleStep(1000)
    app.color_max_area_input.setToolTip(
        "Maximum contour area in pixels. Decrease to ignore large background areas."
    )
    color_layout.addWidget(app.color_max_area_input, row, 1)
    app._color_advanced_widgets.extend([max_area_label, app.color_max_area_input])
    row += 1
    
    # Blur Kernel
    blur_label = QLabel("Blur Kernel:")
    color_layout.addWidget(blur_label, row, 0)
    app.color_blur_input = QSpinBox()
    app.color_blur_input.setRange(1, 15)
    app.color_blur_input.setValue(5)
    app.color_blur_input.setSingleStep(2)
    app.color_blur_input.setToolTip(
        "Gaussian blur kernel size (must be odd). Higher = more smoothing."
    )
    color_layout.addWidget(app.color_blur_input, row, 1)
    app._color_advanced_widgets.extend([blur_label, app.color_blur_input])
    row += 1
    
    # Morph Iterations
    morph_label = QLabel("Morph Iterations:")
    color_layout.addWidget(morph_label, row, 0)
    app.color_morph_input = QSpinBox()
    app.color_morph_input.setRange(0, 5)
    app.color_morph_input.setValue(2)
    app.color_morph_input.setToolTip(
        "Morphological operation iterations. Higher = cleaner mask, but slower."
    )
    color_layout.addWidget(app.color_morph_input, row, 1)
    app._color_advanced_widgets.extend([morph_label, app.color_morph_input])
    row += 1
    
    # =========================================================================
    # CALIBRATION BUTTON
    # =========================================================================
    
    separator3 = QFrame()
    separator3.setFrameShape(QFrame.HLine)
    separator3.setFrameShadow(QFrame.Sunken)
    color_layout.addWidget(separator3, row, 0, 1, 2)
    # Keep this separator visible in basic mode (visually groups preset vs actions)
    app._color_basic_widgets.append(separator3)
    row += 1
    
    app.color_calibrate_btn = QPushButton("Calibrate from ROI")
    app.color_calibrate_btn.setToolTip(
        "Click, then draw a rectangle on the video to sample colors from that region."
    )
    color_layout.addWidget(app.color_calibrate_btn, row, 0, 1, 2)
    app._color_basic_widgets.append(app.color_calibrate_btn)
    row += 1
    
    # Show mask checkbox
    app.color_show_mask_checkbox = QCheckBox("Show Color Mask")
    app.color_show_mask_checkbox.setToolTip(
        "Display the binary color detection mask in a separate window."
    )
    color_layout.addWidget(app.color_show_mask_checkbox, row, 0, 1, 2)
    app._color_basic_widgets.append(app.color_show_mask_checkbox)
    row += 1
    
    # =========================================================================
    # HYBRID FUSION SETTINGS (for modes 7, 8, 9)
    # =========================================================================
    
    separator4 = QFrame()
    separator4.setFrameShape(QFrame.HLine)
    separator4.setFrameShadow(QFrame.Sunken)
    color_layout.addWidget(separator4, row, 0, 1, 2)
    app._color_advanced_widgets.append(separator4)
    app._color_hybrid_widgets.append(separator4)
    row += 1
    
    fusion_label = QLabel("Hybrid Fusion (Modes 7-9):")
    fusion_label.setStyleSheet("font-weight: bold;")
    color_layout.addWidget(fusion_label, row, 0, 1, 2)
    app._color_advanced_widgets.append(fusion_label)
    app._color_hybrid_widgets.append(fusion_label)
    row += 1
    
    # Fusion Strategy
    fusion_strategy_label = QLabel("Fusion Strategy:")
    color_layout.addWidget(fusion_strategy_label, row, 0)
    app.color_fusion_strategy = QComboBox()
    app.color_fusion_strategy.addItems(["AND", "OR"])
    app.color_fusion_strategy.setToolTip(
        "AND: Only keep detections found by both methods.\n"
        "OR: Keep all detections from both methods."
    )
    color_layout.addWidget(app.color_fusion_strategy, row, 1)
    app._color_advanced_widgets.extend([fusion_strategy_label, app.color_fusion_strategy])
    app._color_hybrid_widgets.extend([fusion_strategy_label, app.color_fusion_strategy])
    row += 1
    
    # Overlap Threshold
    overlap_label = QLabel("Overlap Threshold:")
    color_layout.addWidget(overlap_label, row, 0)
    app.color_fusion_overlap = QSlider(Qt.Horizontal)
    app.color_fusion_overlap.setRange(0, 100)
    app.color_fusion_overlap.setValue(30)
    app.color_fusion_overlap.setToolTip(
        "Minimum overlap % required for AND fusion (0-100%)."
    )
    color_layout.addWidget(app.color_fusion_overlap, row, 1)
    app._color_advanced_widgets.extend([overlap_label, app.color_fusion_overlap])
    app._color_hybrid_widgets.extend([overlap_label, app.color_fusion_overlap])
    row += 1
    
    # Add to parent layout
    parent_layout.addWidget(color_group)
    
    # Store reference for visibility toggling
    app.color_settings_group = color_group

    # Default to compact behavior: hide custom HSV rows unless preset is "custom"
    try:
        set_color_custom_hsv_visible(app, False)
    except Exception:
        pass
    
    # Initially hidden (shown when color mode selected)
    color_group.hide()
    
    return color_group


def set_color_advanced_visible(app, visible: bool):
    """Show/hide advanced color-detection widgets (keeps the panel compact)."""
    try:
        widgets = getattr(app, "_color_advanced_widgets", [])
        for w in list(widgets):
            try:
                if w is not None:
                    w.setVisible(bool(visible))
            except Exception:
                pass
    except Exception:
        pass


def set_color_hybrid_visible(app, visible: bool):
    """Show/hide the color-hybrid fusion widgets (modes 7-9 only)."""
    try:
        widgets = getattr(app, "_color_hybrid_widgets", [])
        for w in list(widgets):
            try:
                if w is not None:
                    w.setVisible(bool(visible))
            except Exception:
                pass
    except Exception:
        pass


def set_color_custom_hsv_visible(app, visible: bool):
    """Show/hide custom HSV range widgets (only relevant when preset is 'custom')."""
    try:
        widgets = getattr(app, "_color_custom_hsv_widgets", [])
        for w in list(widgets):
            try:
                if w is not None:
                    w.setVisible(bool(visible))
            except Exception:
                pass
    except Exception:
        pass


def connect_color_signals(app):
    """
    Connect color detection UI signals to handlers.
    
    Args:
        app: Main application instance
    """
    try:
        # Color preset change
        if hasattr(app, "color_preset_combo"):
            app.color_preset_combo.currentTextChanged.connect(
                lambda t: on_color_preset_change(app, t)
            )
        
        # HSV slider changes
        for slider_name in ["color_h_min", "color_h_max", "color_s_min", 
                           "color_s_max", "color_v_min", "color_v_max"]:
            slider = getattr(app, slider_name, None)
            if slider:
                slider.valueChanged.connect(lambda v, a=app: update_custom_color(a))
        
        # Detection param changes
        for widget_name in ["color_min_area_input", "color_max_area_input",
                           "color_blur_input", "color_morph_input"]:
            widget = getattr(app, widget_name, None)
            if widget:
                widget.valueChanged.connect(lambda v, a=app: update_detection_params(a))
        
        # Calibrate button
        if hasattr(app, "color_calibrate_btn"):
            app.color_calibrate_btn.clicked.connect(
                lambda: start_color_calibration(app)
            )
        
        # Show mask checkbox
        if hasattr(app, "color_show_mask_checkbox"):
            app.color_show_mask_checkbox.stateChanged.connect(
                lambda s, a=app: toggle_mask_display(a, s)
            )
            
    except Exception as e:
        print(f"[COLOR UI] Signal connection error: {e}")


def on_color_preset_change(app, preset_name: str):
    """Handle color preset selection change."""
    try:
        if hasattr(app, "color_detector") and app.color_detector is not None:
            if preset_name == "custom":
                # Enable custom sliders, use their values
                update_custom_color(app)
            else:
                app.color_detector.set_active_colors(preset_name)

        # Keep the UI compact: show custom HSV only when it's relevant
        try:
            adv_cb = getattr(app, "show_advanced_detection_checkbox", None)
            adv = bool(getattr(adv_cb, "isChecked", lambda: False)())
            set_color_custom_hsv_visible(app, bool(adv and preset_name == "custom"))
        except Exception:
            pass
        
        # Save settings
        if hasattr(app, "save_settings"):
            app.save_settings()
            
    except Exception as e:
        print(f"[COLOR UI] Preset change error: {e}")


def update_custom_color(app):
    """Update color detector with custom HSV values from sliders."""
    try:
        if not hasattr(app, "color_detector") or app.color_detector is None:
            return
        
        h_min = getattr(app.color_h_min, "value", lambda: 0)()
        h_max = getattr(app.color_h_max, "value", lambda: 10)()
        s_min = getattr(app.color_s_min, "value", lambda: 100)()
        s_max = getattr(app.color_s_max, "value", lambda: 255)()
        v_min = getattr(app.color_v_min, "value", lambda: 100)()
        v_max = getattr(app.color_v_max, "value", lambda: 255)()
        
        app.color_detector.set_custom_range(h_min, s_min, v_min, h_max, s_max, v_max)
        
        # If custom mode, set active colors
        preset = getattr(app.color_preset_combo, "currentText", lambda: "")()
        if preset == "custom":
            app.color_detector.set_active_colors("custom")
            
    except Exception as e:
        print(f"[COLOR UI] Custom color update error: {e}")


def update_detection_params(app):
    """Update color detector parameters from UI inputs."""
    try:
        if not hasattr(app, "color_detector") or app.color_detector is None:
            return
        
        min_area = getattr(app.color_min_area_input, "value", lambda: 300)()
        max_area = getattr(app.color_max_area_input, "value", lambda: 500000)()
        blur = getattr(app.color_blur_input, "value", lambda: 5)()
        morph = getattr(app.color_morph_input, "value", lambda: 2)()
        
        app.color_detector.set_detection_params(
            min_area=min_area,
            max_area=max_area,
            blur_kernel=blur,
            morph_iterations=morph
        )
        
    except Exception as e:
        print(f"[COLOR UI] Param update error: {e}")


def start_color_calibration(app):
    """Start ROI color calibration mode."""
    try:
        # Set a flag that the main loop checks
        app.color_calibration_mode = True
        print("[COLOR] Calibration mode started. Click and drag on video to select region.")
        
        if hasattr(app, "enhancer"):
            app.enhancer.log_serial_output(
                "Color calibration: Draw rectangle on video to sample color",
                fire=False
            )
            
    except Exception as e:
        print(f"[COLOR UI] Calibration start error: {e}")


def toggle_mask_display(app, state: int):
    """Toggle color mask display window."""
    try:
        app.show_color_mask = (state == Qt.Checked)
    except Exception as e:
        print(f"[COLOR UI] Mask toggle error: {e}")


def show_hide_color_panel(app, show: bool):
    """Show or hide the color settings panel."""
    try:
        if hasattr(app, "color_settings_group"):
            if show:
                app.color_settings_group.show()
            else:
                app.color_settings_group.hide()
    except Exception:
        pass
