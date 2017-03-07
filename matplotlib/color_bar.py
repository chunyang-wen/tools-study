import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

women_pop = np.array([5., 30., 45., 22.])
mem_pop   = np.array([5., 25., 50., 20.])

X = np.arange(4)
plt.barh(X, women_pop, color = '.25')
plt.barh(X, -mem_pop,  color = '.75')

plt.title(sys.argv[0][:-3])

plt.savefig('/home/yang/desktop/matplot/%s.png' % (sys.argv[0][:-3]))
