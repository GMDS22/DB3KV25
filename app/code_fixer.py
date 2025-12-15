"""
CODE FIXER - Search, Identify, and Fix Code Issues

This tool allows you to:
1. Search for code patterns (e.g., "HOME", "Button", etc.)
2. View all relevant code blocks
3. Identify issues and errors
4. Edit code and apply fixes
5. Insert corrected code into the main file

Author: Auto Turret Project
Date: 2025-11-17
"""

import sys
import re
import os
from typing import List, Tuple, Dict, Set
from pathlib import Path

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QTextEdit, QLabel, QComboBox,
    QListWidget, QListWidgetItem, QSplitter, QMessageBox,
    QDialog, QTabWidget, QCheckBox, QSpinBox, QStatusBar,
    QMenuBar, QMenu, QFileDialog, QProgressBar
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QFont, QColor, QTextCursor, QSyntaxHighlighter, QTextCharFormat


class PythonHighlighter(QSyntaxHighlighter):
    """Syntax highlighter for Python code."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []
        
        # Keywords format
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor(86, 156, 214))
        keyword_format.setFontWeight(75)
        keywords = ['def', 'class', 'if', 'else', 'elif', 'for', 'while', 'try', 'except',
                   'import', 'from', 'return', 'pass', 'break', 'continue', 'True', 'False', 'None']
        for word in keywords:
            self.highlighting_rules.append((f'\\b{word}\\b', keyword_format))
        
        # String format
        string_format = QTextCharFormat()
        string_format.setForeground(QColor(206, 145, 120))
        self.highlighting_rules.append(('".*?"', string_format))
        self.highlighting_rules.append(("'.*?'", string_format))
        
        # Comment format
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor(87, 166, 74))
        self.highlighting_rules.append(('#.*', comment_format))
    
    def highlightBlock(self, text):
        for pattern, fmt in self.highlighting_rules:
            for match in re.finditer(pattern, text):
                self.setFormat(match.start(), match.end() - match.start(), fmt)


class CodeSearcher:
    """Searches for code patterns in Python files."""
    
    def __init__(self, directory: str = "."):
        self.directory = directory
        self.results: Dict[str, List[Tuple[int, str]]] = {}
    
    def search(self, pattern: str, case_sensitive: bool = False, 
               whole_word: bool = False, file_pattern: str = "*.py") -> Dict[str, List[Tuple[int, str]]]:
        """
        Search for pattern in Python files.
        Returns dict: {filename: [(line_num, code_line), ...]}
        """
        self.results = {}
        
        # Build regex pattern
        if whole_word:
            search_pattern = r'\b' + re.escape(pattern) + r'\b'
        else:
            search_pattern = re.escape(pattern)
        
        flags = 0 if case_sensitive else re.IGNORECASE
        
        try:
            # Find all matching files
            for py_file in Path(self.directory).glob(file_pattern):
                if not py_file.is_file():
                    continue
                
                try:
                    with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                    
                    matches = []
                    for line_num, line in enumerate(lines, 1):
                        if re.search(search_pattern, line, flags):
                            matches.append((line_num, line.rstrip()))
                    
                    if matches:
                        self.results[str(py_file)] = matches
                
                except Exception as e:
                    print(f"Error reading {py_file}: {e}")
        
        except Exception as e:
            print(f"Search error: {e}")
        
        return self.results


class CodeAnalyzer:
    """Analyzes code for potential issues."""
    
    @staticmethod
    def analyze_block(code_block: str, context: str = "") -> List[str]:
        """
        Analyze code block for issues.
        Returns list of potential issues found.
        """
        issues = []
        lines = code_block.split('\n')
        
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            
            # Check for common issues
            if not stripped or stripped.startswith('#'):
                continue
            
            # Missing parentheses
            if 'addAction(' in stripped and 'connect(' not in stripped and '.triggered' not in stripped:
                issues.append(f"Line {i}: Action created but not connected")
            
            # Button not wired
            if 'Button' in context and 'clicked.connect' not in code_block:
                issues.append("Button created but not connected to handler")
            
            # Missing signal connection
            if '.connect(' in stripped and 'lambda' not in stripped and '=' not in stripped:
                issues.append(f"Line {i}: Signal connection without proper callback")
            
            # Undefined variables
            if 'self.' in stripped and '=' not in stripped:
                attr = re.search(r'self\.(\w+)', stripped)
                if attr:
                    var_name = attr.group(1)
                    if not any(f'self.{var_name}' in l for l in lines[:i-1]):
                        pass  # Commented out to reduce noise
            
            # Missing imports
            if any(x in stripped for x in ['QMessageBox', 'QDialog', 'QFileDialog']) and 'import' not in code_block:
                class_name = [x for x in ['QMessageBox', 'QDialog', 'QFileDialog'] if x in stripped][0]
                if f'from PyQt5.QtWidgets import' not in code_block or class_name not in code_block:
                    issues.append(f"⚠️ {class_name} used but may not be imported")
            
            # Syntax issues
            if line.endswith(':') and i < len(lines):
                if lines[i].strip() and not lines[i].startswith(' ' * (len(line) - len(line.lstrip()) + 4)):
                    if not lines[i].strip().startswith('#'):
                        issues.append(f"Line {i+1}: Possible indentation error after colon")
            
            # Unused variables
            if 'self.' in stripped and '=' in stripped:
                var = re.search(r'self\.(\w+)\s*=', stripped)
                if var:
                    var_name = var.group(1)
                    # Check if used later
                    remaining = '\n'.join(lines[i:])
                    if f'self.{var_name}' not in remaining and 'return' not in stripped:
                        pass  # Don't flag as unused (too noisy)
        
        return issues


class CodeFixer(QMainWindow):
    """Main CODE FIXER application window."""
    
    search_updated = pyqtSignal(dict)
    
    def __init__(self, search_directory: str = ".", parent=None):
        super().__init__(parent)
        self.setWindowTitle("CODE FIXER - Search, Analyze & Fix")
        self.setGeometry(100, 100, 1400, 800)
        
        self.search_dir = search_directory
        self.searcher = CodeSearcher(search_directory)
        self.analyzer = CodeAnalyzer()
        self.current_file = None
        self.current_results = {}
        self.selected_code = None
        
        self.init_ui()
        self.apply_dark_theme()
    
    def init_ui(self):
        """Initialize UI components."""
        # Initialize status bar early so it's available to all methods
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(8)
        
        # ====== SEARCH SECTION ======
        search_layout = QHBoxLayout()
        search_layout.setSpacing(8)
        
        # Search input
        search_label = QLabel("Search for:")
        search_label.setStyleSheet("color: #00ff00; font-weight: bold;")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("e.g., 'HOME', 'Button', 'clicked', etc.")
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #444444;
                padding: 6px;
                border-radius: 3px;
            }
        """)
        self.search_input.returnPressed.connect(self.on_search)
        
        # Search options
        self.case_sensitive = QCheckBox("Case Sensitive")
        self.case_sensitive.setStyleSheet("color: #e0e0e0;")
        
        self.whole_word = QCheckBox("Whole Word")
        self.whole_word.setStyleSheet("color: #e0e0e0;")
        
        # File pattern
        file_label = QLabel("Files:")
        file_label.setStyleSheet("color: #e0e0e0;")
        self.file_pattern = QComboBox()
        self.file_pattern.addItems(["*.py", "MAIN_FILE.py", "*.py (all)"])
        self.file_pattern.setStyleSheet("""
            QComboBox {
                background-color: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #444444;
                padding: 4px;
            }
        """)
        
        # Font size control
        font_label = QLabel("Font:")
        font_label.setStyleSheet("color: #e0e0e0;")
        self.font_size_spin = QSpinBox()
        self.font_size_spin.setMinimum(8)
        self.font_size_spin.setMaximum(20)
        self.font_size_spin.setValue(11)
        self.font_size_spin.setStyleSheet("""
            QSpinBox {
                background-color: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #444444;
                padding: 4px;
                width: 50px;
            }
        """)
        self.font_size_spin.valueChanged.connect(self.update_font_size)
        
        # Search button
        search_btn = QPushButton("🔍 Search")
        search_btn.setStyleSheet("""
            QPushButton {
                background-color: #003d00;
                color: #00ff00;
                border: 1px solid #00ff00;
                padding: 6px 16px;
                border-radius: 3px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #005500; }
            QPushButton:pressed { background-color: #002200; }
        """)
        search_btn.clicked.connect(self.on_search)
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input, 1)
        search_layout.addWidget(self.case_sensitive)
        search_layout.addWidget(self.whole_word)
        search_layout.addWidget(file_label)
        search_layout.addWidget(self.file_pattern)
        search_layout.addWidget(font_label)
        search_layout.addWidget(self.font_size_spin)
        search_layout.addWidget(search_btn)
        main_layout.addLayout(search_layout)
        
        # ====== RESULTS SECTION ======
        # Results panel with label
        results_panel = QWidget()
        results_layout = QVBoxLayout(results_panel)
        results_layout.setContentsMargins(0, 0, 0, 0)
        results_layout.setSpacing(2)
        
        results_label = QLabel("📄 Results:")
        results_label.setStyleSheet("color: #00ff00; font-weight: bold; font-size: 10px;")
        results_label.setMaximumHeight(20)
        results_layout.addWidget(results_label)
        
        # Results list (smaller, compact)
        self.results_list = QListWidget()
        self.results_list.setStyleSheet("""
            QListWidget {
                background-color: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #444444;
                outline: none;
                margin: 0px;
            }
            QListWidget::item:selected { background-color: #004d00; }
        """)
        self.results_list.setMinimumWidth(200)
        self.results_list.itemClicked.connect(self.on_result_selected)
        results_layout.addWidget(self.results_list)
        
        # Results splitter (horizontal)
        main_splitter = QSplitter(Qt.Horizontal)
        main_splitter.setCollapsible(0, False)
        main_splitter.setCollapsible(1, False)
        
        main_splitter.addWidget(results_panel)
        
        # Code and analysis panel (right side with vertical splitter)
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(6)
        
        # Vertical splitter for code view and editor
        vertical_splitter = QSplitter(Qt.Vertical)
        vertical_splitter.setCollapsible(0, False)
        vertical_splitter.setCollapsible(1, False)
        
        # Tabs for code/analysis at top
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane { border: 1px solid #444444; }
            QTabBar::tab {
                background-color: #2d2d2d;
                color: #e0e0e0;
                padding: 4px 12px;
                border: 1px solid #444444;
                margin: 0px;
            }
            QTabBar::tab:selected {
                background-color: #003d00;
                color: #00ff00;
                border: 1px solid #00ff00;
            }
        """)
        self.tabs.setMinimumHeight(150)
        
        # Code View Tab
        self.code_view = QTextEdit()
        self.code_view.setReadOnly(True)
        self.code_view.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 1px solid #444444;
                font-family: 'Courier New';
                font-size: 11px;
            }
        """)
        font = QFont('Courier New', 11)
        self.code_view.setFont(font)
        self.highlighter = PythonHighlighter(self.code_view.document())
        self.tabs.addTab(self.code_view, "📝 Code View")
        
        # Analysis Tab
        self.analysis_view = QTextEdit()
        self.analysis_view.setReadOnly(True)
        self.analysis_view.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #ffff00;
                border: 1px solid #444444;
                font-family: 'Courier New';
                font-size: 11px;
            }
        """)
        font = QFont('Courier New', 11)
        self.analysis_view.setFont(font)
        self.tabs.addTab(self.analysis_view, "⚠️ Analysis")
        
        # Fix Library Tab
        fix_library_container = QWidget()
        fix_library_layout = QVBoxLayout(fix_library_container)
        fix_library_layout.setContentsMargins(8, 8, 8, 8)
        fix_library_layout.setSpacing(6)
        
        # Search bar for fixes
        fix_search_layout = QHBoxLayout()
        fix_search_label = QLabel("🔍 Search Fixes:")
        fix_search_label.setStyleSheet("color: #00ff00; font-weight: bold;")
        self.fix_search_input = QLineEdit()
        self.fix_search_input.setPlaceholderText("Type to filter fixes by name or category...")
        self.fix_search_input.setStyleSheet("""
            QLineEdit {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 1px solid #444444;
                padding: 4px;
            }
        """)
        self.fix_search_input.textChanged.connect(self.filter_fixes)
        fix_search_layout.addWidget(fix_search_label)
        fix_search_layout.addWidget(self.fix_search_input)
        fix_library_layout.addLayout(fix_search_layout)
        
        # Fixes list and preview splitter
        fix_splitter = QSplitter(Qt.Horizontal)
        
        # Left: List of available fixes
        fix_list_layout = QVBoxLayout()
        fix_list_label = QLabel("📚 Available Fixes:")
        fix_list_label.setStyleSheet("color: #00ffff; font-weight: bold;")
        fix_list_layout.addWidget(fix_list_label)
        
        self.fix_list_widget = QListWidget()
        self.fix_list_widget.setStyleSheet("""
            QListWidget {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 1px solid #444444;
            }
            QListWidget::item:selected {
                background-color: #003d3d;
                color: #00ffff;
            }
        """)
        self.fix_list_widget.itemClicked.connect(self.on_fix_selected)
        fix_list_layout.addWidget(self.fix_list_widget)
        
        fix_list_widget = QWidget()
        fix_list_widget.setLayout(fix_list_layout)
        
        # Right: Fix preview and details
        fix_preview_layout = QVBoxLayout()
        fix_preview_label = QLabel("📄 Fix Content Preview:")
        fix_preview_label.setStyleSheet("color: #00ffff; font-weight: bold;")
        fix_preview_layout.addWidget(fix_preview_label)
        
        self.fix_preview_view = QTextEdit()
        self.fix_preview_view.setReadOnly(True)
        self.fix_preview_view.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 1px solid #444444;
                font-family: 'Courier New';
                font-size: 10px;
            }
        """)
        font = QFont('Courier New', 10)
        self.fix_preview_view.setFont(font)
        self.fix_preview_highlighter = PythonHighlighter(self.fix_preview_view.document())
        fix_preview_layout.addWidget(self.fix_preview_view)
        
        fix_preview_widget = QWidget()
        fix_preview_widget.setLayout(fix_preview_layout)
        
        fix_splitter.addWidget(fix_list_widget)
        fix_splitter.addWidget(fix_preview_widget)
        fix_splitter.setStretchFactor(0, 1)
        fix_splitter.setStretchFactor(1, 2)
        
        fix_library_layout.addWidget(fix_splitter)
        
        # Action buttons for fixes
        fix_buttons_layout = QHBoxLayout()
        fix_buttons_layout.setSpacing(4)
        
        apply_fix_btn = QPushButton("✅ Load Fix to Editor")
        apply_fix_btn.setMaximumHeight(28)
        apply_fix_btn.setToolTip("Load the selected fix into the editor for review and application.")
        apply_fix_btn.setStyleSheet(self.get_button_style("#003d00", "#00ff00"))
        apply_fix_btn.clicked.connect(self.load_fix_to_editor)
        fix_buttons_layout.addWidget(apply_fix_btn)
        
        view_full_file_btn = QPushButton("📂 View Full File")
        view_full_file_btn.setMaximumHeight(28)
        view_full_file_btn.setToolTip("Open a window showing the complete file after applying the selected fix.")
        view_full_file_btn.setStyleSheet(self.get_button_style("#1a3a1a", "#66ff66"))
        view_full_file_btn.clicked.connect(self.show_full_file_viewer)
        fix_buttons_layout.addWidget(view_full_file_btn)
        
        refresh_scan_btn = QPushButton("🔄 Refresh & Rescan")
        refresh_scan_btn.setMaximumHeight(28)
        refresh_scan_btn.setToolTip("Rescan MAIN_FILE.py to refresh the issues list.")
        refresh_scan_btn.setStyleSheet(self.get_button_style("#003d3d", "#00ffff"))
        refresh_scan_btn.clicked.connect(self.refresh_and_rescan)
        fix_buttons_layout.addWidget(refresh_scan_btn)
        
        fix_buttons_layout.addStretch()
        fix_library_layout.addLayout(fix_buttons_layout)
        
        self.tabs.addTab(fix_library_container, "🔧 Fix Library")
        
        # Load fixes on startup
        self.load_available_fixes()

        vertical_splitter.addWidget(self.tabs)
        
        # Editor section at bottom
        editor_container = QWidget()
        editor_layout = QVBoxLayout(editor_container)
        editor_layout.setContentsMargins(0, 0, 0, 0)
        editor_layout.setSpacing(4)
        
        editor_label = QLabel("✏️ Edit & Fix Code:")
        editor_label.setStyleSheet("color: #00ff00; font-weight: bold; font-size: 10px;")
        editor_layout.addWidget(editor_label)
        
        self.code_editor = QTextEdit()
        self.code_editor.setMinimumHeight(150)
        self.code_editor.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 1px solid #444444;
                font-family: 'Courier New';
                font-size: 11px;
            }
        """)
        font = QFont('Courier New', 11)
        self.code_editor.setFont(font)
        # Add syntax highlighting to editor
        self.editor_highlighter = PythonHighlighter(self.code_editor.document())
        editor_layout.addWidget(self.code_editor)
        
        vertical_splitter.addWidget(editor_container)
        vertical_splitter.setStretchFactor(0, 1)
        vertical_splitter.setStretchFactor(1, 1)
        vertical_splitter.setSizes([250, 250])
        
        right_layout.addWidget(vertical_splitter)
        
        # Action buttons (compact)
        button_layout = QHBoxLayout()
        button_layout.setSpacing(4)
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        copy_btn = QPushButton("📋 Copy")
        copy_btn.setMaximumHeight(28)
        copy_btn.setToolTip("Copy the current code view to the clipboard.")
        copy_btn.setStyleSheet(self.get_button_style("#003d3d", "#00ffff"))
        copy_btn.clicked.connect(self.copy_to_clipboard)
        button_layout.addWidget(copy_btn)
        
        paste_btn = QPushButton("📎 Paste")
        paste_btn.setMaximumHeight(28)
        paste_btn.setToolTip("Paste clipboard contents into the editor.")
        paste_btn.setStyleSheet(self.get_button_style("#003d3d", "#00ffff"))
        paste_btn.clicked.connect(self.paste_from_clipboard)
        button_layout.addWidget(paste_btn)
        
        clear_edit_btn = QPushButton("🗑️ Clear")
        clear_edit_btn.setMaximumHeight(28)
        clear_edit_btn.setToolTip("Clear the editor contents.")
        clear_edit_btn.setStyleSheet(self.get_button_style("#3d0000", "#ff6666"))
        clear_edit_btn.clicked.connect(self.code_editor.clear)
        button_layout.addWidget(clear_edit_btn)
        
        # Format/beautify button
        format_btn = QPushButton("✨ Format")
        format_btn.setMaximumHeight(28)
        format_btn.setToolTip("Format and beautify code with consistent indentation.")
        format_btn.setStyleSheet(self.get_button_style("#1a3a1a", "#66ff66"))
        format_btn.clicked.connect(self.format_code)
        button_layout.addWidget(format_btn)
        
        right_layout.addLayout(button_layout)
        
        # Insert buttons (compact)
        insert_layout = QHBoxLayout()
        insert_layout.setSpacing(4)
        insert_layout.setContentsMargins(0, 0, 0, 0)
        
        insert_btn = QPushButton("✅ Insert to MAIN_FILE")
        insert_btn.setMaximumHeight(28)
        insert_btn.setToolTip("Append the selected code to MAIN_FILE.py (use with caution).")
        insert_btn.setStyleSheet(self.get_button_style("#003d00", "#00ff00"))
        insert_btn.clicked.connect(self.insert_to_main_file)
        insert_layout.addWidget(insert_btn)
        
        insert_any_btn = QPushButton("📁 Insert to Any...")
        insert_any_btn.setMaximumHeight(28)
        insert_any_btn.setToolTip("Choose a file and insert the selected code into it.")
        insert_any_btn.setStyleSheet(self.get_button_style("#1a3a1a", "#66ff66"))
        insert_any_btn.clicked.connect(self.insert_to_any_file)
        insert_layout.addWidget(insert_any_btn)
        
        right_layout.addLayout(insert_layout)
        
        main_splitter.addWidget(right_panel)
        main_splitter.setStretchFactor(0, 0)  # Results list stays compact
        main_splitter.setStretchFactor(1, 1)  # Right panel expands
        main_splitter.setSizes([180, 900])  # Results panel narrow by default, easily resizable
        
        main_layout.addWidget(main_splitter)
        
        # ====== STATUS BAR (already initialized at top of init_ui) ======
        self.status_bar.setStyleSheet("background-color: #2d2d2d; color: #e0e0e0;")
        self.status_bar.showMessage("Ready - Enter search term and click Search")
    
    def on_search(self):
        """Execute search."""
        search_term = self.search_input.text().strip()
        if not search_term:
            QMessageBox.warning(self, "Search", "Please enter a search term")
            return
        
        # Get file pattern
        file_pattern = self.file_pattern.currentText()
        if file_pattern == "*.py (all)":
            file_pattern = "*.py"
        
        self.status_bar.showMessage("Searching...")
        
        # Perform search
        results = self.searcher.search(
            search_term,
            case_sensitive=self.case_sensitive.isChecked(),
            whole_word=self.whole_word.isChecked(),
            file_pattern=file_pattern
        )
        
        self.current_results = results
        self.populate_results_list()
        
        total_matches = sum(len(matches) for matches in results.values())
        self.status_bar.showMessage(f"Found {total_matches} matches in {len(results)} file(s)")
    
    def update_font_size(self):
        """Update font size for code views and editor."""
        size = self.font_size_spin.value()
        
        try:
            # Update code view font
            if hasattr(self, 'code_view'):
                font = QFont('Courier New', size)
                self.code_view.setFont(font)
            
            # Update analysis view font
            if hasattr(self, 'analysis_view'):
                font = QFont('Courier New', size)
                self.analysis_view.setFont(font)
            
            # Update editor font
            if hasattr(self, 'code_editor'):
                font = QFont('Courier New', size)
                self.code_editor.setFont(font)
        except Exception as e:
            print(f"Error updating font size: {e}")
    
    def format_code(self):
        """Format/beautify code in editor with proper indentation."""
        code = self.code_editor.toPlainText()
        if not code.strip():
            self.status_bar.showMessage("No code to format")
            return
        
        try:
            # Simple indentation fixer
            lines = code.split('\n')
            formatted = []
            indent_level = 0
            indent_str = "    "  # 4 spaces
            
            for line in lines:
                stripped = line.strip()
                
                # Skip empty lines and comments
                if not stripped:
                    formatted.append("")
                    continue
                
                # Decrease indent for dedenting keywords
                if any(stripped.startswith(x) for x in ['else:', 'elif ', 'except:', 'except ', 'finally:', 'def ', 'class ']):
                    if indent_level > 0 and not line.startswith(' '):
                        indent_level = max(0, indent_level - 1)
                
                # Add line with current indentation
                formatted.append(indent_str * indent_level + stripped)
                
                # Increase indent if line ends with colon
                if stripped.endswith(':'):
                    indent_level += 1
            
            formatted_code = '\n'.join(formatted)
            self.code_editor.setText(formatted_code)
            self.status_bar.showMessage("✓ Code formatted successfully")
        
        except Exception as e:
            QMessageBox.warning(self, "Format Error", f"Could not format code: {e}")
    
    def populate_results_list(self):
        """Populate results list widget."""
        self.results_list.clear()
        
        if not self.current_results:
            item = QListWidgetItem("No results found")
            item.setForeground(QColor(255, 100, 100))
            self.results_list.addItem(item)
            return
        
        for filename, matches in self.current_results.items():
            file_item = QListWidgetItem(f"📄 {Path(filename).name} ({len(matches)} matches)")
            file_item.setForeground(QColor(0, 255, 0))
            file_item.setData(Qt.UserRole, ("file", filename))
            self.results_list.addItem(file_item)
            
            for line_num, code_line in matches:
                code_item = QListWidgetItem(f"  Line {line_num}: {code_line[:80]}")
                code_item.setForeground(QColor(176, 176, 176))
                code_item.setData(Qt.UserRole, ("code", filename, line_num, code_line))
                self.results_list.addItem(code_item)
    
    def on_result_selected(self, item):
        """Handle result selection."""
        data = item.data(Qt.UserRole)
        if not data:
            return
        
        if data[0] == "file":
            return
        
        item_type, filename, line_num, code_line = data
        self.current_file = filename
        self.selected_code = code_line
        
        # Read the file to get context
        try:
            with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                all_lines = f.readlines()
            
            # Get context (10 lines before and after)
            start = max(0, line_num - 11)
            end = min(len(all_lines), line_num + 10)
            context_lines = all_lines[start:end]
            
            # Display with line numbers
            display_code = ""
            for i, line in enumerate(context_lines, start=start+1):
                marker = ">>>" if i == line_num else "   "
                display_code += f"{marker} {i:5d}: {line.rstrip()}\n"
            
            self.code_view.setText(display_code)
            
            # Analyze the block
            code_block = "".join(all_lines[start:end])
            issues = self.analyzer.analyze_block(code_block, code_line)
            
            # Display analysis
            analysis_text = f"File: {Path(filename).name}\nLine: {line_num}\n\n"
            if issues:
                analysis_text += "⚠️ POTENTIAL ISSUES FOUND:\n"
                for issue in issues:
                    analysis_text += f"  • {issue}\n"
            else:
                analysis_text += "✓ No obvious issues detected"
            
            self.analysis_view.setText(analysis_text)
            self.tabs.setCurrentIndex(0)  # Show code tab
            
        except Exception as e:
            self.analysis_view.setText(f"Error reading file: {e}")
    
    def copy_to_clipboard(self):
        """Copy code to clipboard."""
        text = self.code_view.toPlainText()
        if text:
            from PyQt5.QtWidgets import QApplication
            QApplication.clipboard().setText(text)
            self.status_bar.showMessage("Code copied to clipboard")
        else:
            QMessageBox.warning(self, "Copy", "No code to copy")
    
    def paste_from_clipboard(self):
        """Paste from clipboard to editor."""
        from PyQt5.QtWidgets import QApplication
        text = QApplication.clipboard().text()
        if text:
            self.code_editor.setText(text)
            self.tabs.setCurrentIndex(2)  # Show editor tab
            self.status_bar.showMessage("Pasted from clipboard")
        else:
            QMessageBox.warning(self, "Paste", "Clipboard is empty")
    
    def insert_to_main_file(self):
        """Insert fixed code to MAIN_FILE.py."""
        code = self.code_editor.toPlainText()
        if not code.strip():
            QMessageBox.warning(self, "Insert", "Please enter code in the editor first")
            return
        
        main_file = Path(self.search_dir) / "MAIN_FILE.py"
        if not main_file.exists():
            QMessageBox.critical(self, "Insert", f"MAIN_FILE.py not found in {self.search_dir}")
            return
        
        reply = QMessageBox.question(
            self, "Confirm Insert",
            "This will append the code to MAIN_FILE.py.\n\nContinue?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                code_lines = len(code.strip().split('\n'))
                with open(main_file, 'a', encoding='utf-8') as f:
                    f.write("\n# --- Code inserted by CODE FIXER ---\n")
                    f.write(code + "\n")
                    f.write("# --- End of inserted code ---\n")
                
                self.status_bar.showMessage(f"✓ {code_lines} lines inserted to MAIN_FILE.py")
                QMessageBox.information(
                    self, "Success", 
                    f"✓ Code inserted successfully!\n\n"
                    f"Lines added: {code_lines}\n"
                    f"File: MAIN_FILE.py"
                )
                self.code_editor.clear()
            
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to insert: {e}")
                self.status_bar.showMessage(f"✗ Insert failed: {str(e)[:50]}")
    
    def insert_to_any_file(self):
        """Insert fixed code to any file."""
        code = self.code_editor.toPlainText()
        if not code.strip():
            QMessageBox.warning(self, "Insert", "Please enter code in the editor first")
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Select file to insert code", self.search_dir, "Python Files (*.py);;All Files (*)"
        )
        
        if not file_path:
            return
        
        try:
            code_lines = len(code.strip().split('\n'))
            file_name = Path(file_path).name
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write("\n# --- Code inserted by CODE FIXER ---\n")
                f.write(code + "\n")
                f.write("# --- End of inserted code ---\n")
            
            self.status_bar.showMessage(f"✓ {code_lines} lines inserted to {file_name}")
            QMessageBox.information(
                self, "Success",
                f"✓ Code inserted successfully!\n\n"
                f"Lines added: {code_lines}\n"
                f"File: {file_name}"
            )
            self.code_editor.clear()
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to insert: {e}")
            self.status_bar.showMessage(f"✗ Insert failed: {str(e)[:50]}")
    
    def load_available_fixes(self):
        """Load all available fixes from FIXES_LIBRARY."""
        try:
            import json
            from pathlib import Path
            
            fixes_dir = Path("FIXES_LIBRARY")
            if not fixes_dir.exists():
                self.status_bar.showMessage("No FIXES_LIBRARY found")
                return
            
            # Load index
            index_file = fixes_dir / "FIX_LIBRARY_INDEX.json"
            self.available_fixes = []
            
            if index_file.exists():
                with open(index_file, 'r', encoding='utf-8') as f:
                    index = json.load(f)
                    self.available_fixes = index.get("fixes", [])
            
            # Populate list
            self.fix_list_widget.clear()
            for fix in self.available_fixes:
                item = QListWidgetItem()
                status_icon = "✅" if "READY" in fix.get("status", "") else "⚠️"
                display_text = f"{status_icon} {fix.get('filename', '')}\n   {fix.get('issue', '')[:60]}"
                item.setText(display_text)
                item.setData(Qt.UserRole, fix)
                self.fix_list_widget.addItem(item)
            
            self.status_bar.showMessage(f"Loaded {len(self.available_fixes)} fixes from library")
        except Exception as e:
            print(f"[ERROR] load_available_fixes: {e}")
            self.status_bar.showMessage(f"Error loading fixes: {str(e)[:50]}")
    
    def filter_fixes(self):
        """Filter fixes by search term."""
        search_term = self.fix_search_input.text().lower()
        
        for i in range(self.fix_list_widget.count()):
            item = self.fix_list_widget.item(i)
            fix = item.data(Qt.UserRole)
            
            # Search in filename, category, and issue description
            match = (search_term in fix.get("filename", "").lower() or
                    search_term in fix.get("category", "").lower() or
                    search_term in fix.get("issue", "").lower())
            
            item.setHidden(not match)
    
    def on_fix_selected(self, item):
        """Handle fix selection."""
        try:
            fix = item.data(Qt.UserRole)
            fix_path = fix.get("path", "")
            
            # Load and display fix content
            if Path(fix_path).exists():
                with open(fix_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                self.fix_preview_view.setText(content)
                self.current_selected_fix = fix
                self.status_bar.showMessage(f"Selected: {fix.get('filename', '')}")
            else:
                self.fix_preview_view.setText(f"Error: File not found at {fix_path}")
        except Exception as e:
            self.fix_preview_view.setText(f"Error loading fix: {e}")
            print(f"[ERROR] on_fix_selected: {e}")
    
    def load_fix_to_editor(self):
        """Load selected fix into the code editor."""
        try:
            if not hasattr(self, 'current_selected_fix'):
                QMessageBox.warning(self, "No Fix Selected", "Please select a fix first")
                return
            
            fix = self.current_selected_fix
            fix_path = fix.get("path", "")
            
            if not Path(fix_path).exists():
                QMessageBox.critical(self, "Error", f"Fix file not found: {fix_path}")
                return
            
            # Load fix content
            with open(fix_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract just the code blocks (remove docstrings and instructions)
            lines = content.split('\n')
            code_blocks = []
            in_fix_block = False
            
            for line in lines:
                if '# FIX BLOCK' in line:
                    in_fix_block = True
                    code_blocks.append(line)
                elif '# ============' in line and in_fix_block:
                    in_fix_block = False
                    code_blocks.append(line)
                elif in_fix_block:
                    code_blocks.append(line)
            
            if code_blocks:
                extracted_code = '\n'.join(code_blocks)
            else:
                # If no blocks found, use entire content
                extracted_code = content
            
            # Clear editor and insert fix
            self.code_editor.clear()
            self.code_editor.setText(extracted_code)
            
            # Show preview in code view
            self.code_view.setText(extracted_code)
            self.tabs.setCurrentIndex(0)  # Switch to Code View tab
            
            self.status_bar.showMessage(f"✓ Loaded fix: {fix.get('filename', '')}")
            QMessageBox.information(
                self, "Fix Loaded",
                f"Fix loaded to editor:\n{fix.get('filename', '')}\n\n"
                f"Review in editor, then click 'Insert to MAIN_FILE' to apply."
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load fix: {e}")
            print(f"[ERROR] load_fix_to_editor: {e}")
    
    def show_full_file_viewer(self):
        """Open a window showing the complete file with fix applied."""
        try:
            # Create a new window
            file_viewer = QDialog(self)
            file_viewer.setWindowTitle("📂 Full File Viewer - MAIN_FILE.py")
            file_viewer.setGeometry(100, 100, 1200, 800)
            
            layout = QVBoxLayout(file_viewer)
            
            # Add label
            label = QLabel("Complete MAIN_FILE.py with proposed changes:")
            label.setStyleSheet("color: #00ff00; font-weight: bold;")
            layout.addWidget(label)
            
            # Create text viewer
            file_view = QTextEdit()
            file_view.setReadOnly(True)
            file_view.setStyleSheet("""
                QTextEdit {
                    background-color: #1e1e1e;
                    color: #e0e0e0;
                    border: 1px solid #444444;
                    font-family: 'Courier New';
                    font-size: 10px;
                }
            """)
            font = QFont('Courier New', 10)
            file_view.setFont(font)
            
            # Add syntax highlighting
            highlighter = PythonHighlighter(file_view.document())
            
            # Load current MAIN_FILE.py
            try:
                with open("MAIN_FILE.py", 'r', encoding='utf-8') as f:
                    main_content = f.read()
                
                # Show the file
                file_view.setText(main_content)
            except Exception as e:
                file_view.setText(f"Error loading MAIN_FILE.py: {e}")
            
            layout.addWidget(file_view)
            
            # Add buttons
            button_layout = QHBoxLayout()
            
            copy_btn = QPushButton("📋 Copy All")
            copy_btn.clicked.connect(lambda: self.copy_widget_content(file_view))
            button_layout.addWidget(copy_btn)
            
            close_btn = QPushButton("✓ Close")
            close_btn.clicked.connect(file_viewer.close)
            button_layout.addWidget(close_btn)
            
            button_layout.addStretch()
            layout.addLayout(button_layout)
            
            file_viewer.exec_()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open file viewer: {e}")
            print(f"[ERROR] show_full_file_viewer: {e}")
    
    def copy_widget_content(self, widget):
        """Copy text widget content to clipboard."""
        try:
            text = widget.toPlainText()
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            QMessageBox.information(self, "Copied", f"Copied {len(text)} characters to clipboard")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to copy: {e}")
    
    def refresh_and_rescan(self):
        """Rescan MAIN_FILE.py to update issues after applying fix."""
        try:
            self.status_bar.showMessage("Rescanning MAIN_FILE.py...")
            
            # Re-search for the current search term
            search_term = self.search_input.text().strip()
            if search_term:
                self.on_search()
                QMessageBox.information(
                    self, "Rescan Complete",
                    f"Code rescanned!\n\n"
                    f"Search term: '{search_term}'\n"
                    f"Check the results to see if issues are resolved."
                )
            else:
                QMessageBox.information(self, "Rescan Complete", "Please enter a search term to rescan")
            
            self.status_bar.showMessage("✓ Rescan complete")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Rescan failed: {e}")
            print(f"[ERROR] refresh_and_rescan: {e}")
    
    def apply_dark_theme(self):
        """Apply dark theme to entire app."""
        self.setStyleSheet("""
            QMainWindow { background-color: #1e1e1e; }
            QLabel { color: #e0e0e0; }
            QCheckBox { color: #e0e0e0; }
            QComboBox { background-color: #2d2d2d; color: #e0e0e0; }
        """)
    
    def get_button_style(self, bg_color, text_color):
        """Generate button stylesheet."""
        return f"""
            QPushButton {{
                background-color: {bg_color};
                color: {text_color};
                border: 1px solid {text_color};
                padding: 6px 12px;
                border-radius: 3px;
                font-weight: bold;
            }}
            QPushButton:hover {{ background-color: {text_color}; color: {bg_color}; }}
            QPushButton:pressed {{ opacity: 0.7; }}
        """


def main():
    """Launch the CODE FIXER application."""
    app = None
    try:
        from PyQt5.QtWidgets import QApplication
        
        # Check if QApplication already exists
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        # Get directory
        import os
        if len(sys.argv) > 1:
            search_dir = sys.argv[1]
        else:
            search_dir = os.getcwd()
        
        fixer = CodeFixer(search_directory=search_dir)
        fixer.show()
        
        sys.exit(app.exec_())
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
