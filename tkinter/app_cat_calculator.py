from tkinter import *
from tkinter.ttk import *

"""
tovar - min 2 symbols, not " "..- 
amount - only >0, int
price >0, float, with .00 , 4 dopustimoe
amount days >0, delimoe na 1/2 
total price with .00

vyvod oshibok: 
    - pishem chto nujno sdelat chrobe ispravit - tovar db min 2 symbols
    - amount: govorim chto delat
    - 
    - spaces are allowed 


// fix me
fill default width  - done 
dont print if any field are empty
years allow only digits  and not negative  should work with 0,5 but allow only kratnoe 0.5
all should work witn 1, 2 products only
proverka na 0.5 v dnyah ne rabotaet


//dont show the empty line on bill -fixed
check the days and years with 5.55 -ffixed
if zero on price do not fill up with zero - use '' instead -fixed

// fix
// do not raise error if line is empty - raise error only if whole table is empty
// condition for calculation make simple l108,. l95-l98
"""


def get_report_error(name, amount, price, day):
    name_valid = name.replace(' ', '').replace('.', '').replace('-', '').replace('`', '').isalnum() and len(name) >= 2
    amount_false = not (amount.isdigit() and amount >= '1')
    price_valid = price.replace('.', '', 1).isdigit() and len(price.rpartition('.')[-1]) < 3
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


def set_total_price(list_entries):
    entry_name, entry_amount, entry_price, entry_day, label_warning, entry_total_price = list_entries
    entry_total_price.delete(0, 'end')
    label_warning.config(text='')
    
    name = entry_name.get().strip(' ')
    amount = entry_amount.get().replace(' ', '').replace(',','.', 1)
    price = entry_price.get().replace(' ', '').replace(',','.', 1)
    day = entry_day.get().replace(' ', '').replace(',', '.', 1)
    report_error = get_report_error(name, amount, price, day)
    if not report_error and name:
        label_warning.grid_remove()
        entry_total_price.insert(0, f"{int(amount)*float(price)/float(day):.2f}")
    elif report_error: 
        label_warning.grid()
        label_warning.config(text=report_error)
        entry_total_price.insert(0, '')
        label_bill.config(text='')
    return name, amount, price, day, entry_total_price.get(), report_error

 
def set_total_annual():
    # preparation
    report_error=''
    label_bill.config(text='')
    entry_cost_annual.delete(0, 'end')
    report_error = set_total_price(list_entries1)[-1]
    price1 = entry_total_price1.get()
    report_error= set_total_price(list_entries2)[-1]
    price2 = entry_total_price2.get()
    report_error = set_total_price(list_entries3)[-1]
    price3  = entry_total_price3.get()

    if not price1 and not price2 and not price3: 
        label_warning3.config(text='Fill up at least 1 line')
    elif report_error: 
        entry_cost_annual.insert(0, '')
    else:
        sum_amount= 0
        sum_amount = sum_amount + float(price1) if price1 else sum_amount
        sum_amount = sum_amount + float(price2) if price2 else sum_amount
        sum_amount = sum_amount + float(price3) if price3 else sum_amount
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
    col_width = round(width/6)
    col1_width = width-col_width*4
    bill_string = f"{root.title().center(width)}\n"
    # headers
    bill_string = f"{bill_string}{label0['text'].center(col1_width)}{label1['text'].center(col_width)}{label2['text'].center(col_width)}{label3['text'].center(col_width)}{label5['text'].center(col_width)}\n"
    bill_string = f"{bill_string}{'-'*width}\n"
    # item1
    result = set_total_price(list_entries1)
    if result:
        name, amount, price, day, price_total, error = result
        if name:
            bill_string = f"{bill_string}{name.ljust(col1_width)}{amount.center(col_width)}x{price.center(col_width)}/{day.center(col_width)}={price_total.rjust(col_width-3)}\n"
    # item2
    result = set_total_price(list_entries2)
    if result:
        name, amount, price, day, price_total, error = result
        if name:
            bill_string = f"{bill_string}{name.ljust(col1_width)}{amount.center(col_width)}x{price.center(col_width)}/{day.center(col_width)}={price_total.rjust(col_width-3)}\n"
    # item3
    result = set_total_price(list_entries3)
    if result:
        name, amount, price, day, price_total, error = result
        if name: 
            bill_string = f"{bill_string}{name.ljust(col1_width)}{amount.center(col_width)}x{price.center(col_width)}/{day.center(col_width)}={price_total.rjust(col_width-3)}\n"

    bill_string = f"{bill_string}{'-'*width}\n"
    bill_string = f"{bill_string}{label_annual['text'].rjust(col_width*5-1)} {entry_cost_annual.get().ljust(col_width)}\n"
    bill_string = f"{bill_string}{label_years['text'].rjust(col_width*5-1)} {entry_years.get().ljust(col_width)}\n"
    bill_string = f"{bill_string}{label_cost_total['text'].rjust(col_width*5-1)} {entry_for_full.get().ljust(col_width)}\n"
    label_bill.config(text=bill_string)
    label_bill.grid(row=12, columnspan=6, sticky='nsew')


