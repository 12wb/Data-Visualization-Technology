# coding:gbk
import pyecharts.options as opts
from pyecharts.faker import  Faker
from pyecharts.charts import Line,Bar
import numpy as np
import pandas as pd
df = pd.read_csv('beijing2018AQI.csv',encoding='gbk')
data = pd.DataFrame({'Date':df['Date'],'平均AQI':df['AQI']})
# print(data['Date'])
# 平均数
merage_A = data['平均AQI'].groupby(data['Date']).mean()

attr = ["{}".format(str(i)+'月') for i in range(1,13)]

line = (
    Line()
    .add_xaxis(attr)
    .add_yaxis('月均',merage_A)
    .set_global_opts(
        title_opts=opts.TitleOpts(title='2018北京AQI月均走势图')
    )

)
line.render('AQI月均图.html')
