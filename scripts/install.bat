@echo off
echo ========================================
echo    Zox AI Installation Script
echo    by MrLexCoder
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9 or higher from python.org
    pause
    exit /b 1
)

echo Python found!
python --version
echo.

REM Create virtual environment (optional but recommended)
echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo WARNING: Could not create virtual environment
    echo Continuing with global Python installation...
) else (
    echo Virtual environment created!
    call venv\Scripts\activate.bat
)

echo.
echo Installing Python dependencies...
echo This may take a few minutes...
echo.

pip install --upgrade pip
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install some dependencies
    echo Please check the error messages above
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation complete!
echo ========================================
echo.
echo Next steps:
echo 1. Install Ollama from https://ollama.com
echo 2. Run: ollama serve
echo 3. Run: ollama pull llama3.1:8b-instruct-q4_K_M
echo 4. Run: python test_components.py (to test)
echo 5. Run: python main.py (to start Zox AI)
echo.
echo Or simply run: run.bat
echo.
pause
