from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array ([[1], [2], [3], [4], [5]])
y = np.array ([[1800000], [ 1600000], [14000000], [1200000], [1000000]])
model = LinearRegression()
model.fit (x, y)
prediction = model.predict ( [[6] ] )
print(prediction)

