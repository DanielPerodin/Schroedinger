import pandas as pd
import numpy as np

class CommodityPredictor:
    def __init__(self, commodity, countries_list):
        self.countries_list = []
        self.weather_data = None
        self.imports_data = None
        self.foreign_currency_values = None
        self.historical_output = None
        self.historical_price = None