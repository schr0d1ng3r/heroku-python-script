import json as jn
import requests as rq
from lxml import html
import time
import random
import os

TOKEN = os.environ["tik"]
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
cid = str(os.environ['cid'])
a = 2228
x = 5402


def get_url(url):
    response = rq.get(url)
    content = response.content.decode("utf8")
    return content

def get_json(url):
    content = get_url(url)
    js = jn.loads(content)
    return js

def xkcd():
    b = random.randint(1, a)
    page = html.fromstring(rq.get("https://xkcd.com/{}/".format(str(b))).content)
    src = "https://" + page.xpath('//div[@id="comic"]/img/@src')[0].split("?")[0].split("//")[1]
    title = page.xpath('//meta[@property="og:title"]/@content')[0]
    send(src, title)

def explosm():
    y = random.randint(1, x)
    page = html.fromstring(rq.get("http://explosm.net/comics/{}/".format(str(y))).content)
    src = "https://" + page.xpath('//img[@id="main-comic"]/@src')[0].split("?")[0].split("//")[1]
    send(src, "explosm")

def send(img, title):
    sent = rq.get("{}sendPhoto?chat_id={}&photo={}&caption={}".format(URL, cid, img, title))
    print(img, title)

while True:
    xkcd()
    explosm()
    time.sleep(21600)
