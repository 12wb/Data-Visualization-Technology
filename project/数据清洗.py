import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fdg
from tkinter import messagebox as mgb

import threading

import time

import os

class A:
    # 初始化
    def __init__(self):
        # 设置读取数据pd.read_csv()函数的默认参数
        self.sep = ','
        self.header = 'infer'
        self.encoding = 'utf-8'

        # 建立第一个显示的窗口
        self.root = tk.Tk()
        self.root.title('数据清洗')
        self.root.resizable(width=False, height=False)

        # 设置窗口居中
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (400, 110, (width-400)/2, (height-110)/2))

        # 创建路径输入口
        f = tk.Frame(self.root)

        tk.Label(f, text='路径：', font=('黑体', 15)).grid(row=0, column=0)
        self.ent = tk.Entry(f, width=40)

        scrollbar = tk.Scrollbar(f, orient=tk.HORIZONTAL, command=self.ent.xview)
        self.ent.configure(xscrollcommand=scrollbar.set)

        self.ent.grid(row=0, column=1, ipady=3)
        scrollbar.grid(row=1, column=1, sticky=tk.EW)

        f.pack()

        # 设置按钮
        f1 = tk.Frame(self.root)

        tk.Button(f, text='设'+'\n'+'置', height=1, width=2, command=self.Set_Up_The).grid(row=0, column=2, ipady=3, padx=3)

        tk.Button(f1, text='选择文件', font=('黑体', 14), command=self.import_data, width=8).grid(row=0, column=0, padx=55)
        tk.Button(f1, text='确认', font=('黑体', 14), command=self.conflrm_d, width=8).grid(row=0, column=1, padx=55)

        f1.pack(pady=8)

        self.root.columnconfigure(0, weight=1)  # 相当于开启填充模式，ttk.Treeview这个函数会占满空间,导致root空间不够（默认不填充的）
        self.root.mainloop()

    # 设置
    def Set_Up_The(self):
        def affirm_1():

            # self.sep赋值
            if len(sep.get()) > 0:
                self.sep = sep.get()

            # self.header赋值
            if len(header.get()) > 0:
                try:
                    if header.get() != 'None':
                        self.header = int(header.get())

                    else:
                        self.header = header.get()

                except:
                    mgb.showwarning('提示', 'header：请输入正整数 或 "None"')

            # self.encoding赋值
            if len(encoding.get()) > 0:
                self.encoding = encoding.get()

            root.destroy()

        def cancel_1():
            root.destroy()

        def reset_1():
            try:
                self.sep = ','
                self.header = 'infer'
                self.encoding = 'utf-8'

            except:
                mgb.showwarning('提示', '未知错误')

            else:
                mgb.showwarning('提示', '重置成功')

        root = tk.Toplevel(self.root)
        root.title('设置')
        root.resizable(False, False)
        root.grab_set()

        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (450, 260, (width - 450) / 2, (height - 260) / 2))

        # 设置self.sep
        f = tk.Frame(root)
        f.grid(row=0, column=0, ipady=5)
        tk.Label(f).grid(row=0, column=0, ipadx=18)
        tk.Label(f, text='sep：', font=('黑体', 20)).grid(row=0, column=1, ipadx=3)
        tk.Label(f, text='(从指定行开始读取数据)').grid(row=1, column=1, sticky=tk.N+tk.W)

        sep = tk.Entry(root, width=20, font=('黑体', 15))
        sep.grid(row=0, column=1, ipady=5)

        # 设置self.header
        f1 = tk.Frame(root)
        f1.grid(row=1, column=0, ipady=5)
        tk.Label(f1).grid(row=0, column=0, ipadx=18)
        tk.Label(f1, text='header：', font=('黑体', 20)).grid(row=0, column=1, ipadx=3)
        tk.Label(f1, text='(跳过数据的前几行)').grid(row=1, column=1, sticky=tk.N + tk.W)

        header = tk.Entry(root, width=20, font=('黑体', 15))
        header.grid(row=1, column=1, ipady=5)

        # 设置self.header
        f2 = tk.Frame(root)
        f2.grid(row=2, column=0, ipady=5)
        tk.Label(f2).grid(row=0, column=0, ipadx=18)
        tk.Label(f2, text='encoding：', font=('黑体', 20)).grid(row=0, column=1, ipadx=3)
        tk.Label(f2, text='(指定字符集类型)').grid(row=1, column=1, sticky=tk.N + tk.W)

        encoding = tk.Entry(root, width=20, font=('黑体', 15))
        encoding.grid(row=2, column=1, ipady=5)

        tk.Button(root, text='确认', font=('黑体', 14), width=10, command=affirm_1).grid(row=3, column=1)
        tk.Button(root, text='取消', font=('黑体', 14), width=10, command=cancel_1).grid(row=3, column=0)
        tk.Button(root, text='重'+'\n'+'置', font=('黑体', 14), height=2, command=reset_1).grid(row=3, column=2)

        root.mainloop()

    # 导入数据(按钮：选择文件)
    def import_data(self):
        lr = fdg.askopenfilename()
        try:
            if lr != '':
                self.ent.insert(0, lr)

        except:
            mgb.showwarning('提示', '未知错误！')

    # 连接 B类（按钮：确认）
    def conflrm_d(self):
        if len(self.ent.get()) > 0:
            try:
                f = open(self.ent.get())
                data = pd.read_csv(f, sep=self.sep, header=self.header, encoding=self.encoding)

            except:
                mgb.showwarning('提示', '请输入正确的路径' + '\n' + '请输入正确的文件(文件类型为csv)')

            else:

                time.sleep(0.2)
                self.root.destroy()

                B().read_data(data)

        else:
            mgb.showwarning('提示', '路径不能未空')

