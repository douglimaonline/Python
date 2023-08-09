from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button1_clicked():
    button1["text"] = "I got clicked"


def button2_clicked():
    button2["text"] = "I got clicked"


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "normal"))
my_label.config(padx=50)
my_label.grid(column=0, row=2)

# Buttons
button1 = Button(text="click me", command=button1_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="new button", command=button2_clicked)
button2.grid(column=1, row=2)

# Entry
entry = Entry()
entry.config(width=10)
entry.grid(column=1, row=3)


window.mainloop()
