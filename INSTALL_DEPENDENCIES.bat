@echo off
title DADBOT v4 - Installing Dependencies
echo ============================================================
echo    DADBOT v4 Portable - Installing Dependencies
echo ============================================================
echo.

REM Find Python
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    python "%~dp0install_dependencies.py"
    goto end
)

where python3 >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    python3 "%~dp0install_dependencies.py"
    goto end
)

echo ERROR: Python not found!
echo Please install Python 3.8+ from https://python.org
echo Make sure to check "Add Python to PATH" during installation.

:end
echo.
pause
