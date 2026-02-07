
from PyQt5.QtWidgets import QApplication, QSpinBox
from PyQt5.QtCore import Qt

app = QApplication([])

# Default QSpinBox
spin = QSpinBox()
print(f"Default max: {spin.maximum()}")

# Simulate app logic
TILT_MIN = 40
TILT_MAX = 120
spin.setRange(TILT_MIN, TILT_MAX)
print(f"After setRange({TILT_MIN}, {TILT_MAX}): max={spin.maximum()}")

# Try to set value > 99 without setRange
spin2 = QSpinBox()
spin2.setValue(120)
print(f"Value set to 120 without range update: {spin2.value()} (Max: {spin2.maximum()})")

# Simulate what might happen if TILT_MAX is 70
TILT_MAX_BROKEN = 70
spin3 = QSpinBox()
spin3.setRange(40, TILT_MAX_BROKEN)
print(f"With TILT_MAX=70: max={spin3.maximum()}")
