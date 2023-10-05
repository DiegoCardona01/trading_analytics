import backtrader as bt
from strategies.VIXStrategy import VIXStrategy
import os

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

class SPYVIXData(bt.feeds.GenericCSVData):
    lines = ('vixopen', 'vixhigh', 'vixlow', 'vixclose')

    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('spyopen', 1),
        ('spyhigh', 2),
        ('spylow', 3),
        ('spyclose', 4),
        ('spyadjclose', 5),
        ('spyvolume', 6),
        ('vixopen', 7),
        ('vixhigh', 8),
        ('vixlow', 9),
        ('vixclose', 10)
    )

class VIXData(bt.feeds.GenericCSVData):
    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('vixopen', 1),
        ('vixhigh', 2),
        ('vixlow', 3),
        ('vixclose', 4),
        ('volume', -1),
        ('openinterest', -1)
    )

csv_file = os.path.dirname(os.path.abspath(__file__))+'/data/SPY_VIX.csv'
vix_file = os.path.dirname(os.path.abspath(__file__))+'/data/VIX_short.csv'

spyVixDataFeed = SPYVIXData(dataname=csv_file)
vixDataFeed = VIXData(dataname=vix_file)
cerebro.adddata(spyVixDataFeed)
cerebro.adddata(vixDataFeed)

cerebro.addstrategy(VIXStrategy)

cerebro.run()
cerebro.plot(volume=False)