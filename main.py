import pandas as pd
import updateFunction as uf
import latestUpdate as lu
# import graph as gr
import tkinter as tk
import generatedGUI as gengui

df = pd.read_csv('tasa_cambio.csv')

date, value, upToDate = lu(df)

# update function
# df = uf.updateDB()

gengui.updatebutton.event_add(gengui.updatestatus(tk.Label(text="Updated")))

gengui.window.mainloop()