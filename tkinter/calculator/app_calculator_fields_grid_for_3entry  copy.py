from tkinter import *            
import operator
amount_entry = 4 # including result entry
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
# try to do w/o slice on for. do with if in for 
#  add enumarate fo for 
def calculatate_result(row:list[Entry], func_math:callable):
    entry_result = row[-1]
    result:float = 0
    for entry in row[:-1]:
        number = entry.get().replace(" ", "").replace(",", ".").strip()
        number_valid = number.removeprefix("-").replace(".", "", 1).isdigit() or not number
        div_zero = func_math in [operator.truediv, operator.floordiv, operator.mod] and number == '0' and result is not None
        if not number_valid or div_zero:
            result = ERROR
            break
        elif result is None: 
            result = float(number)
            continue
        elif number is '': 
            continue
        result = func_math(result, float(number))
    entry_result.delete(0, 'end')
    entry_result.insert(0, str(f"{result}").rstrip('0').removesuffix('.'))

def calculatate_result(row:list[Entry], func_math:callable):
    result = ''
    for index, entry in enumerate(row):
        number = entry.get().replace(" ", "").replace(",", ".").strip()
        number_is_zero = number.removeprefix("-").replace(".", "", 1).replace("0", "", number.count("0") - 1) == "0"# treating empty entry as zero.
        zero_division = func_math in [operator.truediv, operator.floordiv, operator.mod] and number_is_zero and result
        number_valid = number.removeprefix("-").replace(".", "", 1).isdigit()
        print(f"{number} {number_valid=} {number_is_zero=} {zero_division=}")
        if not number: 
            continue
        elif not number_valid or zero_division: 
            result = ERROR
        elif result is None and number_valid: 
            result = float(number)
        elif index == amount_entry - 1: 
            entry.delete(0, 'end')
            entry.insert(0, str(f"{result}").rstrip('0').removesuffix('.'))
            return
        elif number_valid: 
            result = func_math(result, float(number))    
root = Tk()
root.title("Ex_3")
for index, list_op in enumerate(LIST_OPERATORS):
    row_entry = []
    sign_operation, func = list_op
    for index_entry in range(amount_entry): 
        entry = Entry(root)
        entry.grid(column=index_entry*2, row=index)
        row_entry.append(entry)
        if index_entry < amount_entry-2:
            Label(root, text=sign_operation).grid(column=index_entry*2+1, row=index)
    # row_entry.append(func)
    Button(root, text='=', command=lambda params_ = row_entry, func_=func :calculatate_result(params_, func_)).grid(column=amount_entry+1, row=index)

root.mainloop()
