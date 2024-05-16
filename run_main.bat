@echo off

:: Isolate the python environment
python -m pip install --upgrade pip
python -m pip install --user virtualenv

:: Create the virtual environment
python -m virtualenv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Install the required packages
python -m pip install -r requirements.txt