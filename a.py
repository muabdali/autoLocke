import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# read data from CSV file
data = pd.read_csv('2.csv')

# extract X and y values from data
X = data.iloc[:, 0].values.reshape(-1, 1)
y = data.iloc[:, 1].values.reshape(-1, 1)

# create polynomial features for X
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

# perform linear regression
regressor = LinearRegression()
regressor.fit(X_poly, y)

# print equation
coef = regressor.coef_
intercept = regressor.intercept_
print(f"y = {coef[0][3]}x^3 + {coef[0][2]}x^2 + {coef[0][1]}x + {intercept[0]}")
