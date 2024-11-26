import tkinter
from tkinter import *
from tkinter.ttk import *
turn = 'X'

"""
"""


def set_button_press(button):
    global turn
    if not str(button.cget('text')).isalnum():
        button.config(text=turn)
        check_winner()
        turn = 'O'if turn == 'X' else 'X'


def clear_fields():
    for button in button_00, button_10, button_20, button_01, button_11, button_21, button_20, button_21, button_22:
        button.config(text='')


def check_winner():
    column1_true = button_00.cget('text') == button_01.cget('text') == button_02.cget('text') and button_00.cget('text').isalnum()
    column2_true = button_10.cget('text') == button_11.cget('text') == button_12.cget('text') and button_10.cget('text').isalnum()
    column3_true = button_20.cget('text') == button_21.cget('text') == button_22.cget('text') and button_20.cget('text').isalnum()
    row1_true = button_00.cget('text') == button_10.cget('text') == button_20.cget('text') and button_00.cget('text').isalnum()
    row2_true = button_01.cget('text') == button_11.cget('text') == button_21.cget('text') and button_01.cget('text').isalnum()
    row3_true = button_02.cget('text') == button_12.cget('text') == button_22.cget('text') and button_02.cget('text').isalnum()
    diagonal_forward_true = button_02.cget('text') == button_11.cget('text') == button_20.cget('text') and button_11.cget('text').isalnum()
    diagonal_back_true = button_00.cget('text') == button_11.cget('text') == button_22.cget('text') and button_11.cget('text').isalnum()
    if column1_true or column2_true or column3_true or row1_true or row2_true or row3_true or diagonal_forward_true or diagonal_back_true:
        print(f"{turn}-WON!")


root = Tk()
root.title('TicTacToe v1.0')
button_00 = Button(text="", command=lambda: set_button_press(button_00))
button_00.grid(column=0, row=0, ipadx=80, ipady=100)
button_01 = Button(text="", command=lambda: set_button_press(button_01))
button_01.grid(column=0, row=1, ipadx=80, ipady=100)
button_02 = Button(text="", command=lambda: set_button_press(button_02))
button_02.grid(column=0, row=2, ipadx=80, ipady=100)
button_10 = Button(text="", command=lambda: set_button_press(button_10))
button_10.grid(column=1, row=0, ipadx=80, ipady=100)
button_11 = Button(text="", command=lambda: set_button_press(button_11))
button_11.grid(column=1, row=1, ipadx=80, ipady=100)
button_12 = Button(text="", command=lambda: set_button_press(button_12))
button_12.grid(column=1, row=2, ipadx=80, ipady=100)
button_20 = Button(text="", command=lambda: set_button_press(button_20))
button_20.grid(column=2, row=0, ipadx=80, ipady=100)
button_21 = Button(text="", command=lambda: set_button_press(button_21))
button_21.grid(column=2, row=1, ipadx=80, ipady=100)
button_22 = Button(text="", command=lambda: set_button_press(button_22))
button_22.grid(column=2, row=2, ipadx=80, ipady=100)
button_new_game = Button(text="New Game", command=clear_fields)
button_new_game.grid(columnspan=3, row=3,ipadx=200, ipady=10)

root.mainloop()