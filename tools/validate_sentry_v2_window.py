import os
import sys


os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")


def _preload_torch_runtime() -> None:
    try:
        import torch  # noqa: F401
    except Exception as exc:
        print(f"[BOOT] Torch preload failed: {exc}", flush=True)


_preload_torch_runtime()


def main() -> int:
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_dir = os.path.join(repo_root, "app")
    if app_dir not in sys.path:
        sys.path.insert(0, app_dir)
    os.chdir(repo_root)

    from PyQt5.QtCore import QTimer, QSize
    from PyQt5.QtWidgets import QApplication
    from run_sentry_v2 import SentryV2StandaloneWindow

    app = QApplication(sys.argv)
    window = SentryV2StandaloneWindow()
    window.show()

    def log(message: str) -> None:
        print(f"[V2-WINDOW] {message}", flush=True)

    def step1() -> None:
        sentry = getattr(window, "sentry_v2_tab", None)
        log(f"tab_exists={sentry is not None}")
        log(f"window_class={type(window).__name__}")
        if sentry is None:
            return
        app.processEvents()
        size = window.size()
        log(f"visible_after_show={window.isVisible()}")
        log(f"host_main_window_is_none={sentry._get_main_window() is None}")
        log(f"enabled_initial={sentry.is_enabled()}")
        log(f"size_initial={size.width()}x{size.height()}")
        QTimer.singleShot(400, step2)

    def step2() -> None:
        sentry = getattr(window, "sentry_v2_tab", None)
        if sentry is None:
            return
        sentry.set_enabled(True)
        app.processEvents()
        log(f"enabled_after_on={sentry.is_enabled()}")
        log(f"single_target_only={sentry.config.engagement.single_target_only}")
        log(f"max_queue_length={sentry.config.engagement.max_queue_length}")
        log(f"window_visible_after_on={window.isVisible()}")
        window.resize(QSize(1410, 910))
        app.processEvents()
        size = window.size()
        log(f"size_after_resize={size.width()}x{size.height()}")
        QTimer.singleShot(400, step3)

    def step3() -> None:
        sentry = getattr(window, "sentry_v2_tab", None)
        if sentry is None:
            return
        sentry.set_enabled(False)
        app.processEvents()
        log(f"visible_after_disable={window.isVisible()}")
        log(f"enabled_after_disable={sentry.is_enabled()}")
        QTimer.singleShot(400, step4)

    def step4() -> None:
        sentry = getattr(window, "sentry_v2_tab", None)
        if sentry is None:
            return
        sentry.set_enabled(True)
        app.processEvents()
        log(f"visible_after_reenable={window.isVisible()}")
        log(f"enabled_after_reenable={sentry.is_enabled()}")
        QTimer.singleShot(400, step5)

    def step5() -> None:
        sentry = getattr(window, "sentry_v2_tab", None)
        if sentry is None:
            return
        splitter = getattr(sentry, "_main_splitter", None)
        if splitter is not None:
            log(f"splitter_sizes={splitter.sizes()}")
        log(f"final_window_visible={window.isVisible()}")
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