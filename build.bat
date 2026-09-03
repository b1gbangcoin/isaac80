@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo.
echo ========================================
echo Build EXE for Isaac80
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo OK: Python detected

echo.
echo Installing dependencies...
pip install -q pyinstaller pillow

echo OK: Dependencies installed

echo.
echo Building EXE...
pyinstaller --onefile --windowed ^
    --name "Isaac80" ^
    --add-data "g1.gif;." ^
    --add-data "g2.gif;." ^
    --add-data "g3.gif;." ^
    --add-data "g4.gif;." ^
    --add-data "g5.gif;." ^
    gui.py

if errorlevel 1 (
    echo Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! Build completed
echo ========================================
echo.
echo Output: dist\Isaac80.exe
echo.
pause
