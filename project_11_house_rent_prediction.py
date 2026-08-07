from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array ([[500], [700], [900], [1100], [1300]])
y = np.array ([[10000], [14000], [18000], [22000], [26000]])
model = LinearRegression()
model.fit (x, y)
prediction = model.predict ([ [1500] ] )
print(prediction)

