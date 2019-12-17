'''任务1：安装开发环境
代码编写：导入相关工具包，进行读取“风景名胜区.csv”文件数据，并且显示前五行数据。'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


data = pd.read_csv('风景名胜区.csv',engine='python')
print(data.head())   #  显示前五行数据
# 分组，提取湖南景点数据
# data = data.loc[data['省份']=='湖南',:]
# 按照分组筛选出湖南省景点名称和总面积数据
group = data.groupby(by='省份')
data1 =dict([i for i in group])['湖南']
print(data1)

group1 = data1.iloc[:,1:3]
print(group1)
data2 = data1['总面积(平方公里)']
# print(data2)

#自定义画布宽为10英寸、高为5英寸，绘出湖南景点总面积折线图，
#并把图形分别保存为本地文件“湖南景点总面积.jpg”
plt.figure(figsize=(10,5))
# x = np.arange(data2)
plt.plot(data2)
plt.show()
plt.savefig('湖南景点总面积.jpg')

# 读出湖南省景点游客量数据
print(data1['游客量(万人次)'])

#自定义画布宽为10英寸、高为5英寸，绘出湖南景点游客量柱状图，
#并把图形分别保存为本地文件“湖南景点游客量.jpg”
data3 = data1['游客量(万人次)']
plt.figure(figsize=(10,5))
plt.bar(range(len(data3)),data3)
plt.show()
plt.savefig('湖南景点游客量.jpg')

df = data['游客量(万人次)']
# print(df)
plt.bar(range(len(df)),df)
plt.show()


# 统计全国景点游客量前十的柱状图，截图
df2 = data.sort_values(by='游客量(万人次)',ascending=False)[:10]
print(df2)

# 统计全国景点游客量前十占比饼图（保留两位小数），截图
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
labels=df2['名称'].head(10).values
womenCount = df2['游客量(万人次)'].head(10)
explode = [0,0,0.1,0,0,0,0, 0, 0, 0] # 确定突出部分
plt.pie(womenCount, explode=explode, labels=labels, shadow=True)
plt.axis('equal')  # 用于显示为一个长宽相等的饼图
plt.show()

