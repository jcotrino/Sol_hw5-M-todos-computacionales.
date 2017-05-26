import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pylab

data = open("Data.txt", "r")

fig1 = plt.figure()
ax = fig1.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[0:100,:])
fig1.savefig("Figure_1.pdf", bbox_inches="tight")

fig2 = plt.figure()
ax = fig2.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[100:200,:])
fig2.savefig("Figure_2.pdf", bbox_inches="tight")

fig3 = plt.figure()
ax = fig3.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[200:300,:])
fig3.savefig("Figure_3.pdf", bbox_inches="tight")

fig4 = plt.figure()
ax = fig4.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[300:400,:])
fig4.savefig("Figure_4.pdf", bbox_inches="tight")

fig5 = plt.figure()
ax = fig5.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[400:500,:])
fig5.savefig("Figure_5.pdf", bbox_inches="tight")

fig6 = plt.figure()
ax = fig6.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[500:600,:])
fig6.savefig("Figure_6.pdf", bbox_inches="tight")

fig7 = plt.figure()
ax = fig7.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[600:700,:])
fig7.savefig("Figure_7.pdf", bbox_inches="tight")

fig8 = plt.figure()
ax = fig8.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[700:800,:])
fig8.savefig("Figure_8.pdf", bbox_inches="tight")

fig9 = plt.figure()
ax = fig9.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[800:900,:])
fig9.savefig("Figure_9.pdf", bbox_inches="tight")

fig10 = plt.figure()
ax = fig1.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[900:1000,:])
fig10.savefig("Figure_10.pdf", bbox_inches="tight")

fig11 = plt.figure()
ax = fig11.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[1000:1100,:])
fig11.savefig("Figure_11.pdf", bbox_inches="tight")

fig12 = plt.figure()
ax = fig12.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[1100:1200,:])
fig12.savefig("Figure_12.pdf", bbox_inches="tight")

fig13 = plt.figure()
ax = fig13.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[1200:1300,:])
fig13.savefig("Figure_13.pdf", bbox_inches="tight")

fig14 = plt.figure()
ax = fig14.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[1300:1400,:])
fig14.savefig("Figure_14.pdf", bbox_inches="tight")

fig15 = plt.figure()
ax = fig15.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[1400:1500,:])
fig15.savefig("Figure_15.pdf", bbox_inches="tight")

fig16 = plt.figure()
ax = fig16.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[1500:1600,:])
fig16.savefig("Figure_16.pdf", bbox_inches="tight")

fig17 = plt.figure()
ax = fig17.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[1600:1700,:])
fig17.savefig("Figure_17.pdf", bbox_inches="tight")

fig18 = plt.figure()
ax = fig18.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[1700:1800,:])
fig18.savefig("Figure_18.pdf", bbox_inches="tight")

fig19 = plt.figure()
ax = fig19.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[1800:1900,:])
fig19.savefig("Figure_19.pdf", bbox_inches="tight")

fig20 = plt.figure()
ax = fig20.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[1900:2000,:])
fig20.savefig("Figure_20.pdf", bbox_inches="tight")

fig21 = plt.figure()
ax = fig21.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[2000:2100,:])
fig21.savefig("Figure_21.pdf", bbox_inches="tight")

fig22 = plt.figure()
ax = fig22.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[2100:2200,:])
fig22.savefig("Figure_22.pdf", bbox_inches="tight")

fig23 = plt.figure()
ax = fig23.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[2200:2300,:])
fig23.savefig("Figure_23.pdf", bbox_inches="tight")

fig24 = plt.figure()
ax = fig24.add_subplot(1, 1, 1, projection='3d')
p = ax.contour(x, y, data[2300:2400,:])
fig24.savefig("Figure_24.pdf", bbox_inches="tight")

