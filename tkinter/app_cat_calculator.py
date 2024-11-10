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

no slices

at the end button " print bill" 

with configurable width
label width
label print bill
and label with printed bill

"""


def set_total_price(entry_name, entry_qty, entry_price, entry_day, entry_warning, entry_total_price):
    # msg_warning = ""
    name = entry_name.get().strip(' ')
    name_valid = name.replace(' ', '').replace('.', '').replace('-', '').replace('`', '').isalnum() and len(name) >= 2
    msg_warning = f"{name}:"
    qty = entry_qty.get().replace(' ', '')
    qty_valid = qty.isdigit() and qty > '0'
    price = entry_price.get().replace(' ', '')
    price_valid = price.replace('.', '', 1).isdigit() and str(float(price)*100).removesuffix('.0').isdigit()
    day = entry_day.get().replace(' ', '')
    day_valid = day.replace('.', '', 1).isdigit() and float(day) % 0.5 == 0
    if not name_valid:
        msg_warning = f"{msg_warning}Input more then 2 symbols in the name(excluded special characters"
    elif not qty_valid:
        msg_warning = f"{msg_warning}qty should be integer >0"
    elif not price_valid:
        msg_warning = f"{msg_warning}price must be float and >0"
    elif not day_valid:
        msg_warning = f"{msg_warning}day myst by number and delimoe na 0.5"
    entry_warning.insert(0, msg_warning) if msg_warning != f"{name}:" else None
    entry_total_price.insert(0, str(round(int(qty)*float(price)/float(day), 2)))


def set_total_year():
    # entry_cost_annual.insert(0, float(entry_total_price1.get())*365)
    entry_cost_annual.insert(0, float("entry_total_price1.get()"+"entry_price2.get()"+"entry_total_price3.get()")*365)


def set_total_cost():
    cost_annual = entry_cost_annual.get()
    years = entry_years.get().replace(' ', '')
    years_valid = years.isdigit() and '0' > years < '99'
    entry_for_full.insert(0, str(round(float(cost_annual) * int(years))))


root = Tk()
root.title('Calculator for cat')
Label(text="Товар").grid(column=0, row=0)
Label(text="Qty,pc").grid(column=1, row=0)
Label(text="Price,pc").grid(column=2, row=0)
Label(text="Qty days").grid(column=3, row=0)
Label(text="Total Price").grid(column=5, row=0)

entry_name1 = Entry()
entry_name1.insert(0, "eda dry")
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
entry_total_price1.grid(column=5, row=1)
entry_warning1 = Entry()
entry_warning1.insert(0, '')
entry_warning1.grid(column=0, columnspan=4, sticky='nsew', row=2)
button_1 = Button(text="=", command=lambda : set_total_price(entry_name1, entry_qty1, entry_price1, entry_days1, entry_warning1, entry_total_price1))
button_1.grid(column=4, row=1)

entry_name2 = Entry()
entry_name2.insert(0, "eda conservy")
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
entry_total_price2.grid(column=5, row=3)
entry_warning2 = Entry()
entry_warning2.grid(column=0, columnspan=4, sticky='nsew', row=4)
button_2 = Button(text="=", command=lambda: set_total_price(entry_name2, entry_qty2, entry_price2, entry_days2, entry_warning2, entry_total_price2))
button_2.grid(column=4, row=3)

entry_name3 = Entry()
entry_name3.insert(0, "napolnitel")
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
entry_total_price3.grid(column=5, row=5)
entry_warning3 = Entry()
entry_warning3.grid(column=0, columnspan=4, sticky='nsew', row=6)
button_3 = Button(text="=", command=lambda : set_total_price(entry_name3, entry_qty3, entry_price3, entry_days3, entry_warning3, entry_total_price3))
button_3.grid(column=4, row=5)


Label(text="Всего затраты за год:", justify=RIGHT).grid(column=0, row=7, columnspan=4)
button_6 = Button(text="=",command=set_total_year)
button_6.grid(column=4, row=7)
entry_cost_annual = Entry()
entry_cost_annual.grid(column=5, row=7)

Label(text="Period, years:", justify=RIGHT).grid(column=0, row=8, columnspan=4)
entry_years = Entry()
entry_years.grid(column=5, row=8)
entry_years.insert(0, "15")

Label(text="Total cost for whole period:", justify=RIGHT).grid(column=0, row=9, columnspan=4)
button_6 = Button(text="=", command=set_total_cost)
button_6.grid(column=4, row=9)
entry_for_full= Entry()
entry_for_full.grid(column=5, row=9)
root.mainloop()