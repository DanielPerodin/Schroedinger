from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, url):
        self.url = url
    def open_website(self, h):
        reqs = requests.get(self.url, headers=h)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        test_file = open("test-file.txt", "w")
        test_file.write(str(soup))
        # print(str(soup))
        
if __name__ == "__main__":
    url = 'https://www.nasdaq.com/market-activity/commodities/cj:nmx/historical'
    scraper = Scraper(url)
    scraper.open_website({"Accept-Language":"en-US,en;q=0.9", "Accept-Encoding":"gzip, deflate, br", "User-Agent":"Java-http-client/"})