import numpy as np

A = np.random.randint(-100, 100, size = (9,9))
print(A)
arr = A[A%2 == 0]
arr.sort()
print(arr)
