import numpy as np
import pandas as pd
'''
# data = pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
# print(data)
# print(data['a'])  # 取得'aSeries'索引对应的值

# 通过字典创建Series
dic = {'first':0.25,"sencond":0.5}
data = pd.Series(dic)  # 字典的键作为索引
print(data)

# 得到Series的索引和值
print(data.index)
print(data.values)
'''


'''
strl = 'a b c d e f'
str2 = strl.split(" ")
print(str2)
'''


# 创建DataFrame对象
# 第一种方式数组创建DataFrame对象
data = pd.DataFrame([['一年级',25,15],['二年级',23,17],['三年级',27,20],['四年级',30,20]],
                    index=['0','1','2','3'],columns=['班级','男生人数','女生人数'])
print(data)


# 第二种方式Series创建
data1 = pd.Series(['一年级','二年级','三年级','四年级'])
data2 = pd.Series([25,25,25,25])
data3 = pd.Series([15,15,15,25])
df2 = pd.DataFrame({"班级":data1,"男生人数":data2,"女生人数":data3})
print(df2)
