# 极坐标图
# 有三种：线状极坐标图/柱状极坐标图/气泡极坐标。
# http://www.cnblogs.com/arnoldlu/p/7553978.html
# 演示线状极坐标图

import numpy as np
import matplotlib.pyplot as plt

# Compute pie slices
N = 20
fig, ax = plt.subplots()
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)

# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)

fig.set_size_inches(10 , 10)
plt.show()
