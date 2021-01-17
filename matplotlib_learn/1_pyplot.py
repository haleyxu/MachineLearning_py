#使用matplotlib 的 pyplot模块
from matplotlib import pyplot as plt
import random 

#建立两个可迭代的对象x, y
x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

#设置图形 大小和清晰度 
# figsize:指定图像大小（长 宽）单位英寸
# dpi:设置清晰度
fig = plt.figure(figsize = (20, 10), dpi = 40)

#绘制图形
plt.plot(x, y)


#设置轴的分度
plt.xticks(range(2, 26, 2))
plt.yticks(range(min(y), max(y) + 1))

#绘制完成后，保存图片
#可以使用.svg格式保存成矢量图
#plt.savefig(".\Tempurature.svg")

#显示图形
plt.show()
