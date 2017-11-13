# 极坐标图
# 有三种：线状极坐标图/柱状极坐标图/气泡极坐标。
# http://www.cnblogs.com/arnoldlu/p/7553978.html
# 演示柱状极坐标图

import matplotlib.pyplot as plt
import numpy as np


# Compute areas and colors
N = 150

fig, ax = plt.subplots()
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta

ax = plt.subplot(111, projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

fig.set_size_inches(10, 10)
plt.show()
