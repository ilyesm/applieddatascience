# Import libraries
from email.quoprimime import header_check
from pandas_datareader.data import DataReader
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt import plotting
import copy
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Import Data
tickers = pd.read_csv('data/Holdings.csv')['Ticker'].tolist()
stocks_df = pd.read_csv('data/pricing.csv').set_index('Date')
daily_returns = pd.read_csv('data/daily_return.csv').set_index('Date')

# Define variables
num_portfolios = 10000
risk_free_rate = 0.018
number = 0

# Define DataFrame to store results
df = pd.DataFrame(columns=['Portfolio','Annualized Return', 'Annualized Volatility', 'Sharpe Ratio'])

# Read CSV with previously generated portfolios
portfolios = pd.read_csv('data/portfolios.csv')

# Define portfolio return function
def annual_perf(weights, avg_returns, cov_matrix):

    returns = np.sum(avg_returns*weights ) *252

    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    return std, returns

# Define portfolio generator
def portfolio_weights(num_portfolios, avg_returns, cov_matrix, risk_free_rate):

    results = np.zeros((3,num_portfolios))

    weight_array = []
    for i in range(num_portfolios):
        # Assign random weights from the 15 tickers to the portfolio
        weights = np.random.random(15)
        weights /= np.sum(weights)
        weight_array.append(weights)
        # calls the annual_perf function to calculate the standard deviation and return of the portfolio
        portfolio_std_dev, portfolio_return = annual_perf(weights, avg_returns, cov_matrix)
        # Calculate Std Dev and Return of the generated portfolio
        results[0,i] = portfolio_std_dev
        results[1,i] = portfolio_return
        # Calculate Sharpe Ratio of generated portfolio
        results[2,i] = (portfolio_return - risk_free_rate) / portfolio_std_dev
    return results, weight_array

# Define function to collect and output results
def simulated_portfolio(number, avg_returns, cov_matrix, num_portfolios, risk_free_rate):
    global df
    # Collect weights from function portfolio_weights
    results, weights = portfolio_weights(num_portfolios, avg_returns, cov_matrix, risk_free_rate)

    max_sharpe_idx = np.argmax(results[2])

    # Collect results from function annual_perf
    stdev_portfolio, returns_portfolio = results[0,max_sharpe_idx], results[1,max_sharpe_idx]

    # Generate the portfolio with the highest Sharpe ratio possible
    max_sharpe_allocation = pd.DataFrame(weights[max_sharpe_idx],index=portfolio, columns=['weight'])
    max_sharpe_allocation.weight = [round(i*100,2)for i in max_sharpe_allocation.weight]

    # Save returns and volatility to dataframe
    temp = pd.DataFrame({'Portfolio': number, 'Annualized Return': returns_portfolio, 'Annualized Volatility': stdev_portfolio, 'Sharpe Ratio': results[2,max_sharpe_idx]},index=[0])
    df = pd.concat([temp, df])


for row in portfolios.index:
    # Load each portfolio
    portfolio = np.array(portfolios.iloc[row])
    portfolio = portfolio[1:]

    # Gather data to pass to function for each portfolio
    returns = daily_returns[portfolio]
    avg_returns = returns.mean()
    cov_matrix = returns.cov()

    # Call function
    simulated_portfolio(number, avg_returns, cov_matrix, num_portfolios, risk_free_rate)

    # Increment number
    number = number + 1

df.to_csv('data/portfolioresults.csv', mode='a', header=['Portfolio','Annualized Return', 'Annualized Volatility','Sharpe Ratio'])