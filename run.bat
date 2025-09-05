@echo off
REM Server Test Engineer Toolkit - Windows Launcher
REM This is for testing on Windows before copying to Linux

echo Server Test Engineer Toolkit - Windows Launcher
echo =============================================

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is required but not installed.
    echo Please install Python and try again.
    pause
    exit /b 1
)

echo Starting Server Test Engineer Toolkit...
python server_test_toolkit.py %*

pause
