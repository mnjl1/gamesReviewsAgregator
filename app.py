import crawler
from crawler import Crawler
import website
from website import Website
import sqlite3

gameSpot = Website('Gamespot', 'https://www.gamespot.com', '^(/reviews/)',
                    False, 'h1', 'img.js-box-art',
                    'div.js-content-entity-body',
                    'div.gs-score__cell')


gsCrawler = Crawler(gameSpot)
gsCrawler.crawl()
