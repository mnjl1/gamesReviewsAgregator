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

db = sqlite3.connect('review.db', check_same_thread=False)

gameSpot = Website('Gamespot', 'https://www.gamespot.com', '^(/reviews/)',
                    False, 'h1', 'img.js-box-art',
                    'div.js-content-entity-body',
                    'div.gs-score__cell')


gsCrawler = Crawler(gameSpot, db)
gsCrawler.crawl()


@app.route('/')
def index():
    con = db.cursor()
    top_reviews = con.execute("SELECT title, url, img_source, score FROM reviews")
    rows = list()
    for row in top_reviews:
        rows.append(row)
    return render_template("index.html", rows=rows)
