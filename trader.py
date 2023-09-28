import backtrader
import datetime
from strategiesini import TestStrategy
import matplotlib

# Instanciamos el centro de control de backtrader (inicializador)
# conecta los datos con la estrategia
cerebro = backtrader.Cerebro()

# por defecto, cerebro crea un broker, el cual tiene 10000 dolares iniciales
# de ejemplo para hacer trading, ES DECIR QUE ASÍ CREAMOS UN SIMULADOR DE BROKER
# luego crearemos la estrategia

# dinero que queremos tener inicialmente
cerebro.broker.set_cash(1000000)

# Los datos son tomados del github de ejemplos de datos de backtrader, en donde
# tenemos las columnas de fecha y OPHLC que es open, high, low, close, basados en
# estos datos y su variación en el tiempo es que creamos la toma de decisiones y
# por ende estrategias

# backtrader ofrece formas de obtener datos de fuentes actualizadas como 
# yahoo finance y otros, también podemos entrar a estas páginas y descargas los csv
# y trabajar con estos

data = backtrader.feeds.YahooFinanceCSVData(
    dataname='oracle.csv',
    # Do not pass values before this date
    fromdate=datetime.datetime(2000, 1, 1),
    # Do not pass values after this date
    todate=datetime.datetime(2000, 12, 31),
    reverse=False)

# conectamos los datos a cerebro
cerebro.adddata(data)

# añadimos la estrategia

cerebro.addstrategy(TestStrategy)

# Add a FixedSize sizer according to the stake
cerebro.addsizer(backtrader.sizers.FixedSize, stake=1000)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()