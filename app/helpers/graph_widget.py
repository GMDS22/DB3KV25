from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QPalette, QPainterPath
from PyQt5.QtCore import Qt, QSize

class HealthGraphWidget(QWidget):
    """
    A simple scrolling line graph to display numerical health data (e.g. current in mA).
    """
    def __init__(
        self,
        parent=None,
        max_points=100,
        min_val=0,
        max_val=2000,
        *,
        unit="mA",
        show_value_text=True,
        value_label="Current",
        max_label="Max",
        danger_threshold=None,
        danger_fill_max_alpha=140,
        expand_max=True,
    ):
        super().__init__(parent)
        self.data_points = []
        self.max_points = max_points
        self.min_val = min_val
        self.max_val = max_val
        self.unit = unit
        self.show_value_text = bool(show_value_text)
        self.value_label = str(value_label) if value_label is not None else ""
        self.max_label = str(max_label) if max_label is not None else ""
        self.danger_threshold = danger_threshold
        self.danger_fill_max_alpha = int(danger_fill_max_alpha)
        self.expand_max = bool(expand_max)
        self.setBackgroundRole(QPalette.NoRole)
        self.setMinimumHeight(100)
        self.setStyleSheet("background-color: #222; border: 1px solid #444;")

    @staticmethod
    def _clamp01(x):
        try:
            xf = float(x)
        except Exception:
            return 0.0
        if xf < 0.0:
            return 0.0
        if xf > 1.0:
            return 1.0
        return xf

    def push_data(self, value):
        if value is None:
            value = 0
        self.data_points.append(value)
        if len(self.data_points) > self.max_points:
            self.data_points.pop(0)
        self.update()  # Trigger repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw Background
        rect = self.rect()
        painter.fillRect(rect, QColor("#1e1e1e"))
        
        # Draw Grid Lines
        painter.setPen(QPen(QColor("#333333"), 1, Qt.DotLine))
        steps = 4
        for i in range(1, steps):
            y = rect.height() * i / steps
            painter.drawLine(0, int(y), rect.width(), int(y))

        if not self.data_points:
            return

        # Scale data
        width = rect.width()
        height = rect.height()
        
        step_x = width / (self.max_points - 1) if self.max_points > 1 else width
        
        # Calculate Y scale.
        # Default behavior: fixed range from init, but optionally expand if data exceeds.
        data_max = max(self.data_points)
        current_max = max(float(data_max), float(self.max_val)) if self.expand_max else float(self.max_val)
        current_min = float(self.min_val)
        
        val_range = current_max - current_min
        if val_range == 0:
            val_range = 1

        points = []
        for i, val in enumerate(self.data_points):
            x = i * step_x
            # Invert Y (0 is top)
            try:
                frac = (float(val) - current_min) / float(val_range)
            except Exception:
                frac = 0.0
            frac = self._clamp01(frac)
            y = height - (frac * height)
            points.append((x, y))

        # Optional translucent red fill that ramps up as we approach danger_threshold.
        # Fills the area under the line (down to the bottom of the graph).
        # Intended for Total Current (mA) where 5000mA == 5A.
        try:
            thr = self.danger_threshold
            if thr is not None:
                thr = float(thr)
            if thr is not None and thr > 0 and points:
                latest_val = float(self.data_points[-1]) if self.data_points else 0.0
                frac = self._clamp01(latest_val / thr)

                max_alpha = int(max(0, min(255, int(self.danger_fill_max_alpha))))
                alpha = int(max(0, min(255, round(max_alpha * frac))))

                if alpha > 0:
                    # Fill polygon under the curve down to the bottom of the graph.
                    painter.save()
                    painter.setPen(Qt.NoPen)
                    painter.setBrush(QBrush(QColor(255, 0, 0, alpha)))
                    fill_path = QPainterPath()
                    fill_path.moveTo(points[0][0], height)
                    fill_path.lineTo(points[0][0], points[0][1])
                    for x, y in points[1:]:
                        fill_path.lineTo(x, y)
                    fill_path.lineTo(points[-1][0], height)
                    fill_path.closeSubpath()

                    painter.drawPath(fill_path)
                    painter.restore()
        except Exception:
            pass

        # Draw Path (optionally ramps from green -> red as danger_threshold is approached)
        line_color = QColor("#00ff00")
        try:
            thr = self.danger_threshold
            if thr is not None:
                thr = float(thr)
            if thr is not None and thr > 0:
                latest_val = float(self.data_points[-1]) if self.data_points else 0.0
                frac = self._clamp01(latest_val / thr)
                # Interpolate green -> red
                r = int(round(255 * frac))
                g = int(round(255 * (1.0 - frac)))
                line_color = QColor(r, g, 0)
        except Exception:
            pass

        painter.setPen(QPen(line_color, 2))
        
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i+1]
            painter.drawLine(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
            
        # Draw value overlay text (optional)
        if self.show_value_text:
            latest = self.data_points[-1]
            painter.setPen(QColor("#ffffff"))

            unit = "" if self.unit is None else str(self.unit).strip()
            suffix = f" {unit}" if unit else ""

            # For current-style metrics, integer display is usually clearer.
            if unit.lower() == "ma":
                latest_text = str(int(latest))
                max_text = str(int(data_max))
            else:
                try:
                    latest_text = f"{float(latest):.1f}"
                    max_text = f"{float(data_max):.1f}"
                except Exception:
                    latest_text = str(latest)
                    max_text = str(data_max)

            vlabel = self.value_label.strip() if isinstance(self.value_label, str) else ""
            mlabel = self.max_label.strip() if isinstance(self.max_label, str) else ""
            if not vlabel:
                vlabel = "Value"
            if not mlabel:
                mlabel = "Max"

            painter.drawText(5, 15, f"{vlabel}: {latest_text}{suffix}")
            painter.drawText(5, 30, f"{mlabel}: {max_text}{suffix}")

    def sizeHint(self):
        return QSize(200, 100)
