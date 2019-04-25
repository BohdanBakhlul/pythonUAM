import matplotlib.pyplot as plt

ax = plt.gca()
ax = plt.axes(polar = True)
f = open("1.txt")
string = ""
string += f.readline()
string = string.split()
string = [float(i) for i in string]
string2=""
string2 += f.readline()
string2 = string2.split()
string2 = [float(i) for i in string2]
t = string2
f.close()
plt.scatter(string, string2, c = t)
plt.show()
