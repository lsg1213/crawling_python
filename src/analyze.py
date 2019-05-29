import numpy as np
import pandas as pd

class AnalizeClass:
    def __init__(self,price):
        self.price = pd.read_json(price)
        self.x = np.arange(len(self.price.index))
        self.candle = self.Candle()
        self.volume = self.Volume()
        self.ma5 = self.MA5()
        self.ma20 = self.MA20()
        self.rsi = self.RSI()
        self.cci = self.CCI()
        self.macd = self.MACD()

    def Candle(self): #data for candle
        ohlc = self.price[['opening_price', 'high_price', 'low_price', 'trade_price']].astype(int).values
        dohlc = np.hstack((np.reshape(self.x, (-1, 1)), ohlc))
        return dohlc

    def Volume(self): #data for volume
        return self.price.candle_acc_trade_volume

    def MA5(self): #Moving Average 5 (이평선)
        #return ma5. length should be equal to price length
        pass

    def MA20(self):
        pass

    def RSI(self): #Relative Strength Index (상대강도지수)
        pass

    def CCI(self):
        pass

    def MACD(self):
        pass