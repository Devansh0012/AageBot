import uuid
import sqlite3
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def create(update: Update, context):
    user_id = update.message.from_user.id
    uuid_id = str(uuid.uuid4())
    
    conn = sqlite3.connect('user_links.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO UserLink (id, telegram_user_id) VALUES (?, ?)", (uuid_id, user_id))
    conn.commit()
    conn.close()

    await update.message.reply_text(f"Your unique link: https://aagebot-e7c002fc374d.herokuapp.com/{uuid_id}")

async def start(update: Update, context):
    await update.message.reply_text("Use /create to generate your unique link.")

if __name__ == '__main__':
    app = ApplicationBuilder().token("7018500770:AAFz1dkDaJxDRfG2DsC3jg65XcAL8i-EMs8").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("create", create))

    app.run_polling()
