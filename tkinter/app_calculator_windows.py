import tkinter.ttk
from tkinter import *
from tkinter.ttk import *

error = "error"

"""
def calculation_numbers(number_1, number_2, operation, value_result):
    value_clean_1 = number_1.get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = number_2.get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    if operation == "+":
        result = str(float(value_clean_1) + float(value_clean_2)) if number_1_true and number_2_true else error
    elif operation == "-":
        result = str(float(value_clean_1) - float(value_clean_2)) if number_1_true and number_2_true else error
    elif operation == "*":
        result = str(float(value_clean_1) * float(value_clean_2)) if number_1_true and number_2_true else error
    elif operation == "**":
        result = str(float(value_clean_1) ** float(value_clean_2)) if number_1_true and number_2_true else error
    elif operation == "/":
        number_2_zero = value_clean_2.find("0") != -1 and len(value_clean_2.removeprefix("-").strip("0")) < 2
        number_2_true = number_2_true and not number_2_zero
        result = str(float(value_clean_1) / float(value_clean_2)) if number_1_true and number_2_true else error
    elif operation == "//":
        number_2_zero = value_clean_2.find("0") != -1 and len(value_clean_2.removeprefix("-").strip("0")) < 2
        number_2_true = number_2_true and not number_2_zero
        result = str(float(value_clean_1) // float(value_clean_2)) if number_1_true and number_2_true else error
    elif operation == "%":
        number_2_zero = value_clean_2.find("1") != -1 and len(value_clean_2.removeprefix("-").strip("0")) < 2
        number_2_true = number_2_true and not number_2_zero
        result = str(float(value_clean_1) % float(value_clean_2)) if number_1_true and number_2_true else error
    else:
        result = error
    value_result.set(result.rstrip("0").removesuffix("."))
"""
"""

true: before we press enter
000 -> 0
01001 -> 1001
0+-003 -> 0-3
1-2+2/2= -> 1-2+2/2=0 
1-2+2/2=+8 -> 1-2+2/2+8
1-2+2/01+8 -> 1-2+2/1+8
1-2+2/0- -> 1-2+2/
 
"""

# def display_result():
#     result = 0
#     string_clean = num.get().replace(" ", "").replace(",", ".").rsplit("=")[0]
#     for numbers_raw in string_clean.split("+"):
#         numbers_true = numbers_raw.removeprefix("-").replace(".", "", 1).removesuffix("=").isdigit()
#         result = result + float(numbers_raw) if numbers_true else error
#     num.set(f'{string_clean}={str(result).rstrip("0").removesuffix(".")}')

def backspace():
    string = num.get()
    string = string.removesuffix(string[-1])
    num.set(string if string else "0")
# delete last symbols in last number -+
    pass


def calculation():
    pass


def set_operator(operator):
    num.set(num.get().rstrip('-+/*')+operator)


def set_number(number):
    string = num.get()
    num.set(f{string.removeprefix('0')}{number})
    

# clear entry, clear last number till next operator
def clear_entry():
    string = num.get()
    string = string.rstrip('1234567890,.')
    num.set(string if string else "0")


def set_dot():
    pass


def display_string(symbol):
    string = num.get().replace(" ", "").replace(",", ".")
    if symbol == chr(8592):
        string = string.removesuffix(string[-1])
        num.set(string if string else "0")
    elif symbol == chr(61):
        delimiters = ["+", "-", "*", "/"]
        string_delimiters = string
        for delimiter in delimiters:
            string_delimiters = string_delimiters.replace(delimiter, " ")
        digits_only = string_delimiters.removeprefix("-").replace(".", "", 1).replace(" ", "").isdigit()
        at_lest_two = len(string_delimiters.split()) > 1 and digits_only
        # if string.find("/"):
        #     print(string)
        #     zero_false = string.split('/')[1].lstrip("0")[0].isdigit()
        # print(zero_false)
        # num.set(error) if not digits_only else num.set(string)
        num.set(eval(string)) if at_lest_two else num.sel(string)
        # num.set(eval(string)) if len(string_delimiters.split()) > 1 else num.set(string)
    else:
        num.set(f'{string.removeprefix("0")}{symbol}')


root = Tk()
root.title("Ex_1")

num = StringVar()
num.set(0)
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
button_backspace = Button(frame_buttons, width=4, text=chr(8592), command=lambda: display_string(chr(8592)))
button_backspace.grid(column=0, row=2)
button_ce = Button(frame_buttons, width=4, text="CE", command=clear_entry)
button_ce.grid(column=1, row=2)
button_c = Button(frame_buttons, width=4, text="C", command=lambda: num.set(0))
button_c.grid(column=2, row=2)
button_toggle = Button(frame_buttons, width=4, text=chr(177))
button_toggle.grid(column=3, row=2)
button_square_root = Button(frame_buttons, width=4, text=chr(8730))
button_square_root.grid(column=4, row=2)
button_7 = Button(frame_buttons, width=4, text="7", command=lambda: display_string("7"))
button_7.grid(column=0, row=3)
button_8 = Button(frame_buttons, width=4, text="8", command=lambda: display_string("8"))
button_8.grid(column=1, row=3)
button_9 = Button(frame_buttons, width=4, text="9", command=lambda: display_string("9"))
button_9.grid(column=2, row=3)
button_division = Button(frame_buttons, width=4, text="/", command=lambda: set_operator("/"))
button_division.grid(column=3, row=3)
button_percentage= Button(frame_buttons, width=4, text="%")
button_percentage.grid(column=4, row=3)
button_4 = Button(frame_buttons, width=4, text="4", command=lambda: display_string("4"))
button_4.grid(column=0, row=4)
button_5 = Button(frame_buttons, width=4, text="5", command=lambda: display_string("5"))
button_5.grid(column=1, row=4)
button_6 = Button(frame_buttons, width=4, text="6", command=lambda: display_string("6"))
button_6.grid(column=2, row=4)
button_multiplication = Button(frame_buttons, width=4, text="*", command=lambda: set_operator("*"))
button_multiplication.grid(column=3, row=4)
button_rational = Button(frame_buttons, width=4, text="1/x", command=lambda: display_string("1/x"))
button_rational.grid(column=4, row=4)
button_1 = Button(frame_buttons, width=4, text="1", command=lambda: display_string("1"))
button_1.grid(column=0, row=5)
button_2 = Button(frame_buttons, width=4, text="2", command=lambda: display_string("2"))
button_2.grid(column=1, row=5)
button_3 = Button(frame_buttons, width=4, text="3", command=lambda: display_string("3"))
button_3.grid(column=2, row=5)
button_subtract = Button(frame_buttons, width=4, text="-", command=lambda: set_operator("-"))
button_subtract.grid(column=3, row=5)
button_equal = Button(frame_buttons, width=4, text="=", command=lambda: display_string("="))
button_equal.grid(column=4, row=5, rowspan=2, sticky=NS)
button_0 = Button(frame_buttons, width=4, text="0", command=lambda: display_string("0"))
button_0.grid(column=0, columnspan=2, row=6, sticky=EW)
button_dot = Button(frame_buttons, width=4, text=".", command=lambda: display_string("."))
button_dot.grid(column=2, row=6)
button_sum = Button(frame_buttons, width=4, text="+", command=lambda: set_operator("+"))
button_sum.grid(column=3, row=6)

root.mainloop()
