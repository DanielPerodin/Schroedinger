from Commodity_Predictor import *

commodity_list = ['cocoa'] 
print(commodity_list)
commodity_input = input('Which commodity? ')
ticker = ''
for commodity in commodity_list:
    if commodity == commodity_input.lower():
       ticker = input("What is the stock ticker of the contract? ")
    else:
        print("Commodity not found, try another commodity.")

Vance = CommodityPredictor(commodity_input, ticker)