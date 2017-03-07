import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 1024)

grid_size = (4, 2)

plt.suptitle('subplot demo')

plt.subplot2grid(grid_size, (0, 0), rowspan = 3, colspan = 1)
plt.plot(np.sin(2 * x), np.cos(0.5 * x), c = 'k', label='hah')
plt.title('plot-1')
plt.legend()

plt.subplot2grid(grid_size, (0, 1), rowspan = 3, colspan = 1)
plt.plot(np.cos(3 * x), np.sin(x), c = 'k', label='heh')
plt.title('plot-2')
plt.legend()

axes = plt.subplot2grid(grid_size, (3, 0), rowspan = 1, colspan = 3)
plt.plot(np.cos(5 * x), np.sin(7 * x), c = 'k', label='hih')
# hidden x and y axis
axes.get_xaxis().set_visible(False)
axes.get_yaxis().set_visible(False)
plt.title('plot-3')
plt.legend()

plt.tight_layout()
plt.savefig('/home/yang/desktop/matplot/%s.png' % (sys.argv[0][:-3]))

"""
another way

import numpy as np
from matplotlib import pyplot as plt

T = np.linspace(-np.pi, np.pi, 1024)
fig, (ax0, ax1) = plt.subplots(ncols = 2)
ax0.plot(np.sin(2 * T), np.cost(0.5 * T))
ax1.plot(np.cos(3 * T), np.sin(T))
plt.tight_layout()
plt.savefig('path')

"""
