from runpy import run_path
from tkinter import *
import mutiprocessing
import os

def make_app():
	app = Tk()
	app.title('运行脚本程序')
	app.geometrix('500x600')
	Listbox(name='lb1', bg='#303030', fg='white', font=('Hack', 16, 'bold')).pack()
	Button(text='run', command=run_script).pack()
	Button(text='stop', command=stop_script).pack()
	return app

def run_script():
	listbox = app.children['lb1']
	s_path = listbox.get(ACTIVE)
	p = mutiprocessing.Process(name='test', target=lambda:run_path(s_path))
	p.start()

def stop_script():
	list = mutiprocessing.active_children()
	for p in list:
		# if p.name == 'print':
		# 	p.terminate()
		p.terminate()

def ui_getPath():
	listbox = app.children['lb1']
	for path in os.listdir():
		listbox.insert(END, path)


app = make_app()
app.after(1000, ui_getPath)
app.mainloop()