"""
YOLO Trainer Window
===================
Standalone PyQt5 application for training custom YOLO object detection models.

Features:
- Dataset selection and validation
- Training parameter configuration
- Real-time training progress monitoring
- Model export and integration with main turret app

Dependencies:
- PyQt5
- ultralytics (YOLO)
- OpenCV
- NumPy
- pathlib

Usage:
    python yolo_trainer_window.py
    or import from main app: from yolo_trainer_window import YoloTrainerWindow
"""

import os
import sys
import json
import subprocess
import threading
from pathlib import Path
from typing import Optional, Dict, Any

import cv2
import numpy as np
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QObject, QThread
from PyQt5.QtGui import QFont, QPixmap, QImage, QIcon
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QGroupBox, QLabel, QPushButton, QLineEdit,
    QSpinBox, QDoubleSpinBox, QProgressBar, QTextEdit, QFileDialog,
    QMessageBox, QSplitter, QFrame, QCheckBox, QComboBox,
    QScrollArea, QSizePolicy
)

try:
    from ultralytics import YOLO
    ULTRALYTICS_AVAILABLE = True
except ImportError:
    ULTRALYTICS_AVAILABLE = False
    YOLO = None

class TrainingWorker(QObject):
    """Worker thread for YOLO training to keep UI responsive."""

    progress_updated = pyqtSignal(str)  # Progress message
    training_finished = pyqtSignal(str)  # Weights path on success
    training_error = pyqtSignal(str)    # Error message

    def __init__(self, config: Dict[str, Any]):
        super().__init__()
        self.config = config
        self.is_training = False

    def run_training(self):
        """Run YOLO training in background thread."""
        try:
            self.is_training = True
            self.progress_updated.emit("Initializing training...")

            if not ULTRALYTICS_AVAILABLE:
                raise ImportError("Ultralytics YOLO not available. Install with: pip install ultralytics")

            # Validate dataset
            data_yaml = self.config['data_yaml']
            if not Path(data_yaml).exists():
                raise FileNotFoundError(f"Dataset config not found: {data_yaml}")

            # Load model
            model_path = self.config.get('model_path', 'yolov8n.pt')
            self.progress_updated.emit(f"Loading model: {model_path}")
            model = YOLO(model_path)

            # Training parameters
            train_config = {
                'data': data_yaml,
                'epochs': self.config['epochs'],
                'batch': self.config['batch_size'],
                'imgsz': self.config['img_size'],
                'device': self.config.get('device', 'cpu'),
                'workers': self.config.get('workers', 0),
                'project': self.config['output_dir'],
                'name': self.config['experiment_name'],
                'save': True,
                'save_period': 10,
                'cache': False,
                'exist_ok': True,
                'pretrained': True,
                'optimizer': 'auto',
                'verbose': True,
                'seed': 0,
                'deterministic': True,
                'single_cls': False,
                'rect': False,
                'cos_lr': False,
                'close_mosaic': 10,
                'resume': False,
                'amp': True,
                'fraction': 1.0,
                'profile': False,
                'freeze': None,
                'multi_scale': False,
                'overlap_mask': True,
                'mask_ratio': 4,
                'dropout': 0.0,
                'val': True,
                'split': 'val',
                'save_json': False,
                'save_hybrid': False,
                'conf': None,
                'iou': 0.7,
                'max_det': 300,
                'half': False,
                'dnn': False,
                'plots': True,
                'source': None,
                'vid_stride': 1,
                'stream_buffer': False,
                'visualize': False,
                'augment': False,
                'agnostic_nms': False,
                'classes': None,
                'retina_masks': False,
                'embed': None,
                'show': False,
                'save_frames': False,
                'save_txt': False,
                'save_conf': False,
                'save_crop': False,
                'show_labels': True,
                'show_conf': True,
                'show_boxes': True,
                'line_width': None
            }

            # Start training
            self.progress_updated.emit("Starting training...")
            results = model.train(**train_config)

            # Find best weights
            weights_dir = Path(self.config['output_dir']) / self.config['experiment_name']
            best_weights = weights_dir / 'weights' / 'best.pt'

            if best_weights.exists():
                final_path = str(best_weights)
                self.progress_updated.emit(f"Training completed! Best weights: {final_path}")
                self.training_finished.emit(final_path)
            else:
                # Fallback to last weights
                last_weights = weights_dir / 'weights' / 'last.pt'
                if last_weights.exists():
                    final_path = str(last_weights)
                    self.progress_updated.emit(f"Training completed! Last weights: {final_path}")
                    self.training_finished.emit(final_path)
                else:
                    raise FileNotFoundError("No trained weights found")

        except Exception as e:
            error_msg = f"Training failed: {str(e)}"
            self.progress_updated.emit(error_msg)
            self.training_error.emit(error_msg)
        finally:
            self.is_training = False

