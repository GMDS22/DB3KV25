import os
import sys


os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")


def main() -> int:
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_dir = os.path.join(repo_root, "app")
    if app_dir not in sys.path:
        sys.path.insert(0, app_dir)
    os.chdir(app_dir)

    from PyQt5.QtCore import QTimer, QSize
    from PyQt5.QtWidgets import QApplication
    from MAIN_FILE_SINGLE_CAM import TrackingApp

    app = QApplication(sys.argv)
    window = TrackingApp()
    window.show()

    def log(message: str) -> None:
        print(f"[V2-WINDOW] {message}", flush=True)

    def step1() -> None:
        sentry = getattr(window, "sentry_v2_tab", None)
        v2_window = getattr(window, "_sentry_v2_window", None)
        action = getattr(window, "_sentry_v2_window_action", None)
        log(f"tab_exists={sentry is not None}")
        log(f"window_exists={v2_window is not None}")
        log(f"action_exists={action is not None}")
        if v2_window is None or sentry is None:
            return
        window._show_sentry_v2_window()
        app.processEvents()
        size = v2_window.size()
        log(f"visible_after_show={v2_window.isVisible()}")
        log(f"enabled_initial={sentry.is_enabled()}")
        log(f"size_initial={size.width()}x{size.height()}")
        QTimer.singleShot(400, step2)

    def step2() -> None:
        sentry = getattr(window, "sentry_v2_tab", None)
        v2_window = getattr(window, "_sentry_v2_window", None)
        action = getattr(window, "_sentry_v2_window_action", None)
        if v2_window is None or sentry is None:
            return
        sentry.set_enabled(True)
        app.processEvents()
        log(f"enabled_after_on={sentry.is_enabled()}")
        log(f"active_flag_after_on={getattr(window, 'sentry_v2_active', None)}")
        log(f"window_visible_after_on={v2_window.isVisible()}")
        log(f"menu_checked_after_on={action.isChecked() if action is not None else None}")
        v2_window.resize(QSize(1410, 910))
        app.processEvents()
        size = v2_window.size()
        log(f"size_after_resize={size.width()}x{size.height()}")
        QTimer.singleShot(400, step3)

    def step3() -> None:
        v2_window = getattr(window, "_sentry_v2_window", None)
        action = getattr(window, "_sentry_v2_window_action", None)
        sentry = getattr(window, "sentry_v2_tab", None)
        if v2_window is None or sentry is None:
            return
        window._toggle_sentry_v2_window(False)
        app.processEvents()
        log(f"visible_after_menu_close={v2_window.isVisible()}")
        log(f"enabled_after_menu_close={sentry.is_enabled()}")
        log(f"active_flag_after_menu_close={getattr(window, 'sentry_v2_active', None)}")
        log(f"menu_checked_after_menu_close={action.isChecked() if action is not None else None}")
        QTimer.singleShot(400, step4)

    def step4() -> None:
        v2_window = getattr(window, "_sentry_v2_window", None)
        action = getattr(window, "_sentry_v2_window_action", None)
        sentry = getattr(window, "sentry_v2_tab", None)
        if v2_window is None or sentry is None:
            return
        window._show_sentry_v2_window()
        app.processEvents()
        log(f"visible_after_reopen={v2_window.isVisible()}")
        sentry.set_enabled(True)
        app.processEvents()
        log(f"enabled_after_reopen_on={sentry.is_enabled()}")
        log(f"menu_checked_after_reopen_on={action.isChecked() if action is not None else None}")
        sentry.set_enabled(False)
        app.processEvents()
        log(f"enabled_after_off={sentry.is_enabled()}")
        log(f"active_flag_after_off={getattr(window, 'sentry_v2_active', None)}")
        QTimer.singleShot(400, step5)

    def step5() -> None:
        sentry = getattr(window, "sentry_v2_tab", None)
        v2_window = getattr(window, "_sentry_v2_window", None)
        if sentry is None or v2_window is None:
            return
        panel_width = getattr(sentry, "_slider_panel_width", None)
        splitter = getattr(sentry, "_main_splitter", None)
        if panel_width is not None:
            panel_width.setValue(510)
            app.processEvents()
            log(f"panel_width_value={panel_width.value()}")
        if splitter is not None:
            log(f"splitter_sizes={splitter.sizes()}")
        log(f"final_window_visible={v2_window.isVisible()}")
        QTimer.singleShot(400, shutdown)

    def shutdown() -> None:
        try:
            window.close()
        finally:
            app.quit()

    QTimer.singleShot(500, step1)
    QTimer.singleShot(8000, lambda: os._exit(0))
    exit_code = app.exec_()
    log(f"exit_code={exit_code}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())