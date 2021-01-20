import numpy as np
import random

#np的数组类型
t1 = np.array([1, 2, 3])
print(t1)
print(type(t1))

#np arange()
t2 = np.arange(1, 9)
print(t2)
print(type(t2))

"""
数据类型代码
    类型            代码
bool                bool
int8    uint8      i8  u8           
int16   uint16     i16  u16
int32   uint32     i32  u32
int64   uint64     i64  u64
float16             f2  
float32             f4
flaot64             f8
float128            f16

complex64           c8
"""


#查看数组内的数据类型
print(t2.dtype)

#设置array中的数据类型
t3 = np.array(range(0, 10), dtype = "i1")
print(t3.dtype)

#调整数据类型
t4 = t3.astype("int64")
print(t4.dtype)

#np的小数
t5 = np.array([random.random() for i in range(10)])
print(t5)
#截取小数位 （返回）
t6 = np.round(t5, 2)
print(t6)

#数组的形状
t7 = np.arange(10)
print(t7)
print(np.shape(t7)) #一维数组

t8 = np.array([[i for i in range(10)], [i**2 for i in range(10)]])
print(t8)
print(np.shape(t8)) #二维维数组

#修改数组形状
t9 = np.array([i for i in range(9)])
print(f"t9:{t9}")
t9 = t9.reshape((3, 3))
print(f"after t9:{t9}")

t10 = np.arange(24).reshape(3,2,4)
print(f"after t10:{t10}")

#高维数组转一维数组 flatten 方法
t10 = t10.flatten()
print(f"flatten t10:{t10}")

#当多维的array与单个数操作时会作用在每个元素上
#对除0的机制
print(t9 / 0)


#np的广播原则
#1*3
ar1 = np.arange(1,4)
#2*3
ar2 = np.arange(6).reshape((2,3))
#4*3
ar3 = np.arange(12).reshape((4,3))
print(f"ar1:{ar1}\n"+
      f"ar2:{ar2}\n"+
      f"ar3:{ar3}")

#ar1 can compute with any 
print(f"ar2 + ar1: {ar2 + ar1}")
print(f"ar3 + ar1: {ar3 + ar1}")
#ar2 and ar3 can not compute
print(ar2 + ar3)