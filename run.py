import numpy as np
import pandas as pd

# Import results
weights = pd.read_csv('data/generatedportfolios/weights/test.csv',names=['ticker','weight'])
results = pd.read_csv('data/portfolioresults.csv').set_index('Portfolio')

# Find portfolio with highest annual return
highest_return_port_num = results.sort_values('Annualized Return',ascending=False).iloc[0].name

highest_return = results.loc[highest_return_port_num]
highest_return_weights = weights.loc[highest_return_port_num*15:(highest_return_port_num*15)+14].set_index('ticker').T

# Find portfolio with the lowest standard deviation
lowest_stdev_port_num = results.sort_values('Annualized Volatility',ascending=True).iloc[0].name

lowest_stdev = results.loc[lowest_stdev_port_num]
lowest_stdev_weights = weights.loc[lowest_stdev_port_num*15:(lowest_stdev_port_num*15)+14].set_index('ticker').T

# Find portfolio with the highest sharpe ratio
highest_sharperatio_port_num = results.sort_values('Sharpe Ratio',ascending=False).iloc[0].name

highest_sharpe = results.loc[highest_sharperatio_port_num]
highest_sharpe_weights = weights.loc[highest_sharperatio_port_num*15:(highest_sharperatio_port_num*15)+14].set_index('ticker').T

print('Welcome to our Applied Data Science Project!')
print('This is a project for the Applied Data Science class at the Católica-Lisbon School of Business and Economics.')
print('We are interested in the impact of different types of portfolios on the performance of a stock market.')
print('Work by: Ilyas Esmail, Joao Pedro Paulo, Pedro Calixto')
print('\n')
print('We have generated three portfolios for you to choose from:')
print('-----------------------------------------------------')
print('The portfolio with the highest annualized return is: ' + str(highest_return_port_num))
print('It has an annualized return of: ' + (str(round((highest_return.iloc[1] * 100), 2)) + '%'))
print('It has an annualized volatility of: ' + (str(round((highest_return.iloc[2] * 100), 2)) + '%'))
print('It has a Sharpe ratio of: ' + str(round(highest_return.iloc[3],4)))
print('The portfolio weights are: ')
print(highest_return_weights)
print('-----------------------------------------------------')
print('The portfolio with the lowest annualized volatility is: ' + str(lowest_stdev_port_num))
print('It has an annualized return of: ' + (str(round((lowest_stdev.iloc[1] * 100), 2)) + '%'))
print('It has an annualized volatility of: ' + (str(round((lowest_stdev.iloc[2] * 100), 2)) + '%'))
print('It has a Sharpe ratio of: ' + str(round(lowest_stdev.iloc[3],4)))
print('The portfolio weights are: ')
print(lowest_stdev_weights)
print('-----------------------------------------------------')
print('The portfolio with the highest Sharpe ratio is: ' + str(highest_sharperatio_port_num))
print('It has an annualized return of: ' + (str(round((highest_sharpe.iloc[1] * 100), 2)) + '%'))
print('It has an annualized volatility of: ' + (str(round((highest_sharpe.iloc[2] * 100), 2)) + '%'))
print('It has a Sharpe ratio of: ' + str(round(highest_sharpe.iloc[3],4)))
print('The portfolio weights are: ')
print(highest_sharpe_weights)
print('-----------------------------------------------------')