"""
ui_builder.py

UI construction logic for the Auto Turret Control System.
This module is responsible for creating and laying out all PyQt widgets.
"""

from typing import Any, cast

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDockWidget,
    QDoubleSpinBox,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSlider,
    QSpinBox,
    QStyleFactory,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from theme_manager import ThemeManager
from turret_presets import PRESETS
from helpers.graph_widget import HealthGraphWidget

# Import centralized logger for error tracking
try:
    from helpers.logger import get_logger, log_exception, log_connection_error
    logger = get_logger()
except ImportError:
    logger = None
    def log_exception(e, ctx=""):
        print(f"ERROR [{ctx}]: {e}")
    def log_connection_error(src, sig, tgt, e):
        print(f"CONNECTION ERROR {src}.{sig} -> {tgt}: {e}")


def build_ui(app: QMainWindow):
    """
    Builds and configures the entire UI for the TrackingApp.
    All widgets are created and attached to the `app` instance.
    """
    # CHANGE WARNING:
    # Modifications here affect UI construction, dock layout, and signal wiring.
    # See CHANGE_IMPACT_REFERENCE.md → Code-Level Change Enforcement.
    # Last modified: 2026-01-06 by Copilot Agent
    # Authoritative UI builder
    try:
        from db3k_meta import get_app_title

        app.setWindowTitle(get_app_title())
    except Exception:
        app.setWindowTitle("AUTO TURRET CONTROL SYSTEM")
    try:
        QApplication.setStyle(QStyleFactory.create("Fusion"))
    except Exception as e:
        if logger: log_exception(e, "Setting Fusion style")

    # Apply theme manager if present
    try:
        app.theme_manager = getattr(app, "theme_manager", ThemeManager())
        try:
            app.theme_manager.apply_theme("dark")
        except Exception as e:
            if logger: log_exception(e, "Applying dark theme")
    except Exception as e:
        if logger: log_exception(e, "Initializing theme manager")

    # Central video area
    app.video_frame = QFrame()
    video_layout = QVBoxLayout(app.video_frame)
    video_layout.setContentsMargins(0, 0, 0, 0)

    if getattr(app, "video_label", None) is None:
        app.video_label = QLabel()
    try:
        lbl = getattr(app, "video_label", None)
        if lbl is not None:
            try:
                try:
                    lbl.setAlignment(cast(Any, getattr(Qt, "AlignCenter", 0)))
                except Exception as e:
                    if logger: log_exception(e, "Setting video_label alignment")
                lbl.setText("No Camera Feed")
            except Exception as e:
                if logger: log_exception(e, "Setting video_label properties")
    except Exception as e:
        if logger: log_exception(e, "Initializing video_label")
    # use safe widget caller for methods that static analyzer may flag
    try:
        app._safe_widget_call("video_label", "setScaledContents", False)
        app._safe_widget_call(
            "video_label", "setSizePolicy", QSizePolicy.Expanding, QSizePolicy.Expanding
        )
    except Exception as e:
        if logger: log_exception(e, "Setting video_label size policy")
    video_layout.addWidget(app.video_label)
    app.setCentralWidget(app.video_frame)

    # Sniper view dock - REMOVED (Dec 2024)
    # All sniper dock initialization code has been disabled

    # --- Build panels (create all names that load_settings expects) ---
    # Configuration & Connection
    settings_group = QGroupBox("Configuration & Connection")
    settings_layout = QGridLayout()
    settings_layout.setSpacing(6)
    settings_layout.setContentsMargins(8, 8, 8, 8)
    settings_layout.addWidget(QLabel("COM Port:"), 0, 0)
    if getattr(app, "com_port_input", None) is None:
        app.com_port_input = QLineEdit()
    try:
        if not getattr(app.com_port_input, "text", lambda: "")():
            app.com_port_input.setText("COM3")
    except Exception:
        pass
    settings_layout.addWidget(app.com_port_input, 0, 1)
    settings_layout.addWidget(QLabel("Baud Rate:"), 1, 0)
    if getattr(app, "baud_rate_input", None) is None:
        app.baud_rate_input = QSpinBox()
    try:
        if getattr(app, "baud_rate_input", None) is not None:
            try:
                app._safe_widget_call("baud_rate_input", "setRange", 2400, 115200)
                # prefer safe call for setValue too
                app._safe_widget_call("baud_rate_input", "setValue", 115200)
            except Exception:
                pass
    except Exception:
        pass
    settings_layout.addWidget(app.baud_rate_input, 1, 1)
    # Factory preset quick-access (keeps UI usable even if Behavior dock is hidden)
    # NOTE: This is a separate combo box from any behavior-panel preset widget.
    # Qt widgets cannot have multiple parents.
    settings_layout.addWidget(QLabel("Factory Preset:"), 2, 0)
    if getattr(app, "connection_preset_combo", None) is None:
        app.connection_preset_combo = QComboBox()
        try:
            app.connection_preset_combo.setToolTip(
                "Quick-apply a factory preset without opening the Behavior panel."
            )
        except Exception:
            pass
    try:
        # Keep items in the same order that apply_preset() expects
        if getattr(app, "connection_preset_combo", None) is not None:
            if app.connection_preset_combo.count() == 0:
                app.connection_preset_combo.addItems(list(PRESETS.keys()))
            app._safe_connect(
                "connection_preset_combo", "currentIndexChanged", app.apply_preset
            )
    except Exception:
        pass
    settings_layout.addWidget(app.connection_preset_combo, 2, 1)

    if getattr(app, "connect_button", None) is None:
        app.connect_button = QPushButton("Connect")
    try:
        # Use safe connect helper - single attempt instead of 10+ nested tries
        if not app._safe_connect("connect_button", "clicked", lambda: app.handle_connect_sound()):
            if logger: log_connection_error("connect_button", "clicked", "handle_connect_sound", "Connection failed")
    except Exception as e:
        if logger: log_exception(e, "Connecting connect_button.clicked signal")
    settings_layout.addWidget(app.connect_button, 3, 0, 1, 2)

    if getattr(app, "sound_checkbox", None) is None:
        app.sound_checkbox = QCheckBox("Sound Effects")
    try:
        scb = getattr(app, "sound_checkbox", None)
        if scb is not None:
            try:
                scb.setChecked(bool(getattr(app, "sound_enabled", True)))
            except Exception:
                pass
            try:
                scb.setToolTip("Toggle UI sound effects (notifications and alerts).")
            except Exception:
                pass
            try:
                try:
                    app._safe_connect(
                        "sound_checkbox", "stateChanged", lambda s: app.set_sound_enabled(s)
                    )
                except Exception:
                    try:
                        try:
                            if not app._safe_connect_path(
                                "sound_checkbox",
                                "stateChanged",
                                lambda s: app.set_sound_enabled(s),
                            ):
                                try:
                                    try:
                                        if not app._safe_connect(
                                            "scb",
                                            "stateChanged",
                                            lambda s: app.set_sound_enabled(s),
                                        ):
                                            try:
                                                try:
                                                    if not app._safe_connect(
                                                        "sound_checkbox",
                                                        "stateChanged",
                                                        lambda s: app.set_sound_enabled(
                                                            s
                                                        ),
                                                    ):
                                                        pass
                                                except Exception:
                                                    pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    except Exception:
                        pass
            except Exception:
                pass
    except Exception:
        pass
    settings_layout.addWidget(app.sound_checkbox, 4, 0, 1, 2)

    # Small status label to show override/suspend states (manual, go-home, hold)
    app.override_status_label = QLabel("")
    try:
        try:
            app.override_status_label.setAlignment(
                cast(Any, getattr(Qt, "AlignCenter", 0))
            )
        except Exception:
            pass
    except Exception:
        pass
    settings_layout.addWidget(app.override_status_label, 7, 0, 1, 2)

    # Camera selection (allow user to prefer a specific camera index or use Auto)
    if getattr(app, "camera_index_combo", None) is None:
        app.camera_index_combo = QComboBox()
        try:
            if app.camera_index_combo.count() == 0:
                app.camera_index_combo.addItems(["Auto", "0", "1", "2", "3", "4"])
        except Exception:
            pass
    settings_layout.addWidget(app.camera_index_combo, 6, 1)

    # Tracking toggle (replaces separate Start/Stop buttons)
    if getattr(app, "tracking_btn", None) is None:
        app.tracking_btn = QPushButton("Start Tracking")
        try:
            app.tracking_btn.setCheckable(True)
        except Exception:
            pass
    try:
        try:
            # Use 'toggled' for checkable toggle buttons to avoid double-press issues
            app._safe_connect("tracking_btn", "toggled", app.toggle_tracking)
        except Exception:
            pass
    except Exception:
        pass

    # Aiming toggle (repurposed from the old Stop Tracking button)
    if getattr(app, "aiming_btn", None) is None:
        app.aiming_btn = QPushButton("Start Aiming")
        try:
            app.aiming_btn.setCheckable(True)
        except Exception:
            pass
    try:
        try:
            # Checkable buttons must use 'toggled' per CHANGE_IMPACT_REFERENCE.md
            app._safe_connect("aiming_btn", "toggled", app.toggle_aiming)
        except Exception:
            pass
    except Exception:
        pass

    settings_layout.addWidget(app.tracking_btn, 5, 0)
    settings_layout.addWidget(app.aiming_btn, 5, 1)
    settings_group.setLayout(settings_layout)

    # Home position
    home_group = QGroupBox("Home Position (°)")
    home_layout = QGridLayout()
    home_layout.setSpacing(6)
    home_layout.setContentsMargins(8, 8, 8, 8)
    home_layout.addWidget(QLabel("Home Pan:"), 0, 0)
    if getattr(app, "home_pan_input", None) is None:
        app.home_pan_input = QSpinBox()
    try:
        try:
            app._safe_widget_call("home_pan_input", "setRange", app.PAN_MIN, app.PAN_MAX)
            app._safe_widget_call("home_pan_input", "setValue", app.HOME_PAN)
            app._safe_connect("home_pan_input", "valueChanged", app.save_settings)
        except Exception:
            pass
    except Exception:
        pass
    home_layout.addWidget(app.home_pan_input, 0, 1)
    home_layout.addWidget(QLabel("Home Tilt:"), 1, 0)
    if getattr(app, "home_tilt_input", None) is None:
        app.home_tilt_input = QSpinBox()
    try:
        try:
            app._safe_widget_call("home_tilt_input", "setRange", app.TILT_MIN, app.TILT_MAX)
            app._safe_widget_call("home_tilt_input", "setValue", app.HOME_TILT)
            app._safe_connect("home_tilt_input", "valueChanged", app.save_settings)
        except Exception:
            pass
    except Exception:
        pass
    home_layout.addWidget(app.home_tilt_input, 1, 1)
    if getattr(app, "go_home_button", None) is None:
        app.go_home_button = QPushButton("Go Home")
    try:
        go_btn = getattr(app, "go_home_button", None)
        if go_btn is not None:
            try:
                try:
                    app._safe_connect("go_home_button", "clicked", app.go_home)
                except Exception:
                    try:
                        try:
                            if not app._safe_connect_path(
                                "go_home_btn", "clicked", app.go_home
                            ):
                                try:
                                    try:
                                        if not app._safe_connect(
                                            "go_btn", "clicked", app.go_home
                                        ):
                                            try:
                                                try:
                                                    if not app._safe_connect(
                                                        "go_home_button",
                                                        "clicked",
                                                        app.go_home,
                                                    ):
                                                        pass
                                                except Exception:
                                                    pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    except Exception:
                        pass
            except Exception:
                pass
    except Exception:
        pass
    home_layout.addWidget(app.go_home_button, 2, 0, 1, 2)
    home_group.setLayout(home_layout)

    # Servo limits
    limits_group = QGroupBox("Servo Limits (°)")
    limits_layout = QGridLayout()
    limits_layout.setSpacing(6)
    limits_layout.setContentsMargins(8, 8, 8, 8)
    limits_layout.addWidget(QLabel("PAN Min:"), 0, 0)
    if getattr(app, "pan_min_input", None) is None:
        app.pan_min_input = QSpinBox()
    try:
        try:
            app._safe_widget_call("pan_min_input", "setRange", 0, 180)
            app._safe_widget_call("pan_min_input", "setValue", app.PAN_MIN)
        except Exception:
            pass
    except Exception:
        pass
    limits_layout.addWidget(app.pan_min_input, 0, 1)
    limits_layout.addWidget(QLabel("PAN Max:"), 1, 0)
    if getattr(app, "pan_max_input", None) is None:
        app.pan_max_input = QSpinBox()
    try:
        try:
            app._safe_widget_call("pan_max_input", "setRange", 0, 270)
            app._safe_widget_call("pan_max_input", "setValue", app.PAN_MAX)
        except Exception:
            pass
    except Exception:
        pass
    limits_layout.addWidget(app.pan_max_input, 1, 1)
    limits_layout.addWidget(QLabel("TILT Min:"), 2, 0)
    if getattr(app, "tilt_min_input", None) is None:
        app.tilt_min_input = QSpinBox()
    try:
        try:
            app._safe_widget_call("tilt_min_input", "setRange", 0, 180)
            app._safe_widget_call("tilt_min_input", "setValue", app.TILT_MIN)
        except Exception:
            pass
    except Exception:
        pass
    limits_layout.addWidget(app.tilt_min_input, 2, 1)
    limits_layout.addWidget(QLabel("TILT Max:"), 3, 0)
    if getattr(app, "tilt_max_input", None) is None:
        app.tilt_max_input = QSpinBox()
    try:
        try:
            app._safe_widget_call("tilt_max_input", "setRange", 0, 180)
            app._safe_widget_call("tilt_max_input", "setValue", app.TILT_MAX)
        except Exception:
            pass
    except Exception:
        pass
    limits_layout.addWidget(app.tilt_max_input, 3, 1)
    if getattr(app, "apply_limits_button", None) is None:
        app.apply_limits_button = QPushButton("Apply New Limits")
    try:
        apply_btn = getattr(app, "apply_limits_button", None)
        if apply_btn is not None:
            try:
                try:
                    app._safe_connect(
                        "apply_limits_button", "clicked", app.apply_new_limits
                    )
                except Exception:
                    try:
                        try:
                            if not app._safe_connect_path(
                                "apply_limits_btn", "clicked", app.apply_new_limits
                            ):
                                try:
                                    try:
                                        if not app._safe_connect(
                                            "apply_btn", "clicked", app.apply_new_limits
                                        ):
                                            try:
                                                try:
                                                    if not app._safe_connect(
                                                        "apply_limits_button",
                                                        "clicked",
                                                        app.apply_new_limits,
                                                    ):
                                                        pass
                                                except Exception:
                                                    pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    except Exception:
                        pass
            except Exception:
                pass
    except Exception:
        pass
    limits_layout.addWidget(app.apply_limits_button, 4, 0, 1, 2)
    limits_group.setLayout(limits_layout)

    # Target Detection
    detection_group = QGroupBox("Target Detection Settings")
    detection_layout = QGridLayout()
    detection_layout.setSpacing(6)
    detection_layout.setContentsMargins(8, 8, 8, 8)
    # row index for grid
    r = 0

    # Camera selection combo
    if getattr(app, "camera_index_combo", None) is None:
        app.camera_index_combo = QComboBox()
    try:
        if app.camera_index_combo.count() == 0:
            # 'Auto' will let the app try indices 0..4; otherwise pick an index
            app.camera_index_combo.addItems(["Auto", "0", "1", "2", "3", "4"])
        combo = getattr(app, "camera_index_combo", None)
        if combo is not None:
            try:
                try:
                    # connect via safe helper to avoid attribute-on-None and analyzer warnings
                    app._safe_connect(
                        "camera_index_combo", "currentIndexChanged", app.save_settings
                    )
                except Exception:
                    try:
                        try:
                            if not app._safe_connect(
                                "combo", "currentIndexChanged", app.save_settings
                            ):
                                try:
                                    try:
                                        if not app._safe_connect(
                                            "combo",
                                            "currentIndexChanged",
                                            app.save_settings,
                                        ):
                                            try:
                                                try:
                                                    if not app._safe_connect(
                                                        "camera_index_combo",
                                                        "currentIndexChanged",
                                                        app.save_settings,
                                                    ):
                                                        pass
                                                except Exception:
                                                    pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    except Exception:
                        pass
            except Exception:
                pass
    except Exception:
        pass

    # initialize target pan/tilt from HOME inputs (safe helpers)
    try:
        app.target_pan = app._safe_int_widget_value("home_pan_input", app.HOME_PAN)
        app.target_tilt = app._safe_int_widget_value("home_tilt_input", app.HOME_TILT)
    except Exception:
        pass

    if getattr(app, "threshold_input", None) is None:
        app.threshold_input = QSpinBox()
    try:
        app._safe_widget_call("threshold_input", "setRange", 0, 255)
        app._safe_widget_call("threshold_input", "setValue", 40)
        app._safe_connect("threshold_input", "valueChanged", app.save_settings)
    except Exception:
        pass
    # Ensure the threshold label is present (fix missing label in screenshot)
    detection_layout.addWidget(QLabel("Detection Threshold:"), r, 0)
    detection_layout.addWidget(app.threshold_input, r, 1)
    r += 1

    detection_layout.addWidget(QLabel("Blur Kernel Size (odd num):"), r, 0)
    if getattr(app, "blur_kernel_input", None) is None:
        app.blur_kernel_input = QSpinBox()
    try:
        try:
            app._safe_widget_call("blur_kernel_input", "setRange", 1, 21)
            app._safe_widget_call("blur_kernel_input", "setSingleStep", 2)
            app._safe_widget_call("blur_kernel_input", "setValue", 5)
            app._safe_connect("blur_kernel_input", "valueChanged", app.save_settings)
        except Exception:
            pass
    except Exception:
        pass
    detection_layout.addWidget(app.blur_kernel_input, r, 1)
    r += 1

    detection_layout.addWidget(QLabel("Dilation Iterations:"), r, 0)
    if getattr(app, "dilate_iter_input", None) is None:
        app.dilate_iter_input = QSpinBox()
    try:
        try:
            app._safe_widget_call("dilate_iter_input", "setRange", 1, 10)
            app._safe_widget_call("dilate_iter_input", "setValue", 2)
            app._safe_connect("dilate_iter_input", "valueChanged", app.save_settings)
        except Exception:
            pass
    except Exception:
        pass
    detection_layout.addWidget(app.dilate_iter_input, r, 1)
    r += 1

    detection_layout.addWidget(QLabel("Detection Mode:"), r, 0)
    if getattr(app, "detection_mode_combo", None) is None:
        app.detection_mode_combo = QComboBox()
    try:
        try:
            if app.detection_mode_combo.count() == 0:
                app._safe_widget_call(
                    "detection_mode_combo",
                    "addItems",
                    ["Frame Difference", "Background Subtraction", "YOLO Object Detection"],
                )
        except Exception:
            pass
        try:
            dcombo = getattr(app, "detection_mode_combo", None)
            if dcombo is not None:
                try:
                    app._safe_connect(
                        "detection_mode_combo", "currentIndexChanged", app.save_settings
                    )
                except Exception:
                    try:
                        try:
                            if not app._safe_connect(
                                "dcombo", "currentIndexChanged", app.save_settings
                            ):
                                try:
                                    try:
                                        if not app._safe_connect(
                                            "dcombo",
                                            "currentIndexChanged",
                                            app.save_settings,
                                        ):
                                            try:
                                                try:
                                                    if not app._safe_connect(
                                                        "detection_mode_combo",
                                                        "currentIndexChanged",
                                                        app.save_settings,
                                                    ):
                                                        pass
                                                except Exception:
                                                    pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    except Exception:
                        pass
                try:
                    app._safe_connect(
                        "detection_mode_combo",
                        "currentIndexChanged",
                        app.on_detection_mode_change,
                    )
                except Exception:
                    try:
                        try:
                            if not app._safe_connect(
                                "dcombo",
                                "currentIndexChanged",
                                app.on_detection_mode_change,
                            ):
                                try:
                                    try:
                                        if not app._safe_connect(
                                            "dcombo",
                                            "currentIndexChanged",
                                            app.on_detection_mode_change,
                                        ):
                                            try:
                                                try:
                                                    if not app._safe_connect(
                                                        "detection_mode_combo",
                                                        "currentIndexChanged",
                                                        app.on_detection_mode_change,
                                                    ):
                                                        pass
                                                except Exception:
                                                    pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    except Exception:
                        pass
        except Exception:
            pass
    except Exception:
        pass
    detection_layout.addWidget(app.detection_mode_combo, r, 1)
    r += 1
    # Debug toggle: gate verbose pipeline prints
    if getattr(app, "debug_checkbox", None) is None:
        app.debug_checkbox = QCheckBox("Debug")
    try:
        # default off; preserve across sessions
        app._safe_connect("debug_checkbox", "stateChanged", app.save_settings)
        app._safe_widget_call("debug_checkbox", "setChecked", False)
    except Exception:
        pass
    # Warmup frames for BackgroundSubtractor (skip detections while building background)
    detection_layout.addWidget(QLabel("BackSub Warmup Frames:"), r, 0)
    if getattr(app, "backsub_warmup_input", None) is None:
        app.backsub_warmup_input = QSpinBox()
    try:
        app._safe_widget_call("backsub_warmup_input", "setRange", 0, 300)
        app._safe_widget_call("backsub_warmup_input", "setValue", 30)
        app._safe_connect("backsub_warmup_input", "valueChanged", app.save_settings)
    except Exception:
        pass
    detection_layout.addWidget(app.backsub_warmup_input, r, 1)
    r += 1

    detection_layout.addWidget(app.debug_checkbox, r, 1)
    r += 1
    detection_group.setLayout(detection_layout)

    # YOLO settings
    if getattr(app, "yolo_settings_group", None) is None:
        app.yolo_settings_group = QGroupBox("YOLO Settings")
    yolo_layout = QGridLayout()
    yolo_layout.setSpacing(6)
    yolo_layout.setContentsMargins(8, 8, 8, 8)
    y = 0
    yolo_layout.addWidget(QLabel("YOLO Model:"), y, 0)
    if getattr(app, "yolo_model_combo", None) is None:
        app.yolo_model_combo = QComboBox()
    try:
        try:
            models = app.yolo_detector.find_models()
        except Exception:
            models = []
        try:
            if app.yolo_model_combo.count() == 0:
                app._safe_widget_call("yolo_model_combo", "addItems", models)
        except Exception:
            pass
        try:
            ycombo = getattr(app, "yolo_model_combo", None)
            if ycombo is not None:
                try:
                    app._safe_connect(
                        "yolo_model_combo", "currentIndexChanged", app.save_settings
                    )
                except Exception:
                    try:
                        try:
                            if not app._safe_connect(
                                "ycombo", "currentIndexChanged", app.save_settings
                            ):
                                try:
                                    try:
                                        if not app._safe_connect(
                                            "ycombo",
                                            "currentIndexChanged",
                                            app.save_settings,
                                        ):
                                            try:
                                                try:
                                                    if not app._safe_connect(
                                                        "yolo_model_combo",
                                                        "currentIndexChanged",
                                                        app.save_settings,
                                                    ):
                                                        pass
                                                except Exception:
                                                    pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    except Exception:
                        pass
                try:
                    app._safe_connect(
                        "yolo_model_combo",
                        "currentIndexChanged",
                        app.on_yolo_model_changed,
                    )
                except Exception:
                    try:
                        try:
                            if not app._safe_connect(
                                "ycombo",
                                "currentIndexChanged",
                                app.on_yolo_model_changed,
                            ):
                                try:
                                    try:
                                        if not app._safe_connect(
                                            "ycombo",
                                            "currentIndexChanged",
                                            app.on_yolo_model_changed,
                                        ):
                                            try:
                                                try:
                                                    if not app._safe_connect(
                                                        "yolo_model_combo",
                                                        "currentIndexChanged",
                                                        app.on_yolo_model_changed,
                                                    ):
                                                        pass
                                                except Exception:
                                                    pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    except Exception:
                        pass
        except Exception:
            pass
    except Exception:
        pass
    yolo_layout.addWidget(app.yolo_model_combo, y, 1)
    y += 1
    # Add a button to open the external YOLO Trainer window
    try:
        if getattr(app, "open_trainer_btn", None) is None:
            app.open_trainer_btn = QPushButton("Open YOLO Trainer")
        try:
            obtn = getattr(app, "open_trainer_btn", None)
            if obtn is not None:
                try:
                    app._safe_connect("open_trainer_btn", "clicked", app.open_yolo_trainer)
                except Exception:
                    try:
                        try:
                            if not app._safe_connect_path(
                                "open_trainer_btn", "clicked", app.open_yolo_trainer
                            ):
                                try:
                                    try:
                                        if not app._safe_connect(
                                            "obtn", "clicked", app.open_yolo_trainer
                                        ):
                                            try:
                                                try:
                                                    if not app._safe_connect(
                                                        "open_trainer_btn",
                                                        "clicked",
                                                        app.open_yolo_trainer,
                                                    ):
                                                        pass
                                                except Exception:
                                                    pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    except Exception:
                        pass
        except Exception:
            pass
        yolo_layout.addWidget(app.open_trainer_btn, y, 1)
        y += 1
    except Exception:
        pass
    yolo_layout.addWidget(QLabel("Confidence Threshold:"), y, 0)
    if getattr(app, "yolo_confidence_input", None) is None:
        app.yolo_confidence_input = QDoubleSpinBox()
        try:
            yc = getattr(app, "yolo_confidence_input", None)
            if yc is not None:
                try:
                    try:
                        app._safe_widget_call("yolo_confidence_input", "setRange", 0.1, 1.0)
                        app._safe_widget_call(
                            "yolo_confidence_input", "setSingleStep", 0.05
                        )
                        app._safe_widget_call("yolo_confidence_input", "setValue", 0.5)
                        app._safe_connect(
                            "yolo_confidence_input", "valueChanged", app.save_settings
                        )
                    except Exception:
                        pass
                except Exception:
                    pass
        except Exception:
            pass
    yolo_layout.addWidget(app.yolo_confidence_input, y, 1)
    y += 1
    yolo_layout.addWidget(QLabel("Target Classes (csv):"), y, 0)
    if getattr(app, "yolo_classes_input", None) is None:
        app.yolo_classes_input = QLineEdit()
    try:
        yc2 = getattr(app, "yolo_classes_input", None)
        if yc2 is not None:
            try:
                if not yc2.text():
                    try:
                        app._safe_widget_call("yolo_classes_input", "setText", "person")
                    except Exception:
                        pass
                try:
                    try:
                        app._safe_connect(
                            "yolo_classes_input", "textChanged", app.save_settings
                        )
                    except Exception:
                        try:
                            if not app._safe_connect_path(
                                "yclass_input", "textChanged", app.save_settings
                            ):
                                try:
                                    try:
                                        if not app._safe_connect(
                                            "yc2", "textChanged", app.save_settings
                                        ):
                                            try:
                                                try:
                                                    if not app._safe_connect(
                                                        "yolo_classes_input",
                                                        "textChanged",
                                                        app.save_settings,
                                                    ):
                                                        pass
                                                except Exception:
                                                    pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                except Exception:
                    pass
            except Exception:
                pass
    except Exception:
        pass
    # Place the text field and a small chooser button side-by-side
    try:
        if getattr(app, "yolo_pick_classes_btn", None) is None:
            app.yolo_pick_classes_btn = QPushButton("Pick...")
            try:
                app.yolo_pick_classes_btn.clicked.connect(app.open_yolo_class_picker)
            except Exception:
                pass
        container = QWidget()
        h = QHBoxLayout()
        h.setContentsMargins(0, 0, 0, 0)
        h.addWidget(app.yolo_classes_input)
        h.addWidget(app.yolo_pick_classes_btn)
        container.setLayout(h)
        yolo_layout.addWidget(container, y, 1)
        y += 1
    except Exception:
        # Fallback: add only the text field
        yolo_layout.addWidget(app.yolo_classes_input, y, 1)
        y += 1
    app.yolo_settings_group.setLayout(yolo_layout)

    # Behavior group
    if getattr(app, "behavior_group", None) is None:
        app.behavior_group = QGroupBox("Tracking Behavior")
    behavior_group = app.behavior_group
    behavior_layout = QGridLayout()
    behavior_layout.setSpacing(6)
    behavior_layout.setContentsMargins(8, 8, 8, 8)
    br = 0
    behavior_layout.addWidget(QLabel("Tracking Speed"), br, 0)
    speed_row = QHBoxLayout()
    if getattr(app, "tracking_speed_slider", None) is None:
        app.tracking_speed_slider = QSlider()
        try:
            try:
                app.tracking_speed_slider.setOrientation(
                    cast(Any, app._qt_enum("Horizontal", 1))
                )
            except Exception:
                pass
        except Exception:
            pass
    try:
        try:
            app._safe_widget_call("tracking_speed_slider", "setRange", 1, 100)
            app._safe_widget_call("tracking_speed_slider", "setValue", 40)
            app._safe_connect(
                "tracking_speed_slider", "valueChanged", app.save_settings
            )
        except Exception:
            pass
    except Exception:
        pass
    if getattr(app, "tracking_speed_label", None) is None:
        try:
            cur_val = app._safe_int_widget_value("tracking_speed_slider", 40)
        except Exception:
            cur_val = 40
        app.tracking_speed_label = QLabel(f"{cur_val}%")
    try:
        try:
            app.tracking_speed_label.setFixedWidth(40)
            app._safe_connect(
                "tracking_speed_slider",
                "valueChanged",
                lambda v: app.tracking_speed_label.setText(f"{v}%"),
            )
        except Exception:
            pass
    except Exception:
        pass
    speed_row.addWidget(app.tracking_speed_slider)
    speed_row.addWidget(app.tracking_speed_label)
    behavior_layout.addLayout(speed_row, br, 1)
    br += 1

    # movement sensitivity
    behavior_layout.addWidget(QLabel("Movement Sensitivity"), br, 0)
    sensitivity_row = QHBoxLayout()
    if getattr(app, "movement_sensitivity_slider", None) is None:
        app.movement_sensitivity_slider = QSlider()
        try:
            try:
                app.movement_sensitivity_slider.setOrientation(
                    cast(Any, app._qt_enum("Horizontal", 1))
                )
            except Exception:
                pass
        except Exception:
            pass
    try:
        try:
            app._safe_widget_call("movement_sensitivity_slider", "setRange", 1, 100)
            app._safe_widget_call("movement_sensitivity_slider", "setValue", 25)
            app._safe_connect(
                "movement_sensitivity_slider", "valueChanged", app.save_settings
            )
        except Exception:
            pass
    except Exception:
        pass
    if getattr(app, "movement_sensitivity_label", None) is None:
        app.movement_sensitivity_label = QLabel("25%")
    try:
        try:
            app.movement_sensitivity_label.setFixedWidth(40)
            app._safe_connect(
                "movement_sensitivity_slider",
                "valueChanged",
                lambda v: app.movement_sensitivity_label.setText(f"{v}%"),
            )
        except Exception:
            pass
    except Exception:
        pass
    sensitivity_row.addWidget(app.movement_sensitivity_slider)
    sensitivity_row.addWidget(app.movement_sensitivity_label)
    behavior_layout.addLayout(sensitivity_row, br, 1)
    br += 1

    # smoothing
    behavior_layout.addWidget(QLabel("Smoothing (0.0 - 1.0):"), br, 0)
    if getattr(app, "smoothing_input", None) is None:
        app.smoothing_input = QDoubleSpinBox()
    try:
        try:
            app._safe_widget_call("smoothing_input", "setRange", 0.0, 1.0)
            app._safe_widget_call("smoothing_input", "setSingleStep", 0.05)
            app._safe_widget_call("smoothing_input", "setValue", 0.95)
            app._safe_connect("smoothing_input", "valueChanged", app.save_settings)
        except Exception:
            pass
    except Exception:
        pass
    behavior_layout.addWidget(app.smoothing_input, br, 1)
    br += 1

    # overshoot percentage: allow small intentional overshoot compensation
    behavior_layout.addWidget(QLabel("Overshoot (%):"), br, 0)
    if getattr(app, "overshoot_input", None) is None:
        app.overshoot_input = QSpinBox()
    try:
        try:
            app._safe_widget_call("overshoot_input", "setRange", -100, 100)
            app._safe_widget_call("overshoot_input", "setValue", 0)
            app._safe_connect("overshoot_input", "valueChanged", app.save_settings)
        except Exception:
            pass
    except Exception:
        pass
    try:
        app.overshoot_input.setToolTip(
            "Percent overshoot applied to motion gain; positive = more aggressive."
        )
    except Exception:
        pass
    behavior_layout.addWidget(app.overshoot_input, br, 1)
    br += 1

    # deadzone and snap
    behavior_layout.addWidget(QLabel("Deadzone (pixels)"), br, 0)
    deadzone_row = QHBoxLayout()
    if getattr(app, "deadzone_slider", None) is None:
        app.deadzone_slider = QSlider()
        try:
            try:
                app.deadzone_slider.setOrientation(
                    cast(Any, app._qt_enum("Horizontal", 1))
                )
            except Exception:
                pass
        except Exception:
            pass
    try:
        try:
            app._safe_widget_call("deadzone_slider", "setRange", 0, 200)
            app._safe_widget_call("deadzone_slider", "setValue", 20)
            app._safe_connect("deadzone_slider", "valueChanged", app.save_settings)
        except Exception:
            pass
    except Exception:
        pass
    if getattr(app, "deadzone_label", None) is None:
        try:
            dz = app._safe_int_widget_value("deadzone_slider", 20)
        except Exception:
            dz = 20
        app.deadzone_label = QLabel(str(dz))
    try:
        try:
            app.deadzone_label.setFixedWidth(40)
            app._safe_connect(
                "deadzone_slider",
                "valueChanged",
                lambda v: app.deadzone_label.setText(str(v)),
            )
        except Exception:
            pass
    except Exception:
        pass
    deadzone_row.addWidget(app.deadzone_slider)
    deadzone_row.addWidget(app.deadzone_label)
    behavior_layout.addLayout(deadzone_row, br, 1)
    br += 1

    behavior_layout.addWidget(QLabel("Snap Threshold (px)"), br, 0)
    snap_row = QHBoxLayout()
    if getattr(app, "snap_threshold_slider", None) is None:
        app.snap_threshold_slider = QSlider()
        try:
            try:
                app.snap_threshold_slider.setOrientation(
                    cast(Any, app._qt_enum("Horizontal", 1))
                )
            except Exception:
                pass
        except Exception:
            pass
    try:
        if getattr(app, "snap_threshold_slider", None) is not None:
            try:
                app._safe_widget_call("snap_threshold_slider", "setRange", 0, 400)
                app._safe_widget_call("snap_threshold_slider", "setValue", 80)
                try:
                    try:
                        app._safe_connect(
                            "snap_threshold_slider", "valueChanged", app.save_settings
                        )
                    except Exception:
                        try:
                            if not app._safe_connect(
                                "snap_threshold_slider",
                                "valueChanged",
                                app.save_settings,
                            ):
                                try:
                                    try:
                                        if not app._safe_connect(
                                            "snap_threshold_slider",
                                            "valueChanged",
                                            app.save_settings,
                                        ):
                                            try:
                                                try:
                                                    if not app._safe_connect(
                                                        "snap_threshold_slider",
                                                        "valueChanged",
                                                        app.save_settings,
                                                    ):
                                                        pass
                                                except Exception:
                                                    pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                except Exception:
                    pass
            except Exception:
                pass
    except Exception:
        pass
    if getattr(app, "snap_threshold_label", None) is None:
        try:
            sv = app._safe_int_widget_value("snap_threshold_slider", 80)
        except Exception:
            sv = 80
        app.snap_threshold_label = QLabel(str(sv))
    try:
        app.snap_threshold_label.setFixedWidth(40)
        try:
            app._safe_connect(
                "snap_threshold_slider",
                "valueChanged",
                lambda v: app.snap_threshold_label.setText(str(v)),
            )
        except Exception:
            try:
                try:
                    if not app._safe_connect(
                        "snap_threshold_slider",
                        "valueChanged",
                        lambda v: app.snap_threshold_label.setText(str(v)),
                    ):
                        try:
                            try:
                                if not app._safe_connect(
                                    "snap_threshold_slider",
                                    "valueChanged",
                                    lambda v: app.snap_threshold_label.setText(str(v)),
                                ):
                                    try:
                                        try:
                                            if not app._safe_connect(
                                                "snap_threshold_slider",
                                                "valueChanged",
                                                lambda v: app.snap_threshold_label.setText(
                                                    str(v)
                                                ),
                                            ):
                                                pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                        except Exception:
                            pass
                except Exception:
                    pass
            except Exception:
                pass
    except Exception:
        pass
    snap_row.addWidget(app.snap_threshold_slider)
    snap_row.addWidget(app.snap_threshold_label)
    behavior_layout.addLayout(snap_row, br, 1)
    br += 1

    # Hold target position for a configurable time after detection loss
    behavior_layout.addWidget(QLabel("Hold target on loss (s):"), br, 0)
    if getattr(app, "lost_hold_input", None) is None:
        app.lost_hold_input = QDoubleSpinBox()
    try:
        if getattr(app, "lost_hold_input", None) is not None:
            try:
                app._safe_widget_call("lost_hold_input", "setRange", 0.0, 60.0)
                app._safe_widget_call("lost_hold_input", "setSingleStep", 0.5)
                try:
                    app._safe_widget_call(
                        "lost_hold_input",
                        "setValue",
                        getattr(app, "lost_hold_seconds", 5.0),
                    )
                except Exception:
                    pass
                try:
                    try:
                        app._safe_connect(
                            "lost_hold_input",
                            "valueChanged",
                            lambda v: setattr(app, "lost_hold_seconds", float(v))
                            or app.save_settings(),
                        )
                    except Exception:
                        try:
                            if not app._safe_connect(
                                "lost_hold_input",
                                "valueChanged",
                                lambda v: setattr(app, "lost_hold_seconds", float(v))
                                or app.save_settings(),
                            ):
                                try:
                                    try:
                                        if not app._safe_connect(
                                            "lost_hold_input",
                                            "valueChanged",
                                            lambda v: (
                                                setattr(app, "lost_hold_seconds", float(v)),
                                                app.save_settings(),
                                            ),
                                        ):
                                            try:
                                                try:
                                                    if not app._safe_connect(
                                                        "lost_hold_input",
                                                        "valueChanged",
                                                        lambda v: (
                                                            setattr(
                                                                app,
                                                                "lost_hold_seconds",
                                                                float(v),
                                                            ),
                                                            app.save_settings(),
                                                        ),
                                                    ):
                                                        pass
                                                except Exception:
                                                    pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                except Exception:
                    pass
                try:
                    app._safe_widget_call(
                        "lost_hold_input",
                        "setToolTip",
                        "When target is lost, keep aiming at the last known position for this many seconds (0 = disable).",
                    )
                except Exception:
                    pass
            except Exception:
                pass
    except Exception:
        pass
    # 'Hold indefinitely' checkbox (when checked, never timeout the hold)
    try:
        if getattr(app, "hold_infinite_checkbox", None) is None:
            app.hold_infinite_checkbox = QCheckBox("Hold indefinitely (no timeout)")
        hic = getattr(app, "hold_infinite_checkbox", None)
        if hic is not None:
            try:
                try:
                    try:
                        app._safe_connect(
                            "hold_infinite_checkbox",
                            "stateChanged",
                            lambda s: setattr(app, "hold_infinite", bool(s)),
                        )
                    except Exception:
                        try:
                            try:
                                if not app._safe_connect(
                                    "hic",
                                    "stateChanged",
                                    lambda s: setattr(app, "hold_infinite", bool(s)),
                                ):
                                    try:
                                        try:
                                            if not app._safe_connect(
                                                "hic",
                                                "stateChanged",
                                                lambda s: setattr(
                                                    app, "hold_infinite", bool(s)
                                                ),
                                            ):
                                                try:
                                                    try:
                                                        if not app._safe_connect(
                                                            "hold_infinite_checkbox",
                                                            "stateChanged",
                                                            lambda s: setattr(
                                                                app,
                                                                "hold_infinite",
                                                                bool(s),
                                                            ),
                                                        ):
                                                            sig = getattr(
                                                                hic, "stateChanged", None
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(
                                                                    lambda s: setattr(
                                                                        app,
                                                                        "hold_infinite",
                                                                        bool(s),
                                                                    )
                                                                )
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                        except Exception:
                            pass
                except Exception:
                    pass
                try:
                    try:
                        app._safe_connect(
                            "hold_infinite_checkbox", "stateChanged", app.save_settings
                        )
                    except Exception:
                        try:
                            try:
                                if not app._safe_connect(
                                    "hic", "stateChanged", app.save_settings
                                ):
                                    try:
                                        try:
                                            if not app._safe_connect(
                                                "hic", "stateChanged", app.save_settings
                                            ):
                                                try:
                                                    try:
                                                        if not app._safe_connect(
                                                            "hold_infinite_checkbox",
                                                            "stateChanged",
                                                            app.save_settings,
                                                        ):
                                                            sig = getattr(
                                                                hic, "stateChanged", None
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(app.save_settings)
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                        except Exception:
                            pass
                except Exception:
                    pass
                try:
                    hic.setToolTip(
                        "When checked, hold the last known target position indefinitely after loss (no timeout). Use to lock aim at the last seen point."
                    )
                except Exception:
                    pass
            except Exception:
                pass
    except Exception:
        pass
    # place both in same row (spinbox right, checkbox below it)
    behavior_layout.addWidget(app.lost_hold_input, br, 1)
    br += 1
    behavior_layout.addWidget(app.hold_infinite_checkbox, br, 0, 1, 2)
    br += 1

    # some toggles
    if getattr(app, "invert_pan_checkbox", None) is None:
        app.invert_pan_checkbox = QCheckBox("Invert PAN Movement")
    try:
        try:
            app._safe_connect(
                "invert_pan_checkbox",
                "stateChanged",
                lambda s: app.set_flip_pan(bool(s)),
            )
        except Exception:
            try:
                try:
                    if not app._safe_connect(
                        "invert_pan_checkbox",
                        "stateChanged",
                        lambda s: app.set_flip_pan(bool(s)),
                    ):
                        try:
                            try:
                                if not app._safe_connect(
                                    "invert_pan_checkbox",
                                    "stateChanged",
                                    lambda s: app.set_flip_pan(bool(s)),
                                ):
                                    sig = getattr(
                                        app.invert_pan_checkbox, "stateChanged", None
                                    )
                                    pass
                            except Exception:
                                pass
                        except Exception:
                            pass
                except Exception:
                    pass
            except Exception:
                pass
        try:
            app._safe_connect("invert_pan_checkbox", "stateChanged", app.save_settings)
        except Exception:
            try:
                try:
                    if not app._safe_connect(
                        "invert_pan_checkbox", "stateChanged", app.save_settings
                    ):
                        try:
                            try:
                                if not app._safe_connect(
                                    "invert_pan_checkbox",
                                    "stateChanged",
                                    app.save_settings,
                                ):
                                    sig = getattr(
                                        app.invert_pan_checkbox, "stateChanged", None
                                    )
                                    pass
                            except Exception:
                                pass
                        except Exception:
                            pass
                except Exception:
                    pass
            except Exception:
                pass
    except Exception:
        pass
    behavior_layout.addWidget(app.invert_pan_checkbox, br, 0, 1, 2)
    br += 1

    if getattr(app, "invert_tilt_checkbox", None) is None:
        app.invert_tilt_checkbox = QCheckBox("Invert TILT Movement")
    try:
        try:
            app._safe_connect(
                "invert_tilt_checkbox",
                "stateChanged",
                lambda s: app.set_flip_tilt(bool(s)),
            )
        except Exception:
            try:
                try:
                    if not app._safe_connect(
                        "invert_tilt_checkbox",
                        "stateChanged",
                        lambda s: app.set_flip_tilt(bool(s)),
                    ):
                        try:
                            try:
                                if not app._safe_connect(
                                    "invert_tilt_checkbox",
                                    "stateChanged",
                                    lambda s: app.set_flip_tilt(bool(s)),
                                ):
                                    sig = getattr(
                                        app.invert_tilt_checkbox, "stateChanged", None
                                    )
                                    pass
                            except Exception:
                                pass
                        except Exception:
                            pass
                except Exception:
                    pass
            except Exception:
                pass
            try:
                if not app._safe_connect(
                    "invert_tilt_checkbox", "stateChanged", app.save_settings
                ):
                    try:
                        sig = getattr(app.invert_tilt_checkbox, "stateChanged", None)
                        pass
                    except Exception:
                        pass
            except Exception:
                pass
    except Exception:
        pass
    behavior_layout.addWidget(app.invert_tilt_checkbox, br, 0, 1, 2)
    br += 1

    if getattr(app, "flip_checkbox", None) is None:
        app.flip_checkbox = QCheckBox("Flip Frame (180°)")
    try:
        try:
            if not app._safe_connect("flip_checkbox", "stateChanged", app.save_settings):
                try:
                    sig = getattr(app.flip_checkbox, "stateChanged", None)
                    try:
                        app.enhancer.log_serial_output("[UI] Failed to connect flip_checkbox stateChanged", fire=False)
                    except Exception:
                        pass
                except Exception:
                    try:
                        app.enhancer.log_serial_output("[UI] Exception in flip_checkbox connection", fire=False)
                    except Exception:
                        pass
        except Exception:
            try:
                app.enhancer.log_serial_output("[UI] Failed to setup flip_checkbox", fire=False)
            except Exception:
                pass
    except Exception:
        try:
            app.enhancer.log_serial_output("[UI] Outer exception in flip_checkbox setup", fire=False)
        except Exception:
            pass
    behavior_layout.addWidget(app.flip_checkbox, br, 0, 1, 2)
    br += 1

    # presets
    behavior_layout.addWidget(QLabel("Preset:"), br, 0)
    if getattr(app, "preset_combo", None) is None:
        app.preset_combo = QComboBox()
    try:
        if app.preset_combo.count() == 0:
            app.preset_combo.addItems(list(PRESETS.keys()))
        app._safe_connect("preset_combo", "currentIndexChanged", app.apply_preset)
    except Exception:
        pass
    behavior_layout.addWidget(app.preset_combo, br, 1)
    br += 1
    behavior_group.setLayout(behavior_layout)

    # Accessories
    accessory_group = QGroupBox("Accessories")
    accessory_layout = QVBoxLayout()
    accessory_layout.setSpacing(6)
    accessory_layout.setContentsMargins(8, 8, 8, 8)
    if getattr(app, "relay1_button", None) is None:
        app.relay1_button = QPushButton("LED (Relay1): OFF")
    try:
        app.relay1_button.setCheckable(True)
        app._safe_connect("relay1_button", "toggled", lambda checked: app.toggle_relay(1, checked))
    except Exception:
        pass
    accessory_layout.addWidget(app.relay1_button)
    if getattr(app, "relay2_button", None) is None:
        app.relay2_button = QPushButton("LASER (Relay2): OFF")
    try:
        app.relay2_button.setCheckable(True)
        app._safe_connect("relay2_button", "toggled", lambda checked: app.toggle_relay(2, checked))
    except Exception:
        pass
    accessory_layout.addWidget(app.relay2_button)
    accessory_group.setLayout(accessory_layout)

    # Manual Movement & Firing (vertical, wrapped)
    manual_group = QGroupBox("Manual Movement & Firing")
    manual_layout = QVBoxLayout()
    manual_layout.setSpacing(8)
    manual_layout.setContentsMargins(8, 8, 8, 8)
    # step size
    manual_settings = QGridLayout()
    manual_settings.addWidget(QLabel("Step Size:"), 0, 0)
    if getattr(app, "step_size_input", None) is None:
        app.step_size_input = QSpinBox()
    try:
        app.step_size_input.setRange(1, 20)
        app.step_size_input.setValue(app.STEP_INCREMENT)
        app._safe_connect("step_size_input", "valueChanged", app.save_settings)
    except Exception:
        pass
    manual_settings.addWidget(app.step_size_input, 0, 1)
    # manual speed
    manual_settings.addWidget(QLabel("Manual Speed:"), 1, 0)
    speed_row2 = QHBoxLayout()
    if getattr(app, "manual_speed_slider", None) is None:
        app.manual_speed_slider = QSlider()
        try:
            try:
                app.manual_speed_slider.setOrientation(
                    cast(Any, app._qt_enum("Horizontal", 1))
                )
            except Exception:
                pass
        except Exception:
            pass
    try:
        app.manual_speed_slider.setRange(1, 100)
        if getattr(app.manual_speed_slider, "value", None) is None:
            app.manual_speed_slider.setValue(50)
        app._safe_connect("manual_speed_slider", "valueChanged", app.save_settings)
    except Exception:
        pass
    if getattr(app, "manual_speed_label", None) is None:
        app.manual_speed_label = QLabel("50%")
    try:
        app.manual_speed_label.setFixedWidth(40)
        app._safe_connect(
            "manual_speed_slider",
            "valueChanged",
            lambda v: app.manual_speed_label.setText(f"{v}%"),
        )
    except Exception:
        pass
    speed_row2.addWidget(app.manual_speed_slider)
    speed_row2.addWidget(app.manual_speed_label)
    manual_settings.addLayout(speed_row2, 1, 1)
    manual_layout.addLayout(manual_settings)

    # Dpad
    pad_layout = QGridLayout()
    pad_layout.setSpacing(6)
    if getattr(app, "btn_up", None) is None:
        app.btn_up = QPushButton("▲")
    if getattr(app, "btn_down", None) is None:
        app.btn_down = QPushButton("▼")
    if getattr(app, "btn_left", None) is None:
        app.btn_left = QPushButton("◀")
    if getattr(app, "btn_right", None) is None:
        app.btn_right = QPushButton("▶")
    if getattr(app, "btn_center", None) is None:
        app.btn_center = QPushButton("●")
    for b in (app.btn_up, app.btn_down, app.btn_left, app.btn_right, app.btn_center):
        try:
            b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            b.setMinimumSize(28, 28)
            try:
                # Ensure buttons are enabled so manual controls always accept input
                b.setEnabled(True)
            except Exception:
                pass
        except Exception:
            pass
    pad_layout.addWidget(app.btn_up, 0, 1)
    pad_layout.addWidget(app.btn_left, 1, 0)
    pad_layout.addWidget(app.btn_center, 1, 1)
    pad_layout.addWidget(app.btn_right, 1, 2)
    pad_layout.addWidget(app.btn_down, 2, 1)
    # Connect D-pad buttons to manual movement (pressed = start move, released = stop)
    try:
        # Use explicit pan/tilt helpers to avoid any axis mixups.
        # These helpers already read the current step size safely.
        app._safe_connect(
            "btn_up",
            "pressed",
            lambda _=None: app.tilt_up(),
        )
        app._safe_connect("btn_up", "released", app.manual_control_released)
        app._safe_connect(
            "btn_down",
            "pressed",
            lambda _=None: app.tilt_down(),
        )
        app._safe_connect("btn_down", "released", app.manual_control_released)
        app._safe_connect(
            "btn_left",
            "pressed",
            lambda _=None: app.pan_left(),
        )
        app._safe_connect("btn_left", "released", app.manual_control_released)
        app._safe_connect(
            "btn_right",
            "pressed",
            lambda _=None: app.pan_right(),
        )
        app._safe_connect("btn_right", "released", app.manual_control_released)
        app._safe_connect(
            "btn_center", "pressed", lambda _=None: app.move_manual(pan=0, tilt=0)
        )
        app._safe_connect("btn_center", "released", app.manual_control_released)
    except Exception:
        pass
    for i in range(3):
        pad_layout.setRowStretch(i, 1)
        pad_layout.setColumnStretch(i, 1)
    manual_layout.addLayout(pad_layout)

    # position label
    pos_layout = QHBoxLayout()
    if getattr(app, "position_label", None) is None:
        app.position_label = QLabel("Pan: 90° | Tilt: 40°")
    try:
        try:
            app.position_label.setAlignment(cast(Any, getattr(Qt, "AlignCenter", 0)))
        except Exception:
            pass
    except Exception:
        pass
    pos_layout.addWidget(app.position_label)
    manual_layout.addLayout(pos_layout)

    # fire controls
    fire_controls = QGridLayout()
    fire_controls.addWidget(QLabel("Trigger Mode:"), 0, 0)
    if getattr(app, "trigger_mode_combo", None) is None:
        app.trigger_mode_combo = QComboBox()
    try:
        if app.trigger_mode_combo.count() == 0:
            app.trigger_mode_combo.addItem("Water (MOSFET)")
            app.trigger_mode_combo.addItem("Projectile (BB Servo)")
        app._safe_connect("trigger_mode_combo", "currentIndexChanged", app.set_trigger_mode)
    except Exception:
        pass
    fire_controls.addWidget(app.trigger_mode_combo, 0, 1)
    fire_controls.addWidget(QLabel("Auto-Fire Cooldown (s):"), 1, 0)
    if getattr(app, "trigger_cooldown_input", None) is None:
        app.trigger_cooldown_input = QDoubleSpinBox()
    try:
        app.trigger_cooldown_input.setRange(0.1, 10.0)
        app.trigger_cooldown_input.setValue(1.5)
        app._safe_connect("trigger_cooldown_input", "valueChanged", app.save_settings)
    except Exception:
        pass
    fire_controls.addWidget(app.trigger_cooldown_input, 1, 1)
    # NOTE: manual_auto_fire_checkbox removed. Auto-fire is now controlled by the Safety (ARM) button.
    if getattr(app, "safety_button", None) is None:
        app.safety_button = QPushButton("Safety: LOCKED (No Fire)")
    try:
        app.safety_button.setCheckable(True)
        app.safety_button.setChecked(False if getattr(app, "safety_state", 1) == 1 else True)
        app._safe_connect("safety_button", "clicked", app.toggle_safety)
    except Exception:
        pass
    # place safety button in row 2 (single authoritative control for arming/auto-fire)
    fire_controls.addWidget(app.safety_button, 2, 0, 1, 2)
    if getattr(app, "fire_button", None) is None:
        app.fire_button = QPushButton("FIRE (Manual)")
    try:
        app._safe_connect("fire_button", "pressed", lambda: app.set_fire_state(1))
        app._safe_connect("fire_button", "released", lambda: app.set_fire_state(0))
    except Exception:
        pass
    fire_controls.addWidget(app.fire_button, 4, 0, 1, 2)
    manual_layout.addLayout(fire_controls)
    manual_group.setLayout(manual_layout)

    # Serial / Log output
    serial_output_group = QGroupBox("Serial / Log Output")
    serial_output_layout = QVBoxLayout()
    if getattr(app, "serial_output", None) is None:
        app.serial_output = QTextEdit()
    try:
        app.serial_output.setReadOnly(True)
    except Exception:
        pass
    serial_output_layout.addWidget(app.serial_output)
    serial_output_group.setLayout(serial_output_layout)

    # Current monitor (Total mA)
    # Pan/Tilt per-servo sensors are optional; keep UI focused on total current.
    current_group = QGroupBox("System Health Monitor")
    current_layout = QFormLayout()

    if getattr(app, "total_current_sensor_checkbox", None) is None:
        app.total_current_sensor_checkbox = QCheckBox("Total current sensor installed")
    try:
        app.total_current_sensor_checkbox.setChecked(
            bool(getattr(app, "total_current_sensor_enabled", False))
        )
    except Exception:
        pass
    try:
        if hasattr(app, "_safe_connect"):
            app._safe_connect(
                "total_current_sensor_checkbox",
                "toggled",
                getattr(app, "set_total_current_sensor_enabled"),
            )
        else:
            app.total_current_sensor_checkbox.toggled.connect(
                getattr(app, "set_total_current_sensor_enabled")
            )
    except Exception:
        pass

    if getattr(app, "total_current_label", None) is None:
        app.total_current_label = QLabel("—")

    current_layout.addRow(app.total_current_sensor_checkbox)
    current_layout.addRow(QLabel("Total (mA):"), app.total_current_label)

    # Add Health Graph (custom visualizer)
    if getattr(app, "health_graph", None) is None:
        app.health_graph = HealthGraphWidget()
    current_layout.addRow(app.health_graph)

    # Add FPS Graph
    current_layout.addRow(QLabel("System Performance (FPS):"))
    if getattr(app, "fps_graph", None) is None:
        app.fps_graph = HealthGraphWidget(max_val=60)
    current_layout.addRow(app.fps_graph)

    # Add Servo Load Graph (New)
    current_layout.addRow(QLabel("Servo Load (Internal):"))
    if getattr(app, "servo_load_graph", None) is None:
        # Load is roughly 0-1000 range
        app.servo_load_graph = HealthGraphWidget(max_val=1000)
    current_layout.addRow(app.servo_load_graph)

    current_group.setLayout(current_layout)

    def _update_current_monitor_labels():
        try:
            total = getattr(app, "total_current_mA", None)
            enabled = bool(getattr(app, "total_current_sensor_enabled", False))

            try:
                if not enabled:
                    app.total_current_label.setText("Disabled")
                    if hasattr(app, "health_graph"):
                         app.health_graph.push_data(0)
                else:
                    app.total_current_label.setText("—" if total is None else f"{int(total)}")
                    if hasattr(app, "health_graph"):
                         app.health_graph.push_data(0 if total is None else total)
                
                # Update FPS Graph
                if hasattr(app, "fps_graph"):
                    fps = getattr(app, "measured_fps_val", 0)
                    app.fps_graph.push_data(fps)

                # Update Servo Load Graph
                if hasattr(app, "servo_load_graph"):
                    # Sum of pan and tilt load
                    pan_load = getattr(app, "pan_load_val", 0) or 0
                    tilt_load = getattr(app, "tilt_load_val", 0) or 0
                    app.servo_load_graph.push_data(pan_load + tilt_load)

            except Exception:
                pass
        except Exception:
            pass

    try:
        if getattr(app, "current_monitor_timer", None) is None:
            app.current_monitor_timer = QTimer(app)
        # Best-effort safe connect (connect once)
        try:
            if not bool(getattr(app, "_current_monitor_timer_connected", False)):
                if hasattr(app, "_safe_connect"):
                    app._safe_connect(
                        "current_monitor_timer", "timeout", _update_current_monitor_labels
                    )
                else:
                    app.current_monitor_timer.timeout.connect(_update_current_monitor_labels)
                app._current_monitor_timer_connected = True
        except Exception:
            try:
                if not bool(getattr(app, "_current_monitor_timer_connected", False)):
                    app.current_monitor_timer.timeout.connect(_update_current_monitor_labels)
                    app._current_monitor_timer_connected = True
            except Exception:
                pass
        try:
            app.current_monitor_timer.start(200)
        except Exception:
            pass
    except Exception:
        pass

    # System status group
    status_group = QGroupBox("System")
    status_layout = QVBoxLayout()
    if getattr(app, "save_layout_btn", None) is None:
        app.save_layout_btn = QPushButton("Save Layout")
    try:
        app._safe_connect("save_layout_btn", "clicked", app.save_dock_layout)
    except Exception:
        pass
    status_layout.addWidget(app.save_layout_btn)
    if getattr(app, "reset_layout_btn", None) is None:
        app.reset_layout_btn = QPushButton("Reset Layout")
    try:
        app._safe_connect("reset_layout_btn", "clicked", app.reset_layout)
    except Exception:
        pass
    status_layout.addWidget(app.reset_layout_btn)
    status_group.setLayout(status_layout)

    # Wrap behavior and manual groups in scroll areas for tall content
    try:
        behavior_scroll = QScrollArea()
        behavior_scroll.setWidget(behavior_group)
        behavior_scroll.setWidgetResizable(True)
    except Exception:
        behavior_scroll = behavior_group
    try:
        manual_scroll = QScrollArea()
        manual_scroll.setWidget(manual_group)
        manual_scroll.setWidgetResizable(True)
    except Exception:
        manual_scroll = manual_group

    # Add docks (use add_dock helper to avoid duplicates)
    try:
        app.add_dock("Configuration & Connection", settings_group, "left")
        app.add_dock("Home Position", home_group, "left")
        app.add_dock("Servo Limits", limits_group, "left")
        app.add_dock("Accessories", accessory_group, "left")

        app.add_dock("Target Detection", detection_group, "right")
        app.add_dock("YOLO Settings", app.yolo_settings_group, "right")
        app.add_dock("Tracking Behavior", behavior_scroll, "right")
        app.add_dock("Manual Movement & Firing", manual_scroll, "right")
        app.add_dock("System Health Monitor", current_group, "right")
        app.add_dock("Serial / Log Output", serial_output_group, "right")
        app.add_dock("System", status_group, "right")
        try:
            # sniper dock - REMOVED (Dec 2024)
            # All sniper dock docking code has been disabled
            pass
        except Exception:
            pass
    except Exception:
        pass

    # Dock behavior: allow nesting and tabbing
    try:
        app.setDockOptions(
            QMainWindow.AllowNestedDocks
            | QMainWindow.AllowTabbedDocks
            | QMainWindow.AnimatedDocks
        )
    except Exception:
        pass

    # Ensure equal starting column widths (non-destructive)
    try:
        QTimer.singleShot(250, lambda: app.equalize_dock_columns())
        # Ensure default stacked two-column layout after docks are created
        try:
            QTimer.singleShot(300, lambda: app.enforce_default_dock_layout())
        except Exception:
            pass
    except Exception:
        pass

    # Final window size
    try:
        app.setMinimumSize(1200, 800)
        app.setGeometry(100, 100, 1200, 800)
    except Exception:
        pass

    # Add a simple menu for diagnostics: Logging on/off and Dump Logs
    try:
        menubar = app.menuBar()
        tools_menu = None
        if menubar is not None:
            try:
                tools_menu = menubar.addMenu("Tools")
            except Exception:
                tools_menu = None

        if tools_menu is not None:
            app.toggle_log_action = cast(Any, tools_menu.addAction("Disable State Logging"))
            try:
                app.toggle_log_action.setCheckable(True)
            except Exception:
                pass
            try:
                app.toggle_log_action.setChecked(False)
            except Exception:
                pass

            def _toggle_log(checked):
                try:
                    enabled = not checked
                    app.state_logger.enable(enabled)
                    try:
                        app.toggle_log_action.setText(
                            "Enable State Logging" if not enabled else "Disable State Logging"
                        )
                    except Exception:
                        pass
                except Exception:
                    pass

            try:
                if not app._safe_connect_path("toggle_log_action", "toggled", _toggle_log):
                    try:
                        conn = getattr(app.toggle_log_action, "toggled", None)
                        if conn is not None:
                            try:
                                c = getattr(conn, "connect", None)
                                if callable(c):
                                    c(_toggle_log)
                            except Exception:
                                pass
                    except Exception:
                        pass
            except Exception:
                pass

            app.dump_logs_action = cast(
                Any, tools_menu.addAction("Dump State Log to file...")
            )

            def _dump_logs():
                # Ask for a default filename in the repo root (stable location)
                try:
                    repo_root = os.path.dirname(app.SETTINGS_FILE)
                    fname = os.path.join(repo_root, "state_log.txt")
                    app.state_logger.dump_to_file(fname, append=False)
                    try:
                        app.enhancer.log_serial_output(
                            f"State log dumped to: {fname}", fire=False
                        )
                    except Exception:
                        pass
                except Exception as e:
                    try:
                        app.enhancer.log_serial_output(
                            f"State log dump failed: {e}", fire=False
                        )
                    except Exception:
                        pass

            try:
                if not app._safe_connect_path("dump_logs_action", "triggered", _dump_logs):
                    try:
                        conn2 = getattr(app.dump_logs_action, "triggered", None)
                        if conn2 is not None:
                            try:
                                c2 = getattr(conn2, "connect", None)
                                if callable(c2):
                                    c2(_dump_logs)
                            except Exception:
                                pass
                    except Exception:
                        pass
            except Exception:
                pass
    except Exception:
        pass

    # Attach enhancer helpers
    try:
        if hasattr(app, "enhancer"):
            try:
                app.enhancer.attach_serial_console(app.serial_output)
            except Exception:
                pass
            try:
                app.enhancer.style_toggle_button(getattr(app, "safety_button", None))
                app.enhancer.style_toggle_button(getattr(app, "relay1_button", None))
                app.enhancer.style_toggle_button(getattr(app, "relay2_button", None))
            except Exception:
                pass
    except Exception:
        pass