from flask import Flask
from app import app
import sqlite3

@app.route('/')
def home():
    return "Please use the bot to generate your unique link."

@app.route('/link/<uuid_id>')
def get_user_link(uuid_id):
    conn = sqlite3.connect('user_links.db')
    cursor = conn.cursor()
    cursor.execute("SELECT telegram_user_id FROM UserLink WHERE id=?", (uuid_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return f"Telegram User ID: {result[0]}"
    else:
        return "Invalid or unknown ID."
