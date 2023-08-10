from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Mananger")
canvas = Canvas(width=400, height=400)
padlock = PhotoImage(file="logo.png")
canvas.create_image(200, 200, image=padlock)
canvas.pack()


window.mainloop()