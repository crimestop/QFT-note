from mpl_toolkits.axisartist import SubplotZero
import numpy as np
import matplotlib.pyplot as plt

def f(t,a):
	return (t*t-a*a)**2

fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
	ax.axis[direction].set_axisline_style("->")
	ax.axis[direction].toggle(ticks=False)
	ax.axis[direction].toggle(ticklabels=False)
	ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
	ax.axis[direction].set_visible(False)

t= np.arange(-1.5, 1.502, 0.002)
#ax.plot(t, f(t,1.0), 'k')
ax.plot(t, t*t, 'k')
plt.show()