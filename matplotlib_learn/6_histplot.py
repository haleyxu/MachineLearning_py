import random

from matplotlib import pyplot as plt

#设置字体
plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

data_num = 1000

data = [random.randint(0, 100) for i in range(data_num)]

#计算组数
d = 5 #组距
num_group = (max(data) - min(data)) // d

#参数为数据和组数
plt.hist(data, num_group)

plt.xticks(range(min(data), max(data) + d, d))
plt.grid(alpha = 0.3)
plt.show()
