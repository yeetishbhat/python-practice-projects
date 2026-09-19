from random import random
from tkinter import *
from tkinter import messagebox
import random
import json

#---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char


    password_entry.delete(0, END)
    password_entry.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please enter all fields")

    is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered : \n email: {email} \n password: {password} \n is it ok to save?")

    if is_ok:
        try:
            with open("password.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("password.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("password.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

#-----------------FIND PASSWORD -----------------------------------------#

def search():
    website = website_entry.get()
    try:
        with open("password.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "data not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email = {email} \n password = {password}")
        else:
            messagebox.showerror("Error", f"no details related to {website} found   ")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.configure(padx=20, pady=20)

canvas = Canvas(width=200,height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(row=0,column=1)

website_lable = Label(text="Website")
website_lable.grid(row=1,column=0)

website_entry = Entry(width=20)
website_entry.grid(row=1,column=1)
website_entry.focus()


wesite_search = Button (text="Search", command=search , width=20)
wesite_search.grid(row=1,column=2)

email_lable = Label(text="Email/mail id")
email_lable.grid(row=2,column=0)

email_entry = Entry(width=45)
email_entry.grid(row=2,column=1, columnspan=2)

password_lable = Label(window, text="Password")
password_lable.grid(row=3,column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

generate_button = Button( text="Generate Password", command=generate_password, width=20)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add", width=36 , command=save)
add_button.grid(row=4,column=1, columnspan=2)

window.mainloop()