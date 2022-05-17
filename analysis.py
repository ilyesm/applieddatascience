# Import required libraries
import pandas as pd

# Import and structure the data
pricing = pd.read_csv('data/pricing.csv')
holdings = pd.read_csv('data/Holdings.csv')
tickers = holdings['Ticker'].tolist()
pricing = pricing.set_index('Date')
change = pricing

data = pd.DataFrame(columns=['Standard Deviation', 'Expected Return'])

# Calculate and save the daily returns
for ticker in tickers:
    change[ticker] = pricing[ticker].pct_change()

change.to_csv('data/daily_return.csv')
change.to_excel('data/daily_return.xlsx')

# Calculate the standard deviation of the daily returns
data['Standard Deviation'] = change.std()

# Calculate the covariance matrix
cov = change.cov()

cov.to_csv('data/covariance.csv')
cov.to_excel('data/covariance.xlsx')

# Calculate the expected return
data['Expected Return'] = change.mean() * 100

data.to_csv('data/data.csv')
data.to_excel('data/data.xlsx')