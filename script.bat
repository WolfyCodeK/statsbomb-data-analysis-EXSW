@echo off
cd MCI
call venv\Scripts\activate
cd mancity

REM Use "start" to launch the server in a new command window
start "" /B python manage.py runserver
