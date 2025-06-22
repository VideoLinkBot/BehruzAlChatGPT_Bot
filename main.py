from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start komandasi uchun handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Salom! Bot ishga tushdi!")

def main():
    # Bot tokeningizni bu yerga qo'ying
    TOKEN = "SIZNING_BOT_TOKEN"

    # Bot ilovasini yaratamiz
    app = ApplicationBuilder().token(TOKEN).build()

    # /start komandasi uchun handler qo'shamiz
    app.add_handler(CommandHandler("start", start))

    # Botni ishga tushuramiz va pollingni boshlaymiz
    app.run_polling()

if __name__ == "__main__":
    main()
