from tkinter import *
from tkinter.ttk import *

from pyasn1_modules.rfc5280 import anotherNameMap

# number_items = 5 # amount of items in the table
list_headers = ['Product', 'Amount', 'Price', 'Days', '', 'Daily Cost']
quantity_items = 3  
"""

"""
list_items = []

class ProductRow:
    def __init__(self, parent: Tk, name:str = '',  row_line: int = 1) -> None:
        self.name = name
        self.amount = ''
        self.price = ''
        self.day = ''
        self.total_price = ''
        if row_line%2 != 0:
            row_line +=1
        widget_at_row = parent.grid_slaves(row=row_line, column=0)
        while widget_at_row:
            row_line += 2
            widget_at_row = parent.grid_slaves(row=row_line, column=0)
        # product line
        self.row = row_line
        ProductRow.row = row_line
        self.__entry_name = Entry()
        self.__entry_name.grid(row=self.row, column=0)
        self.entry_amount = Entry()
        self.entry_amount.grid(row=self.row, column=1)
        self.entry_price = Entry()
        self.entry_price.grid(row=self.row, column=2)
        self.entry_days = Entry()
        self.entry_days.grid(row=self.row, column=3)
        Button(text='=', command=self.set_daily_cost).grid(row=self.row, column=4)
        self.entry_total_price = Entry()
        self.entry_total_price.grid(row=self.row, column=5)
        # warning line
        self.label_warning = Label()


    def set_daily_cost(self):
        self.entry_total_price.delete(0, 'end')
        self.label_warning.config(text='')

        self.name = self.__entry_name.get().strip(' ')
        self.amount = self.entry_amount.get().replace(' ', '').replace(',', '.', 1)
        self.price = self.entry_price.get().replace(' ', '').replace(',', '.', 1)
        self.day = self.entry_days.get().replace(' ', '').replace(',', '.', 1)
        report_error = self.__get_report_error(self.name, self.amount, self.price, self.day)
        if not report_error and self.name:
            self.label_warning.grid_remove()
            self.entry_price.delete(0, 'end')
            self.entry_price.insert(0, f"{float(self.price):.2f}")
            self.total_price =  f"{int(self.amount) * float(self.price) / float(self.day):.2f}"
            self.entry_total_price.insert(0, self.total_price)
        elif report_error:
            self.label_warning.grid(row=self.row+1, column=0, columnspan=5)
            self.label_warning.config(text=report_error)
            self.entry_total_price.insert(0, '')


    @staticmethod
    def __get_report_error(name: str, amount: str, price: str, day: str)->str:
        name_valid = name.replace(' ', '').replace('.', '').replace('-', '').replace('`', '').isalnum() and len(name) >= 2
        amount_valid = amount.isdigit() and amount >= '1'
        price_valid = len(price.rpartition('.')[-1]) < 3 and price.replace('.', '', 1).isdigit()
        day_valid = not day[day.find('.')+1:].rstrip('0').replace('5', '', 1) if day.find('.') !=-1 else day.strip('0').isdigit()
        report_error = ''
        if not name and not amount and not price and not day:
            return f"{report_error}Fill up the line"
        if not name_valid:
            report_error = f"{report_error}Fill up 'Product' field with 2 or more alphabet symbols\n"
        if not amount_valid:
            report_error = f"{report_error}Fill up 'amount' int, positive\n"
        if not price_valid:
            report_error = f"{report_error}Fill up 'Price' with positive number and not more then 2 digits after dot\n"
        if not day_valid:
            report_error = f"{report_error}Fill up 'Day' with positive number and be dividing by 0.5\n"
        return report_error.removesuffix('\n')


def set_total_annual():
    sum_amount = 0
    label_bill.config(text='')
    entry_cost_annual.delete(0, 'end')
    for product in list_items:
        product.set_daily_cost()
        sum_amount_product = product.entry_amount.get()
        print(sum_amount_product)
        sum_amount = sum_amount + float(sum_amount_product) if sum_amount_product else sum_amount
    entry_cost_annual.insert(0, f'{(sum_amount * 365):.2f}')


