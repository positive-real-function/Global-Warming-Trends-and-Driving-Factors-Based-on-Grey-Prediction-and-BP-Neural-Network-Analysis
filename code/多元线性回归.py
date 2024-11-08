import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

df = pd.read_csv("WS.csv")

X = df[['year','month','Latitude_value','Longitude_value' ]]
Y = df['AverageTemperature']
model = LinearRegression()
model.fit(X, Y)

print(model.coef_, model.intercept_)

X2 = sm.add_constant(X)
est = sm.OLS(Y, X2).fit()
print(est.summary())
