from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array ([[1000], [2000], [3000], [4000], [5000]])
y = np.array ([[150], [250], [350], [450], [550]])
model = LinearRegression()
model.fit (x, y)
prediction = model.predict ( [[6000] ] )
print(prediction)

