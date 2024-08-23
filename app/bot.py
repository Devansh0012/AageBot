from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from uuid import uuid4

def store_user_link(user_id, uuid):
    with open("user_links.txt", "a") as file:
        file.write(f"{user_id},{uuid}\n")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return
    await update.message.reply_text("Welcome to AageBot! Use /create to get your unique link.")

async def create(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    if update.message is None:
        print("No message found in the update")
        return


    user_id = update.message.from_user.id
    uuid = str(uuid4())
    
    store_user_link(user_id, uuid)
    
    link = f"https://aagebot-e7c002fc374d.herokuapp.com/link/{uuid}"
    await update.message.reply_text(f"Your unique link is: {link}")

if __name__ == '__main__':
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("No Telegram bot token found. Please set the TELEGRAM_BOT_TOKEN environment variable.")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("create", create))

    app.run_polling()
