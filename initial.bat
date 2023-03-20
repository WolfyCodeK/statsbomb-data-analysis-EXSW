@echo off
cd MCI
call venv\Scripts\activate
cd mancity

REM Install pip packages from reqs.txt
call pip install -r ..\reqs.txt

REM Use "start" to launch the server in a new command window
start "" /B python manage.py runserver
