import re

with open('run.py', 'r') as f:
    code = f.read()

patch = '''
        _show_launcher()
        
        # --- TEST HOOK ---
        print("\\n--- AUTOMATED TEST ---")
        from PyQt5.QtCore import QTimer
        def click_sentry():
            print("Clicking sentry open")
            _open_mode("sentry")
        
        def click_close():
            w = active_window.get("window")
            if w:
                print("Clicking window close")
                w.close()
                
        def end_test():
            print("End test, top level widgets:")
            print([(w.__class__.__name__, w.objectName()) for w in app.topLevelWidgets() if w.isVisible()])
            _request_app_quit()
            
        QTimer.singleShot(1000, click_sentry)
        QTimer.singleShot(2500, click_close)
        QTimer.singleShot(4000, end_test)
'''

code = code.replace("        _show_launcher()", patch)
with open('run.py', 'w') as f:
    f.write(code)
