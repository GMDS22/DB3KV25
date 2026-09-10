import sys
import unittest
from pathlib import Path

import numpy as np
from PyQt5.QtWidgets import QApplication

sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.sentry_v2.face_queue_panel import _bgr_crop_to_pixmap


class FaceQueuePanelThumbnailTest(unittest.TestCase):
    def test_bgr_crop_to_pixmap_renders_valid_image(self):
        app = QApplication.instance() or QApplication([])
        crop = np.zeros((80, 90, 3), dtype=np.uint8)
        crop[10:70, 10:80] = (30, 60, 120)
        pixmap = _bgr_crop_to_pixmap(crop, size=64)
        self.assertFalse(pixmap.isNull())
        self.assertGreater(pixmap.width(), 0)
        self.assertGreater(pixmap.height(), 0)


if __name__ == "__main__":
    unittest.main()
