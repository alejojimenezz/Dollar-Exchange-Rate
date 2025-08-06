import tkinter

window = tkinter.Tk()
window.geometry("400x300")

label = tkinter.Label(window, text="Label", font="Helvetica 20")
label.grid(row=0)

updateStatus = tkinter.Label(window, text="updateStatus")
updateStatus.grid(row=1, column=0)

updateButton = tkinter.Button(window, text="updateButton")
updateButton.grid(row=2, column=0)

# textBox = tkinter.Entry(window)
# textBox.pack()

window.mainloop()