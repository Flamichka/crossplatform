@echo off
if "%VIRTUAL_ENV%"=="" (
    echo Virtual environment is not activated. Please activate a virtual environment first.
    exit /b 1
)

set CUSTOM_PACKAGES=certifi==2023.7.22 charset-normalizer==3.2.0 idna==3.4 pip==23.2.1 PyQt5==5.15.9 PyQt5-Qt5==5.15.2 PyQt5-sip==12.12.2 requests==2.31.0 setuptools==65.5.0 urllib3==2.0.4

python.exe -m pip install --upgrade pip

if not "%CUSTOM_PACKAGES%"=="" (
    pip install %CUSTOM_PACKAGES%
)

echo Setup completed.
