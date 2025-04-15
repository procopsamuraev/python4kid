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
font_default = ('"IBM Plex Mono" 18')
font_selected= ('"IBM Plex Mono" 18 bold')
list_board_colors = ['yellow', 'brown']
list_hightlight_colors = ['greenyellow', 'green']
color_hightlight_square = 'blue'


def get_board_address(column, row):
    column_board = list_fields[column+1]
    row_board = (length-2)-row
    return f"{column_board}{row_board}"
    

def set_color_square(column, row, list_color):
    row_even = row%2 == 0
    column_even = column%2 == 0
    # print((row%2*column%2 + row%2*column%2)/2)
    # return list_color[(row%2*column%2 + row%2*column%2)//2]
    return list_color[0] if not row_even and not column_even or row_even and column_even else list_color[1]
    # return(list)


def fill_entry(column, row):
    address_board = get_board_address(column, row)
    entry.delete(0,'end')
    entry.insert(0, address_board)


def get_selected_address():
    if entry.get():
        address_board = entry.get()
        column = list_fields.index(address_board[0])-1
        row = length - 2 - int(address_board[1])
        print(column,row)
        return column,row


def highlight_board():
    y = 0
    while y < max_size_field-2:
        x = 0
        while x < max_size_field-2:
            color = set_color_square(x, y, list_board_colors)
            list_rows[y][x].config(background=color)
            x += 1
        y += 1 


def hightlight_square():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    square = list_rows[row_selected][column_selected]
    square.config(background=color_hightlight_square)


def highlight_row():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    row = 0
    while row <= len(list_rows):
        column = 0
        while column <= len(list_rows[row]):
            square_selected = row == row_selected and column == column_selected
            if square_selected:
                list_rows[row][column].config(background=color_hightlight_square)
            elif row == row_selected:
                color = set_color_square(column, row, list_hightlight_colors)
                list_rows[row][column].config(background=color)
            column += 1
        row += 1


# def highlight_row(): # 2nd version not recommended
#     highlight_board()
#     column_selected, row_selected = get_selected_address()
#     column = 0
#     while column <= max_size_field:
#         square = list_rows[row_selected][column_selected]
#         square.config(background=color_hightlight_square)
#         color = set_color_square(column, row, list_hightlight_colors)
#         list_rows[row_selected][column].config(background=color)
#         column += 1


# def highlight_column():
#     highlight_board()
#     column_selected, row_selected = get_selected_address()
#     row = 0 
#     while row <= max_size_field:
#         square = list_rows[row_selected][column_selected]
#         square.config(background=color_hightlight_square)
#         color = set_color_square(column_selected, row, list_hightlight_colors)
#         list_rows[row][column_selected].config(background=color)
#         row += 1


def highlight_column():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    row = 0
    while row < max_size_field:
        column = 0
        while column <= max_size_field:
            square_selected = row == row_selected and column == column_selected
            if square_selected:
                list_rows[row][column].config(background=color_hightlight_square)
            elif column == column_selected:
                color = set_color_square(column, row, list_hightlight_colors)
                print(row, column)
                list_rows[row][column].config(background=color)
            column += 1
        row += 1


def highlight_rook():
    highlight_board()
# def highlight_rook():
#     highlight_board()
#     column_selected, row_selected = get_selected_address()
#     row = 0
#     while row < max_size_field:
#         column = 0: 
#         while column
#         if column == column_selected and row == row_selected:
#             list_square[i].config(background=color_hightlight_square)
#         elif column == column_selected or row == row_selected:
#             color = set_color_square(column, row, list_hightlight_colors)
#             list_square[i].config(background=color)
#         i += 1


def highlight_diagonal_back():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0
    while i < len(list_square):
        row, column = i//(length-2), i%(length-2)
        square_selected = row == row_selected and column == column_selected
        diagonal_back_line = column_selected - row_selected == column - row
        if square_selected:
            list_square[i].config(background=color_hightlight_square)
        elif diagonal_back_line:
            color = set_color_square(column, row, list_hightlight_colors)
            list_square[i].config(background=color)
        i += 1


def highlight_diagonal_forward():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2), 
        square_selected = row == row_selected and column == column_selected
        diagonal_forward_line = row + column == row_selected + column_selected
        
        if square_selected:
            list_square[i].config(background=color_hightlight_square)
        elif diagonal_forward_line:
            color = set_color_square(column, row, list_hightlight_colors)
            list_square[i].config(background=color)
        i += 1


