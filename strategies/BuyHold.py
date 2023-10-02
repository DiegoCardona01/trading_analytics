import backtrader as bt

class BuyHold(bt.Strategy):

    def next(self):

        # si no se tiene una posición, se compra con todo el dinero posible
        if self.position.size == 0:
            size = int(self.broker.getcash()/self.data)
            self.buy(size=size)