"""
Создайте оглавление книги. Для задания названий и страницы используйте класс. Для визуализации отступа пробелами, точками или подчеркиваниями используйте свойство класса.
"""
"""
WIDTH_PAGE = 70

class TitleBook:
    symbol_indent:str = ' '
    def __init__(self, text_line: str = '', number_page: int = 0 )->None:
        self.text_line = text_line
        self.number_page = number_page
        size_padding = WIDTH_PAGE - len(self.text_line) - len(str(self.number_page)) - 2
        self.line = f"{self.text_line} {self.symbol_indent*size_padding} {self.number_page}"


print('Table of Content'.center(WIDTH_PAGE))
print('*'*WIDTH_PAGE)
line_1 = TitleBook('PreBeginning',  1)
print(line_1.line)
TitleBook.symbol_indent = '.'
print(TitleBook('Beginning', 2).line)
print(TitleBook('Core', 20).line)
print(TitleBook('End',  100).line)
"""
"""
2 column title
"""
# WIDTH_PAGE = 70
# WIDTH_MIDDLE_GAP = 2 if WIDTH_PAGE%2 == 0 else 3
# WIDTH_COLUMN = int((WIDTH_PAGE - WIDTH_MIDDLE_GAP)/2)
# LIST_TITLE = [
#     ['Prolog', 2],
#     ['The Midnight Library', 5],
#     ['Where the Crawdads Sing', 6],
#     ['Never Let Me Go', 9],
#     ['The Devil Wears Prada', 10],
#     ['Tender is the Flesh', 110],
#     ['Nightbitch', 9999]
# ]
#
# class TitleBookDouble:
#     symbol_indent:str = ' '
#     def __init__(self, list_titles: list = []):
#         self.list_titles = list_titles
#         self.line = ''
#         for number, line in enumerate(self.list_titles):
#             title, number_page = line
#             _line ='\n' if number%2 == 0 else ' '*WIDTH_MIDDLE_GAP
#             size_padding = int(WIDTH_COLUMN - len(title) - len(str(number_page)) - 2)
#             self.line = f"{self.line}{_line}{title} {self.symbol_indent*size_padding} {number_page}"
#
#
# print('Table of Content'.center(WIDTH_PAGE))
# TitleBookDouble.symbol_indent = '.'
# print(TitleBookDouble.symbol_indent*WIDTH_PAGE)
# print(f"{TitleBookDouble(LIST_TITLE).line}")

"""
Реализуйте текстовое меню с выравниванием по центру.
Ширина меню задаётся переменной.
Цифры должны храниться в переменных в числовом типе.
Каждый пункт меню выравнивается отдельно.
Текст должен растягиваться по ширине указанной в переменной.
Реализуйте вывод с помощью одной функции print(), 
т.е. собрать весь чек в виде одно строки и вывести в одном принте.
"""

class TextMenu:
    symbol_indent:str = '-'
    def __init__(self, dictionary_menu: dict = {}):
        self.dictionary_menu = {}
        self.line = 'Menu'.center(WIDTH_PAGE)
        list_two_column, list_titles = [], []
        for title, detail in dictionary_menu.items():
            if title == 'drinks':
                self.line = f"{self.line}\n{title.title().center(WIDTH_PAGE, self.symbol_indent)}"
                for item in detail:
                    line_= f"{item['item'].ljust(WIDTH_PAGE-16)}{str(item['quantity']).rjust(5)} {item['means'].ljust(3)}{str(item['price']).rjust(7)}"
                    self.line = f"{self.line}\n{line_}"
            else:
                list_titles.append(title)
                list_two_column.append(detail)

        width_gap = 2 if WIDTH_PAGE % 2 == 0 else 3
        width_column = int((WIDTH_PAGE - width_gap) / 2)
        self.line=f"{self.line}\n{list_titles[0].title().center(width_column, self.symbol_indent)}{' '*width_gap}{list_titles[1].title().center(width_column, self.symbol_indent)}"
        for itemA, itemB in zip(list_two_column[0], list_two_column[1]):
            line_ = f"{itemA['item'].ljust(width_column - 16)}{str(itemA['quantity']).rjust(5)} {itemA['means'].ljust(3)}{str(itemA['price']).rjust(7)}"
            line_ = f"{line_}{' '*width_gap}{itemA['item'].ljust(width_column - 16)}{str(itemA['quantity']).rjust(5)} {itemA['means'].ljust(3)}{str(itemA['price']).rjust(7)}"
            self.line = f"{self.line}\n{line_}"


WIDTH_PAGE = 70
MENU_SOURCE = {
    'drinks': [
        {'item': 'Tea', 'quantity': 150, 'means': 'ml','price': 2},
        {'item': "Juice", 'quantity': 150, 'means': 'ml', 'price': 3},
        {'item': "Coffee", 'quantity': 50, 'means': 'ml', 'price': 4},
        {'item': "Water", 'quantity': 250, 'means': 'ml', 'price': 1},
    ],
    'pastries': [
        { 'item': "Bread", 'quantity': 150, 'means': 'pc', 'price': 2},
        { 'item': "NotBread", 'quantity': 150, 'means': 'pc', 'price': 2},
        { 'item': "Cake", 'quantity': 1, 'means': 'pc', 'price': 100},
    ],
    'salads': [
        { 'item': "Cesar Salad", 'quantity': 150, 'means': 'g', 'price': 14.3},
        { 'item': "Olivie Salad", 'quantity': 150, 'means': 'g', 'price': 20},
        { 'item': "Vinaigrette", 'quantity': 150, 'means': 'g', 'price': 20},
    ]}
print(TextMenu(MENU_SOURCE).line)
