import numpy as np

#计算nan的个数
ar1 = np.array([[np.nan, 1, 1], [np.nan, np.nan, 4],[1,2,4]])
print(ar1)
    #利用nan != nan
print(np.count_nonzero(ar1 != ar1))
    #np.isnan()
print(np.isnan(ar1))
#nan和任何数计算均为nan


#np中常用的统计函数
ar1.sum()
ar1.sum(axis = 0)
print(ar1.sum(axis = 0))
#mean
print(ar1.mean(axis = 0))
#median
print(np.median(ar1, axis = 0))
#max
print(ar1.max(axis = 0))
#min
print(ar1.min(axis = 0))
#ptp 峰峰值
print(ar1.ptp(axis = 0))
#std 标准差
print(ar1.std(axis = 0))



