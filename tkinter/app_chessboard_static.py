from tkinter import *


def print_button_addr(row1, column1):
    button_coordinate=f'{column1}{row1}'.title()
    if text.get(1.0).isalpha():
        text.insert(END, f', {button_coordinate}')
    else:
        text.insert(END, button_coordinate)



root = Tk()
root.title("chessboard")

button = Button(root, text='', bg="yellow")
button.grid(column=0, row=0)
button = Button(root, text='A', bg="yellow")
button.grid(column=1, row=0)
button = Button(root, text='B', bg="yellow")
button.grid(column=2, row=0)
button = Button(root, text='C', bg="yellow")
button.grid(column=3, row=0)
button = Button(root, text='D', bg="yellow")
button.grid(column=4, row=0)
button = Button(root, text="8", bg="yellow")
button.grid(column=0, row=1)
button = Button(root, text="A8", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=print_button_addr)
button.grid(column=1, row=1)
button = Button(root, text="B8", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=print_button_addr)
button.grid(column=2, row=1)
button = Button(root, text="C8", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=print_button_addr)
button.grid(column=3, row=1)
button = Button(root, text="D8", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=print_button_addr)
button.grid(column=4, row=1)

button = Button(root, text="7", bg="yellow")
button.grid(column=0, row=2)
button = Button(root, text="A7", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=print_button_addr)
button.grid(column=1, row=2)
button = Button(root, text="B7", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=print_button_addr)
button.grid(column=2, row=2)
button = Button(root, text="C7", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=print_button_addr)
button.grid(column=3, row=2)
button = Button(root, text="D7", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=print_button_addr)
button.grid(column=4, row=2)

button = Button(root, text="6", bg="yellow")
button.grid(column=0, row=3)
button = Button(root, text="A6", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=print_button_addr)
button.grid(column=1, row=3)
button = Button(root, text="B6", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=print_button_addr)
button.grid(column=2, row=3)
button = Button(root, text="C6", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=print_button_addr)
button.grid(column=3, row=3)
button = Button(root, text="D6", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=print_button_addr)
button.grid(column=4, row=3)

button = Button(root, text="5", bg="yellow")
button.grid(column=0, row=4)
button = Button(root, text="A5", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=print_button_addr)
button.grid(column=1, row=4)
button = Button(root, text="B5", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=print_button_addr)
button.grid(column=2, row=4)
button = Button(root, text="C5", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=print_button_addr)
button.grid(column=3, row=4)
button = Button(root, text="D5", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=print_button_addr)
button.grid(column=4, row=4)

root.mainloop()