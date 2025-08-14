import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import graphGUI

window = tk.Tk()
window.title = "Cambio de dolar a pesos colombianos"
window.geometry("800x500")

fig = graphGUI.get_figure()

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=1)

# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=1)

label = tk.Label(window, text="Label", font=("Helvetica", 20))
label.place(relx=0.5, rely=0.05, anchor="center")

updateStatus = tk.Label(window, text="updateStatus", font=(20))
updateStatus.grid(row=1, column=0)

updateButton = tk.Button(window, text="updateButton")
updateButton.grid(row=2, column=0)

latestValue = tk.Label(window, text="latestValue")
latestValue.grid(row=3, column=0)

# textBox = tk.Entry(window)
# textBox.pack()

window.mainloop()