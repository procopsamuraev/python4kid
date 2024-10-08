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

# fixme:
#  if = then clear all
#  and clear only till last operator


def backspace():
    line = num.get()
    line = '0' if line.rfind('=') >=0 else line
    line = line[:-1] if line[-1] not in operators else line
    num.set(line if line else "0")

# fixme: check string true before calculation
# delenie na null


def calculation():
    normalization_last_value()
    line = num.get()
    operator_last = line.rstrip('1234567890,.')[-1] if not line.replace('.', '').isdigit() else ''
    line_tail = line.rpartition(f"{operator_last}")[-1] if operator_last else ''
    num.set(line) if line.replace(operators, '').replace('.', '').isdigit() else "Error in the line"
    num.set(f"{line} = Error(division by 0)") if operator_last == "/" and line_tail == "0" else line
    result = str(eval(line)).removesuffix('.0')
    result = result.removesuffix('.0') # if '.' in result else result
    # result = result.rstrip('0').removesuffix('.') if '.' in result else result
    num.set(f"{num.get()}={result}")


def tail_line():
    line = num.get()
    operator_last = line.rstrip('1234567890,.')[-1] if not line.replace('.', '').isdigit() else ''
    line_tail = line.rpartition(f"{operator_last}")[-1] if operator_last else ''
    return line_tail


def toggle():
    line  = num.get()
    operator_last = line.rstrip('1234567890,.')[-1] if not line.replace('.', '').isdigit() else ''
    head, _sep, tail = line.rpartition(operator_last)
    num.set(f'{head}{_sep}-{tail}'.replace('--', '+').replace('+-', '-').replace('-+', '-').replace('*+', '*').replace('/+', '/'))


def normalization_last_value():
    line = num.get()
    operator_last = line.rstrip('1234567890,.')[-1] if not line.replace('.', '').isdigit() else ''
    line_tail = line.rpartition(f"{operator_last}")[-1] if operator_last else ''
    line = line.rstrip('0').rstrip('.') if '.' in line_tail else line
    num.set(line)


def set_operator(operator):
    normalization_last_value()
    num.set(f"{num.get().rstrip(operators)}{operator}")


def set_number(number):
    line = num.get()
    operator_last = line.rstrip('1234567890,.')[-1] if not line.replace('.', '').isdigit() else ''
    line_tail = line.rpartition(operator_last)[-1] if operator_last else line
    num.set(number if line_tail == '0' else f"{line}{number}")


# clear end, clear last number till next operator
def clear_end():
    line = num.get()
    line = line.rstrip('1234567890,.')
    num.set(line if line else "0")


def set_dot():
    line = num.get()
    operator_last = line.rstrip('1234567890,.')[-1] if not line.replace('.', '').isdigit() else ''
    line = f"{line}."
    num.set(line.replace(f"{operator_last}.", f"{operator_last}0."))

# fixme: after = when continue typing do not breake code - just delete till last string

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
button_ce = Button(frame_buttons, width=4, text="CE", command=clear_end)
button_ce.grid(column=1, row=2)
button_c = Button(frame_buttons, width=4, text="C", command=lambda: num.set('0'))
button_c.grid(column=2, row=2)
button_toggle = Button(frame_buttons, width=4, text=chr(177), command=toggle)
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
