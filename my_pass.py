from tkinter import *
from tkinter import messagebox
import pyperclip


# ----- PASSWORD GENERATOR -----
import string
import random

def generate_pass(pass_len=15):
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    numbers = string.digits
    symbols = "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
    # pass_len = 10
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
    """ Check email according to regex template. Return False if it's not match the regex expression. """
    email = ''.join(email)
    match = re.fullmatch(regex, email)
    if match is not None:
        return True
    else:
        messagebox.showinfo(title="Invalid email", message="Please check your email field, address is not valid!")
        return False

# ----- SAVE PASSWORD -----
def save_password():
    """ Save password (FIFO) in *.txt file in the same directory. """
    input_ok = check_inputs()
    email = email_input.get()
    if not input_ok:
        messagebox.showinfo(title="...something goes wrong", message="Please don't leave any fields empty!")
    else:
        if isValid(email):
            is_ok = messagebox.askokcancel(title="Check the input before save",
                                   message=f"Summary: \n\nEmail/username: {email_input.get()}\n"
                                           f"Password: {password_input.get()}\n\nEverything is correct?")

            if is_ok:
                f = open('data.txt', 'a')
                f.write(f'{website_input.get()} | {email_input.get()} | {password_input.get()}\n')
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

def check_inputs():
    """Check all user inputs, returns False either website or password field is empty."""
    website = website_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        return False
    else:
        return True


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