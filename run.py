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
# args = parser.parse_args()



# instanciamos el controlador cerebro
cerebro = bt.Cerebro()
# instanciamos la cantidad de dinero de la simulación
cerebro.broker.setcash(336.70)

# fijamos el data que se va a usar
spy_price = pd.read_csv('data/SPY.csv', index_col='Date', parse_dates=True)
exito_price = pd.read_csv('data/EXITO.CL.csv', index_col='Date', parse_dates=True)
brkaa_price = pd.read_csv('data/BRK-A.csv', index_col='Date', parse_dates=True)
brkab_price = pd.read_csv('data/BRK-B.csv', index_col='Date', parse_dates=True)

datasets = {
    'SPY': spy_price,
    'exito': exito_price,
    'brk-a': brkaa_price,
    'brk-b': brkab_price,
}

parser.add_argument('stock', help='which stock to analyze', type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print('invalid strategy, must be one of {}'.format(strategies.keys()))
    sys.exit()

# feed = alimentar
feed = bt.feeds.PandasData(dataname=datasets[args.stock])
cerebro.adddata(feed)

# cerebro.addstrategy(GoldenCross)
cerebro.addstrategy(strategies[args.strategy])

cerebro.run()
cerebro.plot()
