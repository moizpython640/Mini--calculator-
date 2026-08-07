from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array ([[1], [3], [5], [7], [9]])
y = np.array ([[30000], [50000], [70000], [90000], [110000]])
model = LinearRegression()
model.fit (x, y)
prediction = model.predict ([ [11] ] )
print(prediction)

