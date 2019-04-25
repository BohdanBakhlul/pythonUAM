import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg

x1 = np.linspace(-10, 15, 200)
A=np.array([[2., 3.], [5., 4.], [0., 5.]])
B=np.array([4., 23., 18.])

y1=(4-2*x1)/3
y2=(23 - 5*x1)/4
y3=(18 - 0*x1)/5

# print(scipy.linalg.lu(A))
# print(np.linalg.matrix_rank(A))
# print(np.linalg.cond(A))
# print(np.linalg.solve(A, B))
print(np.linalg.lstsq(A, B, rcond=-1))
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x1, y3)
plt.show()
