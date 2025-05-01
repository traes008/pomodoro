@echo off

:: Create and activate a virtual environment
echo Creating virtual environment...
python -m venv build_env

:: Activate virtual environment (Windows)
call build_env\Scripts\activate.bat

:: Install required packages
echo Installing required packages...
pip install pyinstaller

:: Build the executable with PyInstaller
echo Building executable...
pyinstaller --onefile ^
            --noconsole ^
            --name pomodoro ^
            --add-data "assets;assets" ^
            --clean ^
            main.py

:: Deactivate virtual environment
deactivate

echo Build complete! Executable is in the dist directory
pause