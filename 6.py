import matplotlib.pyplot as plt

x=[0, 5, 10, 15, 20]
y=[0, 11, 13, 14.5, 15]



# axes = plt.axes()
# axes.grid(which="major")
# axes.grid(which="minor", linestyle=":")
# plt.setp( axes.get_xticklabels(), visible=False)
# plt.setp( axes.get_yticklabels(), visible=False)
plt.plot(x,y, linestyle="-.", marker="o", color="red", markerfacecolor="blue")
plt.tick_params(labelbottom="false", labelleft="false", colors="blue")
plt.minorticks_on()
plt.grid(which="major", linestyle="-", linewidth="0.5")
plt.grid(which="minor", linestyle=":", linewidth="0.5")
plt.show()
