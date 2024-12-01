@"
# Binance PNL Tracker - Detaylı Kurulum Kılavuzu

## 📋 İçindekiler
1. [Windows Kurulumu](#windows-kurulumu)
2. [Ubuntu Server Kurulumu](#ubuntu-server-kurulumu)
3. [Telegram Bot Kurulumu](#telegram-bot-kurulumu)
4. [Binance API Ayarları](#binance-api-ayarları)
5. [Sorun Giderme](#sorun-giderme)

## Windows Kurulumu

### Gereksinimler
- Python 3.8 veya üzeri
- Git
- Visual Studio Code (önerilen)

### Adım Adım Kurulum
1. Python Kurulumu:
   - https://www.python.org/downloads/ adresinden Python indirin
   - Kurulum sırasında 'Add Python to PATH' seçeneğini işaretleyin

2. Git Kurulumu:
   - https://git-scm.com/download/win adresinden Git indirin
   - Standart kurulum seçenekleriyle devam edin

3. Repository Kurulumu:
   \`\`\`bash
   git clone https://github.com/birkanbalaban/binance-pnl-tracker.git
   cd binance-pnl-tracker
   \`\`\`

4. Virtual Environment:
   \`\`\`bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   \`\`\`

5. Yapılandırma:
   \`\`\`bash
   cp config.ini.example config.ini
   # config.ini dosyasını düzenleyin
   \`\`\`

## Ubuntu Server Kurulumu

### Gereksinimler
- Ubuntu 20.04 LTS veya üzeri
- Python 3.8+
- Screen

### Adım Adım Kurulum
1. Sistem Güncellemesi:
   \`\`\`bash
   sudo apt update
   sudo apt upgrade
   \`\`\`

2. Gerekli Paketlerin Kurulumu:
   \`\`\`bash
   sudo apt install python3-pip python3-venv screen git
   \`\`\`

3. Repository Kurulumu:
   \`\`\`bash
   git clone https://github.com/birkanbalaban/binance-pnl-tracker.git
   cd binance-pnl-tracker
   \`\`\`

4. Virtual Environment:
   \`\`\`bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   \`\`\`

5. Yapılandırma:
   \`\`\`bash
   cp config.ini.example config.ini
   nano config.ini
   \`\`\`

6. Screen ile Çalıştırma:
   \`\`\`bash
   screen -S pnl_tracker
   python3 main.py
   # CTRL+A+D ile screen'den çıkın
   \`\`\`

7. Screen Komutları:
   - Yeniden Bağlanma: \`screen -r pnl_tracker\`
   - Aktif Screen'ler: \`screen -ls\`
   - Screen Sonlandırma: \`screen -X -S pnl_tracker quit\`

## Telegram Bot Kurulumu

1. BotFather ile Bot Oluşturma:
   - Telegram'da @BotFather'ı açın
   - /newbot komutunu gönderin
   - Bot adı ve kullanıcı adı belirleyin
   - Bot token'ını kaydedin

2. Chat ID Bulma:
   - @userinfobot'u açın
   - Herhangi bir mesaj gönderin
   - Size chat ID'nizi verecektir

## Binance API Ayarları

1. API Oluşturma:
   - Binance hesabınıza giriş yapın
   - API Management sayfasına gidin
   - 'Create API' butonuna tıklayın
   - Sadece 'Read Info' ve 'Enable Futures' izinlerini verin

2. Güvenlik Önerileri:
   - IP kısıtlaması ekleyin
   - Anti-phishing code kullanın
   - 2FA aktif olmalı

## Sorun Giderme

### Sık Karşılaşılan Hatalar

1. Telegram Bağlantı Hatası:
   - Bot token'ı kontrol edin
   - Internet bağlantısını kontrol edin
   - /stop ve /start komutlarını deneyin

2. Binance API Hatası:
   - API anahtarlarını kontrol edin
   - IP kısıtlamalarını kontrol edin
   - Futures hesabı aktif olmalı

3. Screen Sorunları:
   - \`screen -wipe\` ile bozuk screen'leri temizleyin
   - \`killall screen\` ile tüm screen'leri sonlandırın
   - Yeni bir screen başlatın

### Log Dosyaları
- error.log: Hata kayıtları
- app.log: Uygulama kayıtları

## Güncelleme

1. Kodları Güncelleme:
   \`\`\`bash
   git pull origin main
   pip install -r requirements.txt
   \`\`\`

2. Config Kontrolü:
   - config.ini.example ile karşılaştırın
   - Yeni ayarları ekleyin

## İletişim ve Destek
- GitHub Issues üzerinden bildirim açabilirsiniz
- Telegram: @your_support_channel
"@ | Out-File -Encoding UTF8 readmeMain.md