# http://www.cnblogs.com/arnoldlu/p/7553978.html
# 常用统计方法演示

import numpy as np
from scipy.stats import mode

data_list = [1, 3, 4, 23, 565, 1, -8, 123, 111, 54, 45.0, 3, 3]
array = np.array(data_list)
print('求和：', array.sum())
print('最大值：', array.max())
print('最小值：', array.min())
print('条数：', array.size)
print('标准差：', array.std(), '------------偏离平均值的幅度')
print('平均值：', array.mean())
print('中位数：', np.median(array))
print('方差：', np.var(array), '------------这组数据离散程度')
print('众数：', mode(array).mode, mode(array).count)
