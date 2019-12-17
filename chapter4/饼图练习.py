from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie
import pandas as pd

df=pd.read_csv("vote_result.csv",encoding="gbk")
def pie_base() -> Pie:
    c = (
        Pie()
        .add("", [list(z) for z in zip(df['感兴趣的领域'].values.tolist(), df['票数'].values.tolist())],
             radius=["30%", "75%"],)
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .set_global_opts(legend_opts=opts.LegendOpts(orient='vertical', pos_left='10%'))
    )
    return c
pie_base().render("饼图.html")
