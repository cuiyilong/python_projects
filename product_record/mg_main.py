#!/usr/bin/python3

import pymysql
import tkinter
from tkinter import messagebox
from tkinter import *


from tkinter import ttk

import subprocess
w = tkinter.Tk()
subprocess.call('ks1.py', shell=True)  # 调用windows管理员权限启动mysql
ku = pymysql.connect(host="localhost", user="root", password="3981281", db="work_record",charset="utf8")  # 链接到库，需添加登陆账户、账户密码、所使用库名
cursor = ku.cursor(cursor=pymysql.cursors.DictCursor)  # 接受数据为元素为字典的列表


def init():  # 初始化生产记录表
    db = []
    p = input("重新初始化数据表请键入任意字符，否则请键入回车！")
    if p:
        cursor.execute("drop table if exists pdt_table")  # 如果表存在，删除它
        sql = "create table pdt_table(LOTID VARCHAR(100) NOT NULL,ID smallint,SN smallint,IN_TIME datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,IN_USER varchar(20),OUT_TIME datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,OUT_USER varchar(20),QUALITITY INT,primary key(ID))DEFAULT CHARSET `UTF8`;"
        print ("sql %s" % sql)
        cursor.execute(sql)
        print("create table pdt_table")
        db.append({"LOTID":"'M00821501.1'","ID":1, "SN": 1, "IN_TIME": "'2020-01-01 00:00:01'", "IN_USER": "'D08020570'", "OUT_TIME": "'2020-01-01 00:00:00'", "OUT_USER": "'D08020570'", "QUALITITY": 68})
        db.append({"LOTID":"'M00821501.1'","ID":2, "SN": 1, "IN_TIME": "'2020-01-01 00:00:02'", "IN_USER": "'D08020571'", "OUT_TIME": "'2020-01-01 00:00:01'", "OUT_USER": "'D08020571'","QUALITITY": 78})
        db.append({"LOTID":"'M00821501.1'","ID":3, "SN": 1, "IN_TIME": "'2020-01-01 00:00:03'", "IN_USER": "'D08020572'", "OUT_TIME": "'2020-01-01 00:00:02'", "OUT_USER": "'D08020572'","QUALITITY": 68})
        db.append({"LOTID":"'M00821501.1'","ID":4, "SN": 1, "IN_TIME": "'2020-01-01 00:00:04'", "IN_USER": "'D08020573'", "OUT_TIME": "'2020-01-01 00:00:03'", "OUT_USER": "'D08020573'","QUALITITY": 98})
        db.append({"LOTID":"'M00821501.1'","ID":5, "SN": 1, "IN_TIME": "'2020-01-01 00:00:05'", "IN_USER": "'D08020574'", "OUT_TIME": "'2020-01-01 00:00:04'", "OUT_USER": "'D08020574'","QUALITITY": 38})
        # 将db增加到MySQL的表中
        for i in db:
            a1 = "insert into pdt_table(LOTID,ID,SN,IN_TIME,IN_USER,OUT_TIME,OUT_USER,QUALITITY) values ("
            a2 = str(i['LOTID'])
            a3 = str(i['ID'])
            a4 = str(i['SN'])
            a5 = str(i['IN_TIME'])
            a6 = str(i['IN_USER'])
            a7 = str(i['OUT_TIME'])
            a8 = str(i['OUT_USER'])
            a9 = str(i['QUALITITY'])
            sql1 = a1 + a2 + "," + a3 + "," + a4 + "," + a5 + "," + a6 + "," + a7 +"," + a8 +"," + a9 + ");"
            print ("sql1 %s" % sql1)
            cursor.execute(sql1)
            ku.commit()


def add():
    global second
    global add_sno
    global add_yw
    global add_sx
    global add_wl
    global add_en
    second = tk.Toplevel()
    second.title("增加一条学生记录")
    second.geometry('300x300')
    # 主Frame
    frame = tk.Frame(second)
    frame.pack()
    # 两个子Frame,注意子frame是在主frame的框架下
    frame_l = tk.Frame(frame)
    frame_r = tk.Frame(frame)
    frame_l.pack(side='left')
    frame_r.pack(side='right')
    tk.Label(frame_l, text='请输入学号      ').pack()
    add_sno = tk.Entry(frame_r, show=None)
    add_sno.pack()
    tk.Label(frame_l, text='语文成绩        ').pack()
    add_yw = tk.Entry(frame_r, show=None)
    add_yw.pack()
    tk.Label(frame_l, text='数学成绩        ').pack()
    add_sx = tk.Entry(frame_r, show=None)
    add_sx.pack()
    tk.Label(frame_l, text='物理成绩        ').pack()
    add_wl = tk.Entry(frame_r, show=None)
    add_wl.pack()
    tk.Label(frame_l, text='英语成绩        ').pack()
    add_en = tk.Entry(frame_r, show=None)
    add_en.pack()
    # 将录入的成绩保存进数据库中
    b1 = tk.Button(second, text='确定', width=15, height=2, command=insert_1)
    b1.pack()
    second.mainloop()


