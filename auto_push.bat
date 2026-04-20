@echo off
cd /d "C:\Users\harshad Dhuppe\PYTHON LEARNING"

echo ==============================
echo Uploading to GitHub...
echo ==============================

git add .

git diff --cached --quiet
if %errorlevel%==0 (
    echo No changes to commit.
    pause
    exit /b
)

set msg=Auto-update on %date% at %time%
git commit -m "%msg%"

git push origin main

echo ==============================
echo Upload Complete!
echo ==============================
pause