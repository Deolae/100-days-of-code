from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json

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
# ---------------------------- SEARCH MECHANISM ------------------------------- #


def find_password():
    # Get the name in the input box
    website_name = website.get().lower()
    # Read the json file
    try:
        with open(file="password_data.json", mode="r") as file:
            data = json.load(file)
            # Check if the name matches a website name in the json file
            if website_name in data:
                # Show the email and password in a message box
                web_email = data[website_name]["email"]
                web_pass = data[website_name]["password"]
                messagebox.showinfo(title=website_name, message=f"Email: {web_email}\n" f"Password: {web_pass}")
            else:
                messagebox.showwarning(title="oops", message="No details for the website you've entered exists.")
    except FileNotFoundError:
        messagebox.showwarning(title="oops", message="No data file found, Try adding a website first.")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # Get data from inputs
    website_data = website.get().lower()
    email_username_data = email_username.get()
    password_data = password.get()
    new_data = {
        website_data: {
            "email": email_username_data,
            "password": password_data
        }
    }

    # Make sure user didn't leave any blanks
    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="oops", message="Please don't leave any fields empty!")
    else:
        # Try opening the file and reading data inside
        try:
            # Write into the json file
            with open(file="password_data.json", mode="r") as file:
                # read old data
                data = json.load(file)
                # update old data with new data
                data.update(new_data)
        # If failed to find file, create a new file and add the data in it
        except FileNotFoundError:
            with open(file="password_data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        # If found file, update the data in it
        else:
            with open(file="password_data.json", mode="w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
        # Either way, empty the input boxes
        finally:
            # Empty the entry boxes
            website.delete(first=0, last=END)
            password.delete(first=0, last=END)

# ---------------------------- UI SETUP ------------------------------- #
# Create the window


window = Tk()
window.title("Osama's Password Manager")
window.config(padx=30, pady=30)

# App logo
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Website text
website_text = Label(text="Website: ", pady=5)
website_text.grid(row=1, column=0)

# Email text
email_text = Label(text="Email/Username: ", pady=5)
email_text.grid(row=2, column=0)

# Password text
password_text = Label(text="Password: ", pady=5)
password_text.grid(row=3, column=0)

# Website input
website = Entry(width=30)
website.grid(row=1, column=1, sticky="w")
website.focus()

# Email/Username input
email_username = Entry(width=52)
email_username.insert(index=0, string="example@gmail.com")
email_username.grid(row=2, column=1, columnspan=2, sticky="w")

# Password input
password = Entry(width=30)
password.grid(row=3, column=1, sticky="w")

# Generate password button
generate = Button(text="Generate Password", width=14, command=generate_password)
generate.grid(row=3, column=2)

# Add button
generate = Button(text="Add", width=44, pady=4, command=save)
generate.grid(row=4, column=1, columnspan=2, sticky="w")

# Search button
search = Button(text="Search", width=14, command=find_password)
search.grid(row=1, column=2, sticky="w")

window.mainloop()
