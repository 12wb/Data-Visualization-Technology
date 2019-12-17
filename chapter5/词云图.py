# coding:gbk
import jieba     # 中文分词
from wordcloud import WordCloud  # 词云展示库
import itchat   # 微信库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

with open('停用词表.txt',encoding='utf-8') as  f:
    stopword = f.read()
    # print(stopword)
# 读取csv文件
data = pd.read_csv('商品评价信息.csv',engine='python')
# print(data)

# 数据处理
# print(data.drop_duplicates())
# print(data.dropna(inplace=True))

# 从DataFrame转为字符串
# 分词
info = jieba.lcut(str(data['评价信息'].values),cut_all=True)
# print(info)

# 将得到的info到停用词表去查询，如果不在，则保留
result=[]
for word in info:
    if word  in stopword:
        result.append(word)
# print(result)
# 可视化,使用wordcloud
image = np.array(Image.open('heinan.jpg'))
font = 'C:\Windows\Fonts\simkai.ttf'
w = WordCloud(scale=18,mask=image,font_path=font,background_color='white')
w = w.generate(''.join(result))     # result(list)->str
plt.imshow(w)
plt.axis('off')
plt.show()


