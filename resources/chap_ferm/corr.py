from mpl_toolkits.axisartist import SubplotZero
import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos

def f(x):
	return 1-9*(sin(x)-x*cos(x))**2/(x**6)

fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
	ax.axis[direction].set_axisline_style("->")
	ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
	ax.axis[direction].set_visible(False)

ax.axis["yzero"].set_axis_direction("top")
ax.axis["xzero"].label.set_text(r'$k_Fr$')
ax.axis["yzero"].label.set_text(r'$C_{\sigma\sigma}/\rho_0^2$')
ax.set_xticks(range(-8,9,2))
ax.set_ylim(0,1.1)
ax.set_yticks(np.arange(0.2,1.1,0.2))
t= np.concatenate([np.arange(-8, 0, 0.002),np.arange(0.002, 8.002, 0.002)])
ax.plot(t, np.array(list(map(f,t))), 'k')
plt.show()
print(max(np.array(list(map(f,t)))))