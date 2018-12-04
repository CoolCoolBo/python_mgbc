from tkinter import *
import os


window = Tk()
window.title('显示隐藏文件')
window.geometry('600x600')
label = Label(text='隐藏的文件', font=('Hack', 18, 'bold'))
label.pack()
listbox = Listbox(bg='#f2f2f2', fg='red', font=('Hack', 16, 'bold'))
listbox.pack(fill=BOTH, expand=True)
path = '/'
files = os.listdir(path)
for f in files:
    if f.startswith('.'):
        listbox.insert(END, f)

window.mainloop()
