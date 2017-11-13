# 极坐标图
# 有三种：线状极坐标图/柱状极坐标图/气泡极坐标。
# http://www.cnblogs.com/arnoldlu/p/7553978.html
# 演示气泡极坐标图

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

fig, ax = plt.subplots()

ax = plt.subplot(111, projection='polar')

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
plt.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks(np.arange(0, 2, 0.5))
ax.set_rlabel_position(-22.5)
ax.grid(True)

fig.set_size_inches(10, 10)
plt.show()
