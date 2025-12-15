import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QToolBar, QAction, QFontComboBox, QSpinBox, QFileDialog
from PyQt5.QtGui import QKeySequence, QFont, QTextCursor


class NotepadWidget(QWidget):
    """Enhanced notepad widget with markdown support and formatting options.

    - Defaults to <project>/Notepad.md
    - Exposes save_file() so callers can persist content before shutdown.
    - Includes formatting toolbar (bold, italic, code, headers, etc.)
    """

    def __init__(self, parent=None, path=None):
        super().__init__(parent)
        self._file_path = (
            path
            if path is not None
            else os.path.join(os.path.dirname(__file__), "Notepad.md")
        )
        self._dirty = False
        self._init_ui()
        self.load_file()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(2)

        # === Main toolbar with Save / Reload / Open ===
        tb_main = QToolBar("File")
        
        open_act = QAction("Open", self)
        open_act.setShortcut(QKeySequence.Open)
        open_act.triggered.connect(self.open_file)
        tb_main.addAction(open_act)
        
        save_act = QAction("Save", self)
        save_act.setShortcut(QKeySequence.Save)
        save_act.triggered.connect(self.save_file)
        tb_main.addAction(save_act)

        reload_act = QAction("Reload", self)
        reload_act.triggered.connect(self.load_file)
        tb_main.addAction(reload_act)

        layout.addWidget(tb_main)

        # === Formatting toolbar ===
        tb_fmt = QToolBar("Formatting")
        
        # Bold
        bold_act = QAction("Bold (Ctrl+B)", self)
        bold_act.setShortcut("Ctrl+B")
        bold_act.triggered.connect(lambda: self._insert_markdown("**", "**", "bold text"))
        tb_fmt.addAction(bold_act)
        
        # Italic
        italic_act = QAction("Italic (Ctrl+I)", self)
        italic_act.setShortcut("Ctrl+I")
        italic_act.triggered.connect(lambda: self._insert_markdown("*", "*", "italic text"))
        tb_fmt.addAction(italic_act)
        
        # Code
        code_act = QAction("Code", self)
        code_act.triggered.connect(lambda: self._insert_markdown("`", "`", "code"))
        tb_fmt.addAction(code_act)
        
        tb_fmt.addSeparator()
        
        # Header buttons
        h1_act = QAction("# H1", self)
        h1_act.triggered.connect(lambda: self._insert_line_prefix("# "))
        tb_fmt.addAction(h1_act)
        
        h2_act = QAction("## H2", self)
        h2_act.triggered.connect(lambda: self._insert_line_prefix("## "))
        tb_fmt.addAction(h2_act)
        
        h3_act = QAction("### H3", self)
        h3_act.triggered.connect(lambda: self._insert_line_prefix("### "))
        tb_fmt.addAction(h3_act)
        
        tb_fmt.addSeparator()
        
        # Bullet list
        bullet_act = QAction("• Bullet", self)
        bullet_act.triggered.connect(lambda: self._insert_line_prefix("- "))
        tb_fmt.addAction(bullet_act)
        
        # Numbered list
        num_act = QAction("1. Numbered", self)
        num_act.triggered.connect(lambda: self._insert_line_prefix("1. "))
        tb_fmt.addAction(num_act)
        
        # Code block
        block_act = QAction("Code Block", self)
        block_act.triggered.connect(lambda: self._insert_markdown("```\n", "\n```", "code here"))
        tb_fmt.addAction(block_act)
        
        # Separator and quote
        tb_fmt.addSeparator()
        quote_act = QAction("> Quote", self)
        quote_act.triggered.connect(lambda: self._insert_line_prefix("> "))
        tb_fmt.addAction(quote_act)
        
        layout.addWidget(tb_fmt)

        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self._on_text_changed)
        self.text_edit.setStyleSheet("""
            QTextEdit {
                font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
                font-size: 10pt;
                background-color: #1e1e1e;
                color: #e0e0e0;
                border: 1px solid #333333;
            }
        """)
        layout.addWidget(self.text_edit)

    def _on_text_changed(self):
        self._dirty = True

    def _insert_markdown(self, prefix, suffix, placeholder):
        """Insert markdown wrapper around selected text or placeholder."""
        cursor = self.text_edit.textCursor()
        if cursor.hasSelection():
            text = cursor.selectedText()
            cursor.removeSelectedText()
            cursor.insertText(f"{prefix}{text}{suffix}")
        else:
            cursor.insertText(f"{prefix}{placeholder}{suffix}")
            # Move cursor back into the placeholder area
            cursor.movePosition(QTextCursor.Left, QTextCursor.MoveAnchor, len(suffix))
            self.text_edit.setTextCursor(cursor)

    def _insert_line_prefix(self, prefix):
        """Insert prefix at the beginning of the current line."""
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QTextCursor.StartOfLine)
        cursor.insertText(prefix)
        self.text_edit.setTextCursor(cursor)

    def _on_text_changed(self):
        self._dirty = True

    def load_file(self):
        try:
            if os.path.exists(self._file_path):
                with open(self._file_path, "r", encoding="utf-8") as f:
                    txt = f.read()
            else:
                txt = ""
            # setPlainText to preserve raw markdown
            self.text_edit.blockSignals(True)
            self.text_edit.setPlainText(txt)
            self.text_edit.blockSignals(False)
            self._dirty = False
        except Exception as e:
            # keep UI friendly: show error text
            self.text_edit.setPlainText(f"Error loading {self._file_path}: {e}")
            self._dirty = False

    def save_file(self):
        try:
            content = self.text_edit.toPlainText()
            with open(self._file_path, "w", encoding="utf-8") as f:
                f.write(content)
            self._dirty = False
        except Exception as e:
            # Best-effort log to console; avoid crashing the UI
            try:
                print(f"Failed to save Notepad file {self._file_path}: {e}")
            except Exception:
                pass

    def open_file(self):
        """Open a file dialog to choose and load a markdown file."""
        try:
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Open Note File",
                os.path.dirname(self._file_path),
                "Markdown Files (*.md);;Text Files (*.txt);;All Files (*)"
            )
            if file_path:
                self._file_path = file_path
                self.load_file()
        except Exception as e:
            try:
                print(f"Error opening file: {e}")
            except Exception:
                pass

    def is_dirty(self):
        return self._dirty
