df = pd.read_csv(".\数据源\地区信息.csv",encoding="gbk")
group = df.groupby(by="省级单位")
# 防止乱码
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
df = dict([i for i in group])["天津"]
x = df["GDP（亿元）"]
y = df["地级单位"]
# print(x,y)
plt.pie(x,labels=y,autopct='%1.1f')
plt.show()
print(df["县级单位"])
print(df)
d = df["GDP（亿元）"]

new_df = pd.DataFrame({"省级单位":df["省级单位"],"GDP（亿元）":df["GDP（亿元）"],
"地级单位":df["地级单位"]})
print(new_df)
plt.pie()
labels = 'A','B','C','D'
x = df["GDP（亿元）"]
lables = df["地级单位"]
plt.pie(x,lables=lables)
plt.show()

