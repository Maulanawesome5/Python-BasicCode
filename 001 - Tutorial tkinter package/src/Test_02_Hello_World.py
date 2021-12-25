# membuat hello world program menggunakan tkinter

from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

# The grid() method is used to specify the relative layout (position) of the label
# within its containing frame widget, similar to how tables in HTML work.

# destroy() method is used to terminate window