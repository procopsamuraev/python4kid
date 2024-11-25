import tkinter
from tkinter import *
from tkinter.ttk import *
turn = 1

"""

2x2 combinations
00 01
10 11
00 10
01 11
00 11
01 10


3x3 combinations
00 01 02
10 11 12
20 21 22

00 10 20
01 11 11
02 12 22

00 11 22
02 11 20

"""


def set_button_press(button):
    global turn
    buttons_combinations = [button_00, button_10, button_11, button_01]
    # field_empty_true = not str(button.cget('text')).isalnum()
    if not str(button.cget('text')).isalnum():
        button.config(text='X') if turn % 2 != 0 else button.config(text='O')
        turn = turn + 1
    check_winner()

def clear_fields():
    for button in button_00, button_10, button_11, button_01:
        button.config(text='')


def check_winner():
    if button_00.cget('text') == button_01.cget('text') == button_02.cget('text') and button_00.cget('text').isalnum()) or
    elif button_10.cget('text') == button_11.cget('text') == button_12.cget('text') and button_10.cget('text').isalnum():
        print(f"{button_00.cget('text')}-WON!")
    else:
        print("1")


root = Tk()
root.title('TicTacToe v0.9')
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