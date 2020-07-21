import  requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, url, title, imageSrc, body, score):
        self.url = url
        self.title = title
        self.imageSrc = imageSrc
        self.body = body
        self.score = score


    def print_article(self):
        print(f'Title: {self.title}')
        print(f'Url: {self.url}')
        print(f'Image source: {self.imageSrc}')
        # print(f'Body: {self.body}')
        print(f'Score {self.score}')
