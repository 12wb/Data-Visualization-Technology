import pandas as pd

mysql = [{'city': 'BeiJing', 'user_id': 1},
 {'city': 'NanJing', 'user_id': 2},
 {'city': 'BeiJing', 'user_id': 3},
 {'city': 'TianJin', 'user_id': 4}]

mongodb = [{'page_click_count': 20, 'user_id': 1},
 {'page_click_count': 38, 'user_id': 2},
 {'page_click_count': 10, 'user_id': 3}]

oracle = [{'id': 4, "page_click_count": 18, "city": 'TianJin'},
       {'id': 5, "page_click_count": 5, "city": 'BeiJing'},
       {'id': 6, "page_click_count": 25, "city": 'ShangHai'},
       {'id': 7, "page_click_count": 16, "city": 'GuangZhou'},
       {'id': 8, "page_click_count": 19, "city": 'ChangSha'},
       {'id': 9, "page_click_count": 50, "city": 'HangZhou'}]

# print(mysql)
# def demo2(self,dataset1,dataset2,dataset3):
    # ********** Begin **********#

dataset1 = pd.DataFrame(mysql)
dataset2 = pd.DataFrame(mongodb)
# print(dataset2)
dataset3 = pd.DataFrame(oracle)
df = dataset3.rename(columns={'id':'user_id'},inplace=True)   # 重命名列名
# print(df)

df1 = pd.merge(dataset1,dataset2,on='user_id',how='outer')  # 全连接
df2 = pd.concat([df,df1],axis=0)  # 纵向堆叠
print(df2)


