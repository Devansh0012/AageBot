from flask import Flask

app = Flask(__name__)

from app import server, bot, db

db.init_db()
