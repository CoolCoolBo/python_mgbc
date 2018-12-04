from tkinter import *
from tkinter.filedialog import askopenfilenames
from PIL import Image


file_info = {
    'path': []
}
# 用于存储待压缩的图片地址


def make_app():
    window = Tk()
    window.title(' ')
    Label(window, text='图片压缩工具').pack()
    Listbox(window, name='lbox', bg='#f2f2f2').pack(fill=BOTH, expand=True)
    Button(window, text='open', command=ui_getData).pack()
    Button(window, text='compress', command=compress).pack()
    window.geometry('300x500')
    return window
# 创建GUI图形界面


def ui_getData():
    f_names = askopenfilenames()
    file_info['path'] = f_names
    lbox = window.children['lbox']
    for name in f_names:
        lbox.insert(END, name.split('/')[-1])
# 获取显示在图形界面上的数据，即图片的名称


def compress():
    for name in file_info['path']:
        img = Image.open(name)
        save_path = '/home/bo/Desktop' + '/' + name.split('/')[-1]
        img.save(save_path, quality=60)
    print('Done!')
# 压缩图片


window = make_app()
window.mainloop()
