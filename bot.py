import os
from dotenv import load_dotenv

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv("/data/data/com.termux/files/home/exam_bot/.env")

TOKEN = os.getenv("BOT_TOKEN")

WEB_APP_URL = "https://aliasghar2010smart-alt.github.io/exam_bot/"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "📝 شروع آزمون",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]

    await update.message.reply_text(
        "سلام 👋\n"
        "به شبیه‌ساز آزمون خوش آمدی.\n\n"
        "برای شروع آزمون روی دکمه زیر بزن:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN تنظیم نشده است.")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
0

