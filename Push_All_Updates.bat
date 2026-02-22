@echo off
color 0B
echo ==========================================================
echo PUSHING ALL WEBSITE UPDATES TO LIVE SERVER...
echo ==========================================================
echo.

git add .
git commit -m "Updated TradeBlitz website files"
git push

echo.
echo ==========================================================
echo SUCCESS! Your live website has been updated!
echo Changes usually take 1-2 minutes to appear on GitHub.
echo ==========================================================
pause
