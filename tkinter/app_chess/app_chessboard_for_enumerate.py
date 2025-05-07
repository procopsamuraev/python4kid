import tkinter
from tkinter import *
import tkinter.font as font


list_fields = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '']
# list_fields = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', '']
font_default = ('"IBM Plex Mono" 18')
font_selected= ('"IBM Plex Mono" 18 bold')
list_board_colors = ['white', 'grey']
list_hightlight_colors = ['greenyellow', 'green']
COLOR_HIGHTLIGHT_SQUARE = 'lightblue'

def fill_entry(address_board:str):
    entry.delete(0,'end')
    entry.insert(0, address_board)


def get_check_entry()->str:
    addres_board = entry.get()
    if addres_board.isalnum and addres_board[-1].isdecimal: 
        index_column_valid = addres_board[0] in list_fields[1:-1]
        index_row_valid = 0 < int(addres_board[1]) < len(list_fields)
        if index_column_valid and index_row_valid:
            return addres_board
        else: 
            print('not valid input in the field')

def highlight_board():
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row): 
            color = list_board_colors[(index_row + index_column)%2]
            square.config(background=color)


def hightlight_square():
    highlight_board()
    addres_board = get_check_entry()
    index_row_selected = len(list_fields) - 2 - int(addres_board[-1])
    index_column_selected = list_fields.index(addres_board[0]) - 1
    square = list_rows[index_row_selected][index_column_selected]
    square.config(background=COLOR_HIGHTLIGHT_SQUARE)


def highlight_row():
    highlight_board()
    addres_board = get_check_entry()
    for index_row, row in enumerate(list_rows):
        row_selected = index_row == len(row) - int(addres_board[-1])
        if row_selected:
            for index_column, square in enumerate(row):
                square_selected = index_column == list_fields.index(addres_board[0]) - 1
                if  square_selected:
                    square.config(background=COLOR_HIGHTLIGHT_SQUARE)
                else: 
                    square.config(background=list_hightlight_colors[(index_row + index_column)%2])


def highlight_column():
    highlight_board()
    addres_board = get_check_entry()
    for index_row, row in enumerate(list_rows):
        row_selected = index_row == len(row) - int(addres_board[-1])
        for index_column, square in enumerate(row):
            column_selected = index_column == list_fields.index(addres_board[0]) - 1
            if column_selected and row_selected:
                square.config(background=COLOR_HIGHTLIGHT_SQUARE)
            elif column_selected: 
                square.config(background=list_hightlight_colors[(index_row + index_column)%2])


def highlight_rook():
    highlight_board()
    addres_board = get_check_entry()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            if column_selected and row_selected:
                square.config(background=COLOR_HIGHTLIGHT_SQUARE)
            elif column_selected or row_selected: 
                square.config(background=list_hightlight_colors[(index_row + index_column)%2])


def highlight_diagonal_back():
    highlight_board()
    addres_board = get_check_entry()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            diagonal_back_line = index_column - index_row == index_column_selected - index_row_selected
            if column_selected and row_selected:
                square.config(background=COLOR_HIGHTLIGHT_SQUARE)
            elif diagonal_back_line:
                square.config(background=list_hightlight_colors[(index_row + index_column)%2])


def highlight_diagonal_forward():
    highlight_board()
    addres_board = get_check_entry()
    for index_row, row in enumerate(list_rows):
        index_row_selected = len(row) - int(addres_board[-1])
        row_selected = index_row == index_row_selected
        for index_column, square in enumerate(row):
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            diagonal_forward_line = index_column + index_row == index_column_selected + index_row_selected
            if column_selected and row_selected:
                square.config(background=COLOR_HIGHTLIGHT_SQUARE)
            elif diagonal_forward_line:
                square.config(background=list_hightlight_colors[(index_row + index_column)%2])


def highlight_bishop():
    highlight_board()
    addres_board = get_check_entry()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_column_selected = list_fields.index(addres_board[0]) - 1
            index_row_selected = len(row) - int(addres_board[-1])
            diagonal_forward_line = index_column + index_row == index_column_selected + index_row_selected
            diagonal_back_line = index_column - index_row == index_column_selected - index_row_selected
            if diagonal_forward_line and diagonal_back_line:
                square.config(background=COLOR_HIGHTLIGHT_SQUARE)
            elif diagonal_forward_line or diagonal_back_line:
                square.config(background=list_hightlight_colors[(index_row + index_column)%2])
                

