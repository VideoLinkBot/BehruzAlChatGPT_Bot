import os
from dotenv import load_dotenv
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# .env faylni o‘qish
load_dotenv()

# OpenAI va Telegram API kalitlarini olish
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")

# OpenAI API kalitini o‘rnatish
openai.api_key = OPENAI_API_KEY

# /start komandasi uchun handler funksiyasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Men OpenAI yordamida ishlovchi botman. Savolingizni yozing.")

# /ask komandasi uchun handler funksiyasi
async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_text = ' '.join(context.args)
        if not user_text:
            await update.message.reply_text("Iltimos, savolingizni yozing. Masalan: /ask Salom, dunyo!")
            return

        # OpenAI API chaqiruv (eski versiyada Completion.create)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_text,
            max_tokens=100
        )
        answer = response.choices[0].text.strip()
        await update.message.reply_text(answer)
    except Exception as e:
        await update.message.reply_text(f"Xatolik yuz berdi: {e}")

# Botni ishga tushurish
async def main():
    app = ApplicationBuilder().token(TELEGRAM_API_KEY).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask))

    print("Bot ishga tushdi...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
