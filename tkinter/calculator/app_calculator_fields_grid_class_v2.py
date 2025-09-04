from tkinter import *            
import operator

class LineCalculator:
    error_div_zero = "E: Enter numbers only and not 0"

    def __init__(self, parent: Tk, symbol_operator: str ='', operator: operator = None, row: int = 0):
        self.symbol_operator = symbol_operator
        self.operator = operator
        self.row = row
        self.entry1 = Entry(parent, width=5)
        self.entry1.grid(column=0, row=self.row)
        Label(parent, text=self.symbol_operator).grid(column=1, row=self.row)
        self.entry2 = Entry(parent, width=5)
        self.entry2.grid(column=2, row=self.row)
        self.entry_result= Entry(parent, width=5)
        self.entry_result.grid(column=4, row=self.row)
        Button(parent, text='=', command=self.calculate_result).grid(column=3, row=self.row)


    def calculate_result(self):
        number_1 = self.entry1.get().replace(" ", "").replace(",", ".")
        number_1_true = number_1.removeprefix("-").replace(".", "", 1).isdigit()
        number_2 = self.entry2.get().replace(" ", "").replace(",", ".")
        number_2_true = number_2.removeprefix("-").replace(".", "", 1).isdigit()
        number_2_zero = number_2.find("0") != -1 and len(number_2.removeprefix("-").strip('0')) < 2
        div_zero_true = self.operator in [operator.truediv, operator.floordiv, operator.mod] and number_2_zero
        if number_1_true and number_2_true and not div_zero_true:
            string_calculated =  str(self.operator(float(number_1), float(number_2))).rstrip('0').removesuffix('.')
        else:
            string_calculated = self.error_div_zero
        self.entry_result.delete(0, 'end')
        self.entry_result.insert(0, string_calculated)


list_operators = [
    ['+',operator.add],
    ['-',operator.sub],
    ['*',operator.mul],
    ['**', operator.pow],
    ['/',operator.truediv],
    ['//', operator.floordiv],
    ['%', operator.mod],
    ]

root = Tk()

for index, list_op in enumerate(list_operators):
    sign_operation, func = list_op
    LineCalculator(root, symbol_operator=sign_operation, operator=func, row=index)

root.mainloop()