def insert_1():
    s0 = add_sno.get()
    s1 = add_yw.get()
    s2 = add_sx.get()
    s3 = add_wl.get()
    s4 = add_en.get()
    a1 = "insert into biao(sno,yw,sx,wl,en) values ("
    sql1 = a1 + s0 + "," + s1 + "," + s2 + "," + s3 + "," + s4 + ")"
    try:
        cursor.execute(sql1)
        ku.commit()
    except Exception as e:
        ku.rollback()  # 事件回滚
        tk.messagebox.showinfo(title='Hi', message=e)
        return
    ku.commit()
    tk.messagebox.showinfo(title='Hi', message="增加成功")
    # 思考如何在跳出增加成功弹窗后，关闭增加窗口


def delete():
    global del_sno
    third = tk.Toplevel()
    third.title("删除一条学生记录")
    third.geometry('300x300')
    frame = tk.Frame(third)
    frame.pack()
    frame_l = tk.Frame(frame)
    frame_r = tk.Frame(frame)
    frame_l.pack(side='left')
    frame_r.pack(side='right')
    tk.Label(frame_l, text='请输入学号      ').pack()
    del_sno = tk.Entry(frame_r, show=None)
    del_sno.pack()
    b1 = tk.Button(third, text='确定', width=15, height=2, command=delete_1)
    b1.pack()
    third.mainloop()


def delete_1():
    id1 = del_sno.get()
    sql3 = "delete from biao where sno=" + id1
    try:
        i = cursor.execute(sql3)
    except Exception as e:
        tk.messagebox.showinfo(title='Hi', message=e)
    if i != 0:  # mysql会返回一个值，当命令执行成功为1，失败为0
        ku.commit()
    else:
        ku.rollback()
        tk.messagebox.showinfo(title='Hi', message="删除失败")
        return
    tk.messagebox.showinfo(title='Hi', message="删除成功")


def change():
    global fouth
    global change_sno
    global change_yw
    global change_sx
    global change_wl
    global change_en
    fouth = tk.Toplevel()
    fouth.title("修改一条学生记录")
    fouth.geometry('300x300')
    # 主Frame
    frame = tk.Frame(fouth)
    frame.pack()
    # 两个子Frame,注意子frame是在主frame的框架下
    frame_l = tk.Frame(frame)
    frame_r = tk.Frame(frame)
    frame_l.pack(side='left')
    frame_r.pack(side='right')

    tk.Label(frame_l, text='请输入学号      ').pack()
    change_sno = tk.Entry(frame_r, show=None)
    change_sno.pack()
    tk.Label(frame_l, text='语文成绩        ').pack()
    change_yw = tk.Entry(frame_r, show=None)
    change_yw.pack()
    tk.Label(frame_l, text='数学成绩        ').pack()
    change_sx = tk.Entry(frame_r, show=None)
    change_sx.pack()
    tk.Label(frame_l, text='物理成绩        ').pack()
    change_wl = tk.Entry(frame_r, show=None)
    change_wl.pack()
    tk.Label(frame_l, text='英语成绩        ').pack()
    change_en = tk.Entry(frame_r, show=None)
    change_en.pack()
    # 将录入的成绩保存进数据库中
    b1 = tk.Button(fouth, text='确定', width=15, height=2, command=update_1)
    b1.pack()
    fouth.mainloop()


def update_1():
    s0 = change_sno.get()
    s1 = change_yw.get()
    s2 = change_sx.get()
    s3 = change_wl.get()
    s4 = change_en.get()
    a1 = "update biao set yw=" + s1 + ",sx=" + s2 + ",wl=" + s3 + ",en=" + s4 + " where sno=" + s0
    sql1 = a1
    try:
        cursor.execute(sql1)
        ku.commit()
    except Exception as e:
        ku.rollback()
        tk.messagebox.showinfo(title='Hi', message=e)
        return
    ku.commit()
    tk.messagebox.showinfo(title='Hi', message="修改成功")


def query():
    global select_sno
    fifth = tk.Toplevel()
    fifth.title("查询学生记录")
    fifth.geometry('400x300')
    tk.Label(fifth, text='请输入您的查询语句(查询表为:biao)').pack()
    select_sno = tk.Entry(fifth, show=None)
    select_sno.pack()
    b1 = tk.Button(fifth, text='确定', width=15, height=2, command=select_1)
    b1.pack()
    b1 = tk.Button(fifth, text=' ', width=15, height=2, command=select_2('select * from biao'))
    b1.pack()
    fifth.mainloop()


