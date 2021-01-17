from matplotlib import  pyplot as plt
import random

x_1 = list(range(1, 10))
x_2 = list(range(1, 10))

y_1 = [random.randint(0, 20) for i in range(1, 10)]
y_2 = [random.randint(0, 20) for i in range(1, 10)]


#设置字体
plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号



#线的参数设置
plt.plot(x_1, y_1, label = "线 1", color = "#191970", linestyle = "--", linewidth = 1)
plt.plot(x_2, y_2, label = "线 2", color = "cyan",linestyle = ":")
plt.xticks(x_1, [f"点{i}" for i in x_1], rotation = 45)
plt.title("随机折线图")
plt.xlabel("点")
plt.ylabel("随机值")

#添加图例
plt.legend()


plt.show()