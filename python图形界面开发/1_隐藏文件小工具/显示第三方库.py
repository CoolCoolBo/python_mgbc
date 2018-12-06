import pip
import tkinter as tk


window = tk.Tk()
window.title('显示python中安装的第三方库')
window.geometry('300x500')
listbox = tk.Listbox(bg='#303030', fg='white', font=('Hack', 16, 'bold'))
listbox.pack(fill=tk.BOTH, expand=True)
lists = pip.get_installed_distributions()
for f in lists:
	listbox.insert(tk.END, f)

window.mainloop()

