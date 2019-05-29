from upbit import UpbitClass
from analyze import AnalizeClass
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_finance import candlestick_ohlc

# TODO: Init upbit class
upbit = UpbitClass()

markets = upbit.GetMarkets()

print('##Please choose a market')
for i in range(10):
    print(i+1,'-',markets[i]['market'],markets[i]['korean_name'])

select = int(input('Market number: ')) - 1

price = upbit.GetPrices(markets[select]['market'])

analyze = AnalizeClass(price)


#####make chart with matplotlib######
fig = plt.figure(figsize=(8, 5))
fig.set_facecolor('w')
gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
axes = []
axes.append(plt.subplot(gs[0]))
axes.append(plt.subplot(gs[1], sharex=axes[0]))
axes[0].get_xaxis().set_visible(False)

candlestick_ohlc(axes[0], analyze.candle, width=0.5, colorup='r', colordown='b')
axes[1].bar(analyze.x, analyze.volume, color='k', width=0.6, align='center')
#####################################
#http://blog.quantylab.com/candlestick.html



plt.tight_layout()
plt.show()