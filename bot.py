import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Включаем логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Функция обработчика команды /start
async def start(update: Update, context: CallbackContext):
    webapp_url = "https://fincred.space/appfin.html"
    
    keyboard = [[InlineKeyboardButton("📲 Открыть мини-приложение", url=webapp_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет! Нажмите кнопку ниже, чтобы оформить микрозайм прямо в Telegram.",
        reply_markup=reply_markup,
    )

# Функция запуска бота
async def main():
    TOKEN = os.getenv("7754574609:AAEIsZk3EnKCOQTr5w-ubmAiaBNkCbZr080")

    if not TOKEN:
        logger.error("❌ Токен отсутствует! Укажите его в переменных окружения.")
        return
    
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))

    logger.info("✅ Бот запущен! Ожидаем сообщения...")
    
    # Запуск бота
    await application.run_polling()

# Запуск бота
if __name__ == "__main__":
    import asyncio

    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"⚠ Ошибка запуска бота: {e}")
