import tkinter.ttk
from tkinter import *
from tkinter.ttk import *

error = "error"
operators = "+-*/="
current_operator = "="
"""

true: before we press enter
000 -> 0
01001 -> 1001
0+-003 -> 0-3
1-2+2/2= -> 1-2+2/2=0 
1-2+2/2+8 -> 1-2+2/2+8
1-2+2/01+8 -> 1-2+2/1+8
1-2+2/0- -> 1-2+2/
 
"""


def backspace():
    string = num.get()
    string = string.removesuffix(string[-1])
    num.set(string if string else "0")


def calculation():
    clean_string()
    result = str(eval(num.get()))
    result = result.rstrip('0').removesuffix('.') if '.' in result else result
    num.set(f"{num.get()}={result}")


def clean_string():
    string = num.get()
    tail_string = string.rpartition(f"{current_operator}")[-1] if current_operator else ''
    string = string.rstrip('0').rstrip('.') if '.' in tail_string else string
    num.set(string)


def set_operator(operator):
    # to avoid for iterations
    global current_operator
    clean_string()
    string = num.get()
    string = f"{string.rstrip(operators)}{operator}"
    num.set(string)
    current_operator = operator


def set_number(number):
    string = num.get()
    # remove heading zeros at the beginning
    string = string.lstrip('0') if not string.replace('0', '') else string
    # remove zeros
    if current_operator:
        tail = string.rpartition(f"{current_operator}0")[-1]
        string = string.replace(f"{current_operator}0", f"{current_operator}") if not tail else string
    num.set(f"{string}{number}")


# clear entry, clear last number till next operator
def clear_entry():
    string = num.get()
    string = string.rstrip('1234567890,.')
    num.set(string if string else "0")


def set_dot():
    string = f"{num.get().rstrip('.')}."
    # adding 0 before "dot"
    for operator in operators:
        string = string.replace(f"{operator}.", f"{operator}0.")
    num.set(string)


root = Tk()
root.title("Calculator")

num = StringVar()
num.set('0')
frame_entry = Frame(root)
frame_entry.pack()
entry = Entry(frame_entry, text=num, width=26, justify="right")
entry.grid(sticky=EW)

frame_buttons = Frame(root)
frame_buttons.pack()
button_mc = Button(frame_buttons, width=4, text="MC")
button_mc.grid(column=0, row=1)
button_mr = Button(frame_buttons, width=4, text="MR")
button_mr.grid(column=1, row=1)
button_ms = Button(frame_buttons, width=4, text="MS")
button_ms.grid(column=2, row=1)
button_m_add = Button(frame_buttons, width=4, text="M+")
button_m_add.grid(column=3, row=1)
button_m_subtract = Button(frame_buttons, width=4, text="M-")
button_m_subtract.grid(column=4, row=1)
button_backspace = Button(frame_buttons, width=4, text=chr(8592), command=backspace)
button_backspace.grid(column=0, row=2)
button_ce = Button(frame_buttons, width=4, text="CE", command=clear_entry)
button_ce.grid(column=1, row=2)
button_c = Button(frame_buttons, width=4, text="C", command=lambda: num.set('0'))
button_c.grid(column=2, row=2)
button_toggle = Button(frame_buttons, width=4, text=chr(177))
button_toggle.grid(column=3, row=2)
button_square_root = Button(frame_buttons, width=4, text=chr(8730))
button_square_root.grid(column=4, row=2)
button_7 = Button(frame_buttons, width=4, text="7", command=lambda: set_number("7"))
button_7.grid(column=0, row=3)
button_8 = Button(frame_buttons, width=4, text="8", command=lambda: set_number("8"))
button_8.grid(column=1, row=3)
button_9 = Button(frame_buttons, width=4, text="9", command=lambda: set_number("9"))
button_9.grid(column=2, row=3)
button_division = Button(frame_buttons, width=4, text="/", command=lambda: set_operator("/"))
button_division.grid(column=3, row=3)
button_percentage = Button(frame_buttons, width=4, text="%")
button_percentage.grid(column=4, row=3)
button_4 = Button(frame_buttons, width=4, text="4", command=lambda: set_number("4"))
button_4.grid(column=0, row=4)
button_5 = Button(frame_buttons, width=4, text="5", command=lambda: set_number("5"))
button_5.grid(column=1, row=4)
button_6 = Button(frame_buttons, width=4, text="6", command=lambda: set_number("6"))
button_6.grid(column=2, row=4)
button_multiplication = Button(frame_buttons, width=4, text="*", command=lambda: set_operator("*"))
button_multiplication.grid(column=3, row=4)
button_rational = Button(frame_buttons, width=4, text="1/x", command=lambda: set_number("1/x"))
button_rational.grid(column=4, row=4)
button_1 = Button(frame_buttons, width=4, text="1", command=lambda: set_number("1"))
button_1.grid(column=0, row=5)
button_2 = Button(frame_buttons, width=4, text="2", command=lambda: set_number("2"))
button_2.grid(column=1, row=5)
button_3 = Button(frame_buttons, width=4, text="3", command=lambda: set_number("3"))
button_3.grid(column=2, row=5)
button_subtract = Button(frame_buttons, width=4, text="-", command=lambda: set_operator("-"))
button_subtract.grid(column=3, row=5)
button_equal = Button(frame_buttons, width=4, text="=", command=calculation)
button_equal.grid(column=4, row=5, rowspan=2, sticky=NS)
button_0 = Button(frame_buttons, width=4, text="0", command=lambda: set_number("0"))
button_0.grid(column=0, columnspan=2, row=6, sticky=EW)
button_dot = Button(frame_buttons, width=4, text=".", command=set_dot)
button_dot.grid(column=2, row=6)
button_sum = Button(frame_buttons, width=4, text="+", command=lambda: set_operator("+"))
button_sum.grid(column=3, row=6)

root.mainloop()
