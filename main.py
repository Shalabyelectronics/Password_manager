from tkinter import *
from tkinter import messagebox
from random import choices, shuffle
import pyperclip
import json


# ---------------Search Function------------------#
def search_data():
    website = web_entry.get().lower()
    with open("data.json", "r") as data:
        data_file = json.load(data)
    if website in data_file:
        password = data_file[website]["Password"]
        email_username = data_file[website]["E-mail"]
        messagebox.showinfo(title="Login Data Founded", message=f"E-mail/Username : {email_username}\n"
                                                                f"Password : {password}")
    else:
        messagebox.showwarning(title="Attention", message=f"There is no data related to {website.title()}")


# ---------------Add Data Function----------------#
def dump_data(user_data):
    with open("data.json", "w") as data:
        json.dump(user_data, data, indent=4)


# ---------------Save data Function---------------#
def save_data(user_data):
    try:
        with open("data.json", "r") as data:
            data_file = json.load(data)
    except FileNotFoundError:
        dump_data(user_data)
    else:
        data_file.update(user_data)
        dump_data(data_file)
    finally:
        web_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)


# ----------------ٍSave Data to text file-----------#
def save_user_registration():
    if len(web_entry.get().lower()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Attention", message="Please do not leave any fields empty!!")
    else:
        user_data = {
            web_entry.get():
                {
                    "E-mail": email_entry.get(),
                    "Password": password_entry.get()
                }
        }
        ask_user = messagebox.askyesno(title="Conformation", message=f"Your data you entered for : {web_entry.get()}\n"
                                                                     f"Email/Username: {email_entry.get()}\n"
                                                                     f"Password: {password_entry.get()}\n"
                                                                     f"Is it ok to save it?")
        if ask_user:
            save_data(user_data)


# ------------------Generate function--------------#
# ------------------Generate Password Function------------------#
# ---------------PASSWORD CONSTANTTs-------------------#


'''
Passwords should contain three of the four character types:

Uppercase letters: A-Z
Lowercase letters: a-z
Numbers: 0-9
Symbols: ~`!@#$%^&*()_-+={[}]|:;"'<,>.?/
'''
UPPERCASE = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
LOWERCASE = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
UPPERCASE_LIST = list(UPPERCASE.split(" "))
LOWERCASE_LIST = list(LOWERCASE.split(" "))
NUMBER_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SYMBOLS = "!@#$%&*?/"
SYMBOLS_LIST = list(SYMBOLS)


def generate_password():
    upper_random_list = choices(UPPERCASE_LIST, k=4)
    lower_random_list = choices(LOWERCASE_LIST, k=4)
    numbers_random_list = [str(n) for n in choices(NUMBER_LIST, k=4)]
    symbols_random_list = choices(SYMBOLS_LIST, k=4)
    mixed_pass = upper_random_list + lower_random_list + numbers_random_list + symbols_random_list
    shuffle(mixed_pass)
    pass_generated = "".join(map(str, mixed_pass))
    if len(password_entry.get()) == 0:
        password_entry.insert(0, pass_generated)
        pyperclip.copy(password_entry.get())
    else:
        password_entry.delete(0, END)
        password_entry.insert(END, pass_generated)


# ------------------ Password Manager GUI ---------------------#
window = Tk()
window.title("Password Manager v1.0")
window.config(padx=20, pady=20)
# Add the locker photo
locker_img = PhotoImage(file="a_lock_exsml.png")
# create a canvas object from canvas class.
canvas = Canvas(width=200, height=291)
# add the locker_img to canvas object.
canvas.create_image(100, 140, image=locker_img)
canvas.grid(column=1, row=0)
# create a website label
web_label = Label(text="Website :")
web_label.grid(column=0, row=1, sticky=W)
# create a website entry
web_entry = Entry(width=32)
web_entry.focus()
web_entry.grid(column=1, row=1)
# create search button
search_button = Button(text="Search", width=10, command=search_data)
search_button.grid(column=2, row=1)
# create a email_label
email_label = Label(text="E-mail/Username :")
email_label.grid(column=0, row=2, sticky=W)
# create an e-mail entry
email_entry = Entry(width=46)
email_entry.grid(column=1, row=2, pady=5, columnspan=2)
# create a password label
password_label = Label(text="Password :")
password_label.grid(column=0, row=3, sticky=W)
# create a password entry
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)
# create a generate password button.
generate_pass = Button(text="Generate", width=10, command=generate_password)
generate_pass.grid(column=2, row=3)
# create add button
add_button = Button(text="add", width=40, command=save_user_registration)
add_button.grid(column=1, row=4, pady=15, columnspan=2)
window.mainloop()
