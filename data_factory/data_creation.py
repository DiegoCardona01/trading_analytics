import pandas as pd

df_spy = pd.read_csv('./data/SPY.csv', index_col='Date', parse_dates=True)
df_vix = pd.read_csv('./data/VIX_History.csv', index_col='DATE', parse_dates=True)

index_min = df_spy.index.min()
index_max = df_spy.index.max()

df_vix_short = df_vix.copy()[index_min:index_max]
# df_vix_short.to_csv('./data/VIX_short.csv')

df_combined = pd.concat([df_spy, df_vix_short], axis=1)
df_combined.reset_index(inplace=True)

df_combined.rename(columns={
    'index': 'date',
    'Open': 'SPY Open',
    'High':'SPY High',
    'Low':'SPY Low',
    'Close':'SPY Close',
    'Adj Close':'SPY Adj Close',
    'Volume':'SPY Volume',
    'OPEN': 'VIX OPEN',
    'HIGH': 'VIX HIGH',
    'LOW': 'VIX LOW',
    'CLOSE': 'VIX CLOSE'
}, inplace=True)

# df_combined.to_csv('./data/SPY_VIX.csv', index=False)