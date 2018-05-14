import fxcmpy
from pylab import plt
import pandas as pd
import datetime as dt

con = fxcmpy.fxcmpy(config_file='Config.cfg', server='demo')

#print(con.get_instruments())

#instruments = con.get_instruments_for_candles()
##for i in range(int(len(instruments))):
#    print(instruments[i])
start = dt.datetime(2017, 1, 1)
stop = dt.datetime(2018, 5, 1)

#data = con.get_candles('EUR/USD', period='D1',
#               start=start, stop=stop)

#data.to_csv('newUSDJPYhourly.csv', sep='\t')

#plt.style.use('seaborn')

#data.plot(figsize=(10,6),lw=0.8)

#con.get_open_position().T
order = con.open_trade(symbol='USD/JPY', is_buy=True,
                       rate=105, is_in_pips=False,
                       amount='1000', time_in_force='GTC',
                       order_type='AtMarket', limit=120)
#con.get_open_position().T
