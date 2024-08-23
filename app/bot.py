import uuid
import sqlite3
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# async def create(update: Update, context):
#     user_id = update.message.from_user.id
#     uuid_id = str(uuid.uuid4())
    
#     conn = sqlite3.connect('user_links.db')
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO UserLink (id, telegram_user_id) VALUES (?, ?)", (uuid_id, user_id))
#     conn.commit()
#     conn.close()

#     await update.message.reply_text(f"Your unique link: https://aagebot-e7c002fc374d.herokuapp.com/{uuid_id}")

# async def start(update: Update, context):
#     await update.message.reply_text("Use /create to generate your unique link.")

# if __name__ == '__main__':
#     app = ApplicationBuilder().token("7018500770:AAFz1dkDaJxDRfG2DsC3jg65XcAL8i-EMs8").build()

#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("create", create))

#     app.run_polling()

import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context):
    await update.message.reply_text("Welcome to AageBot! Use /create to get your unique link.")

async def create(update: Update, context):
    user_id = update.message.from_user.id
    uuid_id = str(uuid.uuid4())
    
    conn = sqlite3.connect('user_links.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO UserLink (id, telegram_user_id) VALUES (?, ?)", (uuid_id, user_id))
    conn.commit()
    conn.close()

    await update.message.reply_text(f"Your unique link: https://aagebot-e7c002fc374d.herokuapp.com/{uuid_id}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(os.getenv("7018500770:AAFz1dkDaJxDRfG2DsC3jg65XcAL8i-EMs8")).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("create", create))

    # Set webhook
    HEROKU_APP_NAME = "aagebot-e7c002fc374d"
    PORT = int(os.environ.get('PORT', 5000))
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=os.getenv("7018500770:AAFz1dkDaJxDRfG2DsC3jg65XcAL8i-EMs8"),
        webhook_url=f"https://{HEROKU_APP_NAME}.herokuapp.com/{os.getenv('7018500770:AAFz1dkDaJxDRfG2DsC3jg65XcAL8i-EMs8')}"
    )
