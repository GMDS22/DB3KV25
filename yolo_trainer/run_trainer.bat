@echo off
REM YOLO Trainer Launcher
REM This batch file launches the YOLO trainer application

echo Starting YOLO Trainer...
echo.

REM Set environment variables for Torch stability on Windows
set KMP_DUPLICATE_LIB_OK=TRUE
set OMP_NUM_THREADS=1

REM Change to the script directory
cd /d "%~dp0"

REM Launch the trainer
python yolo_trainer_window.py

pause