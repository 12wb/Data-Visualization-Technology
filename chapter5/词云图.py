# coding:gbk
import jieba     # ���ķִ�
from wordcloud import WordCloud  # ����չʾ��
import itchat   # ΢�ſ�
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

with open('ͣ�ôʱ�.txt',encoding='utf-8') as  f:
    stopword = f.read()
    # print(stopword)
# ��ȡcsv�ļ�
data = pd.read_csv('��Ʒ������Ϣ.csv',engine='python')
# print(data)

# ���ݴ���
# print(data.drop_duplicates())
# print(data.dropna(inplace=True))

# ��DataFrameתΪ�ַ���
# �ִ�
info = jieba.lcut(str(data['������Ϣ'].values),cut_all=True)
# print(info)

# ���õ���info��ͣ�ôʱ�ȥ��ѯ��������ڣ�����
result=[]
for word in info:
    if word  in stopword:
        result.append(word)
# print(result)
# ���ӻ�,ʹ��wordcloud
image = np.array(Image.open('heinan.jpg'))
font = 'C:\Windows\Fonts\simkai.ttf'
w = WordCloud(scale=18,mask=image,font_path=font,background_color='white')
w = w.generate(''.join(result))     # result(list)->str
plt.imshow(w)
plt.axis('off')
plt.show()


