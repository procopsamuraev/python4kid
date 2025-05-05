import tkinter
from tkinter import *
import tkinter.font as font


# fix me for with enumerate 
# c
# o 
# l
# 0 1 2 3 4 5 6 7 8 9  # row 
# 10111213141516171819
# 20
# * A B C D E F G H *
# 8 * * * * * * * * 8
# 7 * * * * * * * * 7
# - - - - - - - - - -
# 1 * * * * * * * * 1
# * A B C D E F G H *

list_fields = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '']
# list_fields = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', '']
font_default = ('"IBM Plex Mono" 18')
font_selected= ('"IBM Plex Mono" 18 bold')
list_board_colors = ['yellow', 'brown']
list_hightlight_colors = ['greenyellow', 'green']
color_hightlight_square = 'lightblue'


def get_board_address(column, row):
    column_board = list_fields[column+1]
    row_board =len(list_rows) - row
    return f"{column_board}{row_board}"
    

def fill_entry(column, row):
    address_board = get_board_address(column, row)
    entry.delete(0,'end')
    entry.insert(0, address_board)


def highlight_board():
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row): 
            color = list_board_colors[(index_row + index_column)%2]
            square.config(background=color)


def hightlight_square():
    highlight_board()
    addres_board = entry.get()
    index_row_selected = len(list_fields) - 2 - int(addres_board[-1])
    index_column_selected = list_fields.index(addres_board[0]) - 1
    square = list_rows[index_row_selected][index_column_selected]
    square.config(background=color_hightlight_square)


def highlight_row():
    highlight_board()
    addres_board = entry.get()
    for index_row, row in enumerate(list_rows):
        row_selected = index_row == len(row) - int(addres_board[-1])
        if row_selected:
            for index_column, square in enumerate(row):
                square_selected = index_column == list_fields.index(addres_board[0]) - 1
                if  square_selected:
                    color = color_hightlight_square
                else: 
                    color = list_hightlight_colors[(index_row + index_column)%2]
                square.config(background=color)


def highlight_column():
    highlight_board()
    addres_board = entry.get()
    for index_row, row in enumerate(list_rows):
        row_selected = index_row == len(row) - int(addres_board[-1])
        for index_column, square in enumerate(row):
            column_selected = index_column == list_fields.index(addres_board[0]) - 1
            if column_selected and row_selected:
                color = color_hightlight_square
                square.config(background=color)
            elif column_selected: 
                color = list_hightlight_colors[(index_row + index_column)%2]
                square.config(background=color)



def highlight_rook():
    highlight_board()
    addres_board = entry.get()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            if column_selected and row_selected:
                color = color_hightlight_square
                square.config(background=color)
            elif column_selected or row_selected: 
                color = list_hightlight_colors[(index_row + index_column)%2]
                square.config(background=color)


def highlight_diagonal_back():
    highlight_board()
    addres_board = entry.get()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            diagonal_back_line = index_column - index_row == index_column_selected - index_row_selected
            if column_selected and row_selected:
                color = color_hightlight_square
                square.config(background=color)
            elif diagonal_back_line:
                color = list_hightlight_colors[(index_row + index_column)%2]
                square.config(background=color)

def highlight_diagonal_forward():
    highlight_board()
    addres_board = entry.get()
    for index_row, row in enumerate(list_rows):
        index_row_selected = len(row) - int(addres_board[-1])
        row_selected = index_row == index_row_selected
        for index_column, square in enumerate(row):
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            diagonal_forward_line = index_column + index_row == index_column_selected + index_row_selected
            if column_selected and row_selected:
                color = color_hightlight_square
                square.config(background=color)
            elif diagonal_forward_line:
                color = list_hightlight_colors[(index_row + index_column)%2]
                square.config(background=color)


def highlight_bishop():
    highlight_board()
    addres_board = entry.get()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_column_selected = list_fields.index(addres_board[0]) - 1
            index_row_selected = len(row) - int(addres_board[-1])
            diagonal_forward_line = index_column + index_row == index_column_selected + index_row_selected
            diagonal_back_line = index_column - index_row == index_column_selected - index_row_selected
            if diagonal_forward_line and diagonal_back_line:
                color = color_hightlight_square
                square.config(background=color)
            elif diagonal_forward_line or diagonal_back_line:
                color = list_hightlight_colors[(index_row + index_column)%2]
                square.config(background=color)


def highlight_queen():
    highlight_board()
    addres_board = entry.get()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            diagonal_forward_line = index_column + index_row == index_column_selected + index_row_selected
            diagonal_back_line = index_column - index_row == index_column_selected - index_row_selected
            if diagonal_forward_line and diagonal_back_line:
                color = color_hightlight_square
                square.config(background=color)
            elif diagonal_forward_line or diagonal_back_line or row_selected or column_selected:
                color = list_hightlight_colors[(index_row + index_column)%2]
                square.config(background=color)



def highlight_three_horizontal():
    highlight_board()
    addres_board = entry.get()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            if column_selected and row_selected:
                color = color_hightlight_square
                square.config(background=color)
            elif -1 <= index_row - index_row_selected <= 1:
                color = list_hightlight_colors[(index_row + index_column)%2]
                square.config(background=color)


