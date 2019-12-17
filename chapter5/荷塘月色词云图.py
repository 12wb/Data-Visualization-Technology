import pandas as pd
import numpy as np
from wordcloud import WordCloud
import jieba
import cv2 as cv

with open('text.txt', 'r', encoding='utf-8') as f:
    df = " ".join(f.readlines())

#适用结巴进行分词
data = jieba.lcut(str(df), cut_all=True)
print(data)

#读取停用词表
with open('停用词表.txt', 'r', encoding="UTF-8") as file1:  # with as操作读取文件很ok
    content = "".join(file1.readlines())
    print(content)

result = '' # 待返回字符串
for word in data:
    if word not in content:
        result += word + " "

img = cv.imread('hehua.jpg')
wc = WordCloud(font_path="C:\Windows\Fonts\simkai.ttf",mask=img, background_color="white", max_words=100, max_font_size=100) # 生成词云图
wc.generate("".join(result))
wc.to_file('wordCloudPic4.png')