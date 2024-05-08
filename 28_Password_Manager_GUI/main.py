from tkinter import *
from tkinter import messagebox
import pyperclip
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    random_password = "".join(password_list)

    password.delete(first=0, last=END)
    password.insert(index=0, string=random_password)

    pyperclip.copy(text=random_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # Get data from inputs
    website_data = website.get()
    email_username_data = email_username.get()
    password_data = password.get()

    # Make sure user didn't leave any blanks
    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="oops", message="Please don't leave any fields empty!")
    else:
        # Message box to confirm save
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered:"
                                                                   f"\nEmail: {email_username_data}"
                                                                   f"\nPassword: {password_data}")
        # If the user confirms:
        if is_ok:
            # Empty the entry boxes
            website.delete(first=0, last=END)
            password.delete(first=0, last=END)

            # Write into the txt file
            with open(file="password_data.txt", mode="a") as file:
                file.write(f"{website_data} | {email_username_data} | {password_data}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Osama's Password Manager")
window.config(padx=30, pady=30)

# App logo
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Static texts
# Website text
website_text = Label(text="Website: ", pady=5)
website_text.grid(row=1, column=0)
# Email text
email_text = Label(text="Email/Username: ", pady=5)
email_text.grid(row=2, column=0)
# Password text
password_text = Label(text="Password: ", pady=5)
password_text.grid(row=3, column=0)

# Input boxes
# Website input
website = Entry(width=52)
website.grid(row=1, column=1, columnspan=2, sticky="w")
website.focus()
# Email/Username input
email_username = Entry(width=52)
email_username.insert(index=0, string="example@gmail.com")
email_username.grid(row=2, column=1, columnspan=2, sticky="w")
# Password input
password = Entry(width=30)
password.grid(row=3, column=1, sticky="w")

# Buttons
# Generate password button
generate = Button(text="Generate Password", width=14, command=generate_password)
generate.grid(row=3, column=2)

# Add button
generate = Button(text="Add", width=44, pady=4, command=save)
generate.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
