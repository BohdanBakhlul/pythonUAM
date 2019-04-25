import matplotlib.pyplot as plt

filename = "data3.dat"
file = open(filename, "r")
x=[[float(i) for i in line.split(',')] for line in file]
plt.boxplot(x)
plt.show()
