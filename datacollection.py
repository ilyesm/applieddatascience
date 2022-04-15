# Import Pandas and YFinance
import pandas as pd
import yfinance as yf

# Read the data and filter for the required column
data = pd.read_csv('Holdings.csv')
datalist = data['Ticker'].tolist()

# Create a DataFrame with each ticker and the corresponding closing price for the past 10 years
pricing = yf.download(
        tickers = datalist,
        period = "10y",
        interval = "1d",
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
    )

# Clean up the data (remove the index and rename and drop unnecessary columns)
transposed = pricing.transpose()
transposed = transposed.reset_index()
transposed = transposed.rename(columns={'level_0':'Ticker'})
transposed = transposed[transposed['level_1']=='Close']
transposed = transposed.drop(columns=['level_1'])
transposed = transposed.set_index('Ticker')

# Restore the data into a readable file
final = transposed.transpose()
final = final.sort_values(by=['Date'], ascending=True)

# Export clean data to CSV and Excel
final.to_csv('pricing.csv')
final.to_excel('pricing.xlsx')