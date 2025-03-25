import tkinter
from tkinter import *
import tkinter.font as font

# 
# fixme grid stretch square 

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
# 

list_fields = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '']
list_figures = ['P','R','N','B', 'Q', 'K', 'B', 'N', 'R', 'P']
list_move = []
font_default = ('"IBM Plex Mono" 18')
font_selected= ('"IBM Plex Mono" 18 bold')


def move_figure(column, row):
    square_selected = list_square[row-1][column-1]
    square_selected.config(font=font_selected)
    list_move.append(square_selected)
    if len(list_move) == 2:
        color = list_move[0]['foreground']
        figure = list_move[0]['text']
        list_move[0].config(text='')
        list_move[-1].config(text=figure, foreground=color, font=font_default)
        list_move.clear()


def get_board_address(column, row):
    column_board = list_fields[column]
    row_board = length-row-1
    return f"{column_board}{row_board}"
    

def get_square(column, row):
    return list_square[(column+(row-1)*(length-2))-1]


def get_column_row(address_board):
    column = list_fields.index(address_board[0])
    row = length - int(address_board[1]) - 1 
    return column, row


def set_color_square(column, row, color_scheme):
    if color_scheme == 'yellow':
        color = 'yellow' if (row %2 !=0 and column %2 !=0) or (row %2 ==0 and column %2 ==0) else 'brown'
    elif color_scheme == 'white':
        color = 'white' if (row %2 !=0 and column %2 !=0) or (row %2 ==0 and column %2 ==0) else 'black'
    return color


def convert_entry_address():
    if entry.get():
        address_board = entry.get()
        column, row = get_column_row(address_board)



def fill_entry(column, row):
    square_selected = get_square(column, row)
    # if entry.get():
        # address_board_old = entry.get()
        # column_old, row_old = get_column_row(address_board_old)
        # square_old = get_square(column_old, row_old)
        # color = set_color_square(column_old, row_old, 'yellow')
        # square_old.config(font=font_default, background=color)
    # square_selected.config(font=font_selected, background='blue')
    address_board = get_board_address(column, row)
    entry.delete(0,'end')
    entry.insert(0, address_board)
    


def return_address():
    line = entry.get().capitalize().replace(' ', '')
    if len(line)==2 and line.isalnum() and line[0] in list_fields and line[1]>'0' and line[1]<'f"{length}-2"':
        print(line, 'correct')
        x = list_fields.index(line[0])
        y = line[1]
        return x,y
    else:
        print(line, 'input is not valid. input should be coordinate on the board..[A-H][1-8]')


def highlight_board():
    i = 0
    color_scheme = 'yellow' if list_square[0]['bg'] == 'white' else 'white'
    while i < len(list_square):
        row, column = i//(length-2), i%(length-2)
        color = set_color_square(column, row, color_scheme)
        list_square[i].config(background=color)
        i += 1 


def hightlight_square():
    if entry.get():
        address_board_old = entry.get()
        column_old, row_old = get_column_row(address_board_old)

    i = 0
    while i < len(list_square):
        row, column = i//(length-2), i%(length-2)
        if row == row_old-1 and column != column_old-1:
            list_square[i].config(background='green')
        elif row == row_old-1 and column == column_old-1:
            list_square[i].config(background='blue')
        i += 1

def highlight_row():
    convert_entry_address()
    if entry.get():
        address_board_old = entry.get()
        column_old, row_old = get_column_row(address_board_old)
    row_highlight = row_old-1
    i = 0
    while i < len(list_square):
        row, column = i//(length-2), i%(length-2)
        if row == row_old-1 and column != column_old-1:
            list_square[i].config(background='green')
        elif row == row_old-1 and column == column_old-1:
            list_square[i].config(background='blue')
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
        color = set_color_square(column, row, 'yellow')
        # color = 'yellow' if (row %2 !=0 and column %2 !=0) or (row %2 ==0 and column %2 ==0) else 'brown'
        regular_square = Button(text=' ', bg=color, font=font_default, command=lambda row=row, column=column: fill_entry(column, row))
        # regular_square = Button(text=' ', bg=color, font=font_default, command=lambda row=row, column=column: move_figure(column, row))
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
# * radio button: 1. select button and select square on the board
Button(frame, text='highlight', command=highlight_board).pack(fill='both', expand=1) # perekrashivat dosku,eg: yellow to white, brown to black
Button(frame, text='square', command=fill_entry).pack(fill='both', expand=1) # in entry set square and when press square then only entered square paint to color, only 1 square could be painted 
Button(frame, text='horizontal', command=highlight_row).pack(fill='both', expand=1) # paint only horizontal line on entry with green and square with blue
Button(frame, text='vertical').pack(fill='both', expand=1) # only vertical
Button(frame, text='rook').pack(fill='both', expand=1) # square blue, lines green
Button(frame, text='diagonal-back').pack(fill='both', expand=1)
Button(frame, text='diagonal-forward').pack(fill='both', expand=1)
Button(frame, text='bishop').pack(fill='both', expand=1) # 
Button(frame, text='queen').pack(fill='both', expand=1)
Button(frame, text='three-horizontal').pack(fill='both', expand=1) # horizantal -+1, eg if A8 then A8, A7
Button(frame, text='five-horizontal').pack(fill='both', expand=1) # 
Button(frame, text='three-vertical').pack(fill='both', expand=1)
Button(frame, text='king').pack(fill='both', expand=1) # king sq blue, king pissible steps green
Button(frame, text='knight').pack(fill='both', expand=1)

# green, lightgreen on white, and darkgreen for black, blue is blue



root.mainloop()