"""
checklist_panel.py
==================
Interactive checklist panel docked in MAIN_FILE.py under Tools menu.
Displays all methods, attributes, buttons, and signals with checkboxes.
Validates connectivity and auto-marks issues.
Features:
- Export checked items to new file (JSON/CSV)
- Check all / Check selected boxes
- Filter items by status (all, valid, issues)
- Bulk operations with status feedback
"""

import json
import csv
import threading
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QFileSystemWatcher
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QCheckBox,
    QPushButton,
    QLabel,
    QSpinBox,
    QComboBox,
    QFileDialog,
    QInputDialog,
    QMessageBox,
    QDialog,
    QSplitter,
    QPlainTextEdit,
    QListWidget,
)
from PyQt5.QtGui import QColor, QFont, QTextCursor, QTextCharFormat, QBrush

try:
    from dependencies_checker import DependencyChecker, populate_dependencies_table
except ImportError:
    DependencyChecker = None
    populate_dependencies_table = None


class ChecklistItem(QTableWidgetItem):
    """Table cell that holds a checklist item with validation state"""
    def __init__(self, text, item_type='other', line_no=0, is_checkbox=False):
        super().__init__(text)
        self.item_type = item_type
        self.line_no = line_no
        self.is_checkbox = is_checkbox
        self.is_valid = False
        self.error_msg = ""
        
        if is_checkbox:
            self.setFlags(self.flags() | Qt.ItemIsUserCheckable)
            self.setCheckState(Qt.Unchecked)


