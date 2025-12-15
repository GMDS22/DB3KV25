@echo off
title DADBOT v4 Portable - AI Tracking Turret
echo ============================================================
echo    DADBOT v4 Portable - AI Tracking Turret
echo ============================================================
echo.

REM Try to find Python in common locations
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Found Python in PATH
    python "%~dp0run.py"
    goto end
)

REM Try Python 3 specifically
where python3 >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Found Python3 in PATH
    python3 "%~dp0run.py"
    goto end
)

REM Try common Python installation paths
if exist "C:\Python311\python.exe" (
    echo Found Python at C:\Python311
    "C:\Python311\python.exe" "%~dp0run.py"
    goto end
)

if exist "C:\Python310\python.exe" (
    echo Found Python at C:\Python310
    "C:\Python310\python.exe" "%~dp0run.py"
    goto end
)

if exist "C:\Python39\python.exe" (
    echo Found Python at C:\Python39
    "C:\Python39\python.exe" "%~dp0run.py"
    goto end
)

if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" (
    echo Found Python in AppData
    "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" "%~dp0run.py"
    goto end
)

if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" (
    echo Found Python in AppData
    "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" "%~dp0run.py"
    goto end
)

echo ============================================================
echo    ERROR: Python not found!
echo ============================================================
echo.
echo Please install Python 3.8 or later from:
echo    https://www.python.org/downloads/
echo.
echo Make sure to check "Add Python to PATH" during installation.
echo.

:end
echo.
pause
