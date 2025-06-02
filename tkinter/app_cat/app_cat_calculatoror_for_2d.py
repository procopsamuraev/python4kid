from tkinter import *
from tkinter.ttk import *

# number_items = 5 # amount of items in the table
list_headers = ['Product', 'Amount', 'Price', 'Days', "", 'Daily cost']
quantity_items = 3  
"""

while loop generation of string (just the product list)
can use lambda for function calculation
zadaem kolvo items in the code


"""


def get_report_error(name, amount, price, day)->str:
    name_valid = name.replace(' ', '').replace('.', '').replace('-', '').replace('`', '').isalnum() and len(name) >= 2
    amount_false = not (amount.isdigit() and amount >= '1')
    price_valid = len(price.rpartition('.')[-1]) < 3 and price.replace('.', '', 1).isdigit() 
    day_valid = not day[day.find('.')+1:].rstrip('0').replace('5', '', 1) if day.find('.') !=-1 else day.strip('0').isdigit()
    report_error = ''
    if not name and not amount and not price and not day:
        return
    if not name_valid:
        report_error = f"{report_error}Fill up 'Product' field with 2 or more alphabet symbols\n"
    if amount_false:
        report_error = f"{report_error}Fill up 'amount' int, positive\n"
    if not price_valid:
        report_error = f"{report_error}Fill up 'Price' with positive number and not more then 2 digits after dot\n"
    if not day_valid:
        report_error = f"{report_error}Fill up 'Day' with positive number and be dividing by 0.5\n"
    return report_error.removesuffix('\n')


def set_daily_cost(index_row):
    entry_name, entry_amount, entry_price, entry_day, _button_calculate, entry_total_price = list_entries[index_row]
    label_warning = list_entries[index_row+1][0]
    entry_total_price.delete(0, 'end')
    label_warning.config(text='')
    
    name = entry_name.get().strip(' ')
    amount = entry_amount.get().replace(' ', '').replace(',','.', 1)
    price = entry_price.get().replace(' ', '').replace(',','.', 1)
    day = entry_day.get().replace(' ', '').replace(',', '.', 1)
    report_error = get_report_error(name, amount, price, day)
    if not report_error and name:
        label_warning.grid_remove()
        entry_price.delete(0, 'end')
        entry_price.insert(0, f"{float(price):.2f}")
        entry_total_price.insert(0, f"{int(amount)*float(price)/float(day):.2f}")
    elif report_error: 
        label_warning.grid()
        label_warning.config(text=report_error)
        entry_total_price.insert(0, '')
        label_bill.config(text='')
    return name, amount, price, day, entry_total_price.get(), report_error

 
def set_total_annual():
    sum_amount = 0
    label_bill.config(text='')
    entry_cost_annual.delete(0, 'end')
    for index_row in range(len(list_entries)):
        data_row = index_row%2 == 1 and index_row != 0
        if data_row:
            set_daily_cost(index_row) 
            price_item_total = list_entries[index_row][-1].get()
            sum_amount = sum_amount + float(price_item_total) if price_item_total else sum_amount
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
        label_bill.config(text="Bill: Some errors with on of the product")
        label_bill.grid(column=0, columnspan=6, sticky='nsew', row=20)
        label_bill.grid_forget()
        return

    width = int(entry_bill_width.get().strip(' ')) if entry_bill_width.get().strip(' ').isdigit() else 100
    width_column = round(width/7)
    width_column0 = width - width_column*4
    bill_string = f"{root.title().center(width)}\n"
    bill_string = f"{bill_string}{'-' * width}\n"
    for index_row, list_row in enumerate(list_entries):
        row_header = index_row == 0
        row_data = index_row %2 == 1 and list_row[0].get()
        if row_header:
            entry_name, entry_amount, entry_price, entry_day, _spacer, entry_daily = list_headers
            text_name = entry_name.center(width_column0)
            text_amount = entry_amount.center(width_column)
            text_price = entry_price.center(width_column)
            text_day = entry_day.center(width_column)
            text_daily = entry_daily.rjust(width_column)
            bill_string = f"{bill_string}{text_name}{text_amount}{text_price}{text_day}{text_daily}\n"
            bill_string = f"{bill_string}{chr(8254) * width}\n"
        elif row_data:
            entry_name, entry_amount, entry_price, entry_day, _button, entry_total_price = list_row
            text_name = entry_name.get().center(width_column0)
            text_amount = entry_amount.get().center(width_column)
            text_price = entry_price.get().center(width_column)
            text_day = entry_day.get().center(width_column)
            text_daily = entry_total_price.get().rjust(width_column-3)
            bill_string = f"{bill_string}{text_name}{text_amount}x{text_price}/{text_day}={text_daily}\n"
        bill_string=f"{bill_string}" 

    bill_string = f"{bill_string}{'-' * width}\n"
    bill_string = f"{bill_string}{label_annual['text'].rjust(width_column*5-1)} {entry_cost_annual.get().ljust(width_column)}\n"
    bill_string = f"{bill_string}{label_years['text'].rjust(width_column*5-1)} {entry_years.get().ljust(width_column)}\n"
    bill_string = f"{bill_string}{label_cost_total['text'].rjust(width_column*5-1)} {entry_for_full.get().ljust(width_column)}\n"
    label_bill.config(text=bill_string)
    label_bill.grid(row=row+10, columnspan=6, sticky='nsew')


root = Tk()
root.title('Calculator for cat')
list_entries=[]
list_labels_header = []
for header in list_headers:
    list_labels_header.append(Label(text=header))

list_entries.append(list_labels_header)

for index in range(quantity_items):
    list_entries_line = []
    row = index*2 + 1
    entry_name, entry_amount, entry_price, entry_days, entry_total_price, label_warning = Entry(), Entry(), Entry(), Entry(), Entry(), Label()
    button_calculate=Button(text='=', command=lambda row_index=row: set_daily_cost(row_index))
    list_entries_line = [entry_name, entry_amount, entry_price, entry_days, button_calculate, entry_total_price]
    list_entries.append(list_entries_line)
    list_entries.append([label_warning])

# draw tne table
for index_row, list_entries_row in enumerate(list_entries):
    for index_column, element in enumerate(list_entries_row):
        element.grid(column=index_column, row=index_row)
        warning_row = index_row%2 == 0 and index_row !=0
        if warning_row:
            element.grid(column = 0, row = index_row, columnspan=5, sticky='nsew')
            element.grid_remove()
        
label_annual = Label(text="Total annual cost:", justify=RIGHT)
label_annual.grid(column=0, row=row+2, columnspan=4)
button_6 = Button(text="=", command=set_total_annual)
button_6.grid(column=4, row=row+2)
entry_cost_annual = Entry()
entry_cost_annual.grid(column=5, row=row+2)

label_years = Label(text="Period, years:", justify=RIGHT)
label_years.grid(column=0, row=row+3, columnspan=4)
entry_years = Entry()
entry_years.grid(column=5, row=row+3)
entry_years.insert(0, "15")
label_warning_years = Label()
label_warning_years.grid(column=0, columnspan=6, sticky='nsew', row=row+4)
label_warning_years.grid_remove()

label_cost_total = Label(text="Total cost for whole period:", justify=RIGHT)
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

