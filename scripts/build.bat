@echo off

:: Create and activate a virtual environment
echo Creating virtual environment...
python -m venv build_env

:: Activate virtual environment (Windows)
call build_env\Scripts\activate.bat

:: Install required packages
echo Installing required packages...
pip install pyinstaller

:: Create assets directory if it doesn't exist
if not exist "..\src\pomodoro\assets" mkdir "..\src\pomodoro\assets"

:: Build the executable with PyInstaller
echo Building executable...
pyinstaller --onefile ^
            --noconsole ^
            --name pomodoro ^
            --add-data "..\src\pomodoro\assets;assets" ^
            --clean ^
            --hidden-import tkinter ^
            ..\src\pomodoro\__main__.py

:: Deactivate virtual environment
deactivate

echo Build complete! Executable is in the dist directory
pause 