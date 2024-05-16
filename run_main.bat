@echo off

:: Isolate the python environment
py -m pip install --upgrade pip
py -m pip install virtualenv

:: Create the virtual environment
py -m virtualenv venv

:: Activate the virtual environment
call venv\Scripts\activate

:: Install the required packages
py -m pip install -r requirements.txt