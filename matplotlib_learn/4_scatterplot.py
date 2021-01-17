from matplotlib import pyplot as plt
import random
#设置字体
plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#设置图片
plt.figure(figsize = (20, 20))

data1 = [random.randint(0, 20) for i in range(50)]
data2 = [random.randint(0, 20) for i in range(50)]

#绘制散点图
plt.scatter(range(50), data1, label = "室内")
plt.scatter(range(50, 100), data2, label = "室外")
#设置X axis
plt.xticks(range(100), [f"电压{i}" for i in range(100)], rotation = 90)
#设置标题
plt.xlabel("温度")
plt.ylabel("气压")
plt.title("温度-气压关系图")
#添加图例
plt.legend()


plt.show()