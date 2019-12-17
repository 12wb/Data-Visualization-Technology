import pandas as pd
import numpy as np
df = pd.read_csv('链家北京租房数据.csv',engine='python')
# print(df)
# 去掉重复值
df.drop_duplicates(inplace=True)
# print(df)
# 去空值
# print(pd.isnull(df).sum()) # 判断空值的数目
# 处理"面积(㎡)"这列的数据，例如59.11平方转成59.11
data = df['面积(㎡)'].values
# print(data)
element = []
for i in data:
    element.append(float(i[:-2]))
# print(element)
df['面积(㎡)'] = element
# df[:,'面积(㎡)'] = element
# print(df)

# 处理第三列，"户型",将"房间"换成"室"
el = []
data1 = df['户型'].values
for i in data1:
    el.append(i.replace("房间","室"))
df['户型'] = el
print(df)
# str = "59.11平方"
# print(str[:-2])
# print(type(str[:-2]))
# # 串转换为float 强转
# print(type(float(str[:-2])))

# 图表分析
# quyu = df['区域'].unique
# print(len(quyu))
new_df = pd.DataFrame({'区域':df['区域'].unique(),'房源数量':[0]*13})
print(new_df)
# 如何统计每个城区的房源数量
num = df.groupby(by='区域').count()
print(num)

new_df['房源数量'] = num.values
print(new_df)

# 哪个区域的房源数量是最多的
new_df.sort_values(by='房源数量',ascending=False,inplace=True)
print(new_df)

# 拼接区域和小区名称
df['位置'] = '北京市'+df['区域'].values+"区"+df['小区名称'].values
# print(df)
# # 合并表
# data_df = pd.merge(new_df,df)
price_df = pd.DataFrame({"区域":df["区域"].unique(),'总面积(㎡)':[0]*13})
sum_price = df['价格(元/月)'].groupby(df['区域']).sum()
print(sum_price)
price_df['总价格'] = sum_price.values
sum_area = df['面积(㎡)'].groupby(df['区域']).sum()
print(sum_price)
price_df['总面积(㎡)'] = sum_area.values
print(price_df)

price_df['平均租金'] = round(price_df['总价格']/price_df['总面积(㎡)'],2)
print(price_df)
merge_df = pd.merge(new_df,price_df)
print(merge_df)

# 绘制双Y图
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
# 设置正常显示字符
plt.rcParams['axes.unicode_minus'] = False
num = merge_df['房源数量']
price = merge_df['平均租金']
x = [i for i in range(13)]
labels = merge_df['区域'].unique().tolist()  # 将ndarray转换为list
print(labels)
# print(x)
figure = plt.figure() # 产生画布
ax1 = figure.add_subplot(111)
# 折线图、绘制平均租金
ax1.plot(x,price,"or-",label='价格')
# 绘制折线图上数据
for i,(a,b) in enumerate(zip(x,price)): #  enumerate用于遍历，i表示序号
    plt.text(a,b,price[i],color='black')
ax1.set_ylim([0,200])
ax1.set_ylabel('价格')
ax1.legend(loc='upper left')
# plt.show()

ax2 = ax1.twinx() # 生成镜面坐标
# 绘制房源数量的柱状图
ax2.bar(x,num,color='green',alpha=0.3,label='数量')
ax2.legend(loc='upper right')
ax2.set_ylim([0,2000])
ax2.set_ylabel('数量')
plt.xticks(x,labels) # 设置刻度的文字
plt.show()
#coding=utf-8
# import requests
# import pandas as pd
# import time
# import json
# class LngLat:
#     # 获取位置一列的数据
#     def get_data(self):
#         house_names = df['位置']
#         house_names = house_names.tolist()
#         return house_names
#     def get_url(self):
#         url_temp = "http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak=KTCEBrF2I3r4g3A94hcXB771K6PosaQE&callback=showLocation"
#         house_names = self.get_data()
#         return [url_temp.format(i) for i in house_names]
#     # 发送请求
#     def parse_url(self, url):
#         while 1:
#             try:
#                 r = requests.get(url)
#             except requests.exceptions.ConnectionError:
#                 time.sleep(2)
#                 continue
#             return r.content.decode('UTF-8')
#     def run(self):
#         li = []
#         urls = self.get_url()
#         for url in urls:
#             data = self.parse_url(url)
#             str = data.split("{")[-1].split("}")[0]
#             try:
#                 lng = float(str.split(",")[0].split(":")[1])
#                 lat = float(str.split(",")[1].split(":")[1])
#             except ValueError:
#                 continue
#             # 构建字典
#             dict_data = dict(lng=lng, lat=lat, count=1)
#             li.append(dict_data)
#         f = open(r'经纬度信息.txt', 'w')
#         f.write(json.dumps(li))
#         f.close()
#         print('正在写入...')
#         print('写入成功')
#         # with open(r'经纬度信息.txt','w') as f:
#         #      print(f.read())
# if __name__ == '__main__':
#     execute = LngLat()
#     execute.run()