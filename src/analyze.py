import numpy as np
import pandas as pd
import json


class AnalizeClass:
    def __init__(self,price):
        # price_json: list->dict type of price
        self.price_json = json.loads(price)
        self.price = pd.read_json(price)
        self.x = np.arange(len(self.price.index))
        self.candle = self.Candle()
        self.volume = self.Volume()
        self.low = self.find_low()
        self.high = self.find_high()

    def Candle(self): #data for candle
        ohlc = self.price[['opening_price', 'high_price', 'low_price', 'trade_price']].astype(int).values
        dohlc = np.hstack((np.reshape(self.x, (-1, 1)), ohlc))
        return dohlc

    def Volume(self): #data for volume
        return self.price.candle_acc_trade_volume

    


    def ma(self, number):
        y = [0 for _ in range(len(self.price_json))]
        tmp = [0 for _ in range(len(self.price_json))]
        for i in range(len(self.price_json)):
            y[i] = self.price_json[i]['trade_price']
        for i in range(len(self.price_json)-(number-1)):
            k = 0
            for j in range(number):
                k += y[i+j]
            k /= number
            tmp[i+(number-1)] = k
        y = list(tmp)
        return y

    def find_low(self):
        tmp = self.price_json[0]['low_price']
        for i in range(len(self.price_json)):
            if tmp > self.price_json[i]['low_price']:
                tmp = self.price_json[i]['low_price']
        return tmp

    def find_high(self):
        tmp = self.price_json[0]['high_price']
        for i in range(len(self.price_json)):
            if tmp < self.price_json[i]['high_price']:
                tmp = self.price_json[i]['high_price']
        return tmp

    def CCI(self, ndays=14):
        M = []
        SM = []
        D = []
        CCI = []
        N = 20
        for i in range(len(self.price_json)):
            M.append((self.price_json[i]['high_price'] + self.price_json[i]['low_price'] + self.price_json[i]['opening_price']) / 3)

        for i in range(ndays-1):
            SM.append(0)
        for i in range(ndays-1, len(self.price_json)):
            sum = 0
            for j in range(i - ndays + 1, i + 1):
                sum += M[j]
            sum /= ndays
            SM.append(sum)

        for i in range(N-1):
            D.append(0)
        for i in range(N-1, len(self.price_json)):
            sum = 0
            for j in range(i - N + 1, i + 1):
                sum += M[j] - SM[j]
            sum /= N
            D.append(sum)



        for i in range(len(self.price_json)):
            try:
                CCI.append((M[i]-SM[i])/(0.015*D[i]))
            except ZeroDivisionError:
                CCI.append(0)


        return (CCI, max(CCI), min(CCI))


