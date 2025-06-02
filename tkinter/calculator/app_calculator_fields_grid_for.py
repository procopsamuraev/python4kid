from tkinter import *            
import operator
list_operators = [
    ['+',operator.add],
    ['-',operator.sub],
    ['*',operator.mul],
    ['**', operator.pow],
    ['/',operator.truediv],
    ['//', operator.floordiv],
    # ['%', operator.mod], 
    ['%', operator.mod]
    ]
ERROR = "Error: Enter numbers only and not 0"


def calculatate_result(entry1, entry2, entry_result, func_math):
    number_1 = entry1.get().replace(" ", "").replace(",", ".")
    number_1_true = number_1.removeprefix("-").replace(".", "", 1).isdigit()
    number_2 = entry2.get().replace(" ", "").replace(",", ".")
    number_2_true = number_2.removeprefix("-").replace(".", "", 1).isdigit()
    number_2_zero = number_2.find("0") != -1 and len(number_2.removeprefix("-").strip('0')) < 2
    div_zero_true = func_math in [operator.truediv, operator.floordiv, operator.mod] and number_2_zero
    if number_1_true and number_2_true and not div_zero_true:
        string_calculated =  str(func_math(float(number_1), float(number_2))).rstrip('0').removesuffix('.')
    else:
        string_calculated = ERROR
    entry_result.delete(0, 'end')
    entry_result.insert(0, string_calculated)

    
root = Tk()
root.title("Ex_2")

for index, list_op in enumerate(list_operators):
    sign_operation, func = list_op
    entry1 = Entry(root, width=5)
    entry1.grid(column=0, row=index)
    Label(root, text=sign_operation).grid(column=1, row=index)
    entry2 = Entry(root, width=5)
    entry2.grid(column=2, row=index)
    entry3 = Entry(root, width=10)
    entry3.grid(column=4, row=index)
    # Button(root, text='=', command=lambda e1=entry1, e2=entry2, e3=entry3, func_math = func: calculatate_result(e1, e2, e3, func_math)).grid(column=3, row=index)
    Button(root, text='=', command=lambda _params = [entry1, entry2, entry3, func]:calculatate_result(*_params)).grid(column=3, row=index)

root.mainloop()
