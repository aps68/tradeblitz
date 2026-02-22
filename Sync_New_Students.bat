@echo off
color 0A
echo ==========================================================
echo Syncing your new students to the live TradeBlitz website...
echo ==========================================================
echo.

git add approved_emails.js
git commit -m "Added new student emails to the system"
git push

echo.
echo ==========================================================
echo SUCCESS! The live website is updating right now.
echo It usually takes 1-2 minutes for the changes to appear.
echo ==========================================================
pause
