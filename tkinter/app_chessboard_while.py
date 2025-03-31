import tkinter
from tkinter import *
import tkinter.font as font

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
list_figures = ['P','R','N','B', 'Q', 'K', 'B', 'N', 'R', 'P']
list_move = []
font_default = ('"IBM Plex Mono" 18')
font_selected= ('"IBM Plex Mono" 18 bold')


def move_figure(column, row):
    square_selected = list_square[row][column]
    square_selected.config(font=font_selected)
    list_move.append(square_selected)
    if len(list_move) == 2:
        color = list_move[0]['foreground']
        figure = list_move[0]['text']
        list_move[0].config(text='')
        list_move[-1].config(text=figure, foreground=color, font=font_default)
        list_move.clear()


def get_board_address(column, row):
    column_board = list_fields[column+1]
    row_board = (length-2)-row
    return f"{column_board}{row_board}"
    

def get_square(column, row):
    return list_square[(column+(row)*(length-2))]


def get_column_row(address_board):
    column = list_fields.index(address_board[0])-1
    row = length - 2 - int(address_board[1])
    return column, row


def set_color_square(column, row, mode):
    row_even = row%2 == 0
    column_even = column%2 == 0
    if mode == 'board': 
        color = 'yellow' if not row_even and not column_even or row_even and column_even else 'brown'
    else:
        color = 'greenyellow' if not row_even and not column_even or row_even and column_even else 'green'

    return color


def convert_entry_address():
    if entry.get():
        address_board = entry.get()
        column, row = get_column_row(address_board)



def fill_entry(column, row):
    address_board = get_board_address(column, row)
    entry.delete(0,'end')
    entry.insert(0, address_board)
    


def get_selected_address():
    if entry.get():
        address_board_old = entry.get()
        return get_column_row(address_board_old)


def highlight_board():
    i = 0
    while i < len(list_square):
        row, column = i//(length-2), i%(length-2)
        color = set_color_square(column, row, 'board')
        list_square[i].config(background=color)
        i += 1 


def hightlight_square():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    square=get_square(column_selected,row_selected)
    square.config(font=font_selected, background='lightblue')


def highlight_row():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0
    while i < len(list_square) and row_selected:
        column, row = i%(length-2), i//(length-2)
        square_selected = row == row_selected and column == column_selected
        if row_selected == row and not square_selected:
            color = set_color_square(column, row, 'hightlight')
            list_square[i].config(background=color)
        if square_selected:
            list_square[i].config(background='lightblue')
        i += 1


def highlight_column():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2)
        square_selected = row == row_selected and column == column_selected
        if column == column_selected:
            color = set_color_square(column, row, 'hightlight')
            list_square[i].config(background=color)
        if square_selected:
            list_square[i].config(background='lightblue')
        i += 1

def highlight_rook():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2)
        square_selected = row == row_selected and column == column_selected
        if column == column_selected or row == row_selected and not square_selected:
            color = set_color_square(column, row, 'hightlight')
            list_square[i].config(background=color)
        if square_selected:
            list_square[i].config(background='lightblue')
        i += 1


def highlight_diagonal_back():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    diff_selected = column_selected-row_selected
    i = 0
    while i < len(list_square):
        row, column = i//(length-2), i%(length-2)
        square_selected = row == row_selected and column == column_selected
        if column-row == diff_selected and not square_selected:
            color = set_color_square(column, row, 'hightlight')
            list_square[i].config(background=color)
        if square_selected:
            list_square[i].config(background='lightblue')
        i += 1

def highlight_diagonal_forward():
    highlight_board()
    if entry.get():
        address_board_old = entry.get()
        column_selected, row_selected = get_column_row(address_board_old)
        sum_selected = row_selected+column_selected
    i = 0
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2), 
        square_selected = row == row_selected and column == column_selected
        if row+column == sum_selected and not square_selected:
            color = set_color_square(column, row, 'hightlight')
            list_square[i].config(background=color)
        if square_selected:
            list_square[i].config(background='lightblue')
        i += 1


def highlight_bishop():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    sum_selected = column_selected + row_selected
    diff_selected = column_selected - row_selected
    i = 0
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2) 
        square_selected = row == row_selected and column == column_selected
        if column-row == diff_selected or column+row == sum_selected and not square_selected:
            color = set_color_square(column, row, 'hightlight')
            list_square[i].config(background=color)
        if square_selected:
            list_square[i].config(background='lightblue')
        i += 1


