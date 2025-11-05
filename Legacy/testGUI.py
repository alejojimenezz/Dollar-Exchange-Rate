# https://tkdocs.com/tutorial/index.html

import tkinter as tk
from tkinter import *
from tkinter import ttk

#class App(tk.Frame):
#    def __init__(self, master=None):
#        super().__init__(master)
#        self.pack()

# myapp = App()
# myapp.master.title("My Do-Nothing Application")
# myapp.master.maxsize(1000, 400)
# myapp.mainloop()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()