def highlight_three_vertical():
    highlight_board()
    addres_board = entry.get()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            if column_selected and row_selected:
                color = color_hightlight_square
                square.config(background=color)
            elif -1 <= index_column - index_column_selected <= 1:
                color = list_hightlight_colors[(index_row + index_column)%2]
                square.config(background=color)


def highlight_king():
    highlight_board()
    addres_board = entry.get()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            one_step_vertical = -1 <= index_column - index_column_selected <= 1
            one_step_horizontal = -1 <= index_row - index_row_selected <= 1
            if column_selected and row_selected:
                color = color_hightlight_square
                square.config(background=color)
            elif one_step_horizontal and one_step_vertical: 
                color = list_hightlight_colors[(index_row + index_column)%2]
                square.config(background=color)


def highlight_knight():
    highlight_board()
    addres_board = entry.get()
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row):
            index_row_selected = len(row) - int(addres_board[-1])
            row_selected = index_row == index_row_selected
            index_column_selected = list_fields.index(addres_board[0]) - 1
            column_selected = index_column == index_column_selected
            one_step_vertical = -1 <= index_column - index_column_selected <= 1
            one_step_horizontal = -1 <= index_row - index_row_selected <= 1
            two_step_vertical = -2 <= index_column - index_column_selected <= 2 
            two_step_horizontal = -2 <= index_row - index_row_selected <= 2
            if column_selected and row_selected:
                color = color_hightlight_square
                square.config(background=color)
            elif one_step_vertical and two_step_horizontal or one_step_horizontal and two_step_vertical:
                color = list_hightlight_colors[(index_row + index_column)%2]
                square.config(background=color)


    highlight_board()
    column_selected, row_selected = get_selected_address()
    for row in range(len(list_rows)):
        for column in range(len(list_rows[row])):
            step_column = column - column_selected
            step_row =  row - row_selected
            shift_column2row1 = (step_column == 2 or step_column == -2) and (step_row == 1 or step_row == -1 )
            shift_column1row2 = (step_column ==  1 or step_column == -1) and ( step_row == -2 or step_row == 2 )
            square_selected = row == row_selected and column == column_selected
            if square_selected: 
                list_rows[row][column].config(background=color_hightlight_square)
            elif shift_column2row1 or shift_column1row2: 
                color = list_hightlight_colors[(row+column)%2]
                list_rows[row][column].config(background=color)


root = Tk()
root.title('Chessboard v2.2')
row, list_rows = 0, []
for row in range(len(list_fields)):
    column, list_squares = 0, []
    for column in range(len(list_fields)):
        row_first, row_last = row == 0, row == len(list_fields)-1
        column_first, column_last = column == 0, column == len(list_fields)-1
        if row_first or row_last:
            Label(text=list_fields[column], bg='white').grid(column=column, row=row, sticky='news')
        elif column_first or column_last:
            Label(text=f"{len(list_fields) - 1 - row}", bg='white').grid(column=column, row=row, sticky='news')
        else:
            color = list_board_colors[(row+column)%2]
            regular_square = Button(text=' ', bg=color, command=lambda row=row-1, column=column-1: fill_entry(column, row))
            regular_square.grid(column=column, row=row, sticky="nsew")
            list_squares.append(regular_square)
    if list_squares:
        list_rows.append(list_squares)


frame = Frame(root)
frame.grid(column=11, row=0, rowspan=10, columnspan=5)
entry = Entry(frame)
entry.pack(fill='x')
Button(frame, text='highlight', command=highlight_board).pack(fill='both', expand=1) # perekrashivat dosku,eg: yellow to white, brown to black
Button(frame, text='square', command=hightlight_square).pack(fill='both', expand=1) # in entry set square and when press square then only entered square paint to color, only 1 square could be painted 
Button(frame, text='horizontal', command=highlight_row).pack(fill='both', expand=1) # paint only horizontal line on entry with green and square with lightblue
Button(frame, text='vertical', command=highlight_column).pack(fill='both', expand=1)
Button(frame, text='rook', command=highlight_rook).pack(fill='both', expand=1) 
Button(frame, text='diagonal-back', command=highlight_diagonal_back).pack(fill='both', expand=1)
Button(frame, text='diagonal-forward', command=highlight_diagonal_forward).pack(fill='both', expand=1)
Button(frame, text='bishop', command=highlight_bishop).pack(fill='both', expand=1) # 
Button(frame, text='queen', command=highlight_queen).pack(fill='both', expand=1)
Button(frame, text='three-horizontal', command=highlight_three_horizontal).pack(fill='both', expand=1)
# Button(frame, text='five-horizontal', command=highlight_five_horizontal).pack(fill='both', expand=1) 
Button(frame, text='three-vertical', command=highlight_three_vertical).pack(fill='both', expand=1)
Button(frame, text='king', command=highlight_king).pack(fill='both', expand=1)
Button(frame, text='knight', command=highlight_knight).pack(fill='both', expand=1)

root.mainloop()