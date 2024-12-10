from tkinter import *
from tkinter.ttk import *


"""
tovar - min 2 symbols, not " "..- 
qty - only >0, int
price >0, float, with .00 , 4 dopustimoe
qty days >0, delimoe na 1/2 
total price with .00

vyvod oshibok: 
    - pishem chto nujno sdelat chrobe ispravit - tovar db min 2 symbols
    - qty: govorim chto delat
    - 
    - spaces are allowed 

with configurable width
label width
label print bill
and label with printed bill

"""


def get_report_error(name, qty, price, day):
    name_valid = name.replace(' ', '').replace('.', '').replace('-', '').replace('`', '').isalnum() and len(name) >= 2
    qty_false = not (qty.isdigit() and qty > '0')
    price_valid = price.replace('.', '', 1).isdigit() and len(price.rpartition('.')[-1]) < 3
    day_valid = day.rstrip('05').removesuffix('.').isdigit() 
    msg_warning = ""
    if not name and not qty and not price and not day:
        msg_warning = "Empty_line"
        return msg_warning
    if not name_valid:
        msg_warning = f"{msg_warning}Fill up 'Product' field with 2 or more alphabet symbols\n"
    if qty_false:
        msg_warning = f"{msg_warning}Fill up 'Qty' int, positive\n"
    if not price_valid:
        msg_warning = f"{msg_warning}Fill up 'Price' with positive number and not more then 2 digits after dot\n"
    if not day_valid:
        msg_warning = f"{msg_warning}Fill up 'Day' with positive number and be dividing by 0,5\n"
    return msg_warning.removesuffix('\n')


def set_total_price(list_entries):
    (entry_name, entry_qty, entry_price, entry_day, label_warning, entry_total_price) = list_entries
    name = entry_name.get().strip(' ')
    qty = entry_qty.get().replace(' ', '')
    price = entry_price.get().replace(' ', '')
    day = entry_day.get().replace(' ', '')
    entry_total_price.delete(0, 'end')
    msg_warning = get_report_error(name, qty, price, day)
    label_warning.config(text='')
    if msg_warning == 'Empty_line':
        label_warning.grid_remove()
        entry_total_price.insert(0, '0')
    if msg_warning and msg_warning != 'Empty_line':
        label_warning.grid()
        label_warning.config(text=msg_warning)
        entry_total_price.insert(0, '---')
    elif not msg_warning:
        label_warning.grid_remove()
        entry_total_price.insert(0, str('{0:.2f}'.format(int(qty)*float(price)/float(day))))
        # entry_total_price.insert(0, str(round(int(qty)*float(price)/float(day), 2)))
        return name, qty, price, day, entry_total_price.get()


def set_total_annual():
    entry_cost_annual.delete(0, 'end')
    set_total_price(list_entries1)
    set_total_price(list_entries2)
    set_total_price(list_entries3)
    price1, price2, price3 = entry_total_price1.get(), entry_total_price2.get(), entry_total_price3.get()
    if (price1 or price2 or price3) == '---':
        entry_cost_annual.insert(0, '---')
    else:
        # entry_cost_annual.insert(0, str(round((float(price1)+float(price2)+float(price3)) * 365, 2)))
        entry_cost_annual.insert(0, str('{0:.2f}'.format((float(price1)+float(price2)+float(price3)) * 365)))


def set_total_cost():
    set_total_annual()
    cost_annual = entry_cost_annual.get()
    years = entry_years.get().replace(' ', '')
    data_true = years.replace('.', '', 1).isdigit() and cost_annual.replace('.', '').isdigit()
    entry_for_full.delete(0, 'end')
    if data_true:
        entry_for_full.insert(0, str('{0:.2f}'.format(float(cost_annual)*float(years))))
    else:
        entry_for_full.insert(0, '---')


def print_bill():
    set_total_cost()
    if not entry_cost_annual.get().replace('.', '').isdigit():
        label_bill.config(text="Bill: Some errors with on of the product")
        label_bill.grid(column=0, columnspan=6, sticky='nsew', row=20)
        label_bill.grid_forget()
    else:
        width = int(entry_bill_width.get().strip(' ')) if entry_bill_width.get().strip(' ').isdigit() else '120'
        col_width = round(width/6)
        bill_string = f"{root.title().center(width)}\n"
        # headers
        bill_string = f"{bill_string}{label0['text'].center(col_width*2)}{label1['text'].center(col_width)}{label2['text'].center(col_width)}{label3['text'].center(col_width)}{label5['text'].center(col_width)}\n"
        # item1
        if set_total_price(list_entries1):
            name, qty, price, day, price_total = set_total_price(list_entries1)
            bill_string = f"{bill_string}{name.ljust(col_width*2)}{qty.center(col_width)}x{price.center(col_width)}/{day.center(col_width)}={price_total.ljust(col_width)}\n"
        # item2
        if set_total_price(list_entries2):
            name, qty, price, day, price_total = set_total_price(list_entries2) 
            bill_string = f"{bill_string}{name.ljust(col_width*2)}{qty.center(col_width)}x{price.center(col_width)}/{day.center(col_width)}={price_total.ljust(col_width)}\n"
        # item3
        if set_total_price(list_entries3): 
            name, qty, price, day, price_total = set_total_price(list_entries3)
            bill_string = f"{bill_string}{name.ljust(col_width*2)}{qty.center(col_width)}x{price.center(col_width)}/{day.center(col_width)}={price_total.ljust(col_width)}\n"

        bill_string = f"{bill_string}{label_annual['text'].rjust(col_width*5-1)} {entry_cost_annual.get().ljust(col_width)}\n"
        bill_string = f"{bill_string}{label_years['text'].rjust(col_width*5-1)} {entry_years.get().ljust(col_width)}\n"
        bill_string = f"{bill_string}{label_cost_total['text'].rjust(col_width*5-1)} {entry_for_full.get().ljust(col_width)}\n"
        label_bill.config(text=bill_string)
        label_bill.grid(row=12, columnspan=6, sticky='nsew')


