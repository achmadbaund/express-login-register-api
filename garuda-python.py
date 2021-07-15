import requests
from requests.adapters import HTTPAdapter

class Scraper(object):

    @classmethod
    def scrapy(cls):
        urls = {
            'home': 'https://www.garuda-indonesia.com/id/id/index.page',
        }

        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2683.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
        }

        s = requests.Session()
        s.mount('https://', HTTPAdapter(pool_connections=1))
        r_search = s.get(urls['home'], headers=headers, verify=False)
        return r_search.text

print(Scraper.scrapy())