from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array ([[32], [64], [128], [256], [512]])
y = np.array ([[15000], [25000], [40000], [65000], [95000]])
model = LinearRegression()
model.fit (x, y)
prediction = model.predict ([ [1024] ] )
print(prediction)

