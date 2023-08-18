from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


# -------------------- Words List (CSV Write) -------------------- #


# -------------------- Card Functions -------------------- #

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
finally:
    data = data.to_dict("records")


def flip_card(current_word):
    canvas_card.itemconfigure(card_side, image=card_back)
    canvas_card.itemconfigure(title_text, text="English", fill="white")
    canvas_card.itemconfigure(word_text, text=current_word["English"], fill="white")


def set_random_word():
    global random_word
    random_word = random.choice(data)
    canvas_card.itemconfigure(card_side, image=card_front)
    canvas_card.itemconfigure(title_text, text="French", fill="black")
    canvas_card.itemconfigure(word_text, text=random_word["French"], fill="black")
    window.after(3000, flip_card, random_word)

def is_known():
    global random_word
    data.remove(random_word)
    print(len(data))
    words_to_learn = pd.DataFrame(data)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    set_random_word()

# -------------------- GUI Screen -------------------- #

window = Tk()
window.title("Fhashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creating images object
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

# Cards
canvas_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_side = canvas_card.create_image(400, 263, image=card_front)

# Texts on the flash cards
title_text = canvas_card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas_card.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas_card.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=set_random_word)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(column=1, row=1)

set_random_word()
window.mainloop()
