import tkinter as tk

window = tk.Tk()
window.title = "Cambio de dolar a pesos colombianos"
window.geometry("600x300")

# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=1)

label = tk.Label(window, text="Label", font=("Helvetica", 20))
label.place(relx=0.5, rely=0.05, anchor="center")

updateStatus = tk.Label(window, text="updateStatus")
updateStatus.grid(row=1, column=0)

updateButton = tk.Button(window, text="updateButton")
updateButton.grid(row=2, column=0)

# textBox = tk.Entry(window)
# textBox.pack()

window.mainloop()