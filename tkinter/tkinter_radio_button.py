from tkinter import *
from tkinter.ttk import *


def print_console():
    print(rb_var.get()=='Beijing')


root = Tk()
rb_var = StringVar()
label=Label(text='What is the capital of China?')
label.pack()
Radiobutton(text='Beijing', variable=rb_var, value='Beijing', command=print_console).pack(anchor=W)
Radiobutton(text='HK', variable=rb_var, value='HK', command=print_console).pack(anchor=W)
Radiobutton(text='Tokyo', variable=rb_var, value='Tokya', command=print_console).pack(anchor=W)
Radiobutton(text='Taipei', variable=rb_var, value='Taipei', command=print_console).pack(anchor=W)
root.mainloop()