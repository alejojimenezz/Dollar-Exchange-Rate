# This code is generated using PyUIbuilder: https://pyuibuilder.com

# import os
import tkinter as tk

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

window = tk.Tk()
window.title("USD - COL pesos exchange")
window.config(bg="#E4E2E2")
window.geometry("700x400")

languageselect_options = ["English","Español"]
languageselect_var = tk.StringVar(value="English")
languageselect = tk.OptionMenu(window, languageselect_var, *languageselect_options)
languageselect.config(bg="#E4E2E2", fg="#000")
languageselect.place(x=575, y=20)

title = tk.Label(master=window, text="text: Title", font=("Helvetica", 20))
title.config(bg="#E4E2E2", fg="#000")
title.place(x=200, y=10, height=45)

updatestatus = tk.Label(master=window, text="text: Update Status", font=(20))
updatestatus.config(bg="#E4E2E2", fg="#000")
updatestatus.place(x=12, y=78, height=40)

updatebutton = tk.Button(master=window, text="Update")
updatebutton.config(bg="#E4E2E2", fg="#000")
updatebutton.place(x=63, y=125, height=40)

dollarvalue = tk.Label(master=window, text="Dollar Value: ")
dollarvalue.config(bg="#E4E2E2", fg="#000")
dollarvalue.place(x=14, y=274, height=40)

updatedate = tk.Label(master=window, text="Latest update: ")
updatedate.config(bg="#E4E2E2", fg="#000")
updatedate.place(x=12, y=224, height=40)


window.mainloop()