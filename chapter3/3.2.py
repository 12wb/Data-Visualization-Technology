'''
# 请编写代码绘制住宅商品房平均销售价格柱状图
import os

print(os.getcwd()) #打印出当前工作路径
import matplotlib
matplotlib.use("Agg")

#  请在此添加实现代码  #
# ********** Begin *********#
import matplotlib.pyplot as plt
from numpy import *

xstring = '2015 2014 2013 2012 2011	 \
           2010 2009 2008 2007 2006	 \
           2005 2004 2003 2002 2001	2000'

ystring = '12914 11826 12997 12306.41 12327.28 \
	        11406 10608	8378 8667.02 8052.78 \
	        6922.52	5744 4196 4336 4588	4751'

y = ystring.split()
y.reverse()
# 把列表里面的字符串转成浮点数，列表推导式
y = [float(e) for e in y]
xlabels = xstring.split()
xlabels.reverse()
x = range(len(xlabels))
plt.xticks(x, xlabels, rotation = 45)
plt.yticks(range(4000,13500,1000))
plt.ylim(4000,13500)
plt.bar(x, y, color = '#800080')
plt.savefig('1.png')
plt.show()
'''

'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
x = np.arange(6)
y = [100,200,300,400,500,600],
label = ['长沙','湘潭','株洲','衡阳','娄底','郴州']

plt.xticks(x,labels=label,rotation=45)
plt.xlim(0,6)
plt.yticks()
plt.ylim([])
plt.bar(x,y,width=0.35,alpha=0.7)
'''
# -*- coding: utf-8 -*-
import matplotlib


import matplotlib.pyplot as plt
import numpy as np


xstring = '2015 2014 2013 2012 2011	 \
           2010 2009 2008 2007 2006	 \
           2005 2004 2003 2002 2001	2000' #x轴标签

n = 6
ystring = ['']*n #y轴对应的6组数据
ystring[0] = '6793	6324	6237	5790.99	5357.1	5032	4681	3800	3863.9	3366.79	3167.66	2778	2359	2250	2170	2112'
ystring[1] = '6473	5933	5850	5429.93	4993.17	4725	4459	3576	3645.18	3119.25	2936.96	2608	2197	2092	2017	1948'
ystring[2] = '15157	12965	12591	11460.19	10993.92	10934	9662	7801	7471.25	6584.93	5833.95	5576	4145	4154	4348	4288'
ystring[3] = '12914	11826	12997	12306.41	12327.28	11406	10608	8378	8667.02	8052.78	6922.52	5744	4196	4336	4588	4751'
ystring[4] = '9566	9817	9777	9020.91	8488.21	7747	6871	5886	5773.83	5246.62	5021.75	3884	3675.14	3488.57	3273.53	3260.38'
ystring[5] = '4845	5177	4907	4305.73	4182.11	4099	3671	3219	3351.44	3131.31	2829.35	2235	2240.74	1918.83	2033.08	1864.37'

labels = ['Commercial housing', 'Residential commercial housing',
          'high-end apartments', 'Office Building', 'Business housing', 'Others'] #图例标签
colors = ['#ff7f50', '#87cefa', '#DA70D6', '#32CD32', '#6495ED', '#FF69B4'] #指定颜色

xstring = '2015 2014 2013 2012 2011 2010 2009 2008 2007 2006' \
           '	 2005 2004 2003 2002 2001	2000'
xstring1 = xstring.split()
xstring1.reverse()

x = np.arange(1,n*len(xstring1),n)
plt.xlim([-1,98])
bar_wdith = 0.8
for i in range(n):
    y=ystring[i].split()
    y.reverse()
    y=[float(x) for x in y]
    plt.bar(x+i*bar_wdith,y,bar_wdith,color=colors[i])
plt.ylim([1450,15300])
plt.yticks(range(1450,15300,2000))

plt.ylim([1450,15300])    # y轴范围
plt.yticks(range(2000,15300,2000))     # 刻度
plt.xticks(x+bar_wdith*2.5 ,xstring1,rotation=45)
plt.legend(loc='upper left',labels=labels)  # 图例
plt.title('Selling Prices of Six Types of Housing')
plt.show()
