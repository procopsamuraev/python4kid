from tkinter import *

list_fields = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '']

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


root = Tk()
root.title("Chessboard")
width = 2
length=len(list_fields)
max_size_field = len(list_fields)-1
i = 0 
while i < length*length:
    row, column = i//length, i%length
    color = 'yellow' if (row %2 !=0 and column %2 !=0) or (row %2 ==0 and column %2 ==0) else 'brown'
        
    if row == 0 or row == max_size_field:
        Label(text=list_fields[i%length], bg='white', width=width).grid(column=column, row=row)
    elif column == 0 or column == max_size_field:
        Label(text=f"{max_size_field-row}", bg='white', width=width).grid(column=column, row=row)
    else:
        Button(text='', bg=color).grid(column=column, row=row)

    i += 1


root.mainloop()