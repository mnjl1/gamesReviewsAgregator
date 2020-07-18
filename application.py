from flask import Flask, request, redirect, render_template, session
from flask_session import Session
import sqlite3


app = Flask(__name__)


app.config["TEMPLATES_AUTO_RELOAD"]
Session(app)

db = sqlite3.connect('review.db')

@app.route('/')
def index():
    pass
