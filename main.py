import pandas as pd
import latestUpdate as lu
import generatedGUI as gengui

df = pd.read_csv('tasa_cambio.csv')

date, value, upToDate = lu(df)

gengui.window.mainloop()