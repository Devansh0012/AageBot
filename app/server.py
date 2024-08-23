from flask import Flask
from app import app
import sqlite3

@app.route('/')
def home():
    return '''
        <h1 style="font-family: Arial, sans-serif; color: #333;">Welcome to AageBot</h1>
        <p style="font-family: Arial, sans-serif; color: #666;">Please use the bot to generate your unique link.</p>
        <p style="font-family: Arial, sans-serif; color: #666;">You can access the bot by clicking the link below:</p>
        <a href="https://t.me/Aaagee_bot" target="_blank" style="font-family: Arial, sans-serif; color: #007bff; text-decoration: none;">Access AageBot on Telegram</a>
    '''

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
