@echo off

:: Build the executable
echo Building executable...
call build.bat

:: Create release directory if it doesn't exist
if not exist "..\release" mkdir "..\release"

:: Create zip file with executable and assets
echo Creating release package...
powershell Compress-Archive -Path "..\dist\pomodoro.exe", "..\src\pomodoro\assets" -DestinationPath "..\release\pomodoro-windows.zip" -Force

echo Release package created in release\pomodoro-windows.zip
pause 