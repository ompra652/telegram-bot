import os
import logging
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bot start hone par"""
    await update.message.reply_text(
        "👋 Salam! Main 24/7 online hoon!\n\n"
        "/help - Commands dekho\n"
        "/about - Mere baare mein"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command"""
    await update.message.reply_text(
        "📋 Available Commands:\n"
        "/start - Shuru karo\n"
        "/about - About\n"
        "/hello - Salaam"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """About command"""
    await update.message.reply_text(
        "ℹ️ Main ek Telegram bot hoon jo Render par 24/7 chalraha hai! 🤖"
    )

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hello command"""
    await update.message.reply_text(f"Salam {update.effective_user.first_name}! 👋")

def main():
    """Main function"""
    TOKEN = os.getenv('TELEGRAM_TOKEN')
    
    if not TOKEN:
        raise ValueError("TELEGRAM_TOKEN environment variable set nahi hai!")
    
    app = Application.builder().token(TOKEN).build()
    
    # Commands add karo
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("hello", hello))
    
    # Bot shuru karo
    print("🚀 Bot start ho gaya!")
    app.run_polling()

if __name__ == '__main__':
    main()
