import requests
import json

class UpbitClass:
    def __init__(self):
        self.num = 200
        self.time = '15m'
        self.markets = []
        self.prices = {}
        # self.prices['KRW-XEM'][200]['openingPrice']
        # store latest 200 items (15m). Having 5 data => openingPrice, highPrice, lowPrice, tradePrice, candleAccTradeVolume


        # read saved data
        # if saved data has different value of num or time, delete it and save new one

    def GetMarkets(self):
        #get markets info
        pass

    def GetPrices(self,market):
        #get price and volume info and save it to json
        pass


