"""
layout_manager.py
Extracted LayoutManagerMixin from Movement_Detect_Yolo_me.py
"""

import os
import json

from PyQt5.QtCore import QByteArray
from PyQt5.QtWidgets import (
    QApplication,
    QMessageBox,
    QLabel,
    QMenu,
    QAction,
)


class LayoutManagerMixin:
    def init_layout_menu(self):
        """Create the Layout menu and actions and install a status widget showing current layout.

        New behavior:
        - Adds built-in presets: Minimal, Standard, Analysis
        - Provides five custom placeholders (custom1..custom5) with a submenu
          containing: Load, Save/Override, Clear
        - Shows a small status label in the status bar indicating current layout
        """
        menubar = self.menuBar()
        if menubar is not None:
            # Get or create the Layouts menu
            layout_menu = None
            for action in menubar.actions():
                if action.menu() is not None and action.menu().title() == "Layouts":
                    layout_menu = action.menu()
                    break
            
            if layout_menu is None:
                layout_menu = QMenu("Layouts", menubar)
                # Try to insert before Tools menu, otherwise add at the end
                tools_action = None
                for a in menubar.actions():
                    try:
                        if str(a.text()).strip().lower() == "tools":
                            tools_action = a
                            break
                    except Exception:
                        continue
                
                try:
                    if tools_action is not None:
                        menubar.insertMenu(tools_action, layout_menu)
                    else:
                        menubar.addMenu(layout_menu)
                except Exception:
                    pass

        # Preset layout actions
        layout_menu.addAction("Minimal", lambda: self.load_layout("minimal"))
        layout_menu.addAction("Standard", lambda: self.load_layout("standard"))
        layout_menu.addAction("Analysis", lambda: self.load_layout("analysis"))
        layout_menu.addSeparator()

        # Custom user presets (placeholders) - provide 5 presets
        self._preset_names = [f"custom{i}" for i in range(1, 6)]
        # Keep mapping of submenu objects so we can refresh labels
        self._preset_submenus = {}
        try:
            for idx, pname in enumerate(self._preset_names, start=1):
                display = f"Preset {idx}"
                sub = QMenu(display, layout_menu)
                # Load action
                load_act = QAction("Load", sub)
                load_act.triggered.connect(lambda checked=False, n=pname: self.load_layout(n))
                sub.addAction(load_act)
                # Save/Override action
                save_act = QAction("Save / Override", sub)
                save_act.triggered.connect(lambda checked=False, n=pname: self.save_current_layout_as(n))
                sub.addAction(save_act)
                # Clear action
                clear_act = QAction("Clear (delete preset)", sub)
                clear_act.triggered.connect(lambda checked=False, n=pname: self.clear_layout(n))
                sub.addAction(clear_act)
                layout_menu.addMenu(sub)
                self._preset_submenus[pname] = sub
            layout_menu.addSeparator()
        except Exception:
            pass

        # Add a small persistent status label in the status bar to show the current layout name
        try:
            try:
                self._base_window_title = self.windowTitle()
            except Exception:
                self._base_window_title = ""
            self._current_layout_name = None
            self._layout_status_label = QLabel("Layout: (unsaved)")
            if hasattr(self, "statusBar") and callable(getattr(self, "statusBar")):
                try:
                    sb = self.statusBar()
                    if sb is not None:
                        sb.addPermanentWidget(self._layout_status_label)
                except Exception:
                    pass
        except Exception:
            # If QLabel/statusBar aren't available yet (headless/tests), ignore
            pass

        # refresh menu titles to indicate which presets are already saved
        try:
            self._refresh_layout_menu()
        except Exception:
            pass

    def _layout_file_path(self, name):
        """Ensure the layouts directory exists and return layout path."""
        base_dir = os.path.join(os.path.dirname(__file__), "layouts")
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        return os.path.join(base_dir, f"{name}.json")

    def save_current_layout_as(self, name):
        """Save current dock/geometry state as named layout."""
        try:
            data = {
                "geometry": self.saveGeometry().toBase64().data().decode(),
                "windowState": self.saveState().toBase64().data().decode(),
            }
            path = self._layout_file_path(name)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            if hasattr(self, "_safe_append_log"):
                self._safe_append_log(f"Layout '{name}' saved to {path}")
            try:
                # Update the visible current layout name
                if hasattr(self, "_set_current_layout"):
                    try:
                        self._set_current_layout(name)
                    except Exception:
                        pass
            except Exception:
                pass

            # Refresh the menu entries to reflect saved state
            try:
                self._refresh_layout_menu()
            except Exception:
                pass
        except Exception as e:
            if hasattr(self, "_safe_append_log"):
                self._safe_append_log(f"Failed to save layout '{name}': {e}")

    def clear_layout(self, name):
        """Delete the named preset file if present and refresh the menu."""
        try:
            path = self._layout_file_path(name)
            if os.path.exists(path):
                try:
                    os.remove(path)
                    if hasattr(self, "_safe_append_log"):
                        self._safe_append_log(f"Layout '{name}' cleared (file removed)")
                except Exception as e:
                    if hasattr(self, "_safe_append_log"):
                        self._safe_append_log(f"Failed to remove layout '{name}': {e}")
            else:
                if hasattr(self, "_safe_append_log"):
                    self._safe_append_log(f"Layout '{name}' not found; nothing to clear")
        except Exception:
            pass
        try:
            self._refresh_layout_menu()
        except Exception:
            pass

    def _refresh_layout_menu(self):
        """Update preset submenu titles to indicate saved/empty state."""
        try:
            for name, submenu in getattr(self, "_preset_submenus", {}).items():
                try:
                    path = self._layout_file_path(name)
                    saved = os.path.exists(path)
                    # submenu.title() can be replaced by setTitle
                    display = submenu.title().split("(")[0].strip()
                    if saved:
                        submenu.setTitle(f"{display} (saved)")
                    else:
                        submenu.setTitle(f"{display} (empty)")
                except Exception:
                    pass
        except Exception:
            pass

    def load_layout(self, name):
        """Load and apply a named layout if it exists."""
        try:
            path = self._layout_file_path(name)
            if not os.path.exists(path):
                # Inform the user and offer to save the current layout as this preset
                try:
                    if hasattr(self, "_safe_append_log"):
                        self._safe_append_log(f"Layout '{name}' not found at {path}")
                    # If we have a running QApplication, prompt the user interactively
                    try:
                        app = QApplication.instance()
                        if app is not None:
                            resp = QMessageBox.question(
                                self,
                                "Layout not found",
                                f"Layout '{name}' not found. Save current layout as '{name}'?",
                                QMessageBox.Yes | QMessageBox.No,
                            )
                            if resp == QMessageBox.Yes:
                                self.save_current_layout_as(name)
                    except Exception:
                        # If interactive dialog fails (headless/test), silently return
                        pass
                except Exception:
                    pass
                return

            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

            geom = QByteArray.fromBase64(data["geometry"].encode())
            state = QByteArray.fromBase64(data["windowState"].encode())

            # Apply the geometry and state
            try:
                self.restoreGeometry(geom)
                self.restoreState(state)
                # minor UI refresh
                try:
                    self.update()
                except Exception:
                    pass
                if hasattr(self, "_safe_append_log"):
                    self._safe_append_log(f"Layout '{name}' loaded successfully")
                try:
                    if hasattr(self, "_set_current_layout"):
                        try:
                            self._set_current_layout(name)
                        except Exception:
                            pass
                except Exception:
                    pass
            except Exception as e:
                if hasattr(self, "_safe_append_log"):
                    self._safe_append_log(f"Failed to apply layout '{name}': {e}")
        except Exception as e:
            if hasattr(self, "_safe_append_log"):
                self._safe_append_log(f"Failed to load layout '{name}': {e}")

    def auto_load_default_layout(self):
        """Load your preferred default layout at startup."""
        default_layout = "standard"  # change this as desired
        try:
            self.load_layout(default_layout)
        except Exception:
            pass

    def _set_current_layout(self, name: str):
        """Set the current layout name and update any visible UI indicators."""
        try:
            self._current_layout_name = name
            # update status label if present
            try:
                if hasattr(self, "_layout_status_label"):
                    self._layout_status_label.setText(f"Layout: {name}")
            except Exception:
                pass
            # update window title (append layout name)
            try:
                base = getattr(self, "_base_window_title", None)
                if base is None:
                    base = self.windowTitle()
                if base:
                    self.setWindowTitle(f"{base} — {name}")
            except Exception:
                pass
        except Exception:
            pass
