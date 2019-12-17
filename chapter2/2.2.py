import pandas as pd
df = pd.read_csv('huizong.csv',encoding="utf-8")
print(df)
# 使用loc切片方式获取品牌和评论俩列数据
# print(df.loc[:,['品牌','评论']])
print(df.iloc[:,[4,5]])
print(df.iloc[:,4:6])
# 得到电热水器为"美的"的所有评论数据
print(df.loc[df['品牌']=='美的','评论'])
