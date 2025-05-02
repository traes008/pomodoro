#!/bin/bash

# Create and activate a virtual environment
echo "Creating virtual environment..."
python3 -m venv build_env

# Activate virtual environment (Unix/Linux)
source build_env/bin/activate

# Install required packages
echo "Installing required packages..."
pip install pyinstaller

# Create assets directory if it doesn't exist
mkdir -p assets

# Build the executable with PyInstaller
echo "Building executable..."
pyinstaller --onefile \
            --noconsole \
            --name pomodoro \
            --add-data "assets:assets" \
            --clean \
            --hidden-import tkinter \
            main.py

# Deactivate virtual environment
deactivate

echo "Build complete! Executable is in the dist directory"