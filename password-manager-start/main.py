from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    save_password = messagebox.askokcancel(title="Save Password",
                                           message=f"Website: {entry_website.get()}\n"
                                                   f"E-mail: {entry_email.get()}\n"
                                                   f"Password: {entry_password.get()}")
    if save_password:
        with open("data.txt", "a") as data:
            data.write(f"{entry_website.get()} | {entry_email.get()} | {entry_password.get()}\n")
            data.close()
        entry_email.delete(0, END)
        entry_website.delete(0, END)
        entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=15, pady=20)

canvas = Canvas(width=200, height=200)
padlock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries
entry_website = Entry(width=45)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()
entry_email = Entry(width=45)
entry_email.grid(column=1, row=2, columnspan=2)
entry_password = Entry(width=27)
entry_password.grid(column=1, row=3)

# Add button
button_password = Button(text="Generate Password", width=14)
button_password.grid(column=2, row=3)

button_add = Button(text="Add", width=43, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
