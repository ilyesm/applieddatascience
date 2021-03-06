# Import libraries
import pandas as pd
import numpy as np
import random

# Define function to generate list of random portfolios
def generate_portfolios(stocks, num_portfolios, num_stocks):
    portfolios = []
    for i in range(num_portfolios):
        portfolio = []
        for j in range(num_stocks):
            portfolio.append(random.choice(stocks))
        portfolios.append(portfolio)
    return portfolios

# Read data of available tickers
tickers = pd.read_csv('/Users/ilyas/github/applieddatascience/data/Holdings.csv')['Ticker']

# Call function
portfolios = pd.DataFrame(generate_portfolios(tickers, 10000, 15))

# Export data to CSV and Excel
portfolios.to_csv('/Users/ilyas/github/applieddatascience/data/portfolios.csv')
portfolios.to_excel('/Users/ilyas/github/applieddatascience/data/portfolios.xlsx')