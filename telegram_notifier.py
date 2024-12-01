import asyncio
from telegram import Bot
from telegram.ext import Application, CommandHandler
from datetime import datetime

class TelegramNotifier:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.bot = Bot(token=token)
        self.app = None
        self.loop = None
        
        # Event loop'u başlat
        try:
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
            self.setup_application()
        except Exception as e:
            print(f"Telegram başlatma hatası: {e}")

    def setup_application(self):
        """Telegram uygulamasını başlat"""
        try:
            self.app = Application.builder().token(self.token).build()
            self.app.add_handler(CommandHandler("help", self.cmd_help))
            self.app.add_handler(CommandHandler("pnl", self.cmd_pnl))
            self.app.add_handler(CommandHandler("positions", self.cmd_positions))
            
            # Uygulamayı başlat
            self.loop.run_until_complete(self.app.initialize())
            self.loop.run_until_complete(self.app.start())
            self.loop.run_until_complete(self.app.update_bot_data({}))
        except Exception as e:
            print(f"Telegram uygulama başlatma hatası: {e}")

    def send_message(self, message):
        """Mesaj gönder"""
        try:
            if self.loop and not self.loop.is_closed():
                return self.loop.run_until_complete(self._send_message(message))
            else:
                # Loop kapalıysa yeni bir loop oluştur
                self.loop = asyncio.new_event_loop()
                asyncio.set_event_loop(self.loop)
                return self.loop.run_until_complete(self._send_message(message))
        except Exception as e:
            print(f"Telegram mesaj gönderme hatası: {e}")
            return False

    async def _send_message(self, message):
        """Asenkron mesaj gönderme"""
        try:
            await self.bot.send_message(chat_id=self.chat_id, text=message)
            return True
        except Exception as e:
            print(f"Telegram mesaj gönderme hatası: {e}")
            return False

    def cleanup(self):
        """Uygulama kapatılırken temizlik yap"""
        try:
            if self.loop and not self.loop.is_closed():
                self.loop.run_until_complete(self.app.stop())
                self.loop.run_until_complete(self.app.shutdown())
                self.loop.close()
        except Exception as e:
            print(f"Telegram cleanup hatası: {e}")