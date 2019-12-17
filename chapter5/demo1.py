import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

df=pd.read_csv("链家北京租房数据.csv",encoding='gbk')
print(df)
#去掉重复值
df.drop_duplicates(inplace=True)
print(df)
#去空值
print(pd.isnull(df).sum())#判断空值的数目
#处理"面积(㎡)"这列的数据,例如59.11平米转成59.11
data=df['面积(㎡)'].values
print(data)
elment=[]
for i in data:
    elment.append(float(i[:-2]))
print(elment)
df['面积(㎡)']=elment
#df.loc[:,'面积(㎡)']=elment
print(df)
#处理第三列“户型”，将“房间”换成"室"
el=[]
data1=df['户型'].values
for i in data1:
    el.append(i.replace("房间","室"))
df['户型']=el
print(df)

#图表分析
# quyu=df['区域'].unique()
# print(len(quyu))
new_df=pd.DataFrame({'区域':df['区域'].unique(),'房源数量':[0]*13})
print(new_df)
#如何统计每个城区的房源数量
num=df.groupby(by='区域').count()
print(num)
new_df['房源数量']=num.values
#print(new_df)
#那个区域的房源数量是最多的
new_df.sort_values(by="房源数量",ascending=False,inplace=True)
print(new_df)
#新建位置数据
df['位置']="北京市"+df['区域'].values+"区"+df['小区名称'].values
print(df)

# coding=utf-8
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
#         url_temp = "http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak=KTCEBrF2I3r4g3A94hcXB771K6PosaQE"
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
# if __name__ == '__main__':
#     execute = LngLat()
#     execute.run()
