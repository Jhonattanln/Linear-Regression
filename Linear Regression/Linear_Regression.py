import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels import regression
import statsmodels.api as sm
import math

df = pd.read_excel('Assets PRBR11.xlsx', index_col = 'Data', parse_dates = True)

def reg (X, Y):
    X = sm.add_constant(X)
    model = regression.linear_model.OLS(Y, X).fit()
    return model.summary()

def pct (stock):
    st = df[stock].pct_change().dropna()
    return st

reg(pct('IBOV'), pct('POSI3'))