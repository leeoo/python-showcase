# 柱图（少数分类）
# API: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


opacity = 0.8
data = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
print('data: ', data)

fig, ax = plt.subplots()
index = range(len(data))
print('index: ', index)

plt.subplot(4, 1, 1)
plt.bar(index, data['a'])

plt.subplot(4, 1, 2)
plt.bar(index, data['a'], alpha=opacity, width=0.2)
plt.bar([i+0.2 for i in index], data['b'], alpha=opacity, width=0.2)
plt.bar([i+0.4 for i in index], data['c'], alpha=opacity, width=0.2)
plt.bar([i+0.6 for i in index], data['d'], alpha=opacity, width=0.2)

fig.set_size_inches(40, 32)
plt.xticks(index, list('thisisabar'))
plt.show()
