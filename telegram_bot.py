from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio
import nest_asyncio

# Replace 'YOUR_BOT_API_TOKEN' with your actual bot API token
BOT_API_TOKEN = '7935212447:AAF1QGQkSMwFLWqyWWlERoFTbMPy7z74IEE'

nest_asyncio.apply()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = "Welcome to the Key Generator Bot! Please choose an option:"
    keyboard = [
        [InlineKeyboardButton("Get Token", callback_data='get_token')],
        [InlineKeyboardButton("Generate Keys", callback_data='generate_keys')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'get_token':
        await query.edit_message_text(text="To get a token, please visit the link: [Your Link]")
    elif query.data == 'generate_keys':
        await query.edit_message_text(text="Please enter your token to generate keys.")

async def main():
    application = ApplicationBuilder().token(BOT_API_TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))

    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
