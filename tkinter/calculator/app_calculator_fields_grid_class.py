from tkinter import *            
import operator
entry_count = 4 # including result
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

class single_row():
    def create_row(self, row, func_list):
        sign_func, func = func_list
        _row = []
        for index_entry in range(entry_count): 
            entry = Entry(root)
            entry.grid(column=index_entry*2, row=row)
            _row.append(entry)
            if index_entry < entry_count-2:
                Label(root, text=sign_func).grid(column=index_entry*2+1, row=row)
        _row.append(func)
        Button(root, text='=', command=lambda _params = _row:calculatate_result(_params)).grid(column=entry_count+1, row=row)

    
def calculatate_result(row):
    entry_result, func_math = row[-2:]
    result = None
    for entry in row[:-2]:
        number = entry.get().replace(" ", "").replace(",", ".")
        number_valid = number.removeprefix("-").replace(".", "", 1).isdigit() or number == ''
        div_zero = func_math in [operator.truediv, operator.floordiv, operator.mod] and number == '0' and result != None
        if not number_valid or div_zero:
            result = ERROR
            break
        if result == None: 
            result = float(number)
            continue
        elif number == '': 
            continue
        result = func_math(result, float(number))
    entry_result.delete(0, 'end')
    entry_result.insert(0, str(f"{result}").rstrip('0').removesuffix('.'))

    
root = Tk()
root.title("Ex_3")
row_one = single_row()
for row, list_func in enumerate(LIST_OPERATORS):
    row_one.create_row(row, list_func)
root.mainloop()
