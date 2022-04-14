import pandas as pd
import yfinance as yf

data = pd.read_csv('Holdings.csv')
datalist = data['Ticker'].tolist()

pricing = yf.download(
        tickers = datalist,
        period = "10y",
        interval = "1d",
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
    )

transposed = pricing.transpose()
transposed = transposed.reset_index()
transposed = transposed.rename(columns={'level_0':'Ticker'})
transposed = transposed[transposed['level_1']=='Close']
transposed = transposed.drop(columns=['level_1'])
transposed = transposed.set_index('Ticker')
final = transposed.transpose()
final = final.sort_values(by=['Date'], ascending=True)

final.to_csv('pricing.csv')
final.to_excel('pricing.xlsx')