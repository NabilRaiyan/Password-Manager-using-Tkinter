from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password = password_letters + password_number + password_symbol

    random.shuffle(password)

    new_password = "".join(password)
    pass_entry.insert(0, new_password)
    pyperclip.copy(new_password)






# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    no = "#: "
    website = web_entry.get()
    password = pass_entry.get()
    email = email_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}
    is_ok = messagebox.askokcancel(title=website,
                                   message=f"These are the info which is entered: \nEmail: {email}\nPassword: {password}")

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                 data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ______________________________Find Password_________________________

def search_pass():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} found.")



# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)


# Label function
def label(name, col, row):
    label_name = Label(text=name, font=("Courier", 15, "bold"))
    label_name.grid(column=col, row=row)


website_label = label("Website:", 0, 1)
email_label = label("Email/Username:", 0, 2)
password_label = label("Password:", 0, 3)

# Entry function

web_entry = Entry(width=35)
web_entry.grid(column=1, row=1)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2)
email_entry.insert(0, string="rraiyan77@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)


# Button function
def button(name, col, row, width, command):
    button_name = Button(text=name, width=width, command=command)
    button_name.grid(column=col, row=row, padx=10, pady=10)


search_button = button("Search", 2, 1, width=21, command=search_pass)
add_button = button("Add", 1, 4, width=35, command=save)
generate_button = button("Generate", 2, 3, width=19, command=generate_pass)

window.mainloop()
