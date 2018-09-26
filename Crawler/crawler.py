import re
import json
import datetime

import requests
from bs4 import BeautifulSoup


url = 'https://www.ptt.cc/'
kanban = 'movie'
request = requests.get(url + 'bbs/' + kanban + '/')
soup = BeautifulSoup(request.text, "html.parser")

with open('./history.json', 'r') as f:
    history_data = json.loads(f.read())

history_list = [history['title'] for history in history_data]
new_posts = []

for article in soup.select('.r-list-container .r-ent'):

    title = article.select('.title a')[0].string
    link  = article.select('.title a')[0].get('href')

    if title in history_list or '版規' in title:
        continue

    request = requests.get(url + link)
    content_soup = BeautifulSoup(request.text, "html.parser")

    author  = content_soup.select('.article-meta-value')[0].string
    date    = content_soup.select('.article-meta-value')[3].string
    content = content_soup.select('#main-content')[0].get_text()

    new_posts.append({
        'title': str(title), 'link': link, 'author': author, 'date': date, 'content': content
    })

with open('./history.json', 'r+') as f:
    json.dump(new_posts, f, ensure_ascii=False)


