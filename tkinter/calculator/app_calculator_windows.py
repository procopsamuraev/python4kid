import tkinter.ttk
from tkinter import *
from tkinter.ttk import *
import math

error = "error"
operators = "+-*/="
current_operator = "="
error0 = "Er0: division by zero"

"""
true: before we press enter
000 -> 0
01001 -> 1001
0+-003 -> 0-3
1-2+2/2= -> 1-2+2/2=0 
1-2+2/2+8 -> 1-2+2/2+8
1-2+2/01+8 -> 1-2+2/1+8
1-2+2/0+8= -> error 
1-2+2/0-= ->  error
8-1=34 -> 34
5+07  => 5+7
5+705 => 5+705 
9"+-" => -9
-9"+-" => 9
2-3"+-" => 2--3
2--3
2+-3
2+-8--5*-3/-0.8 => 2+-8--5*-3/-0.8=12.75
"""


def backspace():
    line = num.get()
    if '=' in line:
        line = '0'
    elif not line.endswith(('-', '+', '/', '*')):
        line = line[:-1]
    num.set(line)


def calculation() -> str:
    line = num.get()
    rnumber = find_rnumber(line)
    return error0 if rnumber == '0' and line.replace(rnumber, '').endswith('/') else str(eval(line))


def display_result():
    num.set(str(calculation()).removesuffix('.0'))


def find_rnumber(line):
    index_operator = max(line.rfind('/'), line.rfind('*'), line.rfind('+'), line.rfind('-'), line.rfind('='))
    negative_number_true = line[index_operator] == "-" and line[index_operator - 1] in operators or index_operator == 0
    return line[index_operator:] if negative_number_true else line[index_operator + 1:]


def toggle():
    line = num.get()
    rnumber = find_rnumber(line)
    line = line.removesuffix(rnumber)
    line = f"{line}{rnumber.removeprefix('-')}" if rnumber.startswith('-') else f"{line}-{rnumber}"
    num.set(line) if rnumber.removeprefix('-').replace('.', '').isdigit() else None


def set_dot():
    line = num.get()
    rnumber = find_rnumber(line)
    if not rnumber:
        line = f"{line}0."
    elif '.' not in rnumber:
        line = f"{line}."
    num.set(line)


def set_operator(operator):
    line = num.get()
    rnumber = find_rnumber(line)
    if rnumber == '0' and line.replace(rnumber, '').endswith('/'):
        num.set(f"Error: division by 0")
    else:
        num.set(f"{line.rstrip(operators)}{operator}")


def set_number(number):
    line = num.get()
    if '=' in line:
        line = number
    elif find_rnumber(line).removeprefix('-') == "0":
        line = f"{line.removesuffix('0')}{number}"
    else:
        line = f"{line}{number}"
    num.set(line)


def clear_end():
    line = num.get().rstrip('1234567890.')
    num.set('0' if not line or '=' in line else line)


# 1/x
def rational():
    line = calculation()
    num.set(f"Error: division by 0") if line == 0 else num.set(f"1/{line}")
    display_result()


def sqrt():
    line = calculation()
    if line < '0':
        num.set(f"Error: sqrt from negative")
    else:
        num.set(f"{line}**0.5")
        display_result()


def percentage():
    return


root = Tk()
root.title("Calculator")

num = StringVar()
num.set('0')
frame_entry = Frame(root)
frame_entry.pack()
entry = Entry(frame_entry, textvariable=num, width=26, justify="right")
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
button_ce = Button(frame_buttons, width=4, text="CE", command=clear_end)
button_ce.grid(column=1, row=2)
button_c = Button(frame_buttons, width=4, text="C", command=lambda: num.set('0'))
button_c.grid(column=2, row=2)
button_toggle = Button(frame_buttons, width=4, text=chr(177), command=toggle)
button_toggle.grid(column=3, row=2)
button_square_root = Button(frame_buttons, width=4, text=chr(8730), command=sqrt)
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
button_rational = Button(frame_buttons, width=4, text="1/x", command=rational)
button_rational.grid(column=4, row=4)
button_1 = Button(frame_buttons, width=4, text="1", command=lambda: set_number("1"))
button_1.grid(column=0, row=5)
button_2 = Button(frame_buttons, width=4, text="2", command=lambda: set_number("2"))
button_2.grid(column=1, row=5)
button_3 = Button(frame_buttons, width=4, text="3", command=lambda: set_number("3"))
button_3.grid(column=2, row=5)
button_subtract = Button(frame_buttons, width=4, text="-", command=lambda: set_operator("-"))
button_subtract.grid(column=3, row=5)
button_equal = Button(frame_buttons, width=4, text="=", command=display_result)
button_equal.grid(column=4, row=5, rowspan=2, sticky=NS)
button_0 = Button(frame_buttons, width=4, text="0", command=lambda: set_number("0"))
button_0.grid(column=0, columnspan=2, row=6, sticky=EW)
button_dot = Button(frame_buttons, width=4, text=".", command=set_dot)
button_dot.grid(column=2, row=6)
button_sum = Button(frame_buttons, width=4, text="+", command=lambda: set_operator("+"))
button_sum.grid(column=3, row=6)

root.mainloop()
