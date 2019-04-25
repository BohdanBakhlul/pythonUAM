import matplotlib.pyplot as plt

x=[0.162998851263, 0.950506175973, 0.384844384574, 0.159054356594, 0.996021284449 ]
explode = (0.2, 0.01, 0.01, 0.01, 0.01)
plt.pie(x, explode=explode)
plt.show()
