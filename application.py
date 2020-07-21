from flask import Flask, request, redirect, render_template, session
from flask_session import Session
import sqlite3
import crawler
from crawler import Crawler
import website
from website import Website

app = Flask(__name__)


app.config["TEMPLATES_AUTO_RELOAD"]
Session(app)

gameSpot = Website('Gamespot', 'https://www.gamespot.com', '^(/reviews/)',
                    False, 'h1', 'img.js-box-art',
                    'div.js-content-entity-body',
                    'div.gs-score__cell')


gsCrawler = Crawler(gameSpot)
gsCrawler.crawl()

@app.route('/')
def index():
    return render_template("index.html")
