@echo off && cls && color 4e
pip3 install -r requirements.txt > nul
echo -- All dependencies are as follows, 
echo -- press any key to download again
echo -------------------------------------------------------
pip3 freeze > requirements.txt
type requirements.txt

echo -------------------------------------------------------
echo -- If you don't want to download again, 
echo -- you can close the window
pause>nul
