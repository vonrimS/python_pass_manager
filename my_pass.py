from tkinter import *


# ----- PASSWORD GENERATOR -----

# ----- SAVE PASSWORD -----

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

email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2, sticky='w', pady=10)

password_input = Entry(width=18)
password_input.grid(row=3, column=1, sticky='w', pady=10)

# Buttons
gen_button = Button(text="Generate Password")
gen_button.grid(row=3, column=2, pady=10, sticky='e')

add_button = Button(text="Add", width=34)

add_button.grid(row=4, column=1, columnspan=2, sticky='w', pady=10)

window.mainloop()