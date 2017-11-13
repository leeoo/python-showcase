# http://www.cnblogs.com/arnoldlu/p/7553978.html

# 构成

# 100%堆积柱图(相对差异)

# 堆叠柱图（绝对差异）

# 堆积百分比面积图（相对差异）

# 堆积面积图（相对绝对差异）

# 饼图（占整体比例）

# API Introduction: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.pie

import matplotlib.pyplot as plt
import numpy as np

labels = 'A', 'B', 'C', 'D', 'E', 'F', 'G'
sizes = [20, 45, 68, 98, 60, 28, 99]
np.percentile()
# 大于0的项表示饼图中此项对应的块将“抽出”部分
explode = (0, 0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%.2f%%', shadow=True, startangle=90)
fig.set_size_inches(8, 8)
plt.show()

