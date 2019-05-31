from upbit import UpbitClass
from analyze import AnalizeClass, ma, find_high, find_low, CCI
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_finance import candlestick_ohlc
import json

# TODO: Init upbit class
upbit = UpbitClass()

markets = upbit.GetMarkets()
print('---------------------------------------------------------------')
print('##Please choose a market')
print('##Or if you want to know other coin then put the English name')
print('---------------------------------------------------------------')
while True:
    
    for i in range(10):
        print(i+1,'-',markets[i]['market'],markets[i]['korean_name'])
    try:
        select = input('Market number or English name: ')
        if int(select) <= 10 and int(select) >= 1:
            select = int(select)
            
            break
        print('Please put the number <= 10 and >= 1')
        print('Or put the English name of coin')
        continue
    except ValueError:
        if select.isalpha():
            for i in range(len(markets)):
                if markets[i]['english_name'] == select:
                    select = i
                if type(select) == int:
                    break
            if type(select) == int:
                break
            print('There is no coin that you typed the name')
            print('Put the right name again')
            
        else:
            print('You put wrong input')
            print('Put the right name or number again')
    print('--------------------------------------------------------------')
    
price = upbit.GetPrices(markets[select]['market'])

analyze = AnalizeClass(price)
######################
#이 부분 출력 해보면 좨다 0 나옴 비트코인이랑 대시(1,2)만 제대로 나온다.
print(analyze.candle)

# price_json: list->dict type of price
price_json = json.loads(price)
low = find_low(price_json)
high = find_high(price_json)
_cci=CCI(price_json)
cci_low = min(_cci)
cci_high = max(_cci)

#####make chart with matplotlib######
fig = plt.figure(figsize=(12, 8))
fig.set_facecolor('w')
gs = gridspec.GridSpec(3, 1, height_ratios=[2, 1, 1])
axes = []
axes.append(plt.subplot(gs[0]))
axes.append(plt.subplot(gs[1], sharex=axes[0]))
axes.append(plt.subplot(gs[2], sharex=axes[0]))
axes[0].get_xaxis().set_visible(False)

candlestick_ohlc(axes[0], analyze.candle, width=0.5, colorup='r', colordown='b')
axes[0].plot(analyze.x, ma(price_json,5), color = 'green', marker='o',linestyle='solid', label='ma5')
axes[0].plot(analyze.x, ma(price_json,20), color = 'red', marker='o',linestyle='solid', label='ma20')
axes[0].set_ylim(low + low*0.002, high + high*0.002)

axes[1].bar(analyze.x, analyze.volume, color='k', width=0.6, align='center')
axes[1].title.set_text('transaction amount')

#You can change period of cci, 14 days is default
axes[2].plot(analyze.x, _cci, color = 'red', marker='o', linestyle='solid', label='cci')
axes[2].plot(analyze.x, [100 for _ in range(len(price_json))], color = 'k', marker='o', linestyle='dotted', label='limit_high')
axes[2].plot(analyze.x, [-100 for _ in range(len(price_json))], color = 'k', marker='o', linestyle='dotted', label='limit_low')
axes[2].set_ylim(cci_low+cci_low*0.1, cci_high+cci_high*0.1)
axes[2].title.set_text('cci')
#####################################



plt.tight_layout()
plt.show()
exit()


