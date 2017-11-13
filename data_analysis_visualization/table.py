
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


df = pd.DataFrame(np.random.rand(4, 3), columns=list('abc'))

fig, ax = plt.subplots()
ax.table(cellText=df.values, colLabels=df.columns, loc='center')
ax.axis('off')

plt.show()
