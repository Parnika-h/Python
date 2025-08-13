import random
from tkinter import *
import pandas

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
current_index = -1

# ---------------------------- LOAD DATA ------------------------------- #
try:
    df = pandas.read_csv("./data/Words_to_learn")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")

word_list = df.to_dict(orient="records")

# ------------------------- KNOWN WORD FUNCTION ------------------------ #
def known():
    global current_index
    word_list.pop(current_index)
    data = pandas.DataFrame(word_list)
    data.to_csv("./data/Words_to_learn", index=False)
    show_random_french_word()

# ------------------------- SHOW FRENCH WORD --------------------------- #
def show_random_french_word():
    global current_index, flip_timer
    if len(word_list) == 0:
        canvas.itemconfig(card_image, image=card_front_img)
        canvas.itemconfig(title_text, text="Congratulations!", fill="black")
        canvas.itemconfig(word_text, text="You've learned all the words!",font=("Ariel", 40, "bold"),fill="black")
        return
    if flip_timer:
        window.after_cancel(flip_timer)

    current_index = random.randint(0, len(word_list) - 1)
    french_word = word_list[current_index]["French"]

    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")

    flip_timer = window.after(3000, flip_card)

# ----------------------------- FLIP CARD ------------------------------ #
def flip_card():
    english_word = word_list[current_index]["English"]
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word, fill="white")

# ----------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Load Images
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
tick_img = PhotoImage(file="./images/right.png")
cross_img = PhotoImage(file="./images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_button = Button(image=cross_img, highlightthickness=0, command=show_random_french_word)
wrong_button.grid(column=0, row=1)

right_button = Button(image=tick_img, highlightthickness=0, command=known)
right_button.grid(column=1, row=1)

# ----------------------------- START APP ------------------------------ #
show_random_french_word()
window.mainloop()