root = Tk()
root.title('Calculator for cat')
label0 = Label(text="Product")
label0.grid(column=0, row=0)
label1 = Label(text="amount")
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
entry_amount1 = Entry()
entry_amount1.insert(0, "3")
entry_amount1.grid(column=1, row=1)
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
list_entries1 = [entry_name1, entry_amount1, entry_price1, entry_days1, label_warning1, entry_total_price1]
button_1 = Button(text="=", command=lambda: set_total_price(list_entries1))
button_1.grid(column=4, row=1)

entry_name2 = Entry()
entry_name2.insert(0, "Food tuna in a can")
entry_name2.grid(column=0, row=3)
entry_amount2 = Entry()
entry_amount2.insert(0, "1")
entry_amount2.grid(column=1, row=3)
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
list_entries2 = [entry_name2, entry_amount2, entry_price2, entry_days2, label_warning2, entry_total_price2]
button_2 = Button(text="=", command=lambda: set_total_price(list_entries2))
button_2.grid(column=4, row=3)

entry_name3 = Entry()
entry_name3.insert(0, '')
entry_name3.grid(column=0, row=5)
entry_amount3 = Entry()
entry_amount3.insert(0, '')
entry_amount3.grid(column=1, row=5)
entry_price3 = Entry()
entry_price3.insert(0, '')
entry_price3.grid(column=2, row=5)
entry_days3 = Entry()
entry_days3.insert(0, '')
entry_days3.grid(column=3, row=5)
entry_total_price3 = Entry()
entry_total_price3.insert(0, '')
entry_total_price3.grid(column=5, row=5)
label_warning3 = Label()
label_warning3.grid(column=0, columnspan=6, sticky='nsew', row=6)
label_warning3.grid_remove()
list_entries3 = [entry_name3, entry_amount3, entry_price3, entry_days3, label_warning3, entry_total_price3]
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
label_warning_years = Label()
label_warning_years.grid(column=0, columnspan=6, sticky='nsew', row=9)
label_warning_years.grid_remove()

label_cost_total = Label(text="Total cost for whole period:", justify=RIGHT)
label_cost_total.grid(column=0, row=10, columnspan=4)
button_6 = Button(text="=", command=set_total_cost)
button_6.grid(column=4, row=10)
entry_for_full= Entry()
entry_for_full.grid(column=5, row=10)

Label(text="Print bill with width(min 60):", anchor='e', justify="center").grid(column=0, row=11, columnspan=4)
button_print_bill = Button(text="Print", command=print_bill)
button_print_bill.grid(column=4, row=11)
entry_bill_width = Entry()
entry_bill_width.grid(column=3, row=11)
entry_bill_width.insert(0, '100')

label_bill = Label(font=('Ubuntu Mono', 10))

root.mainloop()

