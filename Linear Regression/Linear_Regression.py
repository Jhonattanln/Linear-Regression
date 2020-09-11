import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels import regression
import statsmodels.api as sm
import math

pd.read_excel(r'')

def reg (X, Y):
    X = sm.add_constant(X)
    model = regression.linear_model.OLS(Y, X).fit()
    a = model[0]
    b = model[1]
    X = X[:,1]

    plt.styler.use('ggplot')
    X2 = np.linspace(X.min(), X.max(), 100)
    Y_hat = X2 * b + a
    plt.scatter(X, Y, alpha=0.5)
    plt.plot(X2, Y_hat, 'r', alpha=1.0)
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    return model.summary()