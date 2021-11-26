from tkinter import *
import random

# ------------------Generate Password Function------------------#
# ---------------PASSWORD CONSTANTTs-------------------#
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
generate_pass = Button(text="Generate")
generate_pass.grid(column=1, row=3, pady=5, sticky=E)
# create add button
add_button = Button(text="add", width=15)
add_button.grid(column=1, row=4, pady=15)
window.mainloop()
