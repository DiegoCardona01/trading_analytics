import os, sys, argparse
import pandas as pd
import backtrader as bt
from strategies.GoldenCross import GoldenCross
from strategies.BuyHold import BuyHold

# para agregar diferentes estrategias usamos argparse
strategies = {
    'golden_cross': GoldenCross,
    'buy_hold': BuyHold
}

parser = argparse.ArgumentParser()
parser.add_argument('strategy', help='which strategy to run', type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print('invalid strategy, must be one of {}'.format(strategies.keys()))
    sys.exit()

# instanciamos el controlador cerebro
cerebro = bt.Cerebro()
# instanciamos la cantidad de dinero de la simulación
cerebro.broker.setcash(100000)

# fijamos el data que se va a usar
spy_price = pd.read_csv('data/SPY.csv', index_col='Date', parse_dates=True)

# feed = alimentar
feed = bt.feeds.PandasData(dataname=spy_price)
cerebro.adddata(feed)

# cerebro.addstrategy(GoldenCross)
cerebro.addstrategy(strategies[args.strategy])

cerebro.run()
cerebro.plot()
