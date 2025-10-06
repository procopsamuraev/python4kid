"""
Создайте оглавление книги. Для задания названий и страницы используйте класс. Для визуализации отступа пробелами, точками или подчеркиваниями используйте свойство класса.
"""


# WIDTH_PAGE = 70
#
# class TitleBook:
#     symbol_indent:str = ' '
#     def __init__(self, text_line: str = '', number_page: int = 0, width_page: int = 50):
#         self.text_line = text_line
#         self.number_page = number_page
#         size_padding = width_page - len(self.text_line) - len(str(self.number_page)) - 2
#         self.line = f"{self.text_line} {self.symbol_indent*size_padding} {self.number_page}"
#
#
# print('Table of Content'.center(WIDTH_PAGE))
# print('*'*WIDTH_PAGE)
# line_1 = TitleBook('PreBeginning',  1, WIDTH_PAGE)
# print(line_1.line)
# TitleBook.symbol_indent = '.'
# print(TitleBook('Beginning', 2, WIDTH_PAGE).line)
# print(TitleBook('Core', 20, WIDTH_PAGE).line)
# print(TitleBook('End',  100, WIDTH_PAGE).line)


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

    def __init__(self, name_item: str = '', quantity_item: int=0, means: str= 'gr', price: float=0, width: int=80):
        self.name_item = name_item
        self.quantity_item = quantity_item
        self.means = means
        self.price_item = price
        line_price = f"{self.price_item:.2f}"
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
width_column = int((WIDTH_PAGE - width_gap) / 2)
# in menu length pastries and salads should match
MENU_SOURCE = [
    {'item': 'Tea', 'quantity': 150, 'means': 'ml','price': 2, 'type': 'drinks'},
    {'item': 'Juice','quantity': 150, 'means': 'ml', 'price': 3, 'type': 'drinks'},
    {'item': "Coffee", 'quantity': 50, 'means': 'ml', 'price': 4, 'type': 'drinks'},
    {'item': "Bread", 'quantity': 1, 'means': 'pc', 'price': 2, 'type': 'pastries'},
    {'item': "Cake", 'quantity': 1, 'means': 'pc', 'price': 100, 'type': 'pastries'},
    {'item': "Cookies", 'quantity': 3, 'means': 'pc', 'price': 150, 'type': 'pastries'},
    {'item': "Cesar Salad", 'quantity': 150, 'means': 'g', 'price': 14.3, 'type': 'salads'},
    {'item': "Olivie Salad", 'quantity': 150, 'means': 'g', 'price': 20, 'type': 'salads'},
    {'item': "Vinaigrette", 'quantity': 150, 'means': 'g', 'price': 20, 'type': 'salads'},
    {'item': "Water", 'quantity': 250, 'means': 'ml', 'price': 1, 'type': 'drinks'},
    {'item': "Borsh", 'quantity': 250, 'means': 'ml', 'price': 200, 'type': 'soups'},
]

root = Tk()
MenuItem.symbol_indent='_'
MenuItem.currency = '\u20BD'
group_items = set()
for lines in MENU_SOURCE:
    group_items.add(lines['type'])


even_amount_types = True if len(group_items)%2 == 0 else False
if even_amount_types:
    width = width_column

list_label_frames = []
list_label_types = []

for dict_single in MENU_SOURCE:
    line_menu = MenuItem()
    line_menu.name_item = dict_single['item']
    line_menu.quantity_item = dict_single['quantity']
    line_menu.means = dict_single['means']
    line_menu.price_item = dict_single['price']
    type = dict_single['type']
    type_is_top =  not list_label_types or dict_single['type'] == list_label_types[0] and not even_amount_types
    if dict_single['type'] not in list_label_types:
        list_label_types.append(dict_single['type'])
        label_frame = LabelFrame(text=dict_single['type'].title())
        if type_is_top:
            row = 0
            column = 0
            label_frame.grid(row=row, column=column, sticky=NW, columnspan=2)
        elif even_amount_types:
            row = list_label_types.index(type) // 2
            column = list_label_types.index(type) % 2
            label_frame.grid(row=row, column=column, sticky=NW)
        else:
            row = (list_label_types.index(type)+1)//2
            column = list_label_types.index(type)%2
            label_frame.grid(row=row, column=column, sticky=NW)
        list_label_frames.append(label_frame)
    else:
        label_frame = list_label_frames[list_label_types.index(dict_single['type'])]
    line_menu.width = WIDTH_PAGE if not even_amount_types and type==list_label_types[0] else width_column
    print(line_menu.get_line())
    Label(label_frame, font=('Ubuntu Mono', 10), text=line_menu.get_line()).pack()

root.mainloop()

"""
2 column title
class should work with single line. and do for our of class, 
create 2 lists from initial list.. and pass to class left, right sides


"""
# WIDTH_PAGE = 71
# WIDTH_MIDDLE_GAP = 2 if WIDTH_PAGE%2 == 0 else 3
# WIDTH_COLUMN = int((WIDTH_PAGE - WIDTH_MIDDLE_GAP)/2)
# LIST_TITLE = [
#     ['Prolog', 2],
#     ['The Midnight Library', 5],
#     ['Where the Crawdads Sing', 6],
#     ['Never Let Me Go', 9],
#
#     ['The Devil Wears Prada', 10],
#     ['Tender is the Flesh', 110],
#     ['Nightbitch', 9990],
#     ['Nightbitch 2', 9999],
# ]
#
# class TitleBookDouble:
#     symbol_indent:str = ' '
#     width_page : int = 60
#     def __init__(self, list_titles: list = None):
#         self.list_titles = list_titles if list_titles else []
#         self.line = ''
#
#         mid: int = len(self.list_titles) // 2
#         list_left: list = self.list_titles[:mid]
#         list_right: list = self.list_titles[mid:]
#         if len(list_left) < len(list_right): # to normalize both list to the same length
#             list_left.append(['', '' ])
#         width_gap: int = 2 if TitleBookDouble.width_page % 2 == 0 else 3
#         # width_gap: int = 2 if self.width_page % 2 == 0 else 3
#         width_column : int = int((TitleBookDouble.width_page - width_gap) / 2)
#
#         for line in zip(list_left, list_right):
#             for line_part in line:
#                 name, page_number = line_part
#                 _padding: int = width_column - len(str(page_number))-1
#                 self.line = f"{self.line}{name.ljust(_padding, self.symbol_indent)} {page_number}{' '*width_gap }"
#             self.line+='\n'
# # TitleBookDouble()
# # TitleBookDouble.width_page = 71
# TitleBookDouble().width_page = 71
# line_book_title = f"{'Table of Content'.center(WIDTH_PAGE)}"
# TitleBookDouble.symbol_indent = '_'
# line_book_title = f"{line_book_title}\n{TitleBookDouble.symbol_indent*WIDTH_PAGE}"
# line_book_title = f"{line_book_title}\n{TitleBookDouble(LIST_TITLE).line}"
# # final print
# print(line_book_title)
