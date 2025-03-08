from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

async def start(update, context):
    # Ссылка на Telegram Mini App
    webapp_url = "https://fincred.space/appfin.html"
    
    # Создаем кнопку для перехода в WebApp
    keyboard = [
        [InlineKeyboardButton("📲 Открыть мини-приложение", url=webapp_url)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопкой
    await update.message.reply_text("Привет! Нажмите кнопку ниже, чтобы оформить микрозайм прямо в Telegram.", reply_markup=reply_markup)

def main():
    TOKEN = "7390701163:AAGTkCEtlNVSD_FRCxQ-w0S-hfeopKuFKKM"

    # Инициализируем бота
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()
