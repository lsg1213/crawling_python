from upbit import UpbitClass
from analyze import AnalizeClass, ma, find_high, find_low, CCI
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_finance import candlestick_ohlc
import json

# TODO: Init upbit class
upbit = UpbitClass()

markets = upbit.GetMarkets()
print('##Please choose a market')

for i in range(10):
    print(i+1,'-',markets[i]['market'],markets[i]['korean_name'])

select = int(input('Market number: ')) - 1

price = upbit.GetPrices(markets[select]['market'])

analyze = AnalizeClass(price)

# price_json: list->dict type of price
price_json = json.loads(price)
low = find_low(price_json)
high = find_high(price_json)
print(price_json[0])

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
axes[0].set_ylim(low - low*0.002, high + high*0.002)

axes[1].bar(analyze.x, analyze.volume, color='k', width=0.6, align='center')
axes[1].title.set_text('transaction amount')

axes[2].plot(analyze.x, CCI(price_json, 14), color = 'red', marker='o', linestyle='solid', label='cci')
axes[2].set_ylim(-500, 500)
axes[2].title.set_text('cci')
#####################################



plt.tight_layout()
plt.show()
exit()


