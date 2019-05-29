from upbit import UpbitClass
from analyze import AnalizeClass
import matplotlib.pyplot as plt

# TODO: Init upbit class
upbit = UpbitClass()

markets = upbit.GetMarkets()

print('##Please choose a market')
for i in range(len(markets)):
    print(i+1,'-',markets[i])

select = int(input('Market number: ')) - 1

price = upbit.GetPrices(markets[select])

analyze = AnalizeClass(price)


#####make chart with matplotlib######
#
#
#####################################



#plt.show()