class YoloTrainerWindow(QMainWindow):
    """Main YOLO Trainer Window."""

    training_finished = pyqtSignal(str)  # Emitted when training completes with weights path

    def __init__(self, model_path: str = "yolov8n.pt"):
        super().__init__()
        self.model_path = model_path
        self.training_worker = None
        self.training_thread = None
        self.last_weights_path = None

        self.init_ui()
        self.load_settings()

    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("YOLO Model Trainer")
        self.setMinimumSize(800, 600)
        self.resize(1000, 700)

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)

        # Create splitter for resizable panels
        splitter = QSplitter(Qt.Vertical)
        main_layout.addWidget(splitter)

        # Top panel - Configuration
        config_widget = self.create_config_panel()
        splitter.addWidget(config_widget)

        # Bottom panel - Progress and Log
        progress_widget = self.create_progress_panel()
        splitter.addWidget(progress_widget)

        # Set splitter proportions
        splitter.setSizes([400, 300])

        # Status bar
        self.statusBar().showMessage("Ready")

        # Apply styling
        self.apply_styling()

    def create_config_panel(self) -> QWidget:
        """Create the configuration panel."""
        config_widget = QWidget()
        layout = QVBoxLayout(config_widget)

        # Dataset Configuration
        dataset_group = QGroupBox("Dataset Configuration")
        dataset_layout = QGridLayout(dataset_group)

        # Dataset folder selection
        dataset_layout.addWidget(QLabel("Dataset Folder:"), 0, 0)
        self.dataset_path_edit = QLineEdit()
        self.dataset_path_edit.setPlaceholderText("Select folder containing images and labels")
        dataset_layout.addWidget(self.dataset_path_edit, 0, 1)

        self.browse_dataset_btn = QPushButton("Browse...")
        self.browse_dataset_btn.clicked.connect(self.browse_dataset)
        dataset_layout.addWidget(self.browse_dataset_btn, 0, 2)

        # Validate dataset button
        self.validate_dataset_btn = QPushButton("Validate Dataset")
        self.validate_dataset_btn.clicked.connect(self.validate_dataset)
        dataset_layout.addWidget(self.validate_dataset_btn, 1, 1, 1, 2)

        layout.addWidget(dataset_group)

        # Training Parameters
        params_group = QGroupBox("Training Parameters")
        params_layout = QGridLayout(params_group)

        row = 0

        # Model selection
        params_layout.addWidget(QLabel("Base Model:"), row, 0)
        self.model_path_edit = QLineEdit(self.model_path)
        self.model_path_edit.setPlaceholderText("Path to YOLO model (.pt file)")
        params_layout.addWidget(self.model_path_edit, row, 1)

        self.browse_model_btn = QPushButton("Browse...")
        self.browse_model_btn.clicked.connect(self.browse_model)
        params_layout.addWidget(self.browse_model_btn, row, 2)
        row += 1

        # Epochs
        params_layout.addWidget(QLabel("Epochs:"), row, 0)
        self.epochs_spin = QSpinBox()
        self.epochs_spin.setRange(1, 1000)
        self.epochs_spin.setValue(100)
        params_layout.addWidget(self.epochs_spin, row, 1)
        row += 1

        # Batch size
        params_layout.addWidget(QLabel("Batch Size:"), row, 0)
        self.batch_size_spin = QSpinBox()
        self.batch_size_spin.setRange(1, 64)
        self.batch_size_spin.setValue(16)
        params_layout.addWidget(self.batch_size_spin, row, 1)
        row += 1

        # Image size
        params_layout.addWidget(QLabel("Image Size:"), row, 0)
        self.img_size_spin = QSpinBox()
        self.img_size_spin.setRange(320, 1280)
        self.img_size_spin.setValue(640)
        self.img_size_spin.setSingleStep(32)
        params_layout.addWidget(self.img_size_spin, row, 1)
        row += 1

        # Device
        params_layout.addWidget(QLabel("Device:"), row, 0)
        self.device_combo = QComboBox()
        self.device_combo.addItems(["cpu", "cuda", "mps"])
        self.device_combo.setCurrentText("cpu")
        params_layout.addWidget(self.device_combo, row, 1)
        row += 1

        # Output directory
        params_layout.addWidget(QLabel("Output Directory:"), row, 0)
        self.output_dir_edit = QLineEdit("yolo_training_output")
        params_layout.addWidget(self.output_dir_edit, row, 1)

        self.browse_output_btn = QPushButton("Browse...")
        self.browse_output_btn.clicked.connect(self.browse_output_dir)
        params_layout.addWidget(self.browse_output_btn, row, 2)
        row += 1

        # Experiment name
        params_layout.addWidget(QLabel("Experiment Name:"), row, 0)
        self.experiment_name_edit = QLineEdit("exp")
        params_layout.addWidget(self.experiment_name_edit, row, 1, 1, 2)
        row += 1

        layout.addWidget(params_group)

        # Control buttons
        buttons_layout = QHBoxLayout()

        self.start_training_btn = QPushButton("Start Training")
        self.start_training_btn.clicked.connect(self.start_training)
        self.start_training_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; padding: 10px; font-size: 14px; }")
        buttons_layout.addWidget(self.start_training_btn)

        self.stop_training_btn = QPushButton("Stop Training")
        self.stop_training_btn.clicked.connect(self.stop_training)
        self.stop_training_btn.setEnabled(False)
        self.stop_training_btn.setStyleSheet("QPushButton { background-color: #f44336; color: white; padding: 10px; font-size: 14px; }")
        buttons_layout.addWidget(self.stop_training_btn)

        self.export_model_btn = QPushButton("Export Model")
        self.export_model_btn.clicked.connect(self.export_model)
        self.export_model_btn.setEnabled(False)
        buttons_layout.addWidget(self.export_model_btn)

        layout.addLayout(buttons_layout)

        return config_widget

    def create_progress_panel(self) -> QWidget:
        """Create the progress and logging panel."""
        progress_widget = QWidget()
        layout = QVBoxLayout(progress_widget)

        # Progress bar
        progress_layout = QHBoxLayout()
        progress_layout.addWidget(QLabel("Training Progress:"))
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        progress_layout.addWidget(self.progress_bar)
        layout.addLayout(progress_layout)

        # Current status
        self.status_label = QLabel("Ready to train")
        self.status_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(self.status_label)

        # Log output
        log_group = QGroupBox("Training Log")
        log_layout = QVBoxLayout(log_group)

        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setFont(QFont("Courier New", 9))
        log_layout.addWidget(self.log_text)

        # Clear log button
        clear_log_btn = QPushButton("Clear Log")
        clear_log_btn.clicked.connect(self.clear_log)
        log_layout.addWidget(clear_log_btn)

        layout.addWidget(log_group)

        return progress_widget

    def apply_styling(self):
        """Apply consistent dark theme styling to match main app."""
        self.setStyleSheet(
            """
        QMainWindow {
            background-color: #101010;
        }

        QWidget {
            background-color: #151515;
            color: #e0e0e0;
            font-family: 'Segoe UI';
            font-size: 9.0pt;
            border: none;
        }

        QGroupBox {
            border: 1px solid #888;
            border-radius: 10px;
            margin-top: 10px;
            font-weight: bold;
            color: #eaeaea;
            padding: 8px;
        }

        QPushButton {
            background-color: #222;
            color: #f0f0f0;
            border: 1px solid #888;
            border-radius: 8px;
            padding: 2px 6px;
            min-height: 22px;
        }

        QPushButton:hover {
            background-color: #2e2e2e;
        }

        QPushButton:checked {
            background-color: #ff3333;
            border: 1px solid #ff5555;
            color: #fff;
        }

        QLabel {
            color: #eaeaea;
        }

        QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox {
            background-color: #1d1d1d;
            color: #f0f0f0;
            border: 1px solid #666;
            border-radius: 6px;
            padding: 2px;
            min-height: 20px;
        }

        QTextEdit, QPlainTextEdit {
            background-color: #0d0d0d;
            color: #00ff88;
            border: 1px solid #666;
            border-radius: 8px;
            font-family: Consolas;
            font-size: 10pt;
        }

        QScrollBar:vertical {
            background: #1a1a1a;
            width: 12px;
        }

        QScrollBar::handle:vertical {
            background: #555;
            border-radius: 6px;
        }

        QScrollBar::handle:vertical:hover {
            background: #777;
        }

        QPushButton:pressed {
            background-color: #1f1f1f;
            border: 1px solid #aaa;
            color: #ffffff;
        }

        QCheckBox {
            color: #eaeaea;
        }
        QCheckBox::indicator {
            width: 16px;
            height: 16px;
            border-radius: 3px;
            background-color: #1d1d1d;
            border: 1px solid #666;
        }
        QCheckBox::indicator:checked {
            background-color: #ff3333;
            border: 1px solid #ff5555;
        }

        QToolTip {
            background-color: #FFFACD;
            color: #000000;
            border: 1px solid #666;
            border-radius: 4px;
            padding: 3px 6px;
            font-size: 10pt;
            font-family: 'Segoe UI';
        }
        """
        )

    def browse_dataset(self):
        """Browse for dataset folder."""
        folder = QFileDialog.getExistingDirectory(self, "Select Dataset Folder")
        if folder:
            self.dataset_path_edit.setText(folder)
            self.validate_dataset()

    def browse_output_dir(self):
        """Browse for output directory."""
        folder = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if folder:
            self.output_dir_edit.setText(folder)

    def browse_model(self):
        """Browse for YOLO model file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select YOLO Model File",
            "",
            "YOLO Model Files (*.pt);;All Files (*)"
        )
        if file_path:
            self.model_path_edit.setText(file_path)

    def validate_dataset(self):
        """Validate the selected dataset."""
        dataset_path = self.dataset_path_edit.text().strip()
        if not dataset_path:
            QMessageBox.warning(self, "No Dataset", "Please select a dataset folder first.")
            return

        dataset_dir = Path(dataset_path)
        if not dataset_dir.exists():
            QMessageBox.warning(self, "Invalid Path", f"Dataset folder does not exist: {dataset_path}")
            return

        # Check for required YOLO dataset structure
        images_dir = dataset_dir / "images"
        labels_dir = dataset_dir / "labels"
        data_yaml = dataset_dir / "data.yaml"

        missing_items = []
        if not images_dir.exists():
            missing_items.append("images/ folder")
        if not labels_dir.exists():
            missing_items.append("labels/ folder")
        if not data_yaml.exists():
            missing_items.append("data.yaml file")

        if missing_items:
            QMessageBox.warning(self, "Invalid Dataset Structure",
                              f"Dataset is missing required items:\n" + "\n".join(f"• {item}" for item in missing_items) +
                              "\n\nPlease ensure your dataset follows YOLO format with images/, labels/, and data.yaml.")
            return

        # Try to read data.yaml
        try:
            import yaml
            with open(data_yaml, 'r') as f:
                data_config = yaml.safe_load(f)

            # Validate data.yaml content
            required_keys = ['train', 'val', 'nc', 'names']
            missing_keys = [key for key in required_keys if key not in data_config]
            if missing_keys:
                QMessageBox.warning(self, "Invalid data.yaml",
                                  f"data.yaml is missing required keys: {', '.join(missing_keys)}")
                return

            num_classes = data_config['nc']
            class_names = data_config['names']

            QMessageBox.information(self, "Dataset Valid",
                                  f"Dataset validated successfully!\n\n"
                                  f"Classes: {num_classes}\n"
                                  f"Class names: {', '.join(class_names[:5])}{'...' if len(class_names) > 5 else ''}")

            self.statusBar().showMessage(f"Dataset ready: {num_classes} classes")

        except ImportError:
            QMessageBox.warning(self, "PyYAML Required",
                              "PyYAML is required to validate data.yaml. Install with: pip install PyYAML")
        except Exception as e:
            QMessageBox.warning(self, "Invalid data.yaml",
                              f"Error reading data.yaml: {str(e)}")

    def start_training(self):
        """Start the training process."""
        if not ULTRALYTICS_AVAILABLE:
            QMessageBox.critical(self, "Ultralytics Not Available",
                               "Ultralytics YOLO is not installed. Install with: pip install ultralytics")
            return

        # Validate inputs
        dataset_path = self.dataset_path_edit.text().strip()
        if not dataset_path:
            QMessageBox.warning(self, "No Dataset", "Please select a dataset folder.")
            return

        data_yaml = Path(dataset_path) / "data.yaml"
        if not data_yaml.exists():
            QMessageBox.warning(self, "Missing data.yaml", "data.yaml not found in dataset folder.")
            return

        # Prepare training config
        config = {
            'data_yaml': str(data_yaml),
            'model_path': self.model_path_edit.text().strip(),
            'epochs': self.epochs_spin.value(),
            'batch_size': self.batch_size_spin.value(),
            'img_size': self.img_size_spin.value(),
            'device': self.device_combo.currentText(),
            'output_dir': self.output_dir_edit.text().strip(),
            'experiment_name': self.experiment_name_edit.text().strip(),
            'workers': 0  # CPU only for safety
        }

        # Disable start button, enable stop
        self.start_training_btn.setEnabled(False)
        self.stop_training_btn.setEnabled(True)
        self.export_model_btn.setEnabled(False)

        # Clear previous log
        self.clear_log()
        self.progress_bar.setValue(0)
        self.status_label.setText("Initializing training...")

        # Create worker and thread
        self.training_worker = TrainingWorker(config)
        self.training_thread = QThread()

        self.training_worker.moveToThread(self.training_thread)

        # Connect signals
        self.training_worker.progress_updated.connect(self.update_progress)
        self.training_worker.training_finished.connect(self.on_training_finished)
        self.training_worker.training_error.connect(self.on_training_error)

        self.training_thread.started.connect(self.training_worker.run_training)
        self.training_thread.start()

    def stop_training(self):
        """Stop the training process."""
        if self.training_worker and self.training_worker.is_training:
            # Note: YOLO training doesn't have a clean stop mechanism
            # This will just terminate the thread
            self.training_thread.terminate()
            self.training_thread.wait()
            self.on_training_error("Training stopped by user")

    def update_progress(self, message: str):
        """Update progress display."""
        self.log_text.append(message)
        self.status_label.setText(message)

        # Try to extract epoch progress from message
        if "epoch" in message.lower() and "/" in message:
            try:
                parts = message.split("/")
                if len(parts) >= 2:
                    current = int(parts[0].split()[-1])
                    total = int(parts[1].split()[0])
                    progress = int((current / total) * 100)
                    self.progress_bar.setValue(progress)
            except:
                pass

    def on_training_finished(self, weights_path: str):
        """Handle training completion."""
        self.last_weights_path = weights_path
        self.progress_bar.setValue(100)
        self.status_label.setText("Training completed successfully!")

        # Re-enable buttons
        self.start_training_btn.setEnabled(True)
        self.stop_training_btn.setEnabled(False)
        self.export_model_btn.setEnabled(True)

        # Emit signal for main app
        self.training_finished.emit(weights_path)

        QMessageBox.information(self, "Training Complete",
                              f"Training finished successfully!\n\nWeights saved to:\n{weights_path}")

    def on_training_error(self, error_msg: str):
        """Handle training error."""
        self.status_label.setText("Training failed")

        # Re-enable buttons
        self.start_training_btn.setEnabled(True)
        self.stop_training_btn.setEnabled(False)
        self.export_model_btn.setEnabled(False)

        QMessageBox.critical(self, "Training Failed", error_msg)

    def export_model(self):
        """Export the trained model to a convenient location."""
        if not self.last_weights_path:
            QMessageBox.warning(self, "No Model", "No trained model available.")
            return

        # Suggest a name based on the experiment
        default_name = f"{self.experiment_name_edit.text()}_trained.pt"

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export Trained Model", default_name,
            "PyTorch Model (*.pt);;All Files (*)"
        )

        if file_path:
            try:
                import shutil
                shutil.copy2(self.last_weights_path, file_path)
                QMessageBox.information(self, "Export Complete",
                                      f"Model exported to:\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Export Failed", f"Failed to export model: {str(e)}")

    def clear_log(self):
        """Clear the training log."""
        self.log_text.clear()
        self.status_label.setText("Log cleared")

    def load_settings(self):
        """Load saved settings."""
        try:
            settings_file = Path("yolo_trainer_settings.json")
            if settings_file.exists():
                with open(settings_file, 'r') as f:
                    settings = json.load(f)

                # Apply settings
                if 'dataset_path' in settings:
                    self.dataset_path_edit.setText(settings['dataset_path'])
                if 'output_dir' in settings:
                    self.output_dir_edit.setText(settings['output_dir'])
                if 'model' in settings:
                    self.model_path_edit.setText(settings['model'])
                if 'epochs' in settings:
                    self.epochs_spin.setValue(settings['epochs'])
                if 'batch_size' in settings:
                    self.batch_size_spin.setValue(settings['batch_size'])
                if 'img_size' in settings:
                    self.img_size_spin.setValue(settings['img_size'])
                if 'device' in settings:
                    self.device_combo.setCurrentText(settings['device'])
                if 'experiment_name' in settings:
                    self.experiment_name_edit.setText(settings['experiment_name'])

        except Exception as e:
            print(f"Failed to load settings: {e}")

    def save_settings(self):
        """Save current settings."""
        try:
            settings = {
                'dataset_path': self.dataset_path_edit.text(),
                'output_dir': self.output_dir_edit.text(),
                'model': self.model_path_edit.text(),
                'epochs': self.epochs_spin.value(),
                'batch_size': self.batch_size_spin.value(),
                'img_size': self.img_size_spin.value(),
                'device': self.device_combo.currentText(),
                'experiment_name': self.experiment_name_edit.text()
            }

            with open("yolo_trainer_settings.json", 'w') as f:
                json.dump(settings, f, indent=2)

        except Exception as e:
            print(f"Failed to save settings: {e}")

    def closeEvent(self, event):
        """Handle window close event."""
        self.save_settings()

        # Stop any running training
        if self.training_thread and self.training_thread.isRunning():
            self.training_thread.terminate()
            self.training_thread.wait()

        event.accept()


def main():
    """Main entry point for standalone execution."""
    app = QApplication(sys.argv)
    app.setApplicationName("YOLO Trainer")
    app.setApplicationVersion("1.0")

    # Configure for Windows Torch stability
    os.environ.setdefault('KMP_DUPLICATE_LIB_OK', 'TRUE')
    os.environ.setdefault('OMP_NUM_THREADS', '1')

    window = YoloTrainerWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()