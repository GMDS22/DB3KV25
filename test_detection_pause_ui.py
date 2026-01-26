"""
Quick test to verify Detection Pause slider exists in UI
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "app"))

from PyQt5.QtWidgets import QApplication
from MAIN_FILE_SINGLE_CAM import TrackingApp

print("Creating app...")
app_qt = QApplication(sys.argv)
print("Creating TrackingApp...")
tracker = TrackingApp()

print("\nChecking for detection_pause_slider:")
if hasattr(tracker, "detection_pause_slider"):
    slider = tracker.detection_pause_slider
    print(f"[OK] detection_pause_slider EXISTS")
    print(f"   Type: {type(slider)}")
    print(f"   Range: {slider.minimum()} - {slider.maximum()}")
    print(f"   Value: {slider.value()}")
    print(f"   Visible: {slider.isVisible()}")
    print(f"   Enabled: {slider.isEnabled()}")
    
    # Check parent
    parent = slider.parent()
    print(f"   Parent: {parent}")
    
    # Check if it's in a layout
    if parent and hasattr(parent, "layout"):
        layout = parent.layout()
        print(f"   In layout: {layout is not None}")
else:
    print(f"[FAIL] detection_pause_slider DOES NOT EXIST")

print("\nChecking for detection_pause_label:")
if hasattr(tracker, "detection_pause_label"):
    label = tracker.detection_pause_label
    print(f"[OK] detection_pause_label EXISTS")
    print(f"   Text: '{label.text()}'")
    print(f"   Visible: {label.isVisible()}")
else:
    print(f"[FAIL] detection_pause_label DOES NOT EXIST")

print("\nChecking behavior_group:")
if hasattr(tracker, "behavior_group"):
    bg = tracker.behavior_group
    print(f"[OK] behavior_group EXISTS")
    print(f"   Type: {type(bg)}")
    print(f"   Title: '{bg.title()}'")
    layout = bg.layout()
    if layout:
        print(f"   Layout type: {type(layout)}")
        print(f"   Layout count: {layout.count()}")
        
        # List all widgets in layout
        print("\n   Widgets in behavior_group layout:")
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    if hasattr(widget, "text"):
                        print(f"      [{i}] {type(widget).__name__}: '{widget.text()}'")
                    else:
                        print(f"      [{i}] {type(widget).__name__}")
                layout_item = item.layout()
                if layout_item:
                    print(f"      [{i}] Layout with {layout_item.count()} items")
else:
    print(f"❌ behavior_group DOES NOT EXIST")

print("\nDone. Exiting...")
sys.exit(0)
