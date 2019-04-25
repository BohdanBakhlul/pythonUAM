import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors as mcolors

x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y=[0.57, 0.47, 0.80, 0.60, 0.38, 0.49, 0.35, 0.41, 0.31, 0.19, 0.12, 0.08]
for cx, cy in zip(x,y):
    rects1=plt.bar(cx, cy, color=[cy, 1, cy, 1])
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                str(height),
                ha='center', va='bottom')

autolabel(rects1)

plt.show()
