#!/usr/bin/env powershell

# Pair Programming API Startup Script

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host " Pair Programming - Backend Server" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

# Check if .env exists
if (-not (Test-Path "backend\.env")) {
    Write-Host "Creating .env from .env.example..." -ForegroundColor Yellow
    Copy-Item "backend\.env.example" "backend\.env"
    Write-Host "Please update backend\.env with your database credentials if needed." -ForegroundColor Yellow
    Write-Host ""
}

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.9+ from https://www.python.org/" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host ""
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r backend/requirements.txt | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Run the server
Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host " Starting FastAPI server..." -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Server will be available at:" -ForegroundColor Green
Write-Host "  http://localhost:8000/" -ForegroundColor Green
Write-Host ""
Write-Host "API Documentation:" -ForegroundColor Green
Write-Host "  http://localhost:8000/docs" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

Set-Location backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Read-Host "Press Enter to exit"
