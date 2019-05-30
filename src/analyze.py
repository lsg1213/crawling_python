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

    def RSI(self): #Relative Strength Index (상대강도지수)
        pass

    def CCI(self):
        pass

    def MACD(self):
        pass


def ma(price_json, number):
    y = [0 for _ in range(len(price_json))]
    tmp = [0 for _ in range(len(price_json))]
    for i in range(len(price_json)):
        y[i] = price_json[i]['trade_price']
    for i in range(len(price_json)-(number-1)):
        k = 0
        for j in range(number):
            k += y[i+j]
        k /= number
        tmp[i+(number-1)] = k
    y = list(tmp)
    return y

def find_low(price_json):
    tmp = price_json[0]['low_price']
    for i in range(len(price_json)):
        if tmp > price_json[i]['low_price']:
            tmp = price_json[i]['low_price']
    return tmp

def find_high(price_json):
    tmp = price_json[0]['high_price']
    for i in range(len(price_json)):
        if tmp < price_json[i]['high_price']:
            tmp = price_json[i]['high_price']
    return tmp
