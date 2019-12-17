# from matplotlib import pyplot as plt
# import numpy as np
#
# # 创建图形(也可以默认的图形)
# plt.figure(figsize=(10,10),facecolor='w')
# # plt.show()
#
# # 保存
# # plt.savefig('路径')
#
# # 创建子图
# plt.subplot(2,1,1) #(行，列，子图编号)
# plt.plot([1,2,3,4],[1,2,3,4])
#
# plt.subplot(2,1,2)
# plt.plot([1,2,3,4],[1,2,3,4])
# plt.show()


import matplotlib.pyplot as plt#导入模块
plt.figure(figsize=(10,10))#创建图形,并设置大小为10 x 10
plt.subplot(2,1,1)#创建子图1（行，列，子图编号）
plt.plot([1,2,3,4], [1,2,3,4])
plt.subplot(2,1,2)#创建子图2（行，列，子图编号）
plt.plot([4,3,2,1], [1,2,3,4])
plt.show()