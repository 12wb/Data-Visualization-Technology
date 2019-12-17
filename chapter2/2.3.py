import pandas as pd
# 读取
df = pd.read_csv('地区信息.csv',engine='python')
# print(df)
# print(df.shape)
# # 判断是否有空值
# print(df.isnull(df).sum())
# # 检测非空值的数目
# print(df.notnull(df).sum())
# # 删除法处理
# len1 = len(df)
# df.dropna(axis=0,inplace=True)
# len2 = len(df)
# print("删除的条数是:",len1-len2)
# 填充缺失值
a = round(df.loc[:,['常住人口（万人）']].mean(),2)  # 求平均值，并且四舍五入精确到俩位
print(a)
df.fillna(a,inplace=True)
# df.to_csv("data/新地区信息.csv")
# 重复值的检测和处理
print(df.duplicated())  # 看到TRUE说明有重复值的存在
# 做去重处理
len3 = len(df)
print(df.drop_duplicates(inplace=True))
print("删除了",len3-len(df),"重复值")