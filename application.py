from flask import Flask, request, redirect, render_template, session
from flask_session import Session
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import time
import telegram
from telebot.credentials import bot_token, bot_user_name, heroku_url
from telebot.mastermind import get_response
from service.getDataFromDataBase import get_last_reviews_json, get_last_reviews_web
import sqlite3
import crawler
from crawler import Crawler
import website
from website import Website

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"]
Session(app)

db = sqlite3.connect('review.db', check_same_thread=False)

gameSpot = Website('Gamespot', 'https://www.gamespot.com', '^(/reviews/)',
                    False, 'h1', 'img.js-box-art',
                    'div.js-content-entity-body',
                    'div.gs-score__cell', 'time')

gsCrawler = Crawler(gameSpot, db)
gsCrawler.crawl()

scheduler = BackgroundScheduler()
scheduler.add_job(func=lambda : gsCrawler.crawl(), trigger='interval', seconds=60)
scheduler.start()

#bot API

@app.route(f'/{TOKEN}', methods = ['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force = True), bot)
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    text = update.message.text.encode('utf-8').decode()
    response = get_last_reviews_json(db)
    bot.sendMessage(chat_id=chat_id, text = response, reply_to_message_id = msg_id)
    return 'ok'

@app.route('/setwebhook', methods = ['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{heroku_url}{HOOK}'.format(heroku_url=heroku_url, HOOK=bot_token))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

#web API
@app.route('/')
def index():
    return render_template("index.html", rows=get_last_reviews_web(db))


if __name__ == '__main__':
    application.run(threaded=True)
