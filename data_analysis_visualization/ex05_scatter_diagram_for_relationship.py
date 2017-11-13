
# 联系

# 散点图(2维) & 气泡图(3维)

# 散点图和气泡图的区别就在于气泡图多了一维数据，是散点具备了不同的半径。

# API: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.scatter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


N = 100

fig, ax = plt.subplots()

data = pd.DataFrame(np.random.rand(N, 3) * 100, columns=['x', 'y', 'r'])
data['r'] = np.pi * (np.pi * data['r'] / 20) ** 2  # s is area
colors = 2 * np.pi * data['x']  # colors is value of circumference

plt.subplot(3, 1, 1)
plt.scatter(data['x'], data['y'], c=colors, s=np.pi*5**2)

plt.subplot(3, 1, 2)
plt.scatter(data['x'], data['y'], c=colors, s=data['r'])

fig.set_size_inches(10, 30)
plt.show()
