import pandas as pd
import numpy as np
from Scraper import *

class CommodityPredictor:
    def __init__(self, commodity_input, ticker):
        self.commodity_input = commodity_input
        self.ticker = ticker
    def run(self):
        if self.commodity_input == 'cocoa':
            Daniel = Scraper('https://www.barchart.com/futures/quotes/CC*0/futures-prices')
            Daniel.open_website()