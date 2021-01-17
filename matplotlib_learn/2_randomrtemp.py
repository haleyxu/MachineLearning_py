from matplotlib import pyplot as plt
import random

#设置字体
plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


temperature = [random.randint(25, 30) for i in range(120)]


fig = plt.figure(figsize = (20, 15), dpi = 40)

x = list(range(1, 121))[::4]
temperature = temperature[::4]

x_str = [f"时间{i}" for i in x] #这里出现中文不显示，是由于matplotlib的默认字体无中文

plt.plot(x, temperature)
#绘制网格 alpha:透明度
plt.grid(alpha = 0.1)
#需要显示字符串，那么显示的内容和字符串长度需要对应，则xticks需要两个参数
#rotation 旋转字符串
plt.xticks(x, x_str, rotation = 45, size = 18)

plt.xlabel("时间", size = 18)
plt.ylabel("温度", size = 18)
plt.title("温度曲线", size = 18)

plt.show()