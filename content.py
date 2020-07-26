import  requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, url, title, imageSrc, body, publicDate, score):
        self.url = url
        self.title = title
        self.imageSrc = imageSrc
        self.body = body
        self.publicDate = publicDate
        self.score = score
