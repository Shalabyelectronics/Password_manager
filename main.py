from tkinter import *
from random import choices
import os

# ------------------Generate Password Function------------------#
# ---------------PASSWORD CONSTANTTs-------------------#
from tkinter import messagebox

'''
Passwords should contain three of the four character types:

Uppercase letters: A-Z
Lowercase letters: a-z
Numbers: 0-9
Symbols: ~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/
'''
UPPERCASE = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
LOWERCASE = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
UPPERCASE_LIST = list(UPPERCASE.split(" "))
LOWERCASE_LIST = list(LOWERCASE.split(" "))
NUMBER_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SYMBOLS = '''~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/'''
SYMBOLS_LIST = list(SYMBOLS)
pass_generated = None


# ----------------ٍSave Data to text file-----------#
def save_user_registration():
    if len(web_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        fill_all_gaps = messagebox.showwarning(title="Attention", message="Please do not leave any gaps empty!!")
    elif len(web_entry.get()) != 0 and len(email_entry.get()) != 0 and len(password_entry.get()) != 0:
        ask_user = messagebox.askyesno(title="Conformation", message="Do you want to save current registration data?")
        if ask_user:
            with open("data.txt", mode="a+") as user_registration:
                user_registration.seek(0)
                data = user_registration.read(100)
                if len(data) > 0:
                    user_registration.write("\n")
                user_registration.write(f"{web_entry.get()}| {email_entry.get()} | {password_entry.get()}")


# ------------------Generate function--------------#
def generate_password():
    global pass_generated
    upper_random_list = choices(UPPERCASE_LIST, k=4)
    lower_random_list = choices(LOWERCASE_LIST, k=4)
    numbers_random_list = [str(n) for n in choices(NUMBER_LIST, k=4)]
    symbols_random_list = choices(SYMBOLS_LIST, k=4)
    mixed_pass = upper_random_list + lower_random_list + numbers_random_list + symbols_random_list
    pass_generated_list = choices(mixed_pass, k=16)
    pass_generated = "".join(map(str, pass_generated_list))
    if len(password_entry.get()) == 0:
        password_entry.insert(END, pass_generated)
    else:
        password_entry.delete(0, last=16)
        password_entry.insert(END, pass_generated)


# ------------------ Password Manager GUI ---------------------#
window = Tk()
window.title("Password Manager v1.0")
window.config(padx=50, pady=50)
# Add the locker photo
locker_img = PhotoImage(file="a_lock_exsml.png")
# create a canvas object from canvas class.
canvas = Canvas(width=200, height=300)
# add the locker_img to canvas object.
canvas.create_image(90, 150, image=locker_img)
canvas.grid(column=1, row=0)
# create a website label
web_label = Label(text="Website :")
web_label.grid(column=0, row=1, sticky=W)
# create a website entry
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, sticky=W)
# create a email_label
email_label = Label(text="E-mail :")
email_label.grid(column=0, row=2, sticky=W)
# create an e-mail entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, sticky=W)
# create a password label
password_label = Label(text="Password :")
password_label.grid(column=0, row=3, sticky=W)
# create a password entry
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky=W)
# create a generate password button.
generate_pass = Button(text="Generate", command=generate_password)
generate_pass.grid(column=1, row=3, pady=5, sticky=E)
# create add button
add_button = Button(text="add", width=15, command=save_user_registration)
add_button.grid(column=1, row=4, pady=15)
window.mainloop()
