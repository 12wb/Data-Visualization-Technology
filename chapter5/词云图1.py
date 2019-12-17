# coding:gbk
import jieba     # 中文分词
from wordcloud import WordCloud  # 词云展示库
import itchat   # 微信库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

data = pd.read_csv('商品评价信息.csv',engine='python')

#  数据处理, 去除重复值
data.drop_duplicates(inplace=True)

# 分词
df = jieba.lcut(str(data['评价信息']), cut_all=True)

# 使用停用词表过滤无用的词

with open('停用词表.txt', encoding='utf-8') as f:  # 读取停用词表
    stopwords = f.read()

# 将得到的 df 到 停用词表去查询，如果不在，有意义的词保留

result = []
for word in df:
    if word not in stopwords:
        result.append(word)

#  可视化， 使用 wordcloud 库

image = np.array(Image.open('heinan.jpg'))
font = "C:\Windows\Fonts\simkai.ttf"
wc = WordCloud(mask=image, font_path=font, background_color='white')

#   result.(list) -> str
wc = wc.generate(" ".join(result))
plt.imshow(wc)
plt.axis('off')
plt.show()

