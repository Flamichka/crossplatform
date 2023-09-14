@echo off
if "%VIRTUAL_ENV%"=="" (
    echo Virtual environment is not activated. Please activate a virtual environment first.
    exit /b 1
)

set CUSTOM_PACKAGES=PyQt5 requests 

python.exe -m pip install --upgrade pip

if not "%CUSTOM_PACKAGES%"=="" (
    pip install %CUSTOM_PACKAGES%
)

echo Setup completed.
