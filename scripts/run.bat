@echo off
echo ========================================
echo    Zox AI - AI Desktop Assistant
echo    by MrLexCoder
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9 or higher
    pause
    exit /b 1
)

REM Check if Ollama is running
echo Checking Ollama connection...
curl -s http://localhost:11434/api/tags >nul 2>&1
if errorlevel 1 (
    echo WARNING: Cannot connect to Ollama
    echo Please make sure Ollama is running: ollama serve
    echo And the model is installed: ollama pull llama3.1:8b-instruct-q4_K_M
    echo.
    echo Press any key to continue anyway, or Ctrl+C to exit
    pause
)

REM Run Zox AI
echo.
echo Starting Zox AI...
echo.
python main.py

pause