def highlight_bishop():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2) 
        diagonal_forward_line = row + column == row_selected + column_selected
        diagonal_back_line = column_selected - row_selected == column - row
        if diagonal_forward_line and diagonal_back_line:
            list_square[i].config(background=color_hightlight_square)
        elif diagonal_forward_line or diagonal_back_line:
            color = set_color_square(column, row, list_hightlight_colors)
            list_square[i].config(background=color)
        i += 1


def highlight_queen():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    # sum_selected = column_selected + row_selected
    # diff_selected = column_selected - row_selected
    i = 0
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2) 
        diagonal_forward_line = row + column == row_selected + column_selected
        diagonal_back_line = column_selected - row_selected == column - row
        bishop_line = diagonal_back_line or diagonal_forward_line
        rook_line = column == column_selected or row == row_selected
        square_selected = row == row_selected and column == column_selected
        if square_selected:
            list_square[i].config(background=color_hightlight_square)
        elif bishop_line or rook_line:
            color = set_color_square(column, row, list_hightlight_colors)
            list_square[i].config(background=color)
        i += 1


def highlight_three_horizontal():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0 
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2) 
        if column == column_selected and row == row_selected:
            list_square[i].config(background=color_hightlight_square)
        elif -1 <= row - row_selected <=1:
            color = set_color_square(column, row, list_hightlight_colors)
            list_square[i].config(background=color)
        i += 1


def highlight_five_horizontal():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0 
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2)
        square_selected = row == row_selected and column == column_selected
        if square_selected:
            list_square[i].config(background=color_hightlight_square)
        elif -2 <= row_selected - row <= 2:
            color = set_color_square(column, row, list_hightlight_colors)
            list_square[i].config(background=color)
        i += 1


def highlight_three_vertical():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0 
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2)
        square_selected = row == row_selected and column == column_selected
        if square_selected:
            list_square[i].config(background=color_hightlight_square)
        elif -1 <= column - column_selected <=1:
            color = set_color_square(column, row, list_hightlight_colors)
            list_square[i].config(background=color)
        i += 1
        

def highlight_king():
    highlight_board()
    # second method - is limit qeen to 1 step
    column_selected, row_selected = get_selected_address()
    i = 0
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2) 
        step_one_column = abs(column - column_selected) <= 1
        step_one_column = abs(column - column_selected) <= 1
        step_one_row =  abs(row - row_selected)  <= 1 
        square_selected = row == row_selected and column == column_selected
        if square_selected:
            list_square[i].config(background=color_hightlight_square)
        elif step_one_column and step_one_row:
            color = set_color_square(column, row, list_hightlight_colors)
            list_square[i].config(background=color)
        i += 1


def highlight_knight():
    highlight_board()
    column_selected, row_selected = get_selected_address()
    i = 0 
    while i < len(list_square):
        column, row = i%(length-2), i//(length-2)
        step_column = abs(column - column_selected)
        step_row = abs(row - row_selected)
        shift_column2row1 = step_column == 2 and step_row == 1  
        shift_column1row2 = step_column == 1 and step_row == 2
        square_selected = row == row_selected and column == column_selected
        if square_selected: 
            list_square[i].config(background=color_hightlight_square)
        elif shift_column2row1 or shift_column1row2: 
            color = set_color_square(column, row, list_hightlight_colors)
            list_square[i].config(background=color)
        i += 1


root = Tk()
root.title("Chessboard v1.2")
length = len(list_fields)
max_size_field = len(list_fields)-1
row, list_rows = 0, []
while row < length:
    column, list_squares = 0, []
    while column < length:
        row_first, row_last = row == 0, row == max_size_field
        column_first, column_last = column == 0, column == max_size_field
        if row_first or row_last:
            Label(text=list_fields[column], bg='white').grid(column=column, row=row, sticky='news')
        elif column_first or column_last:
            Label(text=f"{max_size_field-row}", bg='white').grid(column=column, row=row, sticky='news')
        else:
            color = set_color_square(column, row, list_board_colors)
            regular_square = Button(text=' ', bg=color, command=lambda row=row-1, column=column-1: fill_entry(column, row))
            regular_square.grid(column=column, row=row, sticky="nsew")
            list_squares.append(regular_square)
        
        column += 1
    if list_squares:
        list_rows.append(list_squares)
    row += 1

print(list_rows)

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