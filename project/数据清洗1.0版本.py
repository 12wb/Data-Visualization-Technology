import numpy as np
import pandas as pd
# from pandas import DataFrame

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fdg
from tkinter import messagebox as mgb

import time

import os

import copy

import base64

from sqks import img  # 导入sqks图标(已变成base64编码数据)


# 选择文件
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

        # 把tkinter的图标设置为时崎狂三的图片
        tmp = open("sqks.ico", "wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        self.root.iconbitmap("sqks.ico")  # 设置tkinter图标
        os.remove("sqks.ico")  # 销毁sqks.ico图标

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
                name = self.ent.get().split('/')[-1]

                time.sleep(0.2)
                self.root.destroy()

                B().read_data(data, name)

        else:
            mgb.showwarning('提示', '路径不能未空')


# 数据处理
class B:
    def __init__(self):
        self.data = ''
        self.copy_data = '' # 备份数据
        self.copy_data_copy = ''  # 再次备份数据

        self.name = ''

        self.root = ''

    def window_1(self):
        self.root = tk.Tk()
        self.root.title('数据清洗')
        self.root.resizable(width=False, height=False)

        # 设置窗口居中
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (400, 300, (width - 400) / 2, (height - 300) / 2))

        # 把tkinter的图标设置为时崎狂三的图片
        tmp = open("sqks.ico", "wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        self.root.iconbitmap("sqks.ico")  # 设置tkinter图标
        os.remove("sqks.ico")  # 销毁sqks.ico图标

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

        self.t6 = tk.Button(self.root, text='重置', command=self.www_na_niu, font=('黑体', 15), width=10)
        self.t6.grid(row=1, column=2, padx=12, pady=20)

        self.t7 = tk.Button(self.root, text='保存文件', command=self.save_th_file, font=('黑体', 15), width=10)
        self.t7.grid(row=2, column=0, padx=12, pady=20)

        self.t7 = tk.Button(self.root, text='返回上一级', command=self.cong_xing, font=('黑体', 15), width=10)
        self.t7.grid(row=2, column=1, padx=12, pady=20)

        self.root.mainloop()

    # 第二个窗口
    def window_2(self, root, width=500, height=600):
        root = tk.Toplevel(root)
        root.title('显示数据')
        root.resizable(width=True, height=True)

        # 设置窗口居中
        root_width = root.winfo_screenwidth()
        root_height = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (width, height, (root_width - width) / 2, (root_height - height) / 2))

        # 把tkinter的图标设置为时崎狂三的图片
        tmp = open("sqks.ico", "wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        root.iconbitmap("sqks.ico")  # 设置tkinter图标
        os.remove("sqks.ico")  # 销毁sqks.ico图标

        return root

    # 读取数据
    def read_data(self, data, name):
        self.data = copy.deepcopy(data)
        self.copy_data = copy.deepcopy(data)  # 备份数据
        self.copy_data_copy = copy.deepcopy(data)  # 再次备份数据

        self.name = name

        self.window_1()

    # 滚动条
    def the_scroll_bar(self, root, treeview):
        # 横向滚动条
        scrollbar_x = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=treeview.xview)
        treeview.configure(xscrollcommand=scrollbar_x.set)
        treeview.grid(row=0, column=0)
        scrollbar_x.grid(row=1, column=0, sticky=tk.EW)

        # 竖直滚动条
        scrollbar_y = ttk.Scrollbar(root, orient=tk.VERTICAL, command=treeview.yview)
        treeview.configure(yscrollcommand=scrollbar_y.set)
        treeview.grid(row=0, column=0)
        scrollbar_y.grid(row=0, column=1, sticky=tk.NS)

        return scrollbar_x, scrollbar_y

    # 显示多少行，多少列
    def shou_index_columns(self, root, data):
        stringvar_1 = tk.StringVar(root)
        ttt = data.index.tolist()
        ttt1 = self.data.columns.tolist()
        stringvar_1.set("行：%s" % (len(ttt)) + '\n' + '列：%s' % (len(ttt1)))

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
        dd = treeview.get_children() # 提取所有的行
        [treeview.delete(i) for i in dd]

    # 点击按钮(取消)后,所运行的函数
    def no_1(self, root, an_niu):
        an_niu['state'] = tk.NORMAL
        root.destroy()

    # 窗口关闭，保存数据
    def nno_1(self, root, t):
        self.data = copy.deepcopy(self.copy_data_copy)  # 赋值

        self.no_1(root, t)

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

            list_index = data.index.tolist()

            for i in data.index.tolist():
                t = ['---' for fi in self.data]
                for fkk in list_columns_data:
                    xia_biao = list_columns_self.index(fkk)
                    try:
                        t[xia_biao] = data.loc[i, fkk]
                    except:
                        t[xia_biao] = data[i]
                t.insert(0, list_index[nn])
                treeview.insert('', 'end', values=t)
                nn += 1

            stringvar_1.set("行：%s" % (len(list_index)) + '\n' + '列：%s' % (len(data)))

    # 删除
    def delete_1(self, an_niu, treeview, type, index=None):
        an_niu[0]['state'] = tk.DISABLED
        an_niu[1]['state'] = tk.NORMAL

        def q(event):
            x = treeview.identify_column(event.x)  # 找到x轴
            y = treeview.identify_row(event.y)  # 找到y轴

            col = int(str(x).replace("#", ""))  # 获取列的下标

            if len(y) == 0 and col == 1:
                t = mgb.askyesno('提示', '删除所有行？')
                if t:
                    if type == 'qsz':
                        self.copy_data_copy.dropna(inplace=True)
                    elif type == 'cfz':
                        self.copy_data_copy.drop_duplicates(inplace=True)
                    elif type == 'ycz':
                        self.copy_data_copy.drop(index, inplace=True)

                    dd = treeview.get_children()
                    [treeview.delete(i) for i in dd]

                    time.sleep(0.2)

            elif len(y) > 0:
                for item in treeview.selection():  # 获取鼠标所在的行
                    values_data = treeview.item(item, "values")  # 获取那一行的数据

                    t = mgb.askyesno('提示', '删除这一行？')
                    if t:
                        self.copy_data_copy.drop(int(values_data[0]), inplace=True)

                        treeview.delete(y)

                        time.sleep(0.2)

        treeview.bind("<Double-Button-1>", q)

    # 修改数据
    def modify_the(self, root, treeview, an_niu, data=None):
        an_niu[0]['state'] = tk.DISABLED
        an_niu[1]['state'] = tk.NORMAL

        def q(event):
            x = treeview.identify_column(event.x) # 找到x轴
            y = treeview.identify_row(event.y) # 找到y轴

            for item in treeview.selection(): # 获取鼠标所在的行
                values_data = treeview.item(item, "values") # 获取那一行的数据
                col = int(str(x).replace("#", "")) # 获取列的下标

                if (values_data[col-1] != '---') and (len(y) > 0) and (col-1 != 0):
                    root_bind = self.window_2(root, height=80, width=300)
                    root_bind.title('修改数据')
                    root_bind.grab_set()

                    xiu_gai_shu_ju = tk.Entry(root_bind, font=('黑体', 14), width=25)
                    xiu_gai_shu_ju.pack(ipady=3)

                    def wwt():
                        treeview.set(item, column=x, value=xiu_gai_shu_ju.get()) # 修改treeview控件里的数据

                        try:
                            type_data = type(self.copy_data_copy.iloc[int(values_data[0]), int(col-2)])
                            self.copy_data_copy.iloc[int(values_data[0]), int(col-2)] = type_data(xiu_gai_shu_ju.get())  # 修改数据
                        except:
                            self.copy_data_copy.iloc[int(values_data[0]), int(col - 2)] = xiu_gai_shu_ju.get()

                            mgb.showerror('提示', '你输入的数据与原数据类型不匹配'+'\n'+'前检查是否误输')

                        time.sleep(0.3)

                        root_bind.destroy()

                    button = tk.Button(root_bind, text='确认', font=('黑体', 14), command=wwt)
                    button.pack()

                    root_bind.mainloop()

        treeview.bind("<Double-Button-1>", q)

    # 重置
    def www_na_niu(self):
        t = mgb.askyesno('提示', '会重置你所有数据，是否继续重置?')
        if t:
            self.copy_data_copy = copy.deepcopy(self.copy_data) # 数据初始化
            self.data = copy.deepcopy(self.copy_data)

            mgb.showwarning('提示', '重置成功')

    # 显示数据
    def show_data(self):
        self.t1['state'] = tk.DISABLED

        root = self.window_2(self.root)
        root.title('显示数据')

        # 显示数据，创建ttk.Treeview()控件
        treeview = self.show_treeview(root)

        def www(data, treeview, stringvar_1=None):
            self.empty_1(treeview)

            n = 0
            for i in data.values:
                values_1 = list(i)
                values_1.insert(0, n)
                n += 1

                treeview.insert('', 'end', values=values_1)

            time.sleep(0.2)

            if stringvar_1 != None:
                ttt = data.index.tolist()
                ttt1 = self.data.columns.tolist()
                stringvar_1.set("行：%s" % (len(ttt)) + '\n' + '列：%s' % (len(ttt1)))

        www(self.data, treeview)  # 插入数据

        scrollbar_x, scrollbar_y = self.the_scroll_bar(root, treeview)  # 滚动条

        f = tk.Frame(root)
        f.grid(row=2, column=0)

        ff = [tk.Frame(f), tk.Frame(f)]
        ff[0].grid(row=0, column=0, padx=30)
        ff[1].grid(row=0, column=1)

        stringvar_1 = self.shou_index_columns(root, self.data) # 显示多少行多少列
        tk.Label(ff[0], textvariable=stringvar_1).pack()

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

            root_2 = self.window_2(root, height=200)
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

        tk.Button(ff[1], text='重置', font=('黑体', 14), command=lambda :www(self.data, treeview, stringvar_1=stringvar_1), width=7).grid(row=0, column=2, padx=15)

        root.columnconfigure(0, weight=1) # 相当于开启填充模式，ttk.Treeview这个函数会占满空间,导致root空间不够（默认不填充的）
        root.protocol('WM_DELETE_WINDOW', lambda: self.no_1(root, self.t1))  # 判断窗口关闭
        root.mainloop()

    # 缺失值
    def query_missing_value(self):
        self.t2['state'] = tk.DISABLED

        root = self.window_2(self.root)
        root.title('缺失值')

        # 显示数据，创建ttk.Treeview()控件
        treeview = self.show_treeview(root)

        # 缺失值
        def qsz(data_data, treeview):
            isnull_data = pd.isnull(data_data)
            if len(data_data[isnull_data.values == True]) <= 0:
                pass

            else:
                n = 0
                t = data_data[isnull_data.values == True].index.tolist()
                t = list(set(t))
                t.sort()
                for i in self.data.loc[t].values:
                    values_1 = list(i)
                    values_1.insert(0, t[n])
                    n += 1

                    treeview.insert('', 'end', values=values_1)

            return isnull_data

        isnull_data = qsz(self.data, treeview)

        self.the_scroll_bar(root, treeview)

        f = tk.Frame(root)
        f.grid(row=2, column=0)

        ff = [tk.Frame(f), tk.Frame(f)]
        ff[0].grid(row=0, column=0, padx=30)
        ff[1].grid(row=0, column=1)

        stringvar_1 = self.shou_index_columns(root, self.data[isnull_data.values==True])
        tk.Label(ff[0], textvariable=stringvar_1).pack()

        duo_xian_shi = tk.Button(ff[1], text='修改', font=('黑体', 14), width=7, command=lambda :self.modify_the(root, treeview, list([duo_xian_shi, shan_chu])))
        duo_xian_shi.grid(row=0, column=1, padx=15)

        shan_chu = tk.Button(ff[1], text='删除', font=('黑体', 14), width=7, command=lambda :self.delete_1(list([shan_chu, duo_xian_shi]), treeview, 'qsz'))
        shan_chu.grid(row=0, column=2, padx=15)

        def wwt(data, treeview):
            self.empty_1(treeview)
            qsz(self.data, treeview)
            self.copy_data_copy = copy.deepcopy(self.data)
            time.sleep(0.2)

        tk.Button(ff[1], text='重置', font=('黑体', 14), command=lambda :wwt(self.data, treeview), width=7).grid(row=0, column=3, padx=15)

        root.protocol('WM_DELETE_WINDOW', lambda: self.nno_1(root, self.t2))  # 判断窗口关闭
        root.columnconfigure(0, weight=1)  # 相当于开启填充模式，ttk.Treeview这个函数会占满空间,导致root空间不够（默认不填充的）
        root.mainloop()

    # 重复值
    def query_repeat_value(self):
        self.t3['state'] = tk.DISABLED

        root = self.window_2(self.root)
        root.title('重复值')

        # 显示数据，创建ttk.Treeview()控件
        treeview = self.show_treeview(root)

        # 计算重复值
        def cfz(data_data, treeview):
            duplicated_data = data_data.duplicated()
            if len(data_data[duplicated_data.values == True]) <= 0:
                pass

            else:
                n = 0
                t = data_data[duplicated_data == True].index.tolist()
                t = list(set(t))
                t.sort()
                for i in data_data.loc[t].values:
                    values_1 = list(i)
                    values_1.insert(0, t[n])
                    n += 1

                    treeview.insert('', 'end', values=values_1)

            return duplicated_data

        duplicated_data = cfz(self.data, treeview)
        # 这里是用来显示相同/重复数据的所有出现次数位置（上面只会显示从第二次出现开始的，第一次出现时的不会显示）
        # for i in self.data.index.tolist():
        #     d1 = self.data.iloc[i]
        #     d2 = self.data[duplicated_data == True].iloc[0]
        #
        #     if d1.values.tolist() == d2.values.tolist():
        #         print(i)

        self.the_scroll_bar(root, treeview)

        f = tk.Frame(root)
        f.grid(row=2, column=0)

        ff = [tk.Frame(f), tk.Frame(f)]
        ff[0].grid(row=0, column=0, padx=30)
        ff[1].grid(row=0, column=1)

        stringvar_1 = self.shou_index_columns(root, self.data[duplicated_data == True])
        tk.Label(ff[0], textvariable=stringvar_1).pack()

        duo_xian_shi = tk.Button(ff[1], text='修改', font=('黑体', 14), width=7, command=lambda: self.modify_the(root, treeview, duo_xian_shi))
        duo_xian_shi.grid(row=0, column=1, padx=15)

        shan_chu = tk.Button(ff[1], text='删除', font=('黑体', 14), width=7, command=lambda: self.delete_1(list([shan_chu, duo_xian_shi]), treeview, 'cfz'))
        shan_chu.grid(row=0, column=2, padx=15)

        def wwt(data, treeview):
            self.empty_1(treeview)
            cfz(data, treeview)
            self.copy_data_copy = copy.deepcopy(self.data)
            time.sleep(0.2)

        tk.Button(ff[1], text='重置', font=('黑体', 14), command=lambda :wwt(self. data, treeview), width=7).grid(row=0, column=3, padx=15)

        root.protocol('WM_DELETE_WINDOW', lambda: self.nno_1(root, self.t3))  # 判断窗口关闭
        root.columnconfigure(0, weight=1)  # 相当于开启填充模式，ttk.Treeview这个函数会占满空间,导致root空间不够（默认不填充的）
        root.mainloop()

    # 异常值
    def query_outliers_value(self):
        self.t4['state'] = tk.DISABLED

        # 计算异常值的函数
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

        root = self.window_2(self.root)
        root.title('显示异常值')

        treeview = self.show_treeview(root)

        # 显示异常值的函数
        def cct(data_data, treeview):
            pd_data = []
            data_values_index, data_index, lr = outliers_1(data_data)
            data_index.sort()
            if len(data_index) > 0:
                t = ['---' for i in range(len(data_data.columns.tolist()))]
                t_1 = np.array([t] * len(data_index))

                if len(data_index) > 1:
                    pd_data = pd.DataFrame(t_1, columns=data_data.columns.tolist(), index=data_index)

                    for j, k in data_values_index.items():
                        try:
                            pd_data.loc[k, j] = data_data.loc[k, j]

                        except:
                            pass

                    pd_data.sort_index(inplace=True) # 按行排序，（sort_values：按列排序）
                    for kk in pd_data.index.tolist():
                        values_1 = pd_data.loc[kk].values.tolist()
                        values_1.insert(0, kk)
                        treeview.insert('', 'end', values=values_1)

                else:
                    pd_data = data_data.loc[data_index]

                    for j, k in data_values_index.items():
                        try:
                            pd_data[k] = data_data.loc[k, j]

                            for kk in k:
                                values_1 = pd_data.values.tolist()
                                values_1.insert(0, kk)
                                treeview.insert('', 'end', values=values_1)


                        except:
                            pass

            return data_index

        data_index = cct(self.data, treeview)

        self.the_scroll_bar(root, treeview)

        f = tk.Frame(root)
        f.grid(row=2, column=0)

        ff = [tk.Frame(f), tk.Frame(f)]
        ff[0].grid(row=0, column=0, padx=30)
        ff[1].grid(row=0, column=1)

        stringvar_1 = self.shou_index_columns(root, self.data.loc[data_index])
        tk.Label(ff[0], textvariable=stringvar_1).pack()

        duo_xian_shi = tk.Button(ff[1], text='修改', font=('黑体', 14), width=7, command=lambda: self.modify_the(root, treeview, duo_xian_shi))
        duo_xian_shi.grid(row=0, column=1, padx=15)

        shan_chu = tk.Button(ff[1], text='删除', font=('黑体', 14), width=7, command=lambda: self.delete_1(list([shan_chu, duo_xian_shi]), treeview, 'ycz', index=data_index))
        shan_chu.grid(row=0, column=2, padx=15)

        # 重置
        def wwt():
            self.empty_1(treeview)
            cct(self.data, treeview)
            self.copy_data_copy = copy.deepcopy(self.data)
            time.sleep(0.2)

        tk.Button(ff[1], text='重置', font=('黑体', 14), command=wwt, width=7).grid(row=0, column=3, padx=15)

        root.protocol('WM_DELETE_WINDOW', lambda: self.nno_1(root, self.t4))  # 判断窗口关闭
        root.columnconfigure(0, weight=1)  # 相当于开启填充模式，ttk.Treeview这个函数会占满空间,导致root空间不够（默认不填充的）
        root.mainloop()

    # 可视化
    def visualization_1(self):
        mgb.showerror('提示', '该功能暂未开放')
        # mgb.showwarning('提示', '该功能暂未开放')

    # 保存文件
    def save_th_file(self):
        the_auffix = self.name.split('.')[-1]
        the_old_name = self.name[:(len(self.name)-len(the_auffix)-1)]
        the_new_name = the_old_name + '-副本'

        thr_path = fdg.askdirectory() # 选择保存路径
        if thr_path != '':
            mgb.showwarning('提示', '请输入文件名(自带默认文件名)')

            root_bind = self.window_2(self.root, height=80, width=300)
            root_bind.title('保存数据')
            root_bind.grab_set()

            name = tk.StringVar()
            name.set(the_new_name)
            xiu_gai_shu_ju = tk.Entry(root_bind, font=('黑体', 14), width=25, textvariable=name)
            xiu_gai_shu_ju.pack(ipady=3)

            # 保存
            def cun_dang():
                if len(xiu_gai_shu_ju.get()) > 0:
                    the_full_path = thr_path + '/' + xiu_gai_shu_ju.get() + '.' + the_auffix  # 得到全路径
                    self.data.to_csv(the_full_path, index=0) # 行标签不保存
                    mgb.showwarning('提示', '保存成功')

                    root_bind.destroy()

                else:
                    mgb.showwarning('提示', '请输入文件名')

            tk.Button(root_bind, text='确认', font=('黑体', 14), command=cun_dang).pack()

            def guan_bi():
                mgb.showwarning('提示', '保存失败')
                root_bind.destroy()

            root_bind.protocol('WM_DELETE_WINDOW', guan_bi)  # 判断窗口关闭
            root_bind.mainloop()

    # 重新选择文件
    def cong_xing(self):
        time.sleep(0.2)
        self.root.destroy()
        A()


# 用这个避免上面函数里有可打印的数据，然后被直接打印
# 而且必须在这个模块里 运行才可以运行这个底下的代码
# 如果用其他模块导入这个模块，则不会启动这个底下的代码
if __name__ == '__main__':
    A()


