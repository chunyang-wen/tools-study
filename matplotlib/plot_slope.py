import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def plot_slope(X, Y):
    Xs = X[1:] - X[:-1]
    Ys = Y[1:] - Y[:-1]
    plt.plot(X[1:], Ys / Xs)

x = np.linspace(-3, 3, 100)
y = np.exp(-x ** 2)

plt.plot(x, y)
plot_slope(x, y)

plt.savefig('/home/yang/desktop/matplot/%s.png' % (sys.argv[0][:-3]))