class ChecklistPanel(QDialog):
    """
    Standalone window for code checking and validation.
    Shows methods, attributes, buttons, signals with validation status.
    Includes code element checklist and dependency verification.
    """
    validation_complete = pyqtSignal(dict)  # Emitted when validation finishes
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Code Checker")
        self.parent_app = parent
        self.checklist_data = {}
        self.tables = {}
        self.validation_results = {}
        
        self.setup_ui()
        # Path to the canonical checklist JSON used by the panel
        self.data_file = Path(__file__).parent / "checklist_data.json"
        self.load_checklist_data()
        
        # Start maximized for better visibility of all issues
        self.showMaximized()

        # File watcher disabled by default to prevent performance issues
        # It can cause VS Code crashes if too many file events trigger reloads
        self.watcher = None
        self.watcher_debounce_timer = None
        # Uncomment below if you want file watching (at your own risk):
        # try:
        #     self.watcher = QFileSystemWatcher(self)
        #     if self.data_file.exists():
        #         self.watcher.addPath(str(self.data_file))
        #     self.watcher.fileChanged.connect(self.on_checklist_file_changed_debounced)
        # except Exception as e:
        #     print(f"Warning: Could not start file watcher: {e}")
    
    def setup_ui(self):
        """Create the UI with tabs for each category"""
        layout = QVBoxLayout(self)
        
        # Title and controls
        title = QLabel("� Code Checker")
        title.setToolTip("Verify code elements and dependencies to ensure application integrity.")
        title_font = QFont()
        title_font.setPointSize(11)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Control buttons (row 1)
        button_layout1 = QHBoxLayout()
        
        validate_btn = QPushButton("🔍 Validate All")
        validate_btn.clicked.connect(self.validate_all)
        validate_btn.setToolTip("Scan and validate all code elements")
        button_layout1.addWidget(validate_btn)
        
        check_all_btn = QPushButton("☑️ Check All")
        check_all_btn.clicked.connect(self.check_all_boxes)
        check_all_btn.setToolTip("Mark all items as checked")
        button_layout1.addWidget(check_all_btn)
        
        uncheck_all_btn = QPushButton("☐ Uncheck All")
        uncheck_all_btn.clicked.connect(self.uncheck_all_boxes)
        uncheck_all_btn.setToolTip("Mark all items as unchecked")
        button_layout1.addWidget(uncheck_all_btn)
        
        check_selected_btn = QPushButton("✓ Check Selected")
        check_selected_btn.clicked.connect(self.check_selected_boxes)
        check_selected_btn.setToolTip("Mark selected items as checked")
        button_layout1.addWidget(check_selected_btn)
        
        layout.addLayout(button_layout1)
        
        # Control buttons (row 2)
        button_layout2 = QHBoxLayout()
        
        save_btn = QPushButton("💾 Save State")
        save_btn.clicked.connect(self.save_state)
        save_btn.setToolTip("Save current checklist state")
        button_layout2.addWidget(save_btn)
        
        export_btn = QPushButton("📤 Export Checked")
        export_btn.clicked.connect(self.export_checked_items)
        export_btn.setToolTip("Export checked items to file")
        button_layout2.addWidget(export_btn)

        import_btn = QPushButton("🔁 Import Validation")
        import_btn.clicked.connect(self.import_validation_dialog)
        import_btn.setToolTip("Import validation results from file")
        button_layout2.addWidget(import_btn)

        # DISABLED: Triage functionality causes performance issues
        # triage_btn = QPushButton("🧭 Triage Unused")
        # triage_btn.clicked.connect(self.show_triage_dialog)
        # triage_btn.setToolTip("Find and organize unused code")
        # button_layout2.addWidget(triage_btn)
        
        deps_btn = QPushButton("📦 Check Dependencies")
        deps_btn.clicked.connect(self.check_dependencies_clicked)
        deps_btn.setToolTip("Verify all required files exist")
        button_layout2.addWidget(deps_btn)
        
        clear_btn = QPushButton("Clear Checks")
        clear_btn.clicked.connect(self.clear_all_checks)
        clear_btn.setToolTip("Clear all checkmarks")
        button_layout2.addWidget(clear_btn)
        
        maximize_btn = QPushButton("⛶ Maximize")
        maximize_btn.clicked.connect(self.maximize_window)
        maximize_btn.setToolTip("Maximize window for better viewing")
        button_layout2.addWidget(maximize_btn)
        
        layout.addLayout(button_layout2)
        
        # Filter controls
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Filter:"))
        
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["All", "Valid Only", "Issues Only"])
        self.filter_combo.currentTextChanged.connect(self.apply_filter)
        filter_layout.addWidget(self.filter_combo)
        
        filter_layout.addStretch()
        layout.addLayout(filter_layout)
        
        # Tab widget for categories
        self.tab_widget = QTabWidget()
        layout.addWidget(self.tab_widget, 1)  # Give it stretch factor
        
        # Status bar
        self.status_label = QLabel("Ready")
        layout.addWidget(self.status_label)
        
        self.setGeometry(100, 100, 1000, 700)
    
    def load_checklist_data(self):
        """Load checklist data from JSON and populate tabs"""
        data_file = self.data_file

        # Clear existing tabs so reload doesn't duplicate widgets
        self._clear_tabs()

        if not data_file.exists():
            self.status_label.setText("⚠️ checklist_data.json not found. Run code_scanner.py first.")
            return

        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                self.checklist_data = json.load(f)
        except Exception as e:
            self.status_label.setText(f"❌ Error loading checklist: {e}")
            return
        
        # Create tabs for each category
        categories = [
            ('methods', 'Methods'),
            ('attributes', 'Attributes'),
            ('buttons', 'Buttons'),
            ('checkboxes', 'CheckBoxes'),
            ('sliders', 'Sliders'),
            ('spinboxes', 'SpinBoxes'),
            ('comboboxes', 'ComboBoxes'),
            ('labels', 'Labels'),
            ('text_edits', 'Text Edits'),
            ('signals', 'Signals'),
        ]
        
        for key, label in categories:
            if key in self.checklist_data and self.checklist_data[key]:
                table = self.create_category_table(key, self.checklist_data[key])
                self.tables[key] = table
                self.tab_widget.addTab(table, f"{label} ({len(self.checklist_data[key])})")
        
        total_items = sum(len(self.checklist_data.get(k, [])) for k, _ in categories)
        self.status_label.setText(f"✅ Loaded {total_items} items")
    
    def create_category_table(self, category_key, items):
        """Create a table widget for a category of items"""
        table = QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(['✓', 'Name', 'Line', 'Type', 'Status'])
        table.setColumnWidth(0, 40)
        table.setColumnWidth(1, 300)
        table.setColumnWidth(2, 60)
        table.setColumnWidth(3, 120)
        table.setColumnWidth(4, 150)
        
        table.setRowCount(len(items))
        
        for row, item in enumerate(items):
            # Checkbox column
            check_item = ChecklistItem("", is_checkbox=True)
            # Set checkbox state from the scan data (so imported validations show)
            if item.get('checked'):
                check_item.setCheckState(Qt.Checked)
            else:
                check_item.setCheckState(Qt.Unchecked)
            # Store the full item data (including 'file' field) as metadata for export
            check_item.setData(Qt.UserRole, item)
            table.setItem(row, 0, check_item)
            
            # Name
            name_item = ChecklistItem(item.get('name', ''))
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
            table.setItem(row, 1, name_item)
            
            # Line number
            line_item = ChecklistItem(str(item.get('line', '')))
            line_item.setFlags(line_item.flags() & ~Qt.ItemIsEditable)
            table.setItem(row, 2, line_item)
            
            # Type
            type_item = ChecklistItem(item.get('type', 'N/A'))
            type_item.setFlags(type_item.flags() & ~Qt.ItemIsEditable)
            table.setItem(row, 3, type_item)
            
            # Status (will be updated by validation)
            # If the scan already has a checked/checked_at, show that
            checked = item.get('checked', False)
            checked_at = item.get('checked_at') or item.get('validated_at')
            if checked:
                status_text = f"✅ Validated{(' at ' + checked_at) if checked_at else ''}"
            else:
                status_text = item.get('status', '⏳ Not checked')

            status_item = ChecklistItem(status_text)
            status_item.setFlags(status_item.flags() & ~Qt.ItemIsEditable)
            table.setItem(row, 4, status_item)
        
        return table

    def _clear_tabs(self):
        """Remove and delete all tabs/widgets to prepare for a reload"""
        while self.tab_widget.count() > 0:
            w = self.tab_widget.widget(0)
            # Remove tab and allow widget to be deleted later
            self.tab_widget.removeTab(0)
            try:
                w.deleteLater()
            except Exception:
                pass
        self.tables.clear()

    def on_checklist_file_changed(self, path):
        """Called when the underlying checklist_data.json file is changed on disk.

        Uses a short delayed reload to allow the writer to finish writing the file.
        """
        # Update UI so user knows something happened
        self.status_label.setText("🔁 checklist_data.json changed — reloading...")
        # Delay reload a little to avoid partial reads
        QTimer.singleShot(300, lambda: self._handle_file_change(path))

    def _handle_file_change(self, path):
        p = Path(path)
        # If file temporarily missing, retry shortly
        if not p.exists():
            QTimer.singleShot(500, lambda: self._handle_file_change(path))
            return

        # Ensure the watcher is still watching (some editors replace files)
        try:
            if str(p) not in self.watcher.files():
                self.watcher.addPath(str(p))
        except Exception:
            pass

        # Reload the checklist data (this clears tabs and repopulates)
        self.load_checklist_data()
        self.status_label.setText("✅ Checklist reloaded from disk")
    
    def validate_all(self):
        """Validate all items: check if methods exist, buttons are wired, etc."""
        self.status_label.setText("🔄 Validating...")
        QTimer.singleShot(100, self._do_validation)
    
    def _do_validation(self):
        """Perform actual validation"""
        if not self.parent_app:
            self.status_label.setText("❌ Parent app not available")
            return
        
        valid_count = 0
        invalid_count = 0
        skipped_count = 0
        
        # Validate methods
        for table_key in self.tables:
            table = self.tables[table_key]
            items = self.checklist_data.get(table_key, [])
            
            for row, item in enumerate(items):
                name = item.get('name', '')
                source_file = item.get('file', 'Unknown')
                
                # Try to find the attribute/method on the app
                status = "✅ OK"
                color = QColor(0, 200, 0)  # Green
                
                try:
                    # CRITICAL FIX: Only validate items that belong to MAIN_FILE
                    # Items from other files are skipped with "External" status
                    is_main_file_item = 'MAIN' in source_file or source_file == 'Unknown'
                    
                    if not is_main_file_item:
                        # Item from different file (behavior_presets.py, checklist_panel.py, etc)
                        # Skip validation - these live in their own classes, not on main app
                        status = f"ⓘ {source_file}"
                        color = QColor(100, 150, 200)  # Light blue
                        skipped_count += 1
                    elif table_key == 'methods':
                        # For methods: only validate if they're actually on the main app
                        if hasattr(self.parent_app, name):
                            attr = getattr(self.parent_app, name)
                            if callable(attr):
                                valid_count += 1
                            else:
                                status = "⚠️ Not callable"
                                color = QColor(255, 165, 0)  # Orange
                                invalid_count += 1
                        else:
                            # Method doesn't exist on main app
                            status = "❌ Missing"
                            color = QColor(255, 0, 0)  # Red
                            invalid_count += 1
                    
                    elif table_key in ('buttons', 'checkboxes', 'sliders', 'spinboxes', 'comboboxes', 'labels', 'text_edits', 'signals'):
                        # Check if widget/attribute exists on main app
                        attr_name = name.replace('self.', '') if name.startswith('self.') else name
                        if hasattr(self.parent_app, attr_name):
                            valid_count += 1
                        else:
                            status = "❌ Widget missing"
                            color = QColor(255, 0, 0)
                            invalid_count += 1
                    
                    else:  # attributes
                        # Check if attribute exists on main app
                        attr_name = name.replace('self.', '') if name.startswith('self.') else name
                        if hasattr(self.parent_app, attr_name):
                            valid_count += 1
                        else:
                            status = "⚠️ Unused"
                            color = QColor(255, 165, 0)
                            invalid_count += 1
                
                except Exception as e:
                    status = f"⚠️ Error: {str(e)[:30]}"
                    color = QColor(255, 165, 0)
                    invalid_count += 1
                
                # Update status cell
                status_cell = table.item(row, 4)
                if status_cell:
                    status_cell.setText(status)
                    status_cell.setBackground(color)
        
        total = valid_count + invalid_count + skipped_count
        self.status_label.setText(
            f"✅ {valid_count} valid | ⚠️ {invalid_count} issues | ⓘ {skipped_count} external"
        )
        self.validation_complete.emit({
            'valid': valid_count,
            'invalid': invalid_count,
            'skipped': skipped_count,
            'total': total,
        })
    
    def clear_all_checks(self):
        """Clear all checkboxes"""
        for table in self.tables.values():
            for row in range(table.rowCount()):
                check_item = table.item(row, 0)
                if check_item and isinstance(check_item, ChecklistItem):
                    check_item.setCheckState(Qt.Unchecked)
        
        self.status_label.setText("✓ All checks cleared")
    
    def maximize_window(self):
        """Maximize the window to full screen"""
        self.showMaximized()
        self.status_label.setText("✓ Window maximized")
    
    def save_state(self):
        """Save current check state to JSON"""
        state = {}
        for table_key, table in self.tables.items():
            state[table_key] = []
            for row in range(table.rowCount()):
                check_item = table.item(row, 0)
                if check_item:
                    is_checked = check_item.checkState() == Qt.Checked
                    state[table_key].append(is_checked)
        
        state_file = Path(__file__).parent / "checklist_state.json"
        try:
            with open(state_file, 'w', encoding='utf-8') as f:
                json.dump(state, f, indent=2)
            self.status_label.setText(f"✅ State saved to {state_file.name}")
        except Exception as e:
            self.status_label.setText(f"❌ Error saving state: {e}")
    
    def load_state(self):
        """Load saved check state from JSON"""
        state_file = Path(__file__).parent / "checklist_state.json"
        
        if not state_file.exists():
            return
        
        try:
            with open(state_file, 'r', encoding='utf-8') as f:
                state = json.load(f)
            
            for table_key, checks in state.items():
                if table_key in self.tables:
                    table = self.tables[table_key]
                    for row, is_checked in enumerate(checks):
                        if row < table.rowCount():
                            check_item = table.item(row, 0)
                            if check_item:
                                check_item.setCheckState(Qt.Checked if is_checked else Qt.Unchecked)
        
        except Exception as e:
            print(f"Warning: Could not load checklist state: {e}")

    def _find_python_files(self, max_results=50) -> list:
        """Search workspace for Python source files (limit to max_results)."""
        results = []
        project_root = Path(__file__).parent
        try:
            for py_file in sorted(project_root.rglob('*.py'))[:max_results]:
                # Skip venv, __pycache__, tests in this context
                if '.venv' in py_file.parts or '__pycache__' in py_file.parts:
                    continue
                results.append(py_file)
        except Exception:
            pass
        return results

    def _search_for_method_in_files(self, method_name: str, files: list) -> list:
        """Search Python files for a method/function definition and return (file, line) tuples."""
        candidates = []
        for fpath in files:
            try:
                content = fpath.read_text(encoding='utf-8', errors='ignore')
                for i, line in enumerate(content.splitlines(), 1):
                    # Simple pattern: look for "def method_name(" or "def method_name :"
                    if f'def {method_name}' in line and ('(' in line or ':' in line):
                        candidates.append((str(fpath), i))
            except Exception:
                pass
        return candidates

    def _load_settings(self):
        """Load persistent checklist settings (auto-ignore, etc.)."""
        settings_file = Path(__file__).parent / "checklist_settings.json"
        if not settings_file.exists():
            return {}
        try:
            with open(settings_file, 'r', encoding='utf-8') as fh:
                return json.load(fh)
        except Exception:
            return {}

    def _save_settings(self, settings: dict):
        settings_file = Path(__file__).parent / "checklist_settings.json"
        try:
            with open(settings_file, 'w', encoding='utf-8') as fh:
                json.dump(settings, fh, indent=2)
        except Exception:
            pass

    def _get_snippet(self, filepath: str, line: int | None, context: int = 6) -> str:
        """Return a small code snippet around `line` from `filepath` (as string).

        If the file doesn't exist, attempt a conservative search for a matching filename
        in the same directory as this panel. The returned text prefixes the target
        line with a '>' marker for clarity.
        """
        try:
            p = Path(filepath)
            # If path is not absolute or doesn't exist, try local MAIN_FILE.py fallback
            if not p.exists():
                fallback = Path(__file__).parent / 'MAIN_FILE.py'
                if fallback.exists():
                    p = fallback
            text = p.read_text(encoding='utf-8', errors='ignore')
            lines = text.splitlines()
            if line is None:
                # Show the top of the file if no line available
                start = 0
                end = min(len(lines), context * 2)
                out = []
                for i in range(start, end):
                    out.append(f"{i+1:5d}  {lines[i]}")
                return "\n".join(out)

            idx = max(1, int(line))
            start = max(1, idx - context)
            end = min(len(lines), idx + context)
            out = []
            for i in range(start, end + 1):
                prefix = '>' if i == idx else ' '
                # guard in case of index issues
                try:
                    src_line = lines[i - 1]
                except Exception:
                    src_line = ''
                out.append(f"{i:5d} {prefix} {src_line}")
            return "\n".join(out)
        except Exception as e:
            return f"Could not read {filepath}: {e}"

    def _get_snippet_with_highlight(self, filepath: str, line: int | None, context: int = 6) -> tuple:
        """Return code snippet and highlight line number for visual highlighting in QTextEdit.

        Returns (text: str, highlight_line_number: int where 1 is the first line of snippet).
        If the file doesn't exist, fall back to MAIN_FILE.py.
        The highlight_line_number tells the caller which line to visually highlight.
        """
        try:
            p = Path(filepath)
            if not p.exists():
                fallback = Path(__file__).parent / 'MAIN_FILE.py'
                if fallback.exists():
                    p = fallback
            text = p.read_text(encoding='utf-8', errors='ignore')
            lines = text.splitlines()

            if line is None:
                start = 0
                end = min(len(lines), context * 2)
                highlight_line = 1
            else:
                idx = max(1, int(line))
                start = max(1, idx - context)
                end = min(len(lines), idx + context)
                highlight_line = idx - start + 1  # Line number within snippet (1-indexed)

            out = []
            for i in range(start, end + 1):
                try:
                    src_line = lines[i - 1]
                except Exception:
                    src_line = ''
                out.append(f"{i:5d}  {src_line}")

            return "\n".join(out), highlight_line
        except Exception as e:
            return f"Could not read {filepath}: {e}", -1
    
    def check_all_boxes(self):
        """Check all checkboxes in current tab"""
        current_table = self.tab_widget.currentWidget()
        if current_table:
            for row in range(current_table.rowCount()):
                check_item = current_table.item(row, 0)
                if check_item and isinstance(check_item, ChecklistItem):
                    check_item.setCheckState(Qt.Checked)
            self.status_label.setText("✓ All boxes in current tab checked")
    
    def uncheck_all_boxes(self):
        """Uncheck all checkboxes in current tab"""
        current_table = self.tab_widget.currentWidget()
        if current_table:
            for row in range(current_table.rowCount()):
                check_item = current_table.item(row, 0)
                if check_item and isinstance(check_item, ChecklistItem):
                    check_item.setCheckState(Qt.Unchecked)
            self.status_label.setText("✓ All boxes in current tab unchecked")
    
    def check_selected_boxes(self):
        """Check only selected (highlighted) rows in current tab"""
        current_table = self.tab_widget.currentWidget()
        if current_table:
            selected_rows = set()
            for item in current_table.selectedItems():
                selected_rows.add(item.row())
            
            if not selected_rows:
                self.status_label.setText("⚠️ No rows selected")
                return
            
            for row in selected_rows:
                check_item = current_table.item(row, 0)
                if check_item and isinstance(check_item, ChecklistItem):
                    check_item.setCheckState(Qt.Checked)
            
            self.status_label.setText(f"✓ {len(selected_rows)} selected boxes checked")
    
    def apply_filter(self, filter_text):
        """Filter items by status"""
        for table_key, table in self.tables.items():
            for row in range(table.rowCount()):
                status_item = table.item(row, 4)
                if status_item:
                    status_text = status_item.text()
                    
                    if filter_text == "All":
                        table.setRowHidden(row, False)
                    elif filter_text == "Valid Only":
                        # Show only green (OK) items
                        show = "✅" in status_text or "OK" in status_text
                        table.setRowHidden(row, not show)
                    elif filter_text == "Issues Only":
                        # Show only orange/red items
                        show = "⚠️" in status_text or "❌" in status_text
                        table.setRowHidden(row, not show)
    
    def export_checked_items(self):
        """Export checked items to new file with user-specified name"""
        # Get name from user
        name, ok = QInputDialog.getText(
            self,
            "Export Checked Items",
            "Enter filename (without extension):",
            text=f"checklist_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )
        
        if not ok or not name:
            return
        
        # Get format choice
        format_choice, ok = QInputDialog.getItem(
            self,
            "Export Format",
            "Choose export format:",
            ["JSON", "CSV"],
            0,
            False
        )
        
        if not ok:
            return
        
        # Collect checked items
        checked_items = self._collect_checked_items()
        
        if not checked_items:
            QMessageBox.warning(self, "No Items", "No items checked for export")
            return
        
        # Export based on format
        export_file = Path(__file__).parent / f"{name}.{format_choice.lower()}"
        
        try:
            if format_choice == "JSON":
                self._export_as_json(export_file, checked_items)
            else:
                self._export_as_csv(export_file, checked_items)
            
            msg = f"✅ Exported {len(checked_items)} items to:\n{export_file.name}"
            self.status_label.setText(msg)
            QMessageBox.information(self, "Export Complete", msg)
        
        except Exception as e:
            error_msg = f"❌ Export failed: {e}"
            self.status_label.setText(error_msg)
            QMessageBox.critical(self, "Export Error", error_msg)
    
    def _collect_checked_items(self):
        """Collect all checked items from all tables"""
        checked_items = []
        
        for table_key, table in self.tables.items():
            for row in range(table.rowCount()):
                check_item = table.item(row, 0)
                if check_item and isinstance(check_item, ChecklistItem):
                    if check_item.checkState() == Qt.Checked:
                        # Retrieve the full item metadata (including 'file' field)
                        original_item = check_item.data(Qt.UserRole)
                        
                        if isinstance(original_item, dict):
                            # Use original data as base and update with current state
                            checked_item = original_item.copy()
                            checked_item['category'] = table_key
                            checked_item['status'] = table.item(row, 4).text() if table.item(row, 4) else ""
                            checked_item['checked_at'] = datetime.now().isoformat()
                        else:
                            # Fallback for items without metadata (shouldn't happen)
                            name = table.item(row, 1).text() if table.item(row, 1) else ""
                            line = table.item(row, 2).text() if table.item(row, 2) else ""
                            item_type = table.item(row, 3).text() if table.item(row, 3) else ""
                            status = table.item(row, 4).text() if table.item(row, 4) else ""
                            
                            checked_item = {
                                'category': table_key,
                                'name': name,
                                'line': line,
                                'type': item_type,
                                'status': status,
                                'checked_at': datetime.now().isoformat(),
                            }
                        
                        checked_items.append(checked_item)
        
        return checked_items
    
    def _export_as_json(self, filepath, items):
        """Export items as JSON"""
        export_data = {
            'exported_at': datetime.now().isoformat(),
            'total_items': len(items),
            'items': items,
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2)
    
    def _export_as_csv(self, filepath, items):
        """Export items as CSV"""
        if not items:
            return
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['category', 'name', 'line', 'type', 'status', 'checked_at']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(items)

    def import_validation_dialog(self):
        """Prompt the user to select an exported JSON and run the validator."""
        export_file, _ = QFileDialog.getOpenFileName(
            self,
            "Select Export File",
            str(Path(__file__).parent),
            "JSON Files (*.json *.JSON)",
        )
        if not export_file:
            return
        # Start the import in background
        self.run_import_validation(export_file)

    def run_import_validation(self, export_file: str):
        """Run the import/validation script in a background thread and reload the checklist when done."""
        script = Path(__file__).parent / 'tools' / 'import_export_validate.py'
        report_path = Path(__file__).parent / 'checklist_validation_report.json'
        cmd = [sys.executable, str(script), '--export-file', export_file, '--scan-file', str(self.data_file), '--out-report', str(report_path)]

        self.status_label.setText("🔁 Importing validation (background)...")
        t = threading.Thread(target=self._run_import_thread, args=(cmd, report_path), daemon=True)
        t.start()

    def _run_import_thread(self, cmd, report_path):
        try:
            p = subprocess.run(cmd, capture_output=True, text=True)
            rc = p.returncode
            out = p.stdout
            err = p.stderr
        except Exception as e:
            rc = 1
            out = ''
            err = str(e)

        # Marshal back to the GUI thread
        QTimer.singleShot(0, lambda: self._import_finished(rc, out, err, report_path))

    def _import_finished(self, rc, out, err, report_path: Path):
        if rc != 0:
            QMessageBox.critical(self, "Import Failed", f"Import failed (exit {rc}).\n\nError:\n{err}\n\nOutput:\n{out}")
            self.status_label.setText("❌ Import failed")
            return

        # Try to read the report and present a short summary
        try:
            if report_path.exists():
                with open(report_path, 'r', encoding='utf-8') as f:
                    report = json.load(f)
                counts = report.get('counts', {})
                marked = counts.get('ok', 0) + counts.get('resolved_now_present', 0)
                unused = counts.get('unused', 0)
                imported_at = report.get('imported_at')
                self.status_label.setText(f"✅ Imported: {marked} marked, {unused} unused flagged (at {imported_at})")
            else:
                self.status_label.setText("✅ Import complete; report not found")
        except Exception:
            self.status_label.setText("✅ Import complete (failed to read report)")

        # Reload the checklist data to reflect changes
        try:
            self.load_checklist_data()
        except Exception:
            pass

        # If user has persistent auto-ignore setting, apply it now
        try:
            settings = self._load_settings()
            if settings.get('auto_ignore_unused'):
                report_results = report.get('results', []) if 'report' in locals() else []
                ignore_count = 0
                for rec in report_results:
                    if rec.get('action') != 'unused_flagged_for_review':
                        continue
                    exported = rec.get('exported', {})
                    cat = exported.get('category')
                    if not cat:
                        continue
                    target_name = (rec.get('matched_item') or {}).get('name') or exported.get('name')
                    target_line = (rec.get('matched_item') or {}).get('line') or exported.get('line')
                    for entry in self.checklist_data.get(cat, []):
                        if entry.get('name') == target_name and (str(entry.get('line', '')) == str(target_line) or target_line is None):
                            entry['ignored'] = True
                            ignore_count += 1
                            break
                if ignore_count:
                    try:
                        with open(self.data_file, 'w', encoding='utf-8') as fh:
                            json.dump(self.checklist_data, fh, indent=2)
                        self.load_checklist_data()
                        self.status_label.setText(self.status_label.text() + f" | Auto-ignored {ignore_count} unused items")
                    except Exception as e:
                        print(f"Auto-ignore write failed: {e}")
        except Exception as e:
            print(f"Auto-ignore failed: {e}")

        QMessageBox.information(self, "Import Complete", "Import completed and checklist reloaded.")

    def show_triage_dialog(self):
        """Open a simple dialog to triage 'unused' or ambiguous items from the report."""
        report_path = Path(__file__).parent / 'checklist_validation_report.json'
        if not report_path.exists():
            QMessageBox.warning(self, "No report", "Validation report not found. Run Import Validation first.")
            return

        try:
            with open(report_path, 'r', encoding='utf-8') as f:
                report = json.load(f)
            results = report.get('results') or report.get('results_sample') or []
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Could not read report: {e}")
            return

        # Filter items to triage (unused / not_found / unknown)
        triage_items = [r for r in results if r.get('action') in ('unused_flagged_for_review', 'not_found_in_scan', 'unknown_status')]
        if not triage_items:
            QMessageBox.information(self, "Nothing to triage", "No unused/ambiguous items found in the report.")
            return

        dlg = QDialog(self)
        dlg.setWindowTitle("Triage Unused / Ambiguous Items")
        dlg_layout = QVBoxLayout(dlg)

        splitter = QSplitter(Qt.Horizontal)

        # Left: list of triage entries
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        triage_table = QTableWidget()
        triage_table.setColumnCount(5)
        triage_table.setHorizontalHeaderLabels(['#', 'Category', 'Name', 'Line', 'Action'])
        triage_table.setRowCount(len(triage_items))

        for i, rec in enumerate(triage_items):
            exported = rec.get('exported', {})
            cat = exported.get('category', '')
            matched = rec.get('matched_item') or {}
            name = matched.get('name') or exported.get('name', '')
            line = str(matched.get('line', exported.get('line', '')))
            action = rec.get('action', '')

            triage_table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            triage_table.setItem(i, 1, QTableWidgetItem(cat))
            triage_table.setItem(i, 2, QTableWidgetItem(name))
            triage_table.setItem(i, 3, QTableWidgetItem(line))
            triage_table.setItem(i, 4, QTableWidgetItem(action))

        left_layout.addWidget(QLabel("Select an item to view candidate occurrences and snippet:"))
        left_layout.addWidget(triage_table)
        splitter.addWidget(left_widget)

        # Right: candidates + snippet viewer
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        right_layout.addWidget(QLabel("Candidates (select one):"))
        candidate_table = QTableWidget()
        candidate_table.setColumnCount(2)
        candidate_table.setHorizontalHeaderLabels(['File', 'Line'])
        candidate_table.setColumnWidth(0, 380)
        candidate_table.setColumnWidth(1, 80)
        right_layout.addWidget(candidate_table)

        right_layout.addWidget(QLabel("Code snippet preview (target line highlighted):"))
        snippet_view = QTextEdit()
        snippet_view.setReadOnly(True)
        font = snippet_view.font()
        try:
            font.setFamily('Courier New')
            font.setPointSize(9)
        except Exception:
            pass
        snippet_view.setFont(font)
        snippet_view.setStyleSheet("QTextEdit { background-color: #f5f5f5; }")
        right_layout.addWidget(snippet_view)

        # Persistent auto-ignore option
        settings = self._load_settings()
        auto_ignore_checkbox = QCheckBox("Persist auto-ignore unused (apply on import)")
        auto_ignore_checkbox.setChecked(bool(settings.get('auto_ignore_unused')))
        def _toggle_auto_ignore(state):
            settings['auto_ignore_unused'] = bool(state == QtCore_Qt.Checked)
            self._save_settings(settings)
        auto_ignore_checkbox.stateChanged.connect(_toggle_auto_ignore)
        right_layout.addWidget(auto_ignore_checkbox)

        splitter.addWidget(right_widget)
        dlg_layout.addWidget(splitter)

        btn_layout = QHBoxLayout()
        mark_btn = QPushButton("Mark Checked")
        ignore_btn = QPushButton("Ignore Selected")
        close_btn = QPushButton("Close")
        btn_layout.addWidget(mark_btn)
        btn_layout.addWidget(ignore_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(close_btn)
        dlg_layout.addLayout(btn_layout)

        # Search Python files in workspace once at dialog open
        py_files = self._find_python_files(max_results=100)

        # Helpers to populate candidates and show snippet with highlighting
        def _populate_candidates_for_row(row_index: int):
            candidate_table.setRowCount(0)
            snippet_view.clear()
            if row_index < 0 or row_index >= len(triage_items):
                return
            rec = triage_items[row_index]
            exported = rec.get('exported', {})
            cat = exported.get('category')
            name = (rec.get('matched_item') or {}).get('name') or exported.get('name')

            candidates = []
            # First priority: gather candidates from current checklist_data (same category & name)
            for entry in self.checklist_data.get(cat, []):
                if entry.get('name') == name:
                    fp = entry.get('file') or str(Path(__file__).parent / 'MAIN_FILE.py')
                    ln = entry.get('line')
                    candidates.append((fp, ln))

            # If validator matched a specific item, ensure it's included
            matched = rec.get('matched_item')
            if matched and not any((str(matched.get('line')) == str(c[1])) for c in candidates):
                fp = str(Path(__file__).parent / 'MAIN_FILE.py')
                candidates.insert(0, (fp, matched.get('line')))

            # Second priority: search workspace Python files for the method/attribute definition
            if not candidates and py_files:
                try:
                    workspace_matches = self._search_for_method_in_files(name, py_files)
                    candidates.extend(workspace_matches)
                except Exception:
                    pass

            candidate_table.setRowCount(len(candidates))
            for i, (fp, ln) in enumerate(candidates):
                candidate_table.setItem(i, 0, QTableWidgetItem(str(fp)))
                candidate_table.setItem(i, 1, QTableWidgetItem(str(ln if ln is not None else '')))

        def _show_candidate_snippet():
            r = candidate_table.currentRow()
            if r < 0:
                return
            file_item = candidate_table.item(r, 0)
            line_item = candidate_table.item(r, 1)
            if not file_item:
                return
            fp = file_item.text()
            try:
                ln = int(line_item.text()) if line_item and line_item.text().strip() != '' else None
            except Exception:
                ln = None

            # Get snippet with highlight line number
            snippet_text, highlight_line = self._get_snippet_with_highlight(fp, ln)
            snippet_view.setText(snippet_text)

            # Apply visual highlight to the target line
            if highlight_line > 0:
                cursor = QTextCursor(snippet_view.document())
                # Move to the start of the highlight line
                for _ in range(highlight_line - 1):
                    cursor.movePosition(QTextCursor.Down)
                cursor.select(QTextCursor.LineUnderCursor)

                # Create a format with yellow background
                fmt = QTextCharFormat()
                fmt.setBackground(QBrush(QColor(255, 255, 0, 200)))  # Yellow with slight transparency
                fmt.setForeground(QBrush(QColor(0, 0, 0)))  # Black text

                # Apply the format
                cursor.mergeCharFormat(fmt)

        # Wire selection changes
        triage_table.itemSelectionChanged.connect(lambda: _populate_candidates_for_row(triage_table.currentRow()))
        candidate_table.itemSelectionChanged.connect(_show_candidate_snippet)

        def _mark_checked():
            sel_rows = triage_table.selectionModel().selectedRows()
            if not sel_rows:
                QMessageBox.warning(dlg, "No selection", "No rows selected to mark")
                return
            marked_count = 0
            for index in sel_rows:
                row = index.row()
                rec = triage_items[row]
                exported = rec.get('exported', {})
                cat = exported.get('category')
                if not cat:
                    continue

                # Prefer explicitly selected candidate if present
                cand_row = candidate_table.currentRow()
                if cand_row >= 0 and candidate_table.rowCount() > cand_row:
                    fp_item = candidate_table.item(cand_row, 0)
                    ln_item = candidate_table.item(cand_row, 1)
                    target_line = int(ln_item.text()) if ln_item and ln_item.text().strip() != '' else None
                    target_name = (rec.get('matched_item') or {}).get('name') or exported.get('name')
                    # Find matching entry
                    found = False
                    for entry in self.checklist_data.get(cat, []):
                        if entry.get('name') == target_name and (str(entry.get('line', '')) == str(target_line) or target_line is None):
                            entry['checked'] = True
                            entry['checked_at'] = datetime.now().isoformat()
                            found = True
                            marked_count += 1
                            break
                    if not found:
                        # name-only fallback
                        for entry in self.checklist_data.get(cat, []):
                            if entry.get('name') == target_name:
                                entry['checked'] = True
                                entry['checked_at'] = datetime.now().isoformat()
                                marked_count += 1
                                break
                else:
                    # No candidate selected, fall back to exported/matched info
                    target_name = (rec.get('matched_item') or {}).get('name') or exported.get('name')
                    target_line = (rec.get('matched_item') or {}).get('line') or exported.get('line')
                    for entry in self.checklist_data.get(cat, []):
                        if entry.get('name') == target_name and (str(entry.get('line', '')) == str(target_line) or target_line is None):
                            entry['checked'] = True
                            entry['checked_at'] = datetime.now().isoformat()
                            marked_count += 1
                            break

            try:
                with open(self.data_file, 'w', encoding='utf-8') as fh:
                    json.dump(self.checklist_data, fh, indent=2)
                self.load_checklist_data()
                QMessageBox.information(dlg, "Marked", f"Marked {marked_count} items as checked")
            except Exception as e:
                QMessageBox.critical(dlg, "Error", f"Failed to write checklist file: {e}")

        def _ignore_selected():
            sel_rows = triage_table.selectionModel().selectedRows()
            if not sel_rows:
                QMessageBox.warning(dlg, "No selection", "No rows selected to ignore")
                return
            ignored_count = 0
            for index in sel_rows:
                row = index.row()
                rec = triage_items[row]
                exported = rec.get('exported', {})
                cat = exported.get('category')
                if not cat:
                    continue

                cand_row = candidate_table.currentRow()
                if cand_row >= 0 and candidate_table.rowCount() > cand_row:
                    ln_item = candidate_table.item(cand_row, 1)
                    target_line = int(ln_item.text()) if ln_item and ln_item.text().strip() != '' else None
                    target_name = (rec.get('matched_item') or {}).get('name') or exported.get('name')
                    for entry in self.checklist_data.get(cat, []):
                        if entry.get('name') == target_name and (str(entry.get('line', '')) == str(target_line) or target_line is None):
                            entry['ignored'] = True
                            ignored_count += 1
                            break
                else:
                    target_name = (rec.get('matched_item') or {}).get('name') or exported.get('name')
                    target_line = (rec.get('matched_item') or {}).get('line') or exported.get('line')
                    for entry in self.checklist_data.get(cat, []):
                        if entry.get('name') == target_name and (str(entry.get('line', '')) == str(target_line) or target_line is None):
                            entry['ignored'] = True
                            ignored_count += 1
                            break

            try:
                with open(self.data_file, 'w', encoding='utf-8') as fh:
                    json.dump(self.checklist_data, fh, indent=2)
                self.load_checklist_data()
                QMessageBox.information(dlg, "Ignored", f"Ignored {ignored_count} items")
            except Exception as e:
                QMessageBox.critical(dlg, "Error", f"Failed to write checklist file: {e}")

        mark_btn.clicked.connect(_mark_checked)
        ignore_btn.clicked.connect(_ignore_selected)
        close_btn.clicked.connect(dlg.accept)

        dlg.setLayout(dlg_layout)
        dlg.exec_()

    
    def check_dependencies_clicked(self):
        """Check and display dependencies status in a modal dialog"""
        if not DependencyChecker:
            QMessageBox.warning(self, "Error", "DependencyChecker module not available")
            return
        
        try:
            # Run dependency check
            app_root = Path(__file__).parent
            checker = DependencyChecker(app_root)
            result = checker.check_dependencies()
            
            # Create dialog for results
            dlg = QDialog(self)
            dlg.setWindowTitle("Dependency Check Results")
            dlg.setGeometry(200, 200, 1000, 400)
            
            dlg_layout = QVBoxLayout()
            
            # Status summary
            status_label = QLabel(result['status'])
            status_font = QFont()
            status_font.setBold(True)
            status_label.setFont(status_font)
            
            # Color based on status
            if result['all_ok']:
                status_label.setStyleSheet("color: green; font-weight: bold;")
            else:
                status_label.setStyleSheet("color: red; font-weight: bold;")
            
            dlg_layout.addWidget(status_label)
            
            # Summary info
            summary_text = f"Found: {result['found']}/{result['total']} dependencies"
            if result['missing'] > 0:
                missing_critical = [f for f in result['missing_files'] 
                                   if DependencyChecker.REQUIRED_FILES[f]['critical']]
                if missing_critical:
                    summary_text += f"\nCritical Missing: {', '.join(missing_critical)}"
                else:
                    summary_text += f"\nOptional Missing: {result['missing']}"
            
            summary_label = QLabel(summary_text)
            dlg_layout.addWidget(summary_label)
            
            # Dependencies table
            table = QTableWidget()
            populate_dependencies_table(table, result['results'])
            dlg_layout.addWidget(table)
            
            # Buttons
            btn_layout = QHBoxLayout()
            
            save_btn = QPushButton("💾 Save Report")
            def save_report():
                file_path, _ = QFileDialog.getSaveFileName(
                    dlg, "Save Dependency Report", "",
                    "JSON Files (*.json);;CSV Files (*.csv)"
                )
                if file_path:
                    try:
                        if file_path.endswith('.csv'):
                            with open(file_path, 'w', newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(['Status', 'File Name', 'Category', 'Description', 'Critical'])
                                for dep in result['results']:
                                    writer.writerow([
                                        dep['status'],
                                        dep['file'],
                                        dep['category'],
                                        dep['description'],
                                        'YES' if dep['critical'] else 'No'
                                    ])
                        else:
                            checker.save_check_results(file_path)
                        QMessageBox.information(dlg, "Success", f"Report saved to {file_path}")
                    except Exception as e:
                        QMessageBox.critical(dlg, "Error", f"Failed to save report: {e}")
            
            save_btn.clicked.connect(save_report)
            btn_layout.addWidget(save_btn)
            
            close_btn = QPushButton("Close")
            close_btn.clicked.connect(dlg.accept)
            btn_layout.addWidget(close_btn)
            
            dlg_layout.addLayout(btn_layout)
            dlg.setLayout(dlg_layout)
            dlg.exec_()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Dependency check failed: {e}")


