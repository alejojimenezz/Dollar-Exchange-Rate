# import os
import tkinter as tk
import pandas as pd
import latestUpdate as lu
import updateFunction as uf

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def update_and_disable():
    uf.updateDB(2000, "tasa_cambio.csv")
    df = pd.read_csv('tasa_cambio.csv')
    date, value, upToDate = lu.latestUpdate(df)

    updatestatus.config(text=upToDate)
    dollarvalue.config(f"Dollar Value: {value} COP")
    updatedate.config(text=f"Latest update: {date}")

    updatebutton.config(state="disabled")

df = pd.read_csv('tasa_cambio.csv')
date, value, upToDate = lu.latestUpdate(df)

window = tk.Tk()
window.title("USD - COL pesos exchange")
window.config(bg="#E4E2E2")
window.geometry("700x400")

# TO-DO: Add spanish GUI
languageselect_options = ["English","Español"]
languageselect_var = tk.StringVar(value="English")
languageselect = tk.OptionMenu(window, languageselect_var, *languageselect_options)
languageselect.config(bg="#E4E2E2", fg="#000")
languageselect.place(x=575, y=20)

title = tk.Label(master=window, text="Currency Exchange Rate", font=("Helvetica", 20))
title.config(bg="#E4E2E2", fg="#000")
title.place(x=200, y=10, height=45)

updatestatus = tk.Label(master=window, text=f"{upToDate}", font=(20))
updatestatus.config(bg="#E4E2E2", fg="#000")
updatestatus.place(x=12, y=78, height=40)

updatebutton = tk.Button(master=window, text="Update", command=update_and_disable)
updatebutton.config(bg="#E4E2E2", fg="#000")
updatebutton.place(x=65, y=125, height=40)

if (upToDate == "Database is up to date."):
    updatebutton.config(state="disabled")

dollarvalue = tk.Label(master=window, text=f"Dollar Value: {value} COP")
dollarvalue.config(bg="#E4E2E2", fg="#000")
dollarvalue.place(x=15, y=275, height=40)

updatedate = tk.Label(master=window, text=f"Latest update: {date}")
updatedate.config(bg="#E4E2E2", fg="#000")
updatedate.place(x=15, y=225, height=40)


window.mainloop()