import re
import collections

class Soultion:
    def Counting(self, urls):

        url_list = [re.split('/', url)[-1] for url in urls]
        count = sorted(collections.Counter(url_list).most_common(3))

        for i in range(3):
            print(count[i][0], count[i][1])


urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

res = Soultion()
res.Counting(urls)
