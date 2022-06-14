from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(bg="white")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=350, height=253, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="lock.png")
canvas.create_image(210, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Input

website_label = Label(text="Website", bg="white")
website_label.grid(row=1, column=0)
website_input = Entry(width=30)
website_input.grid(row=1, column=1, columnspan=2)

username_label = Label(text="Email/Username", bg="white")
username_label.grid(row=2, column=0)
website_input = Entry(width=30)
website_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password", bg="white")
password_label.grid(row=3, column=0)
password_input = Entry()
password_input.grid(row=3, column=1)
gen_button = Button(text="Generate Password")
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=50)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()