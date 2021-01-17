from matplotlib import pyplot as plt
import random

#设置中文显示
plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#数据准备
citys = ["上海", "北京","广州","深圳","杭州","成都","重庆","厦门","福州"]
data = [random.randint(0, 100) for i in range(len(citys))] 
#设置图画大小
plt.figure(figsize = (20, 20))
#绘制条形图
plt.bar(citys, data)


#绘制图形
plt.show()
