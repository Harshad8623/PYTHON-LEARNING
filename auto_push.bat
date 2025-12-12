@echo off
cd /d "C:\Users\harshad Dhuppe\PYTHON LEARNING"

REM === AUTO-CREATE NEXT DAY FOLDER ===
for /f "tokens=1-3 delims=/" %%a in ("%date%") do set today=%%a-%%b-%%c
if not exist "%today%" mkdir "%today%"

REM === AUTO STAGE CHANGES ===
git add .

REM === AUTO COMMIT ===
git commit -m "Daily commit %date% %time%" --allow-empty

REM === TRY PUSH ===
git push origin main
if %errorlevel%==0 (
    set msg=Push Success on %date% %time%
) else (
    set msg=Push FAILED (No internet?) %date% %time%
)

REM === SEND TELEGRAM MESSAGE ===
curl -s -X POST "https://api.telegram.org/bot8484287356:AAG5lFgHKnUPJHtwsfqfuIQU5P9RBC7aopM/sendMessage" -d chat_id=987654321 -d text="%msg%"