def highlight_queen():
    highlight_board()
    addres_board = get_check_entry()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            diagonal_forward_line = index_column + index_row == index_column_selected + index_row_selected
            diagonal_back_line = index_column - index_row == index_column_selected - index_row_selected
            if diagonal_forward_line and diagonal_back_line:
                square.config(background=COLOR_HIGHTLIGHT_SQUARE)
            elif diagonal_forward_line or diagonal_back_line or row_selected or column_selected:
                square.config(background=list_hightlight_colors[(index_row + index_column)%2])


def highlight_three_horizontal():
    highlight_board()
    addres_board = get_check_entry()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            if column_selected and row_selected:
                square.config(background=COLOR_HIGHTLIGHT_SQUARE)
            elif -1 <= index_row - index_row_selected <= 1:
                square.config(background=list_hightlight_colors[(index_row + index_column)%2])


def highlight_three_vertical():
    highlight_board()
    addres_board = get_check_entry()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            if column_selected and row_selected:
                square.config(background=COLOR_HIGHTLIGHT_SQUARE)
            elif -1 <= index_column - index_column_selected <= 1:
                square.config(background=list_hightlight_colors[(index_row + index_column)%2])


def highlight_king():
    highlight_board()
    addres_board = get_check_entry()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            one_step_vertical = -1 <= index_column - index_column_selected <= 1
            one_step_horizontal = -1 <= index_row - index_row_selected <= 1
            if column_selected and row_selected:
                square.config(background=COLOR_HIGHTLIGHT_SQUARE)
            elif one_step_horizontal and one_step_vertical: 
                square.config(background=list_hightlight_colors[(index_row + index_column)%2])


def highlight_knight():
    highlight_board()
    addres_board = get_check_entry()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            vertical_shift = index_column - index_column_selected
            horizontal_shift = index_row - index_row_selected
            one_step_vertical = vertical_shift == 1 or vertical_shift == -1
            one_step_horizontal = horizontal_shift == 1 or horizontal_shift == -1
            two_step_vertical = vertical_shift == 2 or vertical_shift == -2 
            two_step_horizontal = horizontal_shift == 2 or horizontal_shift == -2
            if column_selected and row_selected:
                square.config(background=COLOR_HIGHTLIGHT_SQUARE)
            elif one_step_vertical and two_step_horizontal or one_step_horizontal and two_step_vertical:
                square.config(background=list_hightlight_colors[(index_row + index_column)%2])


root = Tk()
root.title('Chessboard v2.2')
list_rows = []

for row in range(len(list_fields)):
    list_squares = []
    for column, field in enumerate(list_fields):
        row_first, row_last = row == 0, row == len(list_fields)-1
        column_first, column_last = column == 0, column == len(list_fields)-1
        if row_first or row_last:
            Label(text=field, bg='white').grid(column=column, row=row, sticky='news')
        elif column_first or column_last:
            Label(text=f"{len(list_fields) - 1 - row}", bg='white').grid(column=column, row=row, sticky='news')
        else:
            color = list_board_colors[(row+column)%2]
            regular_square = Button(text=' ', bg=color, command=lambda address_board=f"{field}{len(list_fields)-1 - row}": fill_entry(address_board))
            regular_square.grid(column=column, row=row, sticky="nsew")
            list_squares.append(regular_square)
    if list_squares:
        list_rows.append(list_squares)



frame = Frame(root)
frame.grid(column=len(list_fields)+1, row=0, rowspan=len(list_fields), columnspan=5)
entry = Entry(frame)
entry.pack(fill='x')
Button(frame, text='highlight', command=highlight_board).pack(fill='both', expand=1)
Button(frame, text='square', command=hightlight_square).pack(fill='both', expand=1)
Button(frame, text='horizontal', command=highlight_row).pack(fill='both', expand=1)
Button(frame, text='vertical', command=highlight_column).pack(fill='both', expand=1)
Button(frame, text='rook', command=highlight_rook).pack(fill='both', expand=1)
Button(frame, text='diagonal-back', command=highlight_diagonal_back).pack(fill='both', expand=1)
Button(frame, text='diagonal-forward', command=highlight_diagonal_forward).pack(fill='both', expand=1)
Button(frame, text='bishop', command=highlight_bishop).pack(fill='both', expand=1) # 
Button(frame, text='queen', command=highlight_queen).pack(fill='both', expand=1)
Button(frame, text='three-horizontal', command=highlight_three_horizontal).pack(fill='both', expand=1)
Button(frame, text='three-vertical', command=highlight_three_vertical).pack(fill='both', expand=1)
Button(frame, text='king', command=highlight_king).pack(fill='both', expand=1)
Button(frame, text='knight', command=highlight_knight).pack(fill='both', expand=1)

root.mainloop()