root = Tk()
root.title('Calculator for cat')
label0 = Label(text="Product")
label0.grid(column=0, row=0)
label1 = Label(text="Qty")
label1.grid(column=1, row=0)
label2 = Label(text="Price")
label2.grid(column=2, row=0)
label3 = Label(text = "Days")
label3.grid(column=3, row=0)
label5 = Label(text="Total Price")
label5.grid(column=5, row=0)

entry_name1 = Entry()
entry_name1.insert(0, "Food dry")
entry_name1.grid(column=0, row=1)
entry_qty1 = Entry()
entry_qty1.insert(0, "3")
entry_qty1.grid(column=1, row=1)
entry_price1 = Entry()
entry_price1.insert(0, "5.30")
entry_price1.grid(column=2, row=1)
entry_days1 = Entry()
entry_days1.insert(0, "21")
entry_days1.grid(column=3, row=1)
entry_total_price1 = Entry()
entry_total_price1.insert(0, '0.00')
entry_total_price1.grid(column=5, row=1)
label_warning1 = Label()
label_warning1.grid(column=0, columnspan=6, sticky='nsew', row=2)
label_warning1.grid_remove()
list_entries1 = [entry_name1, entry_qty1, entry_price1, entry_days1, label_warning1, entry_total_price1]
button_1 = Button(text="=", command=lambda: set_total_price(list_entries1))
button_1.grid(column=4, row=1)

entry_name2 = Entry()
entry_name2.insert(0, "Food tuna in a can")
entry_name2.grid(column=0, row=3)
entry_qty2 = Entry()
entry_qty2.insert(0, "1")
entry_qty2.grid(column=1, row=3)
entry_price2 = Entry()
entry_price2.insert(0, "100.80")
entry_price2.grid(column=2, row=3)
entry_days2 = Entry()
entry_days2.insert(0, "1")
entry_days2.grid(column=3, row=3)
entry_total_price2 = Entry()
entry_total_price2.insert(0, '0.00')
entry_total_price2.grid(column=5, row=3)
label_warning2 = Label()
label_warning2.grid(column=0, columnspan=6, sticky='nsew', row=4)
label_warning2.grid_remove()
list_entries2 = [entry_name2, entry_qty2, entry_price2, entry_days2, label_warning2, entry_total_price2]
button_2 = Button(text="=", command=lambda: set_total_price(list_entries2))
button_2.grid(column=4, row=3)

entry_name3 = Entry()
entry_name3.insert(0, "Toilet Refill")
entry_name3.grid(column=0, row=5)
entry_qty3 = Entry()
entry_qty3.insert(0, "1")
entry_qty3.grid(column=1, row=5)
entry_price3 = Entry()
entry_price3.insert(0, "300.80")
entry_price3.grid(column=2, row=5)
entry_days3 = Entry()
entry_days3.insert(0, "7")
entry_days3.grid(column=3, row=5)
entry_total_price3 = Entry()
entry_total_price3.insert(0, '0.00')
entry_total_price3.grid(column=5, row=5)
label_warning3 = Label()
label_warning3.grid(column=0, columnspan=6, sticky='nsew', row=6)
label_warning3.grid_remove()
list_entries3 = [entry_name3, entry_qty3, entry_price3, entry_days3, label_warning3, entry_total_price3]
button_3 = Button(text="=", command=lambda: set_total_price(list_entries3))
button_3.grid(column=4, row=5)


label_annual = Label(text="Total annual cost:", justify=RIGHT)
label_annual.grid(column=0, row=7, columnspan=4)
button_6 = Button(text="=",command=set_total_annual)
button_6.grid(column=4, row=7)
entry_cost_annual = Entry()
entry_cost_annual.grid(column=5, row=7)

label_years = Label(text="Period, years:", justify=RIGHT)
label_years.grid(column=0, row=8, columnspan=4)
entry_years = Entry()
entry_years.grid(column=5, row=8)
entry_years.insert(0, "15")

label_cost_total = Label(text="Total cost for whole period:", justify=RIGHT)
label_cost_total.grid(column=0, row=9, columnspan=4)
button_6 = Button(text="=", command=set_total_cost)
button_6.grid(column=4, row=9)
entry_for_full= Entry()
entry_for_full.grid(column=5, row=9)

Label(text="Print bill with width:", anchor='e', justify="center").grid(column=0, row=10, columnspan=4)
button_print_bill = Button(text="Print", command=print_bill)
button_print_bill.grid(column=4, row=10)
entry_bill_width = Entry()
entry_bill_width.grid(column=3, row=10)
entry_bill_width.insert(0, '100')

label_bill = Label(font=('Ubuntu Mono', 10))

root.mainloop()

