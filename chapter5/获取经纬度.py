import requests
import pandas as pd
import time
import json

df=pd.read_csv("链家北京租房数据.csv",engine='python')
df=df.drop_duplicates()
#删除缺失值
df=df.dropna()
df['位置']='北京市'+df['区域'].values+'区'+df['小区名称'].values
class LngLat:
    # 获取位置一列的数据
    def get_data(self):
        house_names = df['位置']
        house_names = house_names.tolist()
        return house_names
    def get_url(self):
        #url_temp = "http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak=NGbGbeh6U4mUGrQK5yAxfRd4lZ6Fr6jW&callback=showLocation"
        url_temp="http://api.map.baidu.com/geocoding/v3/?address={}&output=json&ak=KTCEBrF2I3r4g3A94hcXB771K6PosaQE&callback=showLocation"
        house_names = self.get_data()
        data=[url_temp.format(i) for i in house_names]
        return data
    # 发送请求
    def parse_url(self, url):
        while 1:
            try:
                r = requests.get(url)
            except requests.exceptions.ConnectionError:
                time.sleep(2)
                continue
            return r.content.decode('UTF-8')
    def run(self):
        li = []
        urls = self.get_url()
        for url in urls:
            print(url)
            data = self.parse_url(url)
            print(data)
            str = data.split("{")[-1].split("}")[0]
            try:
                lng = float(str.split(",")[0].split(":")[1])
                lat = float(str.split(",")[1].split(":")[1])
            except ValueError:
                continue
            # 构建字典
            dict_data = dict(lng=lng, lat=lat, count=1)
            li.append(dict_data)
        f = open(r'经纬度信息.txt', 'w')
        f.write(json.dumps(li))
        f.close()
        print('正在写入...')
        print('写入成功')
if __name__ == '__main__':
    execute = LngLat()
    execute.run()
#平均租金分析   租金/面积
# df_all=pd.DataFrame({'区域':df['区域'].unique(),'房租总金额':[0]*13,'面积(㎡)':[0]*13})
# sum_price=df['价格(元/月)'].groupby(df['区域']).sum()
# sum_area=df['面积(㎡)'].groupby(df['区域']).sum()
# print(sum_price)
# print(sum_area)