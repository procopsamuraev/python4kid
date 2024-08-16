from tkinter import *


def print_button_addr(address):
    if text.get(1.0).isalpha():
        text.insert(END,f', {address}')
    else:
        text.insert(END, address)


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
button = Button(root, text="A8", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=lambda: print_button_addr("A8"))
button.grid(column=1, row=1)
button = Button(root, text="B8", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=lambda: print_button_addr("B8"))
# button = Button(root, text="B8", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=lambda address = button["text"]: print_button_addr(address))
button.grid(column=2, row=1)
button = Button(root, text="C8", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=lambda: print_button_addr("C8"))
button.grid(column=3, row=1)
button = Button(root, text="D8", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=lambda: print_button_addr("D8"))
button.grid(column=4, row=1)

button = Button(root, text="7", bg="yellow")
button.grid(column=0, row=2)
button = Button(root, text="A7", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=lambda: print_button_addr("A7"))
button.grid(column=1, row=2)
button = Button(root, text="B7", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=lambda: print_button_addr("B7"))
button.grid(column=2, row=2)
button = Button(root, text="C7", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=lambda: print_button_addr("C7"))
button.grid(column=3, row=2)
button = Button(root, text="D7", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=lambda: print_button_addr("D7"))
button.grid(column=4, row=2)

button = Button(root, text="6", bg="yellow")
button.grid(column=0, row=3)
button = Button(root, text="A6", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=lambda: print_button_addr("A6"))
button.grid(column=1, row=3)
button = Button(root, text="B6", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=lambda: print_button_addr("B6"))
button.grid(column=2, row=3)
button = Button(root, text="C6", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=lambda: print_button_addr("C6"))
button.grid(column=3, row=3)
button = Button(root, text="D6", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=lambda: print_button_addr("D6"))
button.grid(column=4, row=3)

button = Button(root, text="5", bg="yellow")
button.grid(column=0, row=4)
button = Button(root, text="A5", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=lambda: print_button_addr("A5"))
button.grid(column=1, row=4)
button = Button(root, text="B5", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=lambda: print_button_addr("A5"))
button.grid(column=2, row=4)
button = Button(root, text="C5", bg="brown", fg="brown", activebackground="brown", activeforeground="brown", command=lambda: print_button_addr("A5"))
button.grid(column=3, row=4)
button = Button(root, text="D5", bg="yellow", fg="yellow", activebackground="yellow", activeforeground="yellow", command=lambda: print_button_addr("A5"))
button.grid(column=4, row=4)

text = Text(root, height=9, width=15)
text.grid(column=5, row=0, rowspan=10)

root.mainloop()