from tkinter import *

root = Tk()
root.title("Welcome to the second entry app")

label_login = Label(root, text="Login")
label_login.grid(column=0, row=0, sticky=E)
field_login = Entry(root, width=10)
field_login.grid(column=1, row=0)

label_pass = Label(root, text="Password")
label_pass.grid(column=0, row=1, sticky=E)
field_pass = Entry(root, width=10)
field_pass.grid(column=1, row=1)

button = Button(root, text="Enter")
button.grid(column=0, row=2, columnspan=2, sticky=NSEW)

root.mainloop()