class B:
    def __init__(self):
        self.data = ''
        self.copy_data = '' # 备份数据
        self.root = ''

    def window_1(self):
        self.root = tk.Tk()
        self.root.title('数据清洗')
        self.root.resizable(width=False, height=False)

        # 设置窗口居中
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (400, 300, (width - 400) / 2, (height - 300) / 2))

        # 设置按钮
        self.t1 = tk.Button(self.root, text='显示数据', command=self.show_data, font=('黑体', 15), width=10)
        self.t1.grid(row=0, column=0, padx=12, pady=20)

        self.t2 = tk.Button(self.root, text='显示缺失值', command=self.query_missing_value, font=('黑体', 15), width=10)
        self.t2.grid(row=0, column=1, padx=12, pady=20)

        self.t3 = tk.Button(self.root, text='显示重复值', command=self.query_repeat_value, font=('黑体', 15), width=10)
        self.t3.grid(row=0, column=2, padx=12, pady=20)

        self.t4 = tk.Button(self.root, text='显示异常值', command=self.query_outliers_value, font=('黑体', 15), width=10)
        self.t4.grid(row=1, column=0, padx=12, pady=20)

        self.t5 = tk.Button(self.root, text='可视化', command=self.visualization_1, font=('黑体', 15), width=10)
        self.t5.grid(row=1, column=1, padx=12, pady=20)

        self.root.mainloop()

    # 第二个窗口
    def window_2(self, width=500, height=600):
        root = tk.Toplevel(self.root)
        root.title('显示数据')
        root.resizable(width=False, height=False)

        # 设置窗口居中
        root_width = root.winfo_screenwidth()
        root_height = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (width, height, (root_width - width) / 2, (root_height - height) / 2))

        return root

    # 滚动条
    def the_scroll_bar(self, root, treeview):
        scrollbar_x = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=treeview.xview)
        treeview.configure(xscrollcommand=scrollbar_x.set)
        treeview.grid(row=0, column=0)
        scrollbar_x.grid(row=1, column=0, sticky=tk.EW)

        scrollbar_y = ttk.Scrollbar(root, orient=tk.VERTICAL, command=treeview.yview)
        treeview.configure(yscrollcommand=scrollbar_y.set)
        treeview.grid(row=0, column=0)
        scrollbar_y.grid(row=0, column=1, sticky=tk.NS)

    # 显示多少行，多少列
    def shou_index_columns(self, root, data, ff):
        stringvar_1 = tk.StringVar(root)
        ttt = data.index.tolist()
        ttt1 = self.data.columns.tolist()
        stringvar_1.set("行：%s" % (len(ttt)) + '\n' + '列：%s' % (len(ttt1)))
        tk.Label(ff, textvariable=stringvar_1).grid(row=2, column=0)

        return stringvar_1

    # 显示页面的模型：treeview
    def show_treeview(self, root):
        title_1 = self.data.columns.tolist()
        title_1.insert(0, '标签')
        treeview = ttk.Treeview(root, columns=title_1, height=25, show='headings')

        [treeview.column(i, width="100", anchor="center") for i in title_1]
        [treeview.heading(column=i, text=i) for i in title_1]

        return treeview

    # 清空 treeview
    def empty_1(self, treeview):
        dd = treeview.get_children()
        [treeview.delete(i) for i in dd]

    # 点击部分按钮(按钮内容：取消)后，所运行的函数
    def no_1(self, root, an_niu):
        an_niu['state'] = tk.NORMAL
        root.destroy()

    # 显示指定的数据，参数：行索引，列索引，控件treeview，显示几行几列的标签
    def ok_1(self, index_1, columns_1, treeview, stringvar_1):
        index_2 = index_1.get()
        columns_2 = columns_1.get()

        # 判断用户输入的内容是多选还是单选
        def pan_duan(data, index=True):
            try:
                # 判断是不是 0:: 这种方式
                if data[-1] == ':':
                    if index:
                        t = self.data.index.tolist()
                    else:
                        t = self.data.columns.tolist()
                    try:
                        qian_data = data.split(':')[0]
                        data = [t[i] for i in range(int(qian_data), len(t))]
                    except:
                        qian_data = data.split(':')[0]
                        xia_biao_qian_data = t.index(qian_data)
                        data = [t[i] for i in range(xia_biao_qian_data, len(t))]

                    return data, 2

                # 判断是不是 0:1 这种方式
                elif data.find(':') >= 0:
                    qian_data = data.split(':')[0]
                    hou_data = data.split(':')[1]

                    data_1 = []
                    data_1.append(qian_data)
                    data_1.append(hou_data)

                    return data_1, 1

                # 判断是不是 [1,2] 这种方式
                elif data.find('[') >= 0 and data.find(']') >= 0:
                    data = eval(data)

                    return data, 2

                # 判断是不是需要显示单个的行或列
                else:
                    return data, 2
            except:
                return data, 2

        # 如果什么都不填写
        if len(index_2) <= 0:
            index_2 = self.data.index.tolist()

        elif len(columns_2) <= 0:
            columns_2 = self.data.columns.tolist()

        data_index, lei_xing_index = pan_duan(index_2)
        data_columns, lei_xing_columns = pan_duan(columns_2, index=False)

        try:
            if lei_xing_index == 1 and lei_xing_columns == 1:
                try:
                    data = self.data.loc[int(data_index[0]):int(data_index[1]), data_columns[0]:data_columns[1]]
                except:
                    data = self.data.iloc[int(data_index[0]):int(data_index[1]), int(data_columns[0]):int(data_columns[1])]

            elif lei_xing_index == 1 and lei_xing_columns == 2:
                try:
                    data = self.data.loc[int(data_index[0]):int(data_index[1]), data_columns]
                except:
                    data_columns = [int(i) for i in data_columns]
                    data_columns.sort()
                    data = self.data.iloc[int(data_index[0]):int(data_index[1]), data_columns]

            elif lei_xing_index == 2 and lei_xing_columns == 1:
                new_data_index = [int(i) for i in data_index]
                new_data_index.sort()
                try:
                    data = self.data.loc[new_data_index, data_columns[0]:data_columns[1]]
                except:
                    data_columns = [int(i) for i in data_columns]
                    data_columns.sort()
                    data = self.data.iloc[new_data_index, int(data_columns[0]):int(data_columns[1])]

            elif lei_xing_index == 2 and lei_xing_columns == 2:
                new_data_index = [int(i) for i in data_index]
                new_data_index.sort()
                try:
                    data = self.data.loc[new_data_index, data_columns]
                except:
                    data_columns = [int(i) for i in data_columns]
                    data_columns.sort()
                    data = self.data.iloc[new_data_index, data_columns]

        except:
            mgb.showwarning('提示', '请正确输入')

        else:
            self.empty_1(treeview)
            nn = 0
            list_columns_self = self.data.columns.tolist()
            try:
                list_columns_data = data.columns.tolist()
            except:
                list_columns_data = []
                list_columns_data.append(columns_2)

            for i in data.index.tolist():
                t = ['---' for fi in self.data]
                for fkk in list_columns_data:
                    xia_biao = list_columns_self.index(fkk)
                    try:
                        t[xia_biao] = data.loc[i, fkk]
                    except:
                        t[xia_biao] = data[i]
                t.insert(0, nn)
                treeview.insert('', 'end', values=t)
                nn += 1

            ttff = data.index.tolist()
            stringvar_1.set("行：%s" % (len(ttff)) + '\n' + '列：%s' % (len(data)))

    # 读取数据
    def read_data(self, data):
        self.data = data
        self.copy_data = data # 备份数据

        self.window_1()

    # 显示数据
    def show_data(self):
        self.t1['state'] = tk.DISABLED

        root = self.window_2()
        root.title('显示数据')

        # 显示数据，创建ttk.Treeview()控件
        treeview = self.show_treeview(root)

        def www(data, treeview):
            self.empty_1(treeview)

            n = 0
            for i in data.values:
                values_1 = list(i)
                values_1.insert(0, n)
                n += 1

                treeview.insert('', 'end', values=values_1)

        www(self.data, treeview) # 插入数据

        self.the_scroll_bar(root, treeview) # 滚动条

        f = tk.Frame(root)
        f.grid(row=2, column=0)

        ff = [tk.Frame(f), tk.Frame(f)]
        ff[0].grid(row=0, column=0, padx=30)
        ff[1].grid(row=0, column=1)

        stringvar_1 = self.shou_index_columns(root, self.data, ff[0]) # 显示多少行多少列

        # 指定显示
        def show_more():
            duo_xian_shi['state'] = tk.DISABLED

            # 确认
            def okk():
                self.ok_1(index_1, columns_1, treeview, stringvar_1)

            # 说明
            def shuo_ming():
                mgb.showwarning('提示', '指定显示需遵循python语言'+'\n'+
                                '多行多列显示：[1,2]或1:2或1::或0::'+'\n'+
                                '单行显示：1或xxx(索引名)'+'\n'+
                                '支持下标和标签索引'+'\n'+
                                '请把输入法切换到英语模式再输入')

            root_2 = self.window_2(height=200)
            root_2.title('指定显示')

            fr = [tk.Frame(root_2), tk.Frame(root_2), tk.Frame(root_2), tk.Frame(root_2)]
            fr[0].pack()
            fr[1].pack()
            fr[2].pack()
            fr[3].pack()

            tk.Label(fr[0], text='多行标签(或下标)：', font=('黑体', 14)).grid(row=0, column=0, padx=5, pady=10)
            index_1 = tk.Entry(fr[0], font=('黑体', 14))
            index_1.grid(row=0, column=1, padx=5, ipady=3, pady=10)

            tk.Label(fr[1], text='多列标签(或下标)：', font=('黑体', 14)).grid(row=0, column=0, padx=5, pady=10)
            columns_1 = tk.Entry(fr[1], font=('黑体', 14))
            columns_1.grid(row=0, column=1, padx=5, ipady=3, pady=10)

            tk.Button(fr[2], text='确认', font=('黑体', 14), width=9, command=okk).grid(row=0, column=1, padx=150, pady=20)

            tk.Label(fr[3]).grid(row=0, column=0, padx=220)
            ttk.Button(fr[3], text='说明', width=6, command=shuo_ming).grid(row=0, column=1)

            root_2.protocol('WM_DELETE_WINDOW', lambda :self.no_1(root_2, duo_xian_shi))  # 判断窗口关闭
            root_2.mainloop()

        duo_xian_shi = tk.Button(ff[1], text='指定显示', font=('黑体', 14), command=show_more)
        duo_xian_shi.grid(row=0, column=1, padx=15)

        tk.Button(ff[1], text='重置', font=('黑体', 14), command=lambda :www(self.data, treeview), width=7).grid(row=0, column=2, padx=15)

        root.columnconfigure(0, weight=1) # 相当于开启填充模式，ttk.Treeview这个函数会占满空间,导致root空间不够（默认不填充的）
        root.protocol('WM_DELETE_WINDOW', lambda: self.no_1(root, self.t1))  # 判断窗口关闭
        root.mainloop()

    # 缺失值
    def query_missing_value(self):
        root = self.window_2()
        root.title('缺失值')

        # 显示数据，创建ttk.Treeview()控件
        treeview = self.show_treeview(root)

        isnull_data = pd.isnull(self.data)
        if len(self.data[isnull_data.values==True]) <= 0:
            pass

        else:
            n = 0
            t = self.data[isnull_data.values==True].index.tolist()
            t = list(set(t))
            for i in self.data.loc[t].values:
                values_1 = list(i)
                values_1.insert(0, t[n])
                n += 1

                treeview.insert('', 'end', values=values_1)

        self.the_scroll_bar(root, treeview)

        stringvar_1 = self.shou_index_columns(root, self.data, root)

        root.columnconfigure(0, weight=1)  # 相当于开启填充模式，ttk.Treeview这个函数会占满空间,导致root空间不够（默认不填充的）
        root.mainloop()

    # 重复值
    def query_repeat_value(self):
        root = self.window_2()
        root.title('重复值')

        # 显示数据，创建ttk.Treeview()控件
        treeview = self.show_treeview(root)

        duplicated_data = self.data.duplicated()
        if len(self.data[duplicated_data.values == True]) <= 0:
            pass

        else:
            n = 0
            t = self.data[duplicated_data == True].index.tolist()
            t = list(set(t))
            for i in self.data.loc[t].values:
                values_1 = list(i)
                values_1.insert(0, t[n])
                n += 1

                treeview.insert('', 'end', values=values_1)

        # 这里是用来显示相同/重复数据的所有出现次数位置（上面只会显示从第二次出现开始的，第一次出现时的不会显示）
        # for i in self.data.index.tolist():
        #     d1 = self.data.iloc[i]
        #     d2 = self.data[duplicated_data == True].iloc[0]
        #
        #     if d1.values.tolist() == d2.values.tolist():
        #         print(i)

        self.the_scroll_bar(root, treeview)

        stringvar_1 = self.shou_index_columns(root, self.data, root)

        root.columnconfigure(0, weight=1)  # 相当于开启填充模式，ttk.Treeview这个函数会占满空间,导致root空间不够（默认不填充的）
        root.mainloop()

    # 异常值
    def query_outliers_value(self):
        def outliers_1(data):
            lr = data.describe() # 这个函数可以把平均值，方差，标准差等等都给你显示出来(pd专用)
            list_lr = lr.columns.tolist()

            zi_dian_1 = {}
            list_index = []
            for i in list_lr:
                # 用正太分布 进行异常点判断（u-3q, u+3q）(正态分布的原则, 可以百度)
                flr = ((lr.loc['mean', i] - 3*lr.loc['std', i] > data[i]) | (lr.loc['mean', i] + 3*lr.loc['std', i] < data[i]))

                # 找到每列数据异常点对应的行
                zi_dian_1[i] = data[i][flr].index.tolist()

                list_index.extend(data[i][flr].index.tolist())

            new_list_index = list(set(list_index))
            return zi_dian_1, new_list_index, lr

        root = self.window_2()
        root.title('显示异常值')

        treeview = self.show_treeview(root)

        pd_data = []
        data_values_index, data_index, lr = outliers_1(self.data)
        data_index.sort()
        if len(data_index) > 0:
            t = ['---' for i in range(len(self.data.columns.tolist()))]
            t_1 = np.array([t] * len(data_index))

            if len(data_index) > 1:
                pd_data = pd.DataFrame(t_1, columns=self.data.columns.tolist(), index=data_index)

                for j, k in data_values_index.items():
                    try:
                        pd_data.loc[k, j] = self.data.loc[k, j]

                    except:
                        pass

                pd_data.sort_index(inplace=True) # 按行排序，（sort_values：按列排序）
                for kk in pd_data.index.tolist():
                    values_1 = pd_data.loc[kk].values.tolist()
                    values_1.insert(0, kk)
                    treeview.insert('', 'end', values=values_1)

            else:
                pd_data = self.data.loc[data_index]

                for j, k in data_values_index.items():
                    try:
                        pd_data[k] = self.data.loc[k, j]

                        for kk in k:
                            values_1 = pd_data.values.tolist()
                            values_1.insert(0, kk)
                            treeview.insert('', 'end', values=values_1)

                    except:
                        pass

        self.the_scroll_bar(root, treeview)

        stringvar_1 = self.shou_index_columns(root, self.data, root)

        root.columnconfigure(0, weight=1)  # 相当于开启填充模式，ttk.Treeview这个函数会占满空间,导致root空间不够（默认不填充的）
        root.mainloop()

    # 可视化
    def visualization_1(self):
        pass


if __name__ == '__main__':
    dd = A()

    # B()


