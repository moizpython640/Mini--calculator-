from sklearn.linear_model import LogisticRegression
import numpy as np
x = np.array([[10], [20], [30], [40], [50], [60]])
y = np.array ([0,   0,   0,    1,  1,  1,])
model = LogisticRegression()
model.fit (x, y)
prediction = model.predict ([ [45] ] )
print(prediction)
if prediction [0] == 1:
	print("Result:  SPAM")
else:
	    print("Result: NOT SPAM")

