import tkinter
from tkinter import *
import tkinter.font as font

list_fields = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '']
list_figures = ['P','R','N','B', 'Q', 'K', 'B', 'N', 'R', 'P']
list_move = []
font_default = ('Helvetica 12 bold')
font_selected = ('Helvetica 12 bold italic')


#create Font object

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




root = Tk()
root.title("Chessboard")
width = 2
length=len(list_fields)
max_size_field = len(list_fields)-1
list_square = []
list_square_line = []

# draw board
i = 0 
j = 0
while i < length*length:
    row, column = i//length, i%length
    color = 'yellow' if (row %2 !=0 and column %2 !=0) or (row %2 ==0 and column %2 ==0) else 'brown'
        
    if row == 0 or row == max_size_field:
        Label(text=list_fields[i%length], bg='white', width=width).grid(column=column, row=row)
    elif column == 0 or column == max_size_field:
        Label(text=f"{max_size_field-row}", bg='white', width=width).grid(column=column, row=row)
    else:
        regular_square = Button(text='', bg=color, width=6, height=4, font=font_default, command=lambda row=row, column=column: move_figure(column, row))
        regular_square.grid(column=column, row=row)
        list_square_line.append(regular_square)
        # creating list of list 
        j += 1
        if j == 8: 
            list_square.append(list_square_line)
            list_square_line = []
            j = 0;
        # set board with figures
        if row == 1: 
            regular_square.config(text=list_figures[i%length], foreground='black', compound='c')
        if row == 2: 
            regular_square.config(text=list_figures[0], foreground='black', compound='c')
        elif row == 7: 
            regular_square.config(text=list_figures[0], foreground='gray', compound='c')
        elif row == 8: 
            regular_square.config(text=list_figures[i%length], foreground='gray', compound='c')
    i += 1

root.mainloop()