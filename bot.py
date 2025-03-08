import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Включаем логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Функция обработчика команды /start
def start(update: Update, context: CallbackContext):
    webapp_url = "https://fincred.space/appfin.html"
    image_url = "https://imgur.com/a/GEj9eCh"  # Замените на реальную ссылку на изображение

    # Кнопка "Оформити кредит"
    keyboard = [[InlineKeyboardButton("💰 Оформити кредит", url=webapp_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Приветственное сообщение
    welcome_text = (
        "👋 Вітаємо у сервісі підбору кредитів!\n\n"
        "💵 Отримайте швидку фінансову допомогу без зайвих документів.\n"
        "📲 Просто натисніть кнопку нижче, щоб оформити заявку!"
    )

    # Отправка изображения
    update.message.reply_photo(photo=image_url, caption=welcome_text, reply_markup=reply_markup)

# Функция запуска бота
def main():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    if not TOKEN:
        logger.error("❌ Токен відсутній! Укажіть його в змінних оточення.")
        return

    # Создаем объект Updater с токеном
    updater = Updater(TOKEN, use_context=True)

    # Получаем диспетчер
    dispatcher = updater.dispatcher

    # Добавляем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))

    logger.info("✅ Бот запущений! Очікуємо повідомлення...")

    # Запуск бота
    updater.start_polling()

    # Ждем завершения работы
    updater.idle()

# Запуск бота
if __name__ == "__main__":
    main()
