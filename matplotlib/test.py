import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)


#plt.plot(x, y, '--*r')
plt.plot(x, y, linestyle = 'dashed', c = 'r', marker=7)

plt.savefig('/home/yang/desktop/matplot/%s.png' % (sys.argv[0][:-3]))
