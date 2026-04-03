@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "VENV_PYTHON=%SCRIPT_DIR%.venv\Scripts\python.exe"

if not exist "%VENV_PYTHON%" (
    echo Local virtual environment not found: "%VENV_PYTHON%"
    echo Recreate it with: py -3.12 -m venv .venv
    exit /b 1
)

pushd "%SCRIPT_DIR%"
"%VENV_PYTHON%" run.py
set "EXIT_CODE=%ERRORLEVEL%"
popd

exit /b %EXIT_CODE%