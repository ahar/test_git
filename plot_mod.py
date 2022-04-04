#!/usr/bin/env python3

from cProfile import label
from tkinter import font
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('mathtext', default='regular')
# plt.rcParams['text.usetex'] = True
# //////////////////////////////////////////////////
# plot convergence performance
# //////////////////////////////////////////////////

data = {'x_data' : np.arange(0, 1000, 100),
    'data_1' : [0.08, 0.11, 0.09, 0.106, 0.112, 0.12, 0.127, 0.1285, 0.13, 0.13],
            'data_2' : [91.2, 90.42, 90.5, 90.1, 89.8, 89.65, 89.5, 89.45, 89.4, 89.4],
            'data_3' : [0.08, 0.11, 0.1, 0.11, 0.12, 0.125, 0.128, 0.13, 0.13, 0.13],
            'data_4' : [91.2, 90.45, 90.56, 90.1, 89.8, 89.65, 89.5, 89.4, 89.4, 89.4]}

cm = 1/2.54
plt.rcParams['font.size'] = '14'
fig = plt.figure()
fig.set_figwidth(6)
fig.set_figheight(5)

ax = fig.add_subplot(111)
color = 'tab:red'
ax.set_ylim(0.08, 0.132)
ax.scatter(data['x_data'], data['data_1'], marker='s', color=color, label = "v")
ax2 = ax.twinx()
color = 'tab:blue'
ax2.scatter(data['x_data'], data['data_2'], color = color, label = r'$\phi$')

# added these three lines
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=[0.05, 0.3])

ax.grid()
ax.set_xlabel(r"Time (msec)", fontsize = 15)
ax.set_ylabel(r"v(m/sec)", fontsize = 15)
ax2.set_ylabel(r'$\phi(deg)$', fontsize = 15)

plt.tight_layout()
# plt.show()
fig.savefig('/home/anindya/reconfigurable_LIDAR_results/images/mot_1.jpg')
fig.savefig('/home/anindya/reconfigurable_LIDAR_results/images/mot_1.eps', format = 'eps')

fig1 = plt.figure()
fig1.set_figwidth(6)
fig1.set_figheight(5)
ax_1 = fig1.add_subplot(111)
color = 'tab:red'
ax_1.set_ylim(0.08, 0.132)
ax_1.scatter(data['x_data'], data['data_3'], marker='s', color=color, label = "v")
ax_12 = ax_1.twinx()
color = 'tab:blue'
ax_12.scatter(data['x_data'], data['data_4'], color = color, label = r'$\phi$')

# added these three lines
lines, labels = ax_1.get_legend_handles_labels()
lines2, labels2 = ax_12.get_legend_handles_labels()
ax_12.legend(lines + lines2, labels + labels2, loc=[0.05, 0.7])

ax_1.grid()
ax_1.set_xlabel(r"Time (msec)", fontsize = 15)
ax_1.set_ylabel(r"v(m/sec)", fontsize = 15)
ax_12.set_ylabel(r'$\phi(deg)$', fontsize = 15)

plt.tight_layout()
# plt.show()
fig1.savefig('/home/anindya/reconfigurable_LIDAR_results/images/mot_2.jpg')
fig1.savefig('/home/anindya/reconfigurable_LIDAR_results/images/mot_2.eps', format = 'eps')

# /////////////////////////////////////////////
# plot average alignment error
# /////////////////////////////////////////////