import tkinter
from tkinter import *

list_fields = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '']
list_figures = ['P','R','N','B', 'Q', 'K', 'B', 'N', 'R', 'P']
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


def move_figure():



root = Tk()
root.title("Chessboard")
image_square = tkinter.PhotoImage(width=1, height=1)
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
        regular_square = Button(text='', bg=color, image=image_square, width=50, height=50, font='bold', command=)
        regular_square.grid(column=column, row=row)
        list_square_line.append(regular_square)
        # creating list of list 
        if j == 7: 
            list_square.append(list_square_line)
            list_square_line = []
            j = 0;
        j += 1
        if row == 1: 
            regular_square.config(text=list_figures[i%length], foreground='black', compound='c')
        if row == 2: 
            regular_square.config(text=list_figures[0], foreground='black', compound='c')
        elif row == 7: 
            regular_square.config(text=list_figures[0], foreground='gray', font='bold', compound='c')
        elif row == 8: 
            regular_square.config(text=list_figures[i%length], foreground='gray', compound='c')
            
    
    i += 1



# list_square[1][1].config(text='t')

root.mainloop()