import sys
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

start_date = datetime.datetime(1998, 1, 1)

def make_label(value, pos):
    time = start_date + datetime.timedelta(days = 365 * value)
    return time.strftime('%b %y')

ax = plt.axes()
ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_label))

X = np.linspace(0, 1, 256)
plt.plot(X, np.exp(-10 * X), c = 'k')
plt.plot(X, np.exp(-5 * X), c = 'k', ls = '--')

labels = ax.get_xticklabels()
plt.setp(labels, rotation = 30.)

# Display all
plt.grid(True, ls='--') # open grid
plt.axis('scaled') # 'tight'

plt.savefig('/home/yang/desktop/matplot/%s.png' % (sys.argv[0][:-3]))