def select_1():
    fifth_1 = tk.Toplevel()
    fifth_1.geometry('400x100')
    t = tk.Text(fifth_1, height=8)
    t.pack()
    order = select_sno.get()
    cursor.execute(order)
    db = cursor.fetchall()
    for i in db:
        t.insert('end', i)
        t.insert('end', '\n')


def select_2(order):
    fifth_2 = tk.Toplevel()
    fifth_2.geometry('400x100')
    t = tk.Text(fifth_2, height=8)
    t.pack()
    cursor.execute(order)
    db = cursor.fetchall()
    for i in db:
        t.insert('end', i)
        t.insert('end', '\n')


def inquire():
    global inquire_lotid
    sixth = Toplevel()
    sixth.title("查询流程编号")
    sixth.geometry('300x150')
    frame = Frame(sixth)
    frame.pack()
    frame_l = Frame(frame)
    frame_r = Frame(frame)
    frame_l.pack(side='left')
    frame_r.pack(side='right')
    Label(frame_l, text='请输入流程编号      ').pack()
    inquire_lotid = Entry(frame_r, show=None)
    inquire_lotid.pack()
    b1 = Button(sixth, text='确定', width=15, height=2, command=inquire_1)
    b1.pack()
    sixth.mainloop()

def inquire_1():
    id2 = inquire_lotid.get()
    sql_order = "select * from pdt_table where LOTID=" + "\"" + id2 + "\""
    print("sql: %s" % sql_order)
    cursor.execute(sql_order)
    try:
        j = cursor.execute(sql_order)
    # mysql会返回一个值，当命令执行成功为1，失败为0
    except Exception as e:\
        w.messagebox.showinfo(title='Hi', message=e)
    if j != 0:
        sixth_1 = Toplevel()
        sixth_1.geometry('400x100')
        frame = Frame(sixth_1)
        frame.pack()
        frame_l = Frame(frame)
        frame_r = Frame(frame)
        frame_l.pack(side='left')
        frame_r.pack(side='right')
        db = cursor.fetchall()

        #columns = cursor.description
        #print(columns)
        columns = ("流程卡号","ID","序列号","录入时间","录入员工","录出时间","录出员工","质量");
        treeview = ttk.Treeview(sixth_1, columns=columns, height=10, show="headings")


        treeview.column("流程卡号", width=100, anchor='center')  # 表示列,不显示
        treeview.column("ID", width=100, anchor='center')
        treeview.column("序列号", width=100, anchor='center')
        treeview.column("录入时间", width=100, anchor='center')
        treeview.column("录入员工", width=100, anchor='center')
        treeview.column("录出时间", width=100, anchor='center')
        treeview.column("录出员工", width=100, anchor='center')
        treeview.column("质量", width=100, anchor='center')

        treeview.heading("流程卡号", text="流程卡号")  # 显示表头
        treeview.heading("ID", text="ID")
        treeview.heading("序列号", text="序列号")
        treeview.heading("录入时间", text="录入时间")
        treeview.heading("录入员工", text="录入员工")
        treeview.heading("录出时间", text="录出时间")
        treeview.heading("录出员工", text="录出员工")
        treeview.heading("质量", text="质量")

        print("db :%s" % db)

        for rows in db:
            print(" rows %s" % rows)
            print("Length : %d" % len(rows))
            #dict to list
            values_col = list(rows.values())
            treeview.insert('', 'end', values=values_col)

        treeview.pack(side=LEFT, fill=BOTH)
        ku.commit()
    else:
        ku.rollback()
        w.messagebox.showinfo(title='Hi', message="查询失败")
        return


#init()

w.title('ERS查询')  # 主窗口标题
w.geometry('500x350')  # 窗口尺寸
#use grid

#标签控件，显示文本和位图，展示在第一行
LotidLebel = Label(w,text="流程卡号：").grid(row=0,sticky = W)
LotidEntry = Entry(w).grid(row=0,column=1,sticky = E)
L2 = Label(w,text="员工工号：").grid(row=1,sticky = W)
E1 = Entry(w).grid(row=1,column=1,sticky = E)
L3 = Label(w,text="圆盘编号：").grid(row=2,sticky = W)
E1 = Entry(w).grid(row=2,column=1,sticky = E)





B1 = Button(w, text="增加记录", command=add, bg='yellow')
B1.grid(row=10,column=0)

B2 = Button(w, text="删除记录", command=delete, bg='yellow')
B2.grid(row=10,column=5)

B3 = Button(w, text="修改记录", command=change, bg='yellow')
B3.grid(row=10,column=10)

CheckButton = Button(w, text="查询", command=inquire, bg='yellow')
CheckButton.grid(row=5,column=1,rowspan=5,columnspan=3)

B5 = Button(w, text="自由查询记录", command=query, bg='yellow')
B5.grid(row=20,column=5)

B6 = Button(w, text="退出", command=exit, bg='yellow')
B6.grid(row=20,column=10)
w.mainloop()