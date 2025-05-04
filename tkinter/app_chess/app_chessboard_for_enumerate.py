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


def get_selected_address():
    if entry.get():
        address_board = entry.get()
        column = list_fields.index(address_board[0])-1
        row = len(list_rows) - int(address_board[1])
        return column, row


def highlight_board():
    for index_row, row in enumerate(list_rows):
        for index_column, square in enumerate(row): 
            color = list_board_colors[(index_row + index_column)%2]
            square.config(background=color)


def hightlight_square():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    square = list_rows[row_selected][column_selected]
    square.config(background=color_hightlight_square)


def highlight_row():
    highlight_board()
    addres_board = entry.get()
    for index_row, row in enumerate(list_rows):
        if index_row == 8 - int(addres_board[-1]):
            for index_column, square in enumerate(row):
                if  index_column == 8 - int(addres_board[0]):
                    square.config(background=color_hightlight_square)
                color = list_board_colors[(index_row + index_column)%2]
                square.config(background=color)
                # list_rows[index_row][index_column].config(background='black')
#        for column in range(len(list_rows[row])):
#            square_selected = row == row_selected and column == column_selected
#            if square_selected:
#                list_rows[row][column].config(background=color_hightlight_square)
#            elif row == row_selected:
#                color = list_hightlight_colors[(row+column)%2]
#                list_rows[row][column].config(background=color)


def highlight_column():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    row = 0
    for row in range(len(list_rows)):
        column = 0
        for column in range(len(list_rows[row])):
            square_selected = row == row_selected and column == column_selected
            if square_selected:
                list_rows[row][column].config(background=color_hightlight_square)
            elif column == column_selected:
                color = list_hightlight_colors[(row+column)%2]
                list_rows[row][column].config(background=color)



def highlight_rook():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    for row in range(len(list_rows)):
        for column in range(len(list_rows[row])):
            if column == column_selected and row == row_selected:
                list_rows[row][column].config(background=color_hightlight_square)
            elif column == column_selected or row == row_selected:
                color = list_hightlight_colors[(row+column)%2]
                list_rows[row][column].config(background=color)


def highlight_diagonal_back():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    for row in range(len(list_rows)):
        for column in range(len(list_rows[row])):
            square_selected = row == row_selected and column == column_selected
            diagonal_back_line = column_selected - row_selected == column - row
            if square_selected:
                list_rows[row][column].config(background=color_hightlight_square)
            elif diagonal_back_line:
                color = list_hightlight_colors[(row+column)%2]
                list_rows[row][column].config(background=color)


def highlight_diagonal_forward():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    for row in  range(len(list_rows)):
        for column in range(len(list_rows[row])):
            square_selected = row == row_selected and column == column_selected
            diagonal_forward_line = row + column == row_selected + column_selected
            if square_selected:
                list_rows[row][column].config(background=color_hightlight_square)
            elif diagonal_forward_line:
                color = list_hightlight_colors[(row+column)%2]
                list_rows[row][column].config(background=color)


def highlight_bishop():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    for row in range(len(list_rows)):
        for column in range(len(list_rows[row])):
            diagonal_back_line = column_selected - row_selected == column - row
            diagonal_forward_line = row + column == row_selected + column_selected
            bishop_line = diagonal_back_line or diagonal_forward_line
            if diagonal_forward_line and diagonal_back_line:
                list_rows[row][column].config(background=color_hightlight_square)
            elif bishop_line:
                color = list_hightlight_colors[(row+column)%2]
                list_rows[row][column].config(background=color)


def highlight_queen():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    for row in range(len(list_rows)):
        for column in range(len(list_rows[row])):
            diagonal_back_line = column_selected - row_selected == column - row
            diagonal_forward_line = row + column == row_selected + column_selected
            bishop_line = diagonal_back_line or diagonal_forward_line
            rook_line = column == column_selected or row == row_selected
            if diagonal_forward_line and diagonal_back_line:
                list_rows[row][column].config(background=color_hightlight_square)
            elif bishop_line or rook_line:
                color = list_hightlight_colors[(row+column)%2]
                list_rows[row][column].config(background=color)


def highlight_three_horizontal():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    for row in range(len(list_rows)):
        for column in range(len(list_rows[row])):
            square_selected = row == row_selected and column == column_selected
            if square_selected:
                list_rows[row][column].config(background=color_hightlight_square)
            elif -1 <= row - row_selected <=1:
                color = list_hightlight_colors[(row+column)%2]
                list_rows[row][column].config(background=color)


def highlight_five_horizontal():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    for row in range(len(list_rows)):
        for column in range(len(list_rows[row])):
            square_selected = row == row_selected and column == column_selected
            if square_selected:
                list_rows[row][column].config(background=color_hightlight_square)
            elif -2 <= row - row_selected <= 2:
                color = list_hightlight_colors[(row+column)%2]
                list_rows[row][column].config(background=color)


def highlight_three_vertical():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    for row in range(len(list_rows)):
        for column in range(len(list_rows[row])):
            square_selected = row == row_selected and column == column_selected
            if square_selected:
                list_rows[row][column].config(background=color_hightlight_square)
            elif -1 <= column - column_selected <= 1:
                color = list_hightlight_colors[(row+column)%2]
                list_rows[row][column].config(background=color)
        

def highlight_king():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    for row in range(len(list_rows)):
        for column in range(len(list_rows[row])):
            step_one_column = -1 <= column - column_selected <= 1
            step_one_row = -1 <= row - row_selected  <= 1 
            square_selected = row == row_selected and column == column_selected
            if square_selected:
                list_rows[row][column].config(background=color_hightlight_square)
            elif step_one_column and step_one_row:
                color = list_hightlight_colors[(row+column)%2]
                list_rows[row][column].config(background=color)
    

def highlight_knight():
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
Button(frame, text='five-horizontal', command=highlight_five_horizontal).pack(fill='both', expand=1) 
Button(frame, text='three-vertical', command=highlight_three_vertical).pack(fill='both', expand=1)
Button(frame, text='king', command=highlight_king).pack(fill='both', expand=1)
Button(frame, text='knight', command=highlight_knight).pack(fill='both', expand=1)

root.mainloop()