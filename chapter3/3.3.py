from pyecharts.charts import Line,Bar
import pyecharts.options as opts
from pyecharts.faker import Faker  # 生成伪数据

line9 = Line()
line9.add_xaxis(Faker.choose())  # 添加x轴上的数据
line9.add_yaxis('price',Faker.values())
line9.set_global_opts(title_opts=opts.TitleOpts(title="Line阶梯图"))

line9.render('pyecharts-line.html')  #生成网页文件，如果括号里面不给参数，生成的是render.html

bar = Bar()
bar.add_xaxis(["1月","2月","3月","4月","5月","6月"])
bar.add_yaxis("商家A裤子销量",[200,300,280,300,290,270])
bar.set_global_opts(title_opts=opts.TitleOpts(title="柱状图"))
bar.render()


