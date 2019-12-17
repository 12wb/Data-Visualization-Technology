import  pandas  as pd
df=pd.read_excel('1.xlsx')
data=df.head()#默认读取前5行的数据
print("获取到所有的值:\n{0}".format(data))#格式化输出

#导入读取Excel的库
import xlrd
#导入需要读取Excel表格的路径
data = xlrd.open_workbook('1.xlsx')
table = data.sheets()[0]
y=''
#将列的值存入字符串
y=table.col_values(2)#读取列的值
#导入pyechats库
from pyecharts import Bar
import numpy as np
t=np.linspace(1,3,len(y))#等间隔取值
bar=Bar("电影名称","电影分数")#主副标题
bar.add("豆瓣电影排名",t,y,is_more_utils=True)#标题
bar.show_config()#展示HTML源代码
bar.render("movie_bar.png")