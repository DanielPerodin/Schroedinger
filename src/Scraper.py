from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, url) -> None:
        self.url = url

    def open_website(self):
        reqs = requests.get(self.url)
        soup = BeautifulSoup(reqs.text, 'html.parser')