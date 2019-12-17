# coding=gbk

from pyecharts.charts import Bar   # Line 代表折线图，Bar代表柱状图
import pyecharts.options as opts    # 选项
from  pyecharts.faker import  Faker

attr = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
A = [25,50,50.5,44.5,53.5,49,54,66,59,68,54]
B = [24,31,26,30.5,38,37,52,63,59,64.5,43]
C = [22,23.5,25.5,29.5,32,32,37,49,42,55,37]

bar = (
    Bar()
    .add_xaxis(attr)
    .add_yaxis('A',A,stack='stack1')
    .add_yaxis('B',B,stack='stack1')
    .add_yaxis('C',C,stack='stack1')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title='柱形图数据堆叠示意'))
)

bar.render('zuoye.html')


from pyecharts.charts import Bar,Scatter3D
from pyecharts.charts import Page
import pandas as pd
import csv

page = Page()
bar = Bar()
datax = []
datay = []
with open("hot-dog-places.csv") as f:
    reader = csv.reader(f)
    for datarow in reader:
        datax.append(datarow)

