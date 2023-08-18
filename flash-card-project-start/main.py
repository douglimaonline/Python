from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# -------------------- GUI Screen -------------------- #
def set_random_word():
    data = pd.read_csv("./data/french_words.csv")
    data = data.to_dict("records")
    random_word = random.choice(data)
    canvas_card_front.itemconfigure(word_text, text=random_word["French"])
    print(random_word["English"])


# -------------------- GUI Screen -------------------- #

window = Tk()
window.title("Fhashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

canvas_card_front = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card_front.create_image(400, 263, image=card_front)

title_text = canvas_card_front.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))

word_text = canvas_card_front.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas_card_front.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=set_random_word)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=set_random_word)
right_button.grid(column=1, row=1)

window.mainloop()
