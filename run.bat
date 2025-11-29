@echo off
REM Pair Programming API Startup Script

echo.
echo ===================================
echo  Pair Programming - Backend Server
echo ===================================
echo.

REM Check if .env exists
if not exist "backend\.env" (
    echo Creating .env from .env.example...
    copy backend\.env.example backend\.env
    echo Please update backend\.env with your database credentials if needed.
    echo.
)

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://www.python.org/
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r backend/requirements.txt >nul 2>&1
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

REM Run the server
echo.
echo ===================================
echo  Starting FastAPI server...
echo ===================================
echo.
echo Server will be available at:
echo   http://localhost:8000/
echo.
echo API Documentation:
echo   http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause
