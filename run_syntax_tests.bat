@echo off
cd /d "F:\SMART SENTRY_v2a\SMART SENTRY"

echo Running syntax checks...
echo.

echo [1/3] Checking face_identity.py...
python -c "import py_compile; py_compile.compile('app/sentry_v2/face_identity.py', doraise=True); print('face_identity OK')"
if %ERRORLEVEL% NEQ 0 (
    echo face_identity.py FAILED
    exit /b 1
)
echo.

echo [2/3] Checking face_queue_panel.py...
python -c "import py_compile; py_compile.compile('app/sentry_v2/face_queue_panel.py', doraise=True); print('face_queue_panel OK')"
if %ERRORLEVEL% NEQ 0 (
    echo face_queue_panel.py FAILED
    exit /b 1
)
echo.

echo [3/3] Checking sentry_v2_tab.py...
python -c "import py_compile; py_compile.compile('app/sentry_v2/sentry_v2_tab.py', doraise=True); print('sentry_v2_tab OK')"
if %ERRORLEVEL% NEQ 0 (
    echo sentry_v2_tab.py FAILED
    exit /b 1
)
echo.

echo All syntax checks passed!
