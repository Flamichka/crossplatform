@echo off
:: Sets up all dependencies for the project
set VIRTUAL_ENV_NAME=.venv
set CUSTOM_PACKAGES=PyQt5 requests

if "%os%"=="Windows_NT" (
    set VENV_BIN=%VIRTUAL_ENV_NAME%\Scripts
) else (
    set VENV_BIN=%VIRTUAL_ENV_NAME%/bin
)

:: Check if Python is installed
where python >nul 2>nul || (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

:: Upgrade pip
python -m pip install --upgrade pip || (
    echo Failed to upgrade pip. Please ensure you have a working internet connection and try again.
    exit /b 1
)

:: Check if pip is installed
where pip >nul 2>nul || (
    echo pip is not installed. Please install pip and try again.
    exit /b 1
)

:: Create virtual environment if it doesn't exist
if not exist %VIRTUAL_ENV_NAME% (
    python -m venv %VIRTUAL_ENV_NAME%
) || (
    echo Failed to create virtual environment. Please check your Python installation and try again.
    exit /b 1
)

:: Activate the virtual environment
call %VENV_BIN%\activate || (
    echo Failed to activate the virtual environment. Please check your Python installation and try again.
    exit /b 1
)

:: Install custom packages if specified
if not "%CUSTOM_PACKAGES%"=="" (
    pip install %CUSTOM_PACKAGES% || (
        echo Failed to install custom packages. Please check the package names and try again.
        exit /b 1
    )
)

echo Setup completed. Your virtual environment is activated, and dependencies are installed.
