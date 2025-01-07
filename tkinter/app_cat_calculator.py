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


// fix me
fill default width  - done 
dont print if any field are empty
years allow only digits  and not negative  should work with 0,5 but allow only kratnoe 0.5
all should work witn 1, 2 products only
proverka na 0.5 v dnyah ne rabotaet


//dont show the empty line on bill
check the days and years with 5.55
if zero on price do not fill up with zero - use '' instead
replace msg_warning to report_error - *
qty to amount
"""
message_warning = ''

def check_time_period(period):
    if period.find('.') != -1:
        period[period.find('.')+1:].rstrip('0').replace('5', '', 1)


def get_report_error(name, qty, price, day):
    name_valid = name.replace(' ', '').replace('.', '').replace('-', '').replace('`', '').isalnum() and len(name) >= 2
    qty_false = not (qty.isdigit() and qty >= '1')
    price_valid = price.replace('.', '', 1).isdigit() and len(price.rpartition('.')[-1]) < 3
    day_valid = not day[day.find('.')+1:].rstrip('0').replace('5', '', 1) if day.find('.') !=-1 else day.replace('.', '').isdigit()
    global message_warning
    msg_warning = ''
    if not name and not qty and not price and not day:
        msg_warning = 'Fill the line'
        return msg_warning
    if not name_valid:
        msg_warning = f"{msg_warning}Fill up 'Product' field with 2 or more alphabet symbols\n"
    if qty_false:
        msg_warning = f"{msg_warning}Fill up 'Qty' int, positive\n"
    if not price_valid:
        msg_warning = f"{msg_warning}Fill up 'Price' with positive number and not more then 2 digits after dot\n"
    if not day_valid:
        msg_warning = f"{msg_warning}Fill up 'Day' with positive number and be dividing by 0.5\n"
    message_warning = msg_warning
    return msg_warning.removesuffix('\n')


def set_total_price(list_entries):
    entry_name, entry_qty, entry_price, entry_day, label_warning, entry_total_price = list_entries
    entry_total_price.delete(0, 'end')
    label_warning.config(text='')
    
    name = entry_name.get().strip(' ')
    qty = entry_qty.get().replace(' ', '').replace(',','.', 1)
    price = entry_price.get().replace(' ', '').replace(',','.', 1)
    day = entry_day.get().replace(' ', '').replace(',', '.', 1)
    msg_warning = get_report_error(name, qty, price, day)
    if msg_warning == 'Fill the line':
        label_warning.grid()
        label_warning.config(text=msg_warning)
        entry_total_price.insert(0, '0.00')
    elif msg_warning:
        label_warning.grid()
        label_warning.config(text=msg_warning)
        entry_total_price.insert(0, '0.00')
        label_bill.config(text='')
    elif not msg_warning or msg_warning == 'Fill the line':
        label_warning.grid_remove()
        entry_total_price.insert(0, f"{int(qty)*float(price)/float(day):.2f}")
    return name, qty, price, day, entry_total_price.get()

 
def set_total_annual():
    label_bill.config(text='')
    entry_cost_annual.delete(0, 'end')
    set_total_price(list_entries1)
    set_total_price(list_entries2)
    set_total_price(list_entries3)
    price1, price2, price3 = entry_total_price1.get(), entry_total_price2.get(), entry_total_price3.get()
    msg_warning1, msg_warning2, msg_warning3 = label_warning1['text'], label_warning2['text'], label_warning3['text'] 
    msg1_true = msg_warning1 and msg_warning1 != 'Fill the line'
    msg2_true = msg_warning2 and msg_warning2 != 'Fill the line'
    msg3_true = msg_warning3 and msg_warning3 != 'Fill the line'
    if msg1_true or msg2_true or msg3_true: 
        entry_cost_annual.insert(0, '0.00')
    else:
        entry_cost_annual.insert(0, f'{((float(price1)+float(price2)+float(price3)) * 365):.2f}')


def set_total_cost():
    set_total_annual()
    cost_annual = entry_cost_annual.get()
    year = entry_years.get().replace(' ', '').replace(',', '.', 1)
    year_valid = not year[year.find('.')+1:].rstrip('0').replace('5', '', 1) if year.find('.') !=-1 else year.replace('.', '').isdigit()
    if not year_valid:
        label_warning_years.grid()
        label_warning_years.config(text="Fill up 'Year' with positive number and be dividing by 0.5")
        return
    data_true = year_valid and cost_annual.replace('.', '').isdigit()
    entry_for_full.delete(0, 'end')
    entry_for_full.insert(0, f"{(float(cost_annual)*float(year)):.2f}") if data_true else 0, ''


def print_bill():
    set_total_cost()
    if message_warning and message_warning != 'Fill the line':
        return
    if not entry_cost_annual.get().replace('.', '').isdigit():
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
        name, qty, price, day, price_total = result
        bill_string = f"{bill_string}{name.ljust(col1_width)}{qty.center(col_width)}x{price.center(col_width)}/{day.center(col_width)}={price_total.rjust(col_width-3)}\n"
    # item2
    result = set_total_price(list_entries2)
    if result:
        name, qty, price, day, price_total = result
        bill_string = f"{bill_string}{name.ljust(col1_width)}{qty.center(col_width)}x{price.center(col_width)}/{day.center(col_width)}={price_total.rjust(col_width-3)}\n"
    # item3
    result = set_total_price(list_entries3)
    if result:
        name, qty, price, day, price_total = result
        bill_string = f"{bill_string}{name.ljust(col1_width)}{qty.center(col_width)}x{price.center(col_width)}/{day.center(col_width)}={price_total.rjust(col_width-3)}\n"

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
entry_name3.insert(0, '')
entry_name3.grid(column=0, row=5)
entry_qty3 = Entry()
entry_qty3.insert(0, '')
entry_qty3.grid(column=1, row=5)
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
label_warning_years = Label()
label_warning_years.grid(column=0, columnspan=6, sticky='nsew', row=9)
label_warning_years.grid_remove()

label_cost_total = Label(text="Total cost for whole period:", justify=RIGHT)
label_cost_total.grid(column=0, row=10, columnspan=4)
button_6 = Button(text="=", command=set_total_cost)
button_6.grid(column=4, row=10)
entry_for_full= Entry()
entry_for_full.grid(column=5, row=10)

Label(text="Print bill with width(min 60):", anchor='e', justify="center").grid(column=0, row=10, columnspan=4)
button_print_bill = Button(text="Print", command=print_bill)
button_print_bill.grid(column=4, row=11)
entry_bill_width = Entry()
entry_bill_width.grid(column=3, row=11)
entry_bill_width.insert(0, '100')

label_bill = Label(font=('Ubuntu Mono', 10))

root.mainloop()

