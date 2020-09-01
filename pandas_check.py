import pandas as pd
print(pd.__version__)

budget = pd.read_csv('Budget.csv')
print(budget.head())
