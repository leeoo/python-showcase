# 趋势
# 线图（很多日期）& 多线图（多种分类）
# API: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig, ax = plt.subplots()

plt.subplot(4, 1, 1)
data = pd.DataFrame(np.random.randn(1000, 4), columns=['x', 'y', 'z', 't'])
print('data: ', data)
index = range(len(data))
print('index: ', index)

plt.plot(index, data['x'].cumsum(), label='xxx')

plt.subplot(4, 1, 2)
plt.plot(index, data.loc[:, ['x', 'y']].cumsum())

plt.subplot(4, 1, 3)
plt.plot(index, data.loc[:, ['x', 'y', 'z']].cumsum())

plt.subplot(4, 1, 4)
plt.plot(index, data.cumsum())

fig.set_size_inches(40, 32)
plt.show()
