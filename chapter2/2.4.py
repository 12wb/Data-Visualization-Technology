import pandas as pd
from sklearn import datasets

iris = datasets.load_iris().data    # 鸢尾花数据集，返回的是array
print(iris)

# 获取鸢尾花数据集的前30行
df = pd.DataFrame(iris)
#print(df)
#print(df.head(30))
a = df[:30]
print(a)
print(a - a.iloc[0])

