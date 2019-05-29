import numpy as np

class AnalizeClass:
    def __init__(self,price):
        self.price = price
        self.ma5 = self.MA5()
        self.ma20 = self.MA20()
        self.rsi = self.RSI()
        self.cci = self.CCI()
        self.macd = self.MACD()
        #price[200]['openingPrice']

    def MA5(self): #Moving Average 5 (이평선)
        #return ma5. length should be equal to price length
        #example: ma5[200] = 2348
        pass

    def MA10(self):
        pass

    def RSI(self): #Relative Strength Index (상대강도지수)
        pass

    def CCI(self):
        pass

    def MACD(self):
        pass