from tkinter import *


def print_button_addr(row1, column1):
    button_coordinate=f'{column1}{row1}'.title()
    if text.get(1.0).isalpha():
        text.insert(END, f', {button_coordinate}')
    else:
        text.insert(END, button_coordinate)


def draw_board():
    list_c = "abcd"
    list_r = "8765"
    column = 1
    for c in list_c:
        row = 1
        for r in list_r:
            button_text = f'{c}{r}'
            if (column % 2 == 0 and row % 2 != 0) or (column % 2 !=0 and row % 2 ==0):
                button = Button(root, text=button_text, bg="brown", activebackground="brown",activeforeground="brown", foreground="brown", command=lambda row1=r, column1=c: print_button_addr(row1, column1))
                button.grid(column=column, row=row)
            else:
                button = Button(root, text=button_text, bg="yellow", foreground="yellow", activeforeground="yellow", activebackground="yellow", command=lambda row1=r, column1=c: print_button_addr(row1, column1))
                button.grid(column=column, row=row)
            row = row + 1
        column = column + 1


root = Tk()
root.title("chessboard")


# draw 1st row and 1st column
column = 0
column_list = " ABCD"
for column_name in column_list:
    button = Button(root, text=column_name, bg="yellow")
    button.grid(column=column, row=0)
    column = column + 1

row = 1
row_list = "8765"
for row_name in row_list:
    button = Button(root, text=row_name, bg="yellow")
    button.grid(column=0, row=row)
    row = row + 1

draw_board()
text = Text(root, height=9, width=15)
text.grid(column=5, row=0, rowspan=10)

root.mainloop()