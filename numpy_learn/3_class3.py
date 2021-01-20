import numpy as np

#需要对array中的一些值进行筛选
ar1 = np.array([[1,23,4], [2,3,5]])
print(ar1)
#bool索引
# ar1[ar1 < 5 ] = 0
# print(ar1)
# 还可以使用np.where(confidence, value1, value2)函数
# ar2 = np.where(ar1 > 2, 0, -1)
# print(ar2)
# clip()方法 用于取限制范围
print(ar1.clip(3,5))
# 赋值nan  
ar1 = ar1.astype(float)
ar1[0,0] = np.nan
print(ar1)

#行交换
ar1[[0,1],:] = ar1[[1,0],:]

#拼接
# np.vstack((A, B))
# np.hstack((A, B))

#创建特殊数组 全0 和 全1 单位矩阵
print(np.ones((2,4)))
print(np.zeros((2,4)))
print(np.eye((4)))

#numpy的随机
#种子的设置（通过设置种子可以得到一样的随机数）
np.random.seed(10)
#2r4l 的 0-1 的随机阵列
ar2 = np.random.rand(2,4)
print(ar2)
#2r4l 的 0-1 的随机阵列
#np.random.rand(2,4)

#copy 和 view

