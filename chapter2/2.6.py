import pandas as pd
df = pd.read_csv('地区信息.csv',engine='python')
print(df)
# 分组
datagroup = df.groupby('省级单位')
print(datagroup)
# 遍历分组
for i in datagroup:
    print(i)

# 第二种方法取得每组数据
data = dict([i for i in datagroup])['北京']
print(data)


import pandas as pd
import numpy as np
data_frame=pd.DataFrame(np.arange(36).reshape((6,6)),columns=list('abcdef'))
data_frame['key']=pd.Series(list('aaabbb'),name='key')
#分组
data_group=data_frame.groupby('key')
#使用agg方法聚合
print(data_group.agg(np.sum))


