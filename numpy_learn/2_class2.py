import numpy as np
from matplotlib import pyplot as plt
import random

"""
numpy 中轴axis概念
对于一维数组 有 0 axis
对于2维数组 有 0 axis 和 1 axis; e.g.(2,3) 0 axis代表行2， 1 axis代表列3
同理可得


"""
# #转置
# t1 = np.array([[1,2,3],[4,5,6]])
# print(t1)
#     #transpose()方法
# print(t1.transpose())
#     #T属性
# print(t1.T)

#numpy的数据读取
data_file_path = "./ws-ag-1.txt"
original_data = np.loadtxt(data_file_path, skiprows = 28)
# print(original_data)

#获取行和列
#取行的操作时python的基础list
#取第0行
# print(original_data[0])
#取不连续的行 numpy的操作 
# print(original_data[[0,3,5]])

#取列 original_data[r,l] 第一个是行，第二个是列,这里就可以和上面的结合，得到要的数据
potential = original_data[:,0]
current = original_data[:,1]
plt.plot(potential, current)
plt.show()
