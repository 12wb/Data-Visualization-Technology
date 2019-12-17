import pandas as pd
df = pd.read_csv('风景名胜区.csv',engine='python')
print(df)
# print(type(df))
# print(df.size)
# print(df.shape)

# 需要前五行数据
print(df.head())
# 选出后五条数据
# print(df.tail())
# 选出姓名这列的数据
# print(df['姓名'])
# 选出所有的出生年份(年)
# print(df.loc[:,'出生年份（年）'])
# 选出所有的"姓名"和"出生年份"这俩列数据
# print(df.loc[:,['姓名','出生年份（年）']])
# 选出所有的"姓名"和"出生年份"这俩列前五行数据
# print(df.loc[0:4,['姓名','出生年份（年）']])
# print(df.loc[:,['姓名','出生年份（年）']].head())

# 选出体重大于75kg的运动员的姓名
#print(df.loc[df['体重(kg)']>75,'姓名'])


# 使用iloc选出姓名
# print(df.iloc[:,0])

# 使用iloc选出姓名和性别
#print(df.iloc[:,[0,1]])

# 使用iloc选出姓名和性别前两行
#print(df.iloc[0:2],0,1)



# 在DataFrame里面中增加一列
# df['身价'] = 100000
# print(df)
# df.to_csv("新体重运动员.csv") # 存入csv文件
#
#
#
#
#
# area = pd.Series({'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'Illinois': 149995})
# pop = pd.Series({'California': 38332521, 'Texas': 26448193, 'New York': 19651127, 'Florida': 19552860, 'Illinois': 12882135})
# data = pd.DataFrame({'area':area, 'pop':pop})
# print(data)
# #增加一列数据
# data['人口密度']=data['pop']/data['area']
# print(data)
# # 删除“人口密度”数据
# data.drop(labels='人口密度',axis=1,inplace=True)
# print(data)
#
#
#
# import pandas as pd
# import numpy as np
#
# arr = input()
# dates = pd.date_range('20190101', periods=25) # 生成时间序列
# df = pd.Series(eval(arr),index=dates)