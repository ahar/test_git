#!/usr/bin/env python3

# import numpy as np
# from mpl_toolkits.axes_grid1 import host_subplot
# import mpl_toolkits.axisartist as AA
# import matplotlib as mp
# import matplotlib.pyplot as plt

x_data = [0, 100, 200, 350, 500, 600, 700, 800, 900, 1000]
y_data_1 = [0, 0.09, 0.11, 0.106, 0.112, 0.12, 0.127, 1285, 0.13, 0.13]

# y_data_2 = [91.5, 90.45, 90.5, 90.1, 89.8, 89.65, 89.5, 89.45, 89.4, 89.4]

# host = host_subplot(111, axes_class=AA.Axes)
# plt.subplots_adjust(right=0.75)

# par1 = host.twinx()
# par2 = host.twinx()

# offset = 92
# new_fixed_axis = par2.get_grid_helper().new_fixed_axis
# par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
#                                         offset=(offset, 0))

# par2.axis["right"].toggle(all=True)

# host.set_xlim(0, 2)
# host.set_ylim(0, 2)

# host.set_xlabel("Distance")
# host.set_ylabel("v(m/sec)")
# par1.set_ylabel("Temperature")


# p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
# p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")


# par1.set_ylim(0, 4)
# par2.set_ylim(1, 65)

# host.legend()

# host.axis["left"].label.set_color(p1.get_color())
# par1.axis["right"].label.set_color(p2.get_color())
# par2.axis["right"].label.set_color(p3.get_color())

# plt.draw()
# plt.show()

# plt.rcParams['text.usetex'] = True

# # plt.rcParams.update({
# #     "text.usetex": True,
# #     "font.family": "sans-serif",
# #     "font.sans-serif": ["Helvetica"]})

# # plt.subplot()
# # plt.plot()
# fig, ax = plt.subplots()
# N = 500
# delta = 0.6
# X = np.linspace(-1, 1, N)
# ax.plot(X, (1 - np.tanh(4 * X / delta)) / 2,    # phase field tanh profiles
#         X, (1.4 + np.tanh(4 * X / delta)) / 4, "C2",  # composition profile
#         X, X < 0, "k--")                        # sharp interface

# # ax.plot(x_data, y_data_2)
# ax.set_ylabel(r"\phi (rad)")
# ax.set_xlabel("time")
# # plt.axis()
# # plt.xlabel('v(m/sec)')
# # plt.ylabel(r"\Tex\ $\phi$")
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True


fig, ax = plt.subplots()
# interface tracking profiles
# N = 500
# delta = 0.6
# X = np.linspace(-1, 1, N)
# ax.plot(X, (1 - np.tanh(4 * X / delta)) / 2,    # phase field tanh profiles
        # X, (1.4 + np.tanh(4 * X / delta)) / 4, "C2",  # composition profile
        #  "k--")                        # sharp interface
ax.scatter(x_data, y_data_1)
# legend
# ax.legend(("phase field", "level set", "sharp interface"),
        #   shadow=True, loc=(0.01, 0.48), handlelength=1.5, fontsize=16)

# the arrow
# ax.annotate("", xy=(-delta / 2., 0.1), xytext=(delta / 2., 0.1),
            # arrowprops=dict(arrowstyle="<->", connectionstyle="arc3"))
# ax.text(0, 0.1, r"$\delta$",
#         color="black", fontsize=24,
#         horizontalalignment="center", verticalalignment="center",
#         bbox=dict(boxstyle="round", fc="white", ec="black", pad=0.2))

# Use tex in labels
ax.set_xticks([-1, 0, 1])
ax.set_xticklabels(["$-1$", r"$\pm 0$", "$+1$"], color="k", size=20)

# Left Y-axis labels, combine math mode and text mode
ax.set_ylabel(r"\bf{phase field} $\phi$", color="C0", fontsize=20)
ax.set_yticks([0, 0.5, 1])
ax.set_yticklabels([r"\bf{0}", r"\bf{.5}", r"\bf{1}"], color="k", size=20)

# Right Y-axis labels
# ax.text(1.02, 0.5, r"\bf{level set} $\phi$",
#         color="C2", fontsize=20, rotation=90,
#         horizontalalignment="left", verticalalignment="center",
#         clip_on=False, transform=ax.transAxes)

# Use multiline environment inside a `text`.
# level set equations
# eq1 = (r"\begin{eqnarray*}"
    #    r"|\nabla\phi| &=& 1,\\"
    #    r"\frac{\partial \phi}{\partial t} + U|\nabla \phi| &=& 0 "
    #    r"\end{eqnarray*}")
# ax.text(1, 0.9, eq1, color="C2", fontsize=18,
        # horizontalalignment="right", verticalalignment="top")

# phase field equations
# eq2 = (r"\begin{eqnarray*}"
    #    r"\mathcal{F} &=& \int f\left( \phi, c \right) dV, \\ "
    #    r"\frac{ \partial \phi } { \partial t } &=& -M_{ \phi } "
    #    r"\frac{ \delta \mathcal{F} } { \delta \phi }"
    #    r"\end{eqnarray*}")
# ax.text(0.18, 0.18, eq2, color="C0", fontsize=16)

# ax.text(-1, .30, r"gamma: $\gamma$", color="r", fontsize=20)
# ax.text(-1, .18, r"Omega: $\Omega$", color="b", fontsize=20)

plt.show()