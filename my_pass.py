from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import os

# ----- PASSWORD GENERATOR -----
import string
import random

def generate_pass(pass_len=15):
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    numbers = string.digits
    symbols = "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
    password_list = [upper_letters, lower_letters, numbers, symbols]
    password = ''

    while pass_len > 0:
        symbol = password_list[random.randint(0, len(password_list)-1)]
        password += symbol[random.randint(0, len(symbol)-1)]
        pass_len -= 1
    password_input.insert(0, password)
    # Copy generated password
    pyperclip.copy(password)


# ----- VALIDATE EMAIL ADDRESS -----
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    """ Check email according to regex template. Return False if it's not match the regex expression.
    """
    email = ''.join(email)
    match = re.fullmatch(regex, email)
    if match is not None:
        return True
    else:
        messagebox.showinfo(title="Invalid email", message="Please check your email field, address is not valid!")
        return False

# ----- SAVE PASSWORD -----
def save_password():
    """ Save password (FIFO) in *.json file in the root directory. """
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    file_name = "data.json"
    input_ok = check_inputs(website, email, password)

    if input_ok:
        # Prepare new data to insert
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }
        # Temporally assign new_data to data
        data = new_data
        # Check if file has some content
        try:
            f = open(file_name, 'r')
        except FileNotFoundError:
            f = open(file_name, 'w')
            json.dump(data, f, indent=4)
        else:
            if os.stat(file_name).st_size != 0:
                # If file is empty then reassign found file deserialized content to 'data' variable
                data = json.load(f)
                data.update(new_data)
                f.close()
            f = open(file_name, 'w')
            json.dump(data, f, indent=4)

        finally:
            clean_inputs()
            f.close()


# ----- CLEAN INPUT FIELDS -----
def clean_inputs():
    """Clean all user inputs, restore placeholder text for an email and focus bock on the first input field."""
    website_input.delete(0, END)
    email_input.delete(0, END)
    email_input.insert(0, "your_email@gmail.com")
    password_input.delete(0, END)
    website_input.focus()

def check_inputs(website, email, password):
    """Check all user inputs, returns False either website or password field is empty."""
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="...something goes wrong", message="Please don't leave any fields empty!")
        return False
    else:
        if isValid(email):
            return True
        else:
            return False


# ----- UI SETUP -----
window = Tk()
window.title("Password Manager")
window.config(bg="white")
window.config(padx=50, pady=50)

# App logo canvas
canvas = Canvas(width=350, height=253, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="lock.png")
canvas.create_image(210, 100, image=lock_img)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = Label(text="Website", bg="white")
website_label.grid(row=1, column=0, padx=10, sticky='e')

username_label = Label(text="Email/Username", bg="white")
username_label.grid(row=2, column=0, padx=10, sticky='e')

password_label = Label(text="Password", bg="white")
password_label.grid(row=3, column=0, padx=10, sticky='e')

# Entries
website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2, sticky='w', pady=10)
website_input.focus()

email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2, sticky='w', pady=10)
email_input.insert(0, "your_email@gmail.com")

password_input = Entry(width=18)
password_input.grid(row=3, column=1, sticky='w', pady=10)

# Buttons
gen_button = Button(text="Generate Password", command=generate_pass)
gen_button.grid(row=3, column=2, pady=10, sticky='e')
add_button = Button(text="Add", width=34, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='w', pady=10)

window.mainloop()
