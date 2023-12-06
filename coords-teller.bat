@echo off

REM Set the path to your virtual environment
set VENV_PATH=C:\Users\rober\development\python\coords_teller\.venv

REM Activate the virtual environment
call "%VENV_PATH%\Scripts\activate.bat"

REM Run your Python script
python C:\Users\rober\development\python\coords_teller\src\main.py

REM Deactivate the virtual environment
call "%VENV_PATH%\Scripts\deactivate.bat"
