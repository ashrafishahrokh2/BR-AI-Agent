from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "به دستیار هوشمند B&R خوش آمدید.\n\n"
        "من برای معرفی محصولات، تولید محتوا و راهنمایی فروشگاهی ساخته شده‌ام."
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "پیام شما دریافت شد ✅\n\n"
        "نسخه اولیه ربات B&R فعال است.\n"
        "به‌زودی هوش مصنوعی GPT و Gemini به من وصل می‌شود."
    )

def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN is not set")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    app.run_polling()

if __name__ == "__main__":
    main()