def set_total_cost():
    set_total_annual()
    cost_annual = entry_cost_annual.get()
    year = entry_years.get().replace(' ', '').replace(',', '.', 1)
    year_valid = not year[year.find('.')+1:].rstrip('0').replace('5', '', 1).isdigit() if year.find('.') !=-1 else year.isdigit()
    entry_for_full.delete(0, 'end')
    if not year_valid:
        label_warning_years.grid()
        label_warning_years.config(text="Fill up 'Year' with positive number and be dividing by 0.5")
    else: 
        label_warning_years.grid_remove()
        data_true = year_valid and cost_annual.replace('.', '').isdigit()
        entry_for_full.insert(0, f"{(float(cost_annual)*float(year)):.2f}") if data_true else 0, ''


def print_bill():
    set_total_cost()
    if not entry_for_full.get().replace('.', '').isdigit():
        label_bill.config(text="Bill: Some errors with one of the product")
        label_bill.grid(column=0, columnspan=6, sticky='nsew', row=20)
        label_bill.grid_forget()
        return

    width = int(entry_bill_width.get().strip(' ')) if entry_bill_width.get().strip(' ').isdigit() else 100
    width_column = round(width/7)
    width_column0 = width - width_column*4
    bill_string = f"{root.title().center(width)}\n"
    bill_string = f"{bill_string}{'-' * width}\n"
    # print header
    header_name, header_amount, header_price, header_day, __empty, header_total_price = list_headers
    bill_string += f"{header_name.center(width_column0)}"
    bill_string += f"{header_amount.center(width_column)}"
    bill_string += f"{header_price.center(width_column)}"
    bill_string += f"{header_day.center(width_column)}"
    bill_string += f"{header_total_price.rjust(width_column)}\n"

    for product in list_items:
        name, amount, price, daily, total_price = product.name, product.amount, product.price, product.day, product.total_price
        if total_price:
            bill_string += f"{name.center(width_column0)}{amount.center(width_column)}x{price.center(width_column)}/{daily.center(width_column)}={total_price.rjust(width_column-3)}\n"

    bill_string = f"{bill_string}{'-' * width}\n"
    bill_string = f"{bill_string}{label_annual['text'].rjust(width_column*5-1)} {entry_cost_annual.get().ljust(width_column)}\n"
    bill_string = f"{bill_string}{label_years['text'].rjust(width_column*5-1)} {entry_years.get().ljust(width_column)}\n"
    bill_string = f"{bill_string}{label_cost_total['text'].rjust(width_column*5-1)} {entry_for_full.get().ljust(width_column)}\n"
    label_bill.config(text=bill_string)
    label_bill.grid(row=row+10, columnspan=6, sticky='nsew')

root = Tk()
root.title('Calculator for cat')
for index_column, header in enumerate(list_headers):
    Label(text=header).grid(row=0, column=index_column)
# todo: make with for
number_item = 0
while number_item < quantity_items:
    item = ProductRow(parent=root, name='test1')
    list_items.append(item)
    number_item += 1

row = len(list_items)*2+1

label_annual = Label(text="Total annual cost:", justify='right')
label_annual.grid(column=0, row=row+2, columnspan=4)
button_6 = Button(text="=", command=set_total_annual)
button_6.grid(column=4, row=row+2)
entry_cost_annual = Entry()
entry_cost_annual.grid(column=5, row=row+2)

label_years = Label(text="Period, years:", justify='right')
label_years.grid(column=0, row=row+3, columnspan=4)
entry_years = Entry()
entry_years.grid(column=5, row=row+3)
entry_years.insert(0, "15")
label_warning_years = Label()
label_warning_years.grid(column=0, columnspan=6, sticky='nsew', row=row+4)
label_warning_years.grid_remove()

label_cost_total = Label(text="Total cost for whole period:", justify='right')
label_cost_total.grid(column=0, row=row+5, columnspan=4)
button_6 = Button(text="=", command=set_total_cost)
button_6.grid(column=4, row=row+5)
entry_for_full= Entry()
entry_for_full.grid(column=5, row=row+5)

Label(text="Print bill with width(min 70):", anchor='e', justify="center").grid(column=0, row=row+6, columnspan=4)
button_print_bill = Button(text="Print", command=print_bill)
button_print_bill.grid(column=4, row=row+6)
entry_bill_width = Entry()
entry_bill_width.grid(column=3, row=row+6)
entry_bill_width.insert(0, '100')

label_bill = Label(font=('Ubuntu Mono', 10))

root.mainloop()

