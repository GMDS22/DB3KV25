from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QApplication, QCheckBox


def get_dark_palette():
    """Creates and returns a dark theme palette for a Qt application."""
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.Base, QColor(42, 42, 42))
    dark_palette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
    # Tooltip colors - light yellow background with black text for readability
    dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 250, 205))  # Light yellow
    dark_palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))  # Black text
    dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    dark_palette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
    dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
    return dark_palette


class ThemeManager:
    def __init__(self):
        self.light_palette = QApplication.palette()
        self.dark_palette = get_dark_palette()

    def apply_theme(self, theme_name="dark"):
        """
        Applies a theme to the current QApplication instance.

        Args:
            theme_name (str): The name of the theme to apply ("dark" or "light").
        """
        if theme_name.lower() == "dark":
            QApplication.setPalette(self.dark_palette)
        else:
            QApplication.setPalette(self.light_palette)

    def create_theme_toggle_checkbox(self):
        """Creates a QCheckBox to toggle between light and dark themes."""
        theme_toggle = QCheckBox("Dark Theme")
        theme_toggle.setChecked(True)
        theme_toggle.stateChanged.connect(
            lambda: self.apply_theme("dark" if theme_toggle.isChecked() else "light")
        )
        return theme_toggle
