import requests
import json

#https://docs.upbit.com/v1.0.3/reference#%EB%B6%84minute-%EC%BA%94%EB%93%A4-1
#https://systemtraders.tistory.com/648


class UpbitClass:
    def __init__(self):
        self.num = '50'
        self.timeunit = 'minutes'
        self.timeinterval = '15'
        """
        time interval for minute: 1, 3, 5, 15, 10, 30, 60, 240
        
        """

    def GetMarkets(self):
        #get markets info
        url = 'https://api.upbit.com/v1/market/all'

        response = requests.get(url).json()
        return response

    def GetPrices(self,market):
        #get price and volume info and save it to json
        url = 'https://api.upbit.com/v1/candles/' + self.timeunit + '/'+ self.timeinterval +'?market='+ market +'&count=' + self.num

        response = requests.get(url).json()
        response.reverse()
        return json.dumps(response)