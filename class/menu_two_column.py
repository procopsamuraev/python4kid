"""
Реализуйте текстовое меню с выравниванием по центру.
Ширина меню задаётся переменной.
Цифры должны храниться в переменных в числовом типе.
Каждый пункт меню выравнивается отдельно.
Текст должен растягиваться по ширине указанной в переменной.
Реализуйте вывод с помощью одной функции print(), 
т.е. собрать весь чек в виде одно строки и вывести в одном принте.
"""

from tkinter import *

class MenuItem:
    currency: str = '$'
    symbol_indent: str = '.'

    def __init__(self, name: str = '', quantity_item: int=0, means: str= 'gr', price: float=0, type_item: str = '',  width: int=80):
        self.name_item = name
        self.quantity_item = quantity_item
        self.means = means
        self.price_item = price
        line_price = f"{self.price_item:.2f}"
        self.type_item = type_item
        self.width = width
        line_middle = f"{str(self.quantity_item).rjust(4)}{self.means.rjust(3)}"
        line_end = f"{line_middle}{line_price.rjust(7)}{MenuItem.currency}"
        self.line = f"{self.name_item.ljust(self.width-len(line_end), MenuItem.symbol_indent)} {line_end}"

    def get_line(self):
        line_price = f"{self.price_item:.2f}"
        line_middle = f"{str(self.quantity_item).rjust(4)}{self.means.rjust(3)}"
        line_end = f"{line_middle}{line_price.rjust(7)}{MenuItem.currency}"
        self.line = f"{self.name_item.ljust(self.width-len(line_end), MenuItem.symbol_indent)} {line_end}"
        return self.line


WIDTH_PAGE = 71
width_gap = 0 if WIDTH_PAGE % 2 == 0 else 1
MENU_SOURCE = [
    {'name': 'Tea', 'quantity': 150, 'means': 'ml','price': 2, 'type': 'drinks'},
    {'name': 'Juice','quantity': 150, 'means': 'ml', 'price': 3, 'type': 'drinks'},
    {'name': "Coffee", 'quantity': 50, 'means': 'ml', 'price': 4, 'type': 'drinks'},
    {'name': "Bread", 'quantity': 1, 'means': 'pc', 'price': 2, 'type': 'pastries'},
    {'name': "Cake", 'quantity': 1, 'means': 'pc', 'price': 100, 'type': 'pastries'},
    {'name': "Cookies", 'quantity': 3, 'means': 'pc', 'price': 150, 'type': 'pastries'},
    {'name': "Cesar Salad", 'quantity': 150, 'means': 'g', 'price': 14.3, 'type': 'salads'},
    {'name': "Olivie Salad", 'quantity': 150, 'means': 'g', 'price': 20, 'type': 'salads'},
    {'name': "Vinaigrette", 'quantity': 150, 'means': 'g', 'price': 20, 'type': 'salads'},
    {'name': "Water", 'quantity': 250, 'means': 'ml', 'price': 1, 'type': 'drinks'},
    # {'name': "Borsh", 'quantity': 250, 'means': 'ml', 'price': 200, 'type': 'soups'},
]

root = Tk()
MenuItem.symbol_indent='_'
MenuItem.currency = '\u20BD'

dict_item_groups = {}
for dict_ in MENU_SOURCE:
    item_type = dict_['type']
    dict_item_groups.setdefault(item_type, [])
    dict_item_groups[item_type].append(dict_)

even_item_groups = len(dict_item_groups)%2 == 0

for index, (group, list_dict) in enumerate(dict_item_groups.items()):
    label_frame = LabelFrame(root, text=group.title())
    column_span=1
    width_column = int((WIDTH_PAGE - width_gap) / 2)
    column = index % 2
    if not even_item_groups and index==0:
        row = (index+1)//2
        width_column = WIDTH_PAGE
        column_span = 2
    elif not even_item_groups:
        row = (index + 1) // 2
    else:
        row = index // 2

    label_frame.grid(row=row, column=column, sticky=NW, columnspan=column_span )
    for dict_item in list_dict:
        line_menu = MenuItem()
        line_menu.name_item = dict_item['name']
        line_menu.quantity_item = dict_item['quantity']
        line_menu.means = dict_item['means']
        line_menu.price_item = dict_item['price']
        line_menu.type_item = group
        line_menu.width = width_column
        print(line_menu.get_line())
        Label(label_frame, font=('Ubuntu Mono', 10), text=line_menu.get_line()).grid()

root.mainloop()

# for dict_single in MENU_SOURCE:
#     menu_item = MenuItem()
#     menu_item.name_item = dict_single['item']
#     menu_item.quantity_item = dict_single['quantity']
#     menu_item.means = dict_single['means']
#     menu_item.price_item = dict_single['price']
#     menu_item.type = dict_single['type']
#     if menu_item.type not in list_label_types:
#         label_frame = LabelFrame(text=menu_item.type.title())
#         list_label_types.append(menu_item.type)
#         single_column = [menu_item.type] == list_label_types[0:1]
#         if single_column and not even_amount_type:
#             row = 0
#             column = 0
#             column_span = 2
#             label_frame.grid(row=row, column=column, sticky=NW, columnspan=column_span)
#         elif even_amount_type:
#             row = list_label_types.index(menu_item.type) // 2
#             column = list_label_types.index(menu_item.type) % 2
#             label_frame.grid(row=row, column=column, sticky=NW)
#         else:
#             row = (list_label_types.index(menu_item.type)+1)//2
#             column = list_label_types.index(menu_item.type)%2
#             label_frame.grid(row=row, column=column, sticky=NW)
#         list_label_frames.append(label_frame)
#     else:
#         label_frame = list_label_frames[list_label_types.index(menu_item.type)]
#     menu_item.width = WIDTH_PAGE if not even_amount_type and menu_item.type == list_label_types[0] else width_column
#     Label(label_frame, font=('Ubuntu Mono', 10), text=menu_item.get_line()).pack()
