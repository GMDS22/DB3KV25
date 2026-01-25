from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QPalette
from PyQt5.QtCore import Qt, QSize

class HealthGraphWidget(QWidget):
    """
    A simple scrolling line graph to display numerical health data (e.g. current in mA).
    """
    def __init__(self, parent=None, max_points=100, min_val=0, max_val=2000):
        super().__init__(parent)
        self.data_points = []
        self.max_points = max_points
        self.min_val = min_val
        self.max_val = max_val
        self.setBackgroundRole(QPalette.NoRole)
        self.setMinimumHeight(100)
        self.setStyleSheet("background-color: #222; border: 1px solid #444;")

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
        
        # Calculate Y scale
        # Dynamic scaling or fixed? 
        # For health monitor, fixed range is often better to see spikes, 
        # but dynamic is good if we don't know the range.
        # Let's use fixed range from init, but expand if data exceeds.
        current_max = max(max(self.data_points), self.max_val)
        current_min = 0 # Current shouldn't be negative
        
        val_range = current_max - current_min
        if val_range == 0:
            val_range = 1

        points = []
        for i, val in enumerate(self.data_points):
            x = i * step_x
            # Invert Y (0 is top)
            y = height - ((val - current_min) / val_range * height)
            points.append((x, y))

        # Draw Path
        painter.setPen(QPen(QColor("#00ff00"), 2))
        
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i+1]
            painter.drawLine(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
            
        # Draw current value text
        latest = self.data_points[-1]
        painter.setPen(QColor("#ffffff"))
        painter.drawText(5, 15, f"Current: {int(latest)} mA")
        painter.drawText(5, 30, f"Max: {int(current_max)} mA")

    def sizeHint(self):
        return QSize(200, 100)
