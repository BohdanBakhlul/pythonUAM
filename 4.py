import matplotlib.pyplot as plt

filename = "data2.dat"
file = open(filename, "r")
x=[float(line) for line in file]
print(x)

plt.subplot(121)
plt.hist(x, cumulative="True")
plt.subplot(122)
plt.hist(x)

plt.show()
