# 比较
# 表格（许多项目）

# http://www.cnblogs.com/arnoldlu/p/7553978.html

# 注意：原文中的代码运行后并不能显示table，需要将ax.table()方法中的animated=True去掉！！！而且行label也显示不出来！
# 因为可以在Matplotlib 2.x源码中看到这个方法中并没有animated参数，但是Maplotlib 2.x文档中的确有这个参数。

import matplotlib.pyplot as plt
import numpy as np

col_labels = ['col1', 'col2', 'col3']
row_labels = ['row1', 'row2', 'row3']
row_colors = ['red', 'gold', 'green']

table_vals = np.random.randn(3, 3)
print('table_vals: ', table_vals)

fig, ax = plt.subplots()
my_table = ax.table(cellText=table_vals,
                    colWidths=[0.5]*3,
                    rowLabels=row_labels,
                    colLabels=col_labels,
                    rowColours=row_colors,
                    colColours=row_colors,
                    loc='center'
                    # ,
                    # animated=True
                    )
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.axis('off')
fig.set_size_inches(10, 10)
plt.show()
