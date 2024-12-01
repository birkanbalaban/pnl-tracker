@echo off
TITLE Binance PNL Tracker
COLOR 0A

:: Python kontrolü
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python bulunamadi! Lutfen Python'u yukleyin.
    echo https://www.python.org/downloads/
    pause
    exit
)

:: Sanal ortam kontrolü
if not exist "venv" (
    echo Sanal ortam olusturuluyor...
    python -m venv venv
    call venv\Scripts\activate
    echo Gerekli kutuphaneler yukleniyor...
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate
)

:: Uygulamayı başlat
echo PNL Tracker baslatiliyor...
python main.py

:: Hata durumunda bekle
IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo Bir hata olustu! 
    pause
)

deactivate 