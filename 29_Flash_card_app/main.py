from tkinter import *
import pandas as pd
import random
import os

GREEN_CARD_QUOTES = ["So, did you get it right?", "Be honest, did you remember what it was?",
                     "YOU GOT IT CORRECT!.. right?", "nah, you remembered it correctly right?",
                     "It's okay, even if you didn't remember it right!",
                     "If you got it right, I'm proud.. if you didn't I'm still proud", "YIPPE YOU GOT IT!!.. for sure?"]
WHITE_CARD_QUOTES = ["Can you remember what the word above means in English?",
                     "I'm sure this one is easy, what does it mean in English?", "You definitely know this one, cmon!",
                     "Hurry up! What does the word mean in English?",
                     "You remember this one You remember this one You remember this one",
                     "Hey even my cat knows the word above in English, cmon!",
                     "That one's kinda hard.. BUT YOU REMEMBER RIGHT?"]
BACKGROUND_COLOR = "#B1DDC6"
WORDS_FILE = "data/french_words.csv"
language = "test"
timer = None
random_word = {}
with open(file="data/score.txt", mode="r") as file:
    correct_num = int(file.read())
# [--------------------CREATE NEW CARDS MECHANISM--------------------]


def open_file():
    # Try opening the words to learn file first
    try:
        file = pd.read_csv("data/words_to_learn.csv")
        generate_word(file)
    # if words_to_learn.csv not found, use the french_words.csv file
    except FileNotFoundError:
        file = pd.read_csv(WORDS_FILE)
        generate_word(file)


def generate_word(file):
    global random_word, random_english
    word_dict = pd.DataFrame.to_dict(file, orient="records")

    # Get a random word
    random_word = random.choice(word_dict)

    random_french = random_word["French"]
    random_english = random_word["English"]

    # Put word on card and adjust UI for French card
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_french, fill="black")
    canvas.itemconfig(card_img, image=card_front)
    # Count down
    count_down(4)


def correct_answer():
    global random_word, correct_num

    # Read the full words file, then remove the one chosen if the use knows it
    try:
        words_to_learn = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        words_to_learn = pd.read_csv(WORDS_FILE)

    # Update score
    with open(file="data/score.txt", mode="w") as file:
        correct_num += 1
        file.write(str(correct_num))
    canvas.itemconfig(correct_text, text=f"Correct words: {correct_num}/102")

    words_to_learn = words_to_learn[words_to_learn["French"] != random_word["French"]]
    # Make the words_to_learn.csv file to contain the words the user hasn't got correctly yet
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    open_file()


def reset_score():
    global correct_num
    # Reset score
    with open(file="data/score.txt", mode="w") as file:
        file.write("0")
        correct_num = 0
        canvas.itemconfig(correct_text, text="Correct words: 0/102")
    # Reset the words file
    os.remove("data/words_to_learn.csv")
# [-----------------------------UI DESIGN----------------------------]


# Create the window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Osama's Flash Card")

# Flash card canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# Create the images for the flashcard
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# Create the text for the flashcard
language_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
remember_text = canvas.create_text(400, 475, text=random.choice(WHITE_CARD_QUOTES),
                                   font=("Ariel", 15, "italic"))
correct_text = canvas.create_text(110, 35, text=f"Correct words: {correct_num}/102", font=("Ariel", 14, "italic"))
timer_text = canvas.create_text(730, 50, text="0", font=("Ariel", 25, "bold"))

# Wrong button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=open_file)
wrong_button.grid(row=1, column=0)

# Correct button
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=correct_answer)
right_button.grid(row=1, column=1)

# Reset button
reset_button = Button(text="Reset Score", highlightthickness=0, borderwidth=0, bg="#90EE90",
                      font=("Ariel", 14, "italic"), command=reset_score)
reset_button.grid(row=1, column=0, columnspan=2, rowspan=1)
# [--------------------COUNTDOWN & CARD FLIP MECHANISM-------------------]


def count_down(count):
    global timer
    # To make sure the text only changes once, not with every count
    if count == 4:
        canvas.itemconfig(remember_text, text=random.choice(WHITE_CARD_QUOTES))
    # As long as the timer is above 0, keep counting
    if count > 0:
        canvas.itemconfig(timer_text, text=count)
        timer = window.after(1000, count_down, count - 1)
    # If time is over:
    else:
        canvas.itemconfig(remember_text, text=random.choice(GREEN_CARD_QUOTES))
        canvas.itemconfig(timer_text, text=count)
        # Stop timer
        window.after_cancel(timer)
        # Flip card
        flip_card()


def flip_card():
    # Change the title to "English" and change the card back color
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(card_img, image=card_back)
    # Put English word on card
    canvas.itemconfig(word_text, text=random_english, fill="white")


# [-------------------------------------------------------------------]

open_file()
window.mainloop()
