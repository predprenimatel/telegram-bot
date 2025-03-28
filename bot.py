import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext

# Включаем логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Функция обработчика команды /start
async def start(update: Update, context: CallbackContext):
    webapp_url = "https://finappvercel.vercel.app/"
    image_url = "https://imgur.com/a/vXTU7Jc"  # Замените на реальную ссылку на изображение

    # Кнопка для запуска веб-приложения
    keyboard = [[InlineKeyboardButton("🚀 Запустити додаток", web_app=WebAppInfo(url=webapp_url))]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Приветственное сообщение
    welcome_text = (
        "👋 Вітаємо у сервісі підбору кредитів!\n\n"
        "💵 Отримайте швидку фінансову допомогу без зайвих документів.\n"
        "📲 Просто натисніть кнопку нижче, щоб запустити додаток!"
    )

    # Отправка изображения с кнопкой
    await update.message.reply_photo(photo=image_url, caption=welcome_text, reply_markup=reply_markup)

# Функция запуска бота
def main():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    if not TOKEN:
        logger.error("❌ Токен відсутній! Укажіть його в змінних оточення.")
        return

    # Создаем объект Application с токеном
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))

    logger.info("✅ Бот запущений! Очікуємо повідомлення...")

    # Запуск бота
    application.run_polling()

# Запуск бота
if __name__ == "__main__":
    main()
