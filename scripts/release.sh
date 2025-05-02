#!/bin/bash

# Build the executable
echo "Building executable..."
./build.sh

# Create release directory if it doesn't exist
mkdir -p ../release

# Create zip file with executable and assets
echo "Creating release package..."
zip -r ../release/pomodoro-linux.zip ../dist/pomodoro ../src/pomodoro/assets/

echo "Release package created in release/pomodoro-linux.zip" 