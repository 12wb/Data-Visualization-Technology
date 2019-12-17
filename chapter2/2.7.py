import pandas as pd
import numpy as np
df = pd.read_csv('附件.csv',engine='python')
# print(df)
# 是否有缺失值
print(df.isnull().sum())
# print(df.info())
print(df.dropna(inplace=True))
print(df.duplicated())  # 看到TRUE说明有重复值的存在
# print(df.shape)
print(df.drop_duplicates(inplace=True))
print(df.shape)
# 选出销售金额这一列
df['销售金额'] = round(df['销售数量']*df.loc[:,'商品单价'],2)
print(df['销售金额'])
# 统计大类中商品销售金额
print(df['大类名称'].value_counts()) # value_counts统计值得数目
group = df.groupby(by='大类名称')['销售金额'].sum()
group1 = df.groupby(by='大类名称')['销售金额'].agg(np.sum)
print(group)
print(group1)
# 自定义求极差值的函数
def range_data_group(arr):
    return arr.max() - arr.min()
group2 = df.groupby(by='大类名称')['销售金额'].agg(range_data_group)
print(group2)

dict = {'销售数量':[np.max],'销售金额':[np.mean]}
group3 = df.groupby(by='大类名称').agg(dict)  # agg聚合函数
print(group3)


# for i,j in group:
#     print(i,j)  # 每组的组名，比如休休闲，文体


