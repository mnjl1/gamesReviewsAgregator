import requests
import re
from bs4 import BeautifulSoup
import content
import datetime
from datetime import datetime

class Crawler:

    def __init__(self, site, data_base):
        self.site = site
        self.data_base = data_base
        self.visited = []


    def getPage(self, url):
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
        try:
            req = session.get(url, headers=headers)
        except requests.exceptions.RequestException:
            return None
        bs = BeautifulSoup(req.text, 'html.parser')
        return bs


    def safeGet(self, pageObject, selector):
        selectedElements = pageObject.select(selector)
        if selectedElements is not None and len(selectedElements) > 0:
            result = 'n'.join([elem.get_text() for elem in selectedElements])
            return result
        return ''


    def getImage(self, pageObject, selector):
        try:
            img = pageObject.select(selector)[0]['src']
            if img is not None:
                return img
            else:
                return ''
        except:
            return ''


    def parse(self, url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = self.safeGet(bs, self.site.bodyTag)
            imageSrc = self.getImage(bs, self.site.imgTag)
            score = self.safeGet(bs, self.site.scoreTag)
            if title != '' and body != '':
                self.data_base.execute("INSERT INTO reviews(title, url, img_source, body,"
                            +"created_at, score) VALUES(:title, :url,"
                            +":imageSrc, :body, :created_at, :score)",
                            dict(title=title, url=url, imageSrc=imageSrc,
                             body=body, created_at=datetime.now(), score=score))
                self.data_base.commit()



    def crawl(self):
        bs = self.getPage(self.site.url)
        targetPages = bs.findAll('a', href=re.compile(self.site.targetPattern))
        for targetPage in targetPages:
            targetPage = targetPage.attrs['href']
            if targetPage not in self.visited:
                print("new Content detected..")
                self.visited.append(targetPage)
                if not self.site.absoluteUrl:
                    targetPage = f'{self.site.url}{targetPage}'
                    print(targetPage)
                self.parse(targetPage)
