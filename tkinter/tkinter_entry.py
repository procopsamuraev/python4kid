"""
from tkinter import *

root = Tk()
root.title("Welcome to entry app")

message = StringVar()
print(message)
print(type(message))
message.set("Any")
print(message)
print(message.get())
root.mainloop()


from tkinter import *

root = Tk()
root.title("ex_1")
text = Entry(root, width=50)
text.insert(0,"Текстовое поле вводит и выводит текст только одной строкой")
text.pack()
root.mainloop()

"""
"""
from tkinter import *


def paste_message():
    message.set("The button clicked")


def clear_message():
    message.set("")


root = Tk()
root.title("GUI на Python")

message = StringVar()
# entry_message = Entry(textvariable=message)
# entry_message.pack()
entry = Entry(textvariable=message)
entry.pack()

button_paste = Button(text="Paste", command=paste_message)
button_paste.pack()

button_clear = Button(text="Clear", command=clear_message)
button_clear.pack()

root.mainloop()
"""

"""
from tkinter import *


def paste_message():
    # clear_message()
    entry_message.delete(0,END)
    entry_message.insert(0, "The button clicked")


def clear_message():
    entry_message.delete(0, END)


root = Tk()
root.title("GUI на Python")

entry_message = Entry(root, width=20)
entry_message.pack()

button_paste = Button(text="Paste", command=paste_message)
button_paste.pack()

button_clear = Button(text="Clear", command=clear_message)
button_clear.pack()

root.mainloop()
"""

"""
# ex 4
from tkinter import *


def copy_console():
    print(message.get())


root = Tk()
root.title("Ex_4")

message = StringVar()
entry = Entry(textvariable=message)
entry.pack()
entry.insert(0, "test")

button_copy = Button(text="Copy to console", command=copy_console)
button_copy.pack()

root.mainloop()

"""
# ex 5
"""
from tkinter import *


def copy_console():
    print(entry.get())


root = Tk()
root.title("Ex_5")

entry = Entry()
entry.pack()
entry.insert(0, "test")

button_copy = Button(text="Copy to console", command=copy_console)
button_copy.pack()

root.mainloop()
"""
# ex 6
"""
from tkinter import *


def print_raw():
    print(f'{message_1.get()}\n{message_2.get()}')


def print_format():
    print(f'"Value of first field: {message_1.get()}"\n"Value of second field: {message_2.get()}"')


root = Tk()
root.title("Ex_6")

message_1 = StringVar()
entry_1 = Entry(textvariable=message_1)
entry_1.pack()
entry_1.insert(0, "test1")

message_2 = StringVar()
entry_2 = Entry(textvariable=message_2)
entry_2.pack()
entry_2.insert(0, "test2")

button_copy = Button(text="print raw", command=print_raw)
button_copy.pack()
button_format = Button(text="print format text", command=print_format)
button_format.pack()

root.mainloop()

"""

"""
# ex 7
from tkinter import *


def copy_text():
    message_2.set(message_1.get())


root = Tk()
root.title("Ex_7")

message_1 = StringVar()
entry_1 = Entry(textvariable=message_1)
entry_1.pack()

button_copy = Button(text="copy", command=copy_text)
button_copy.pack()

message_2 = StringVar()
entry_2 = Entry(textvariable=message_2)
entry_2.pack()

root.mainloop()
"""
"""
# ex 8
from tkinter import *


def copy_text():
    message_1_str = message_1.get().strip()
    if message_1_str:
        message_2.set(f'"{message_1_str}", - its the >first entry content')


root = Tk()
root.title("Ex_8")

message_1 = StringVar()
entry_1 = Entry(textvariable=message_1)
entry_1.pack()

button_copy = Button(text="copy", command=copy_text)
button_copy.pack()

message_2 = StringVar()
entry_2 = Entry(textvariable=message_2)
entry_2.pack()

root.mainloop()
"""
"""
# ex 9
from tkinter import *


def copy_text():
    line_1 = message_1.get().strip().title()
    line_2 = message_2.get().strip().title()
    if line_1 and line_2:
        message_3.set(f'{line_1} {line_2}')


root = Tk()
root.title("Ex_8")

message_1 = StringVar()
entry_1 = Entry(textvariable=message_1)
entry_1.pack()

message_2 = StringVar()
entry_2 = Entry(textvariable=message_2)
entry_2.pack()

button_copy = Button(text="copy", command=copy_text)
button_copy.pack()

message_3 = StringVar()
entry_3 = Entry(textvariable=message_3)
entry_3.pack()

root.mainloop()

"""