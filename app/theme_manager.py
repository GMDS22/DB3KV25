from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QApplication, QCheckBox


def get_dark_palette():
    """Creates and returns a dark theme palette for a Qt application."""
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(18, 14, 12))
    dark_palette.setColor(QPalette.WindowText, QColor(243, 236, 228))
    dark_palette.setColor(QPalette.Base, QColor(23, 18, 15))
    dark_palette.setColor(QPalette.AlternateBase, QColor(34, 26, 22))
    dark_palette.setColor(QPalette.ToolTipBase, QColor(253, 226, 176))
    dark_palette.setColor(QPalette.ToolTipText, QColor(34, 22, 16))
    dark_palette.setColor(QPalette.Text, QColor(237, 228, 218))
    dark_palette.setColor(QPalette.Button, QColor(45, 32, 26))
    dark_palette.setColor(QPalette.ButtonText, QColor(245, 238, 231))
    dark_palette.setColor(QPalette.BrightText, QColor(216, 109, 95))
    dark_palette.setColor(QPalette.Link, QColor(242, 166, 90))
    dark_palette.setColor(QPalette.Highlight, QColor(140, 63, 36))
    dark_palette.setColor(QPalette.HighlightedText, QColor(255, 245, 238))
    dark_palette.setColor(QPalette.Disabled, QPalette.Text, QColor(134, 118, 106))
    dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(134, 118, 106))
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
