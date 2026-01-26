from __future__ import annotations

import sys
from PyQt5.QtWidgets import QApplication

from .ui import AutoTrackLabWindow


def main() -> int:
    app = QApplication(sys.argv)
    window = AutoTrackLabWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    raise SystemExit(main())