def highlight_queen():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    sum_selected = column_selected + row_selected
    diff_selected = column_selected - row_selected
    i = 0
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2) 
        square_selected = row == row_selected and column == column_selected
        if (column-row == diff_selected or column+row == sum_selected or column == column_selected or row == row_selected) and not square_selected:
            color = set_color_square(column, row, 'hightlight')
            list_square[i].config(background=color)
        if square_selected:
            list_square[i].config(background='lightblue')
        i += 1


def highlight_three_horizontal():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0 
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2) 
        square_selected = row == row_selected and column == column_selected
        if (row == row_selected or row == row_selected-1 or row == row_selected+1) and not square_selected:
            color = set_color_square(column, row, 'hightlight')
            list_square[i].config(background=color)
        if square_selected:
            list_square[i].config(background='lightblue')
        i += 1


def highlight_five_horizontal():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0 
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2) 
        square_selected = row == row_selected and column == column_selected
        diff = str(row_selected-row).replace('-', '')
        if int(diff) < 3 and not square_selected:
            color = set_color_square(column, row, 'hightlight')
            list_square[i].config(background=color)
        if square_selected:
            list_square[i].config(background='lightblue')
        i += 1

def highlight_three_vertical():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0 
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2), 
        square_selected = row == row_selected and column == column_selected
        if column == column_selected or column == column_selected-1 or column == column_selected+1 and not square_selected:
            color = set_color_square(column, row, 'hightlight')
            list_square[i].config(background=color)
        if square_selected:
            list_square[i].config(background='lightblue')
        i += 1

        

def highlight_king():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    sum_selected = column_selected + row_selected
    diff_selected = column_selected - row_selected
    i = 0
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2) 
        column_step = int(str(column_selected - column).removeprefix('-')) < 2
        square_selected = row == row_selected and column == column_selected
        print(square_selected)
        row_step = int(str(row_selected - row).removeprefix('-')) < 2
        if (column-row == diff_selected or column+row == sum_selected or column == column_selected or row == row_selected) and column_step and row_step and not square_selected:
            color = set_color_square(column, row, 'hightlight')
            list_square[i].config(background=color)
        if square_selected:
            list_square[i].config(background='lightblue')
        i += 1



def highlight_horse():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0 
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2) 
        square_selected = row == row_selected and column == column_selected
        horse_true_1 = (row == row_selected-1 or row == row_selected+1) and (column == column_selected - 2 or column == column_selected + 2 )
        horse_true_2 = (row == row_selected-2 or row == row_selected+2) and (column == column_selected - 1 or column == column_selected + 1 )
        if (horse_true_1 or horse_true_2) and not square_selected:
            color = set_color_square(column, row, 'hightlight')
            list_square[i].config(background=color)
        if square_selected:
            list_square[i].config(background='lightblue')
        i += 1


root = Tk()
# root.geometry("600x600")
root.title("Chessboard v1.0")
length=len(list_fields)
max_size_field = len(list_fields)-1
list_square = []
# list_square_line = []
# draw board
i = 0 
j = 0
while i < length*length:
    row, column = i//length, i%length
        
    if row == 0 or row == max_size_field:
        Label(text=list_fields[i%length], bg='white').grid(column=column, row=row, sticky='news')
    elif column == 0 or column == max_size_field:
        Label(text=f"{max_size_field-row}", bg='white').grid(column=column, row=row, sticky='news')
    else:
        color = set_color_square(column, row, 'board')
        regular_square = Button(text=' ', bg=color, font=font_default, command=lambda row=row-1, column=column-1: fill_entry(column, row))
        regular_square.grid(column=column, row=row, sticky="nsew")
        list_square.append(regular_square)
        # creating list of list 
        # set board with figures
        # if row == 1: 
        #     regular_square.config(text=list_figures[i%length], foreground='black', compound='c')
        # if row == 2:
        #     regular_square.config(text=list_figures[0], foreground='black', compound='c')
        # elif row == 7: 
        #     regular_square.config(text=list_figures[0], foreground='gray', compound='c')
        # elif row == 8: 
        #     regular_square.config(text=list_figures[i%length], foreground='gray', compound='c')
    i += 1

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
Button(frame, text='five-horizontal', command=highlight_five_horizontal).pack(fill='both', expand=1) 
Button(frame, text='three-vertical', command=highlight_three_vertical).pack(fill='both', expand=1)
Button(frame, text='king', command=highlight_king).pack(fill='both', expand=1)
Button(frame, text='knight', command=highlight_horse).pack(fill='both', expand=1)

root.mainloop()