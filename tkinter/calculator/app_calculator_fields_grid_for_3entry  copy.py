from tkinter import *            
import operator
entry_count = 4 # including result entry
LIST_OPERATORS = [
    ['+',operator.add],
    ['-',operator.sub],
    ['*',operator.mul],
    ['**', operator.pow],
    ['/',operator.truediv],
    ['//', operator.floordiv],
    ['%', operator.mod],
]
ERROR = "Error: Enter numbers only and not 0"

def calculatate_result(row):
    entry_result, func_math = row[-2:]
    result = None
    for entry in row[:-2]:
        number = entry.get().replace(" ", "").replace(",", ".")
        number_valid = number.removeprefix("-").replace(".", "", 1).isdigit() or number is ''
        div_zero = func_math in [operator.truediv, operator.floordiv, operator.mod] and number == '0' and result is not None
        if not number_valid or div_zero:
            result = ERROR
            break
        if result is None: 
            result = float(number)
            continue
        elif number is '': 
            continue
        result = func_math(result, float(number))
    entry_result.delete(0, 'end')
    entry_result.insert(0, str(f"{result}").rstrip('0').removesuffix('.'))

    
root = Tk()
root.title("Ex_3")
for index, list_op in enumerate(LIST_OPERATORS):
    row_entry = []
    sign_operation, func = list_op
    for index_entry in range(entry_count): 
        entry = Entry(root)
        entry.grid(column=index_entry*2, row=index)
        row_entry.append(entry)
        if index_entry < entry_count-2:
            Label(root, text=sign_operation).grid(column=index_entry*2+1, row=index)
    row_entry.append(func)
    Button(root, text='=', command=lambda _params = row_entry:calculatate_result(_params)).grid(column=entry_count+1, row=index)

root.mainloop()
