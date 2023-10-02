import math
import backtrader as bt

class GoldenCross(bt.Strategy):
    # primero definimos los parámetros de la mma rápida y lenta
    # los valores usuales son 50 para la corta y 200 larga
    # también definimos el porcentaje del dinero que queremos ir invirtiendo
    # definimos el símbolo de la inversion en este caso s&p500 como spy
    params = (('fast', 50), ('slow', 200), ('order_percentage', 0.95), ('ticker', 'SPY'))

    def __init__(self):
        # definimos si el dato es de subida 1 o de bajada -1
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.fast, plotname='50 day moving average'
        )

        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.slow, plotname='200 day moving average'
        )

        self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:
                amount_to_invest = (self.params.order_percentage*self.broker.cash)
                self.size = math.floor(amount_to_invest/self.data.close)

                print('Buy {} shares of {} at {}'.format(self.size, self.params.ticker, self.data.close[0]))

                self.buy(size=self.size)

        if self.position.size > 0:
            if self.crossover < 0:

                print('Sell {} shares of {} at {}'.format(self.size, self.params.ticker, self.data.close[0]))
                
                self.close()