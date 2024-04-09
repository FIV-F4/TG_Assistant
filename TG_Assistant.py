# Основной файл бота

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from W_R_Excel import add_rent_entry

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я ваш финансовый ассистент. Используйте команды для управления вашими финансами и заметками.")

async def add_rent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) < 4:
        await update.message.reply_text('Пожалуйста, используйте правильный формат: /addrent арендатор тип сумма описание')
        return

    tenant = args[0]
    entry_type = args[1]
    try:
        amount = float(args[2])
    except ValueError:
        await update.message.reply_text('Ошибка: сумма должна быть числом.')
        return

    description = ' '.join(args[3:])

    try:
        add_rent_entry(tenant, entry_type, amount, description)
        await update.message.reply_text('Запись успешно добавлена.')
    except Exception as e:
        await update.message.reply_text(f'Произошла ошибка: {e}')

def main() -> None:
    application = Application.builder().token("7163360485:AAFedGG0jckHDN7WH5BhITWRVtjjXleNuUQ").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("addrent", add_rent))

    application.run_polling()

if __name__ == '__main__':
    main()
