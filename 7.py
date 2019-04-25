import numpy as np

data=np.random.rand(25)*100
max = np.amax(data)
print('Max element from Numpy Array : ', max)
data[data < 50] = 0
data[np.argmax(data)] = 200
print(data)
