from tkinter import*
from tkinter import Tk, ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm,text="hello world!").grid(coloumn=0, row=0)
ttk.button(frm,text="quit",command=root.destory).grid(colloumn=1, row=-0)
root.mainloop()
