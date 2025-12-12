@echo off
cd /d "C:\Users\harshad Dhuppe\PYTHON LEARNING"

git add .
git commit -m "Auto-update: %date% %time%" --allow-empty
git push origin main
