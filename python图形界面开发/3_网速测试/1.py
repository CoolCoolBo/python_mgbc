import psutil
import time
from tkinter import *


def make_app():
    app = Tk()
    app.geometry('300x150')
    app.config(bg='#303030')
    app.title('')
    Label(text='网速监测器',
          font=('Hack', 25, 'bold'),
          bg='#303030',
          fg='white'
          ).pack()

    Label(name='lb2',
          text='-kb/s',
          font=('Hack', 20, 'bold'),
          bg='#303030',
          fg='white'
          ).pack()
    return app
# 定义窗口


def speed_test():
    s1 = psutil.net_io_counters(pernic=False)
    time.sleep(1)
    s2 = psutil.net_io_counters(pernic=False)
    result = s2.bytes_recv - s1.bytes_recv
    return str(result / 1024) + 'kb/s'
# 获得网速值


def ui_update(do):
    data = do()
    lb2 = app.children['lb2']
    lb2.config(text=data)
    # 1000ms后调用ui_update函数(此处使用匿名函数的原因是：让ui_update(do)以函数的名字传进去来调用，而不是执行函数后的结果)
    app.after(1000, lambda: ui_update(do))
# 将speed_test函数作为参数传递进来，执行它来获得网速值，将其显示到ui上


app = make_app()
app.after(1000, lambda: ui_update(speed_test))
app.mainloop()
