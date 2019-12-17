import jieba
import itchat
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import matplotlib.colors as colors
import pandas as pd
import csv
from PIL import Image
import numpy as np

data = pd.read_csv('huizong.csv')

#  数据处理, 去除重复值
data.drop_duplicates(inplace=True)

# 分词
df = jieba.lcut(str(data['评论']), cut_all=True)

with open('t.txt', encoding='utf-8') as f:  # 读取停用词表
    stopwords = f.read()

    # 将得到的 df 到 停用词表去查询，如果不在，有意义的词保留

result = []
for word in df:
    if word not in stopwords:
        result.append(word)

#  可视化， 使用 wordcloud 库

color = ['#00FF00']
colormap = colors.ListedColormap(color)

image = np.array(Image.open('cat.png'))
font = "C:\Windows\Fonts\simkai.ttf"
wc = WordCloud(mask=image, font_path=font, colormap=colormap, background_color='white')

#   result.(list) -> str
wc = wc.generate(" ".join(result))
plt.imshow(wc)
plt.axis('off')
plt.show()
