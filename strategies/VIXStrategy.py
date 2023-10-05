import backtrader as bt
import datetime

class VIXStrategy(bt.Strategy):
    def __init__(self):
        self.vix = self.datas[0].vixclose
        self.spyopen = self.datas[0].open
        self.spyclose = self.datas[0].close

    def log(self, txt, dt=None):
        """Logging function for this strategy"""
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()}, {txt}')
    
    def next(self):
        # la estrategia considera que en picos superiores a 75
        # se debe activar la compra
        if self.vix[0] > 75:
            self.log(f'Previous VIX, {self.vix[0]}')
            self.log(f'SPY Open, {self.spyopen[0]}')

            if not self.position or self.broker.getcash() > 5000:
                size = int(self.broker.getcash()/self.spyopen[0])
                print(f'Buying {size} SPY at {self.spyopen[0]}')
                self.buy(size=size)

        # estrategia en el caso de que quiera añadir dinero
        if len(self.spyopen)%20 == 0:
            self.log(f'Adding 5000 in cash, never selling. I now have {self.broker.getcash()} in cash on the sidelines')
            self.broker.add_cash(5000)

        # estrategia en el caso en el que vea muy bajo el índice y quiera cerrar una posición
        # if self.vix[0] < 12 and self.position:
        #     self.close()