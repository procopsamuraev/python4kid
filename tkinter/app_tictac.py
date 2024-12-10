import tkinter
from tkinter import *
from tkinter.ttk import *
turn = 'X'

"""
"""


def set_button_press(button):
    global turn
    if not str(button.cget('text')).isalnum() and str(button_new_game.cget('text')) == "New Game":
        button.config(text=turn)
        check_winner()
        turn = 'O'if turn == 'X' else 'X'
        label_turn.config(text=f"Next turn player: {turn}")


def clear_fields():
    list_butons = [ button_00, button_01, button_02, button_10, button_11, button_12, button_20, button_21, button_22 ]
    # for button in button_00, button_01, button_02, button_10, button_11, button_12, button_20, button_21, button_22:
    for button in list_butons:
        button.config(text='')
    button_new_game.config(text='New Game')


def check_winner():
    column1_true = button_00.cget('text') == button_01.cget('text') == button_02.cget('text') in ( 'X', 'O')
    column2_true = button_10.cget('text') == button_11.cget('text') == button_12.cget('text') and button_10.cget('text').isalnum()
    column3_true = button_20.cget('text') == button_21.cget('text') == button_22.cget('text') and button_20.cget('text').isalnum()
    row1_true = button_00.cget('text') == button_10.cget('text') == button_20.cget('text') and button_00.cget('text').isalnum()
    row2_true = button_01.cget('text') == button_11.cget('text') == button_21.cget('text') and button_01.cget('text').isalnum()
    row3_true = button_02.cget('text') == button_12.cget('text') == button_22.cget('text') and button_02.cget('text').isalnum()
    diagonal_forward_true = button_02.cget('text') == button_11.cget('text') == button_20.cget('text') and button_11.cget('text').isalnum()
    diagonal_back_true = button_00.cget('text') == button_11.cget('text') == button_22.cget('text') and button_11.cget('text').isalnum()
    if column1_true or column2_true or column3_true or row1_true or row2_true or row3_true or diagonal_forward_true or diagonal_back_true:
        message=f" {turn}-won \nPress here for\na new game"
        button_new_game.config(text=message)
        count_wins(turn)
    elif button_00.cget('text').isalnum() and button_01.cget('text').isalnum() and button_02.cget('text').isalnum() and button_10.cget('text').isalnum() and button_11.cget('text').isalnum() and button_12.cget('text').isalnum() and button_20.cget('text').isalnum() and button_21.cget('text').isalnum() and button_22.cget('text').isalnum():
        message=f" Draw\nPress here for\na new game"
        button_new_game.config(text=message)
        count_wins('draw')


def count_wins(player):
    if player == 'X':
        count = int(label_player_X.cget('text'))
        label_player_X.config(text=str(count+1))
    if player == 'O':
        count = int(label_player_O.cget('text'))
        label_player_O.config(text=str(count+1))
    else:
        count = int(label_draw.cget('text'))
        label_draw.config(text=str(count+1))



root = Tk()
root.title('TicTacToe v1.1')
ipad_x = 40
ipad_y = 60
label_turn=Label(text=f'The player: {turn} start the game')
label_turn.grid(column=0,columnspan=3, row=6)
button_00 = Button(text="", command=lambda: set_button_press(button_00))
button_00.grid(column=0, row=0, ipadx=ipad_x, ipady=ipad_y)
button_01 = Button(text="", command=lambda: set_button_press(button_01))
button_01.grid(column=0, row=1, ipadx=ipad_x, ipady=ipad_y)
button_02 = Button(text="", command=lambda: set_button_press(button_02))
button_02.grid(column=0, row=2, ipadx=ipad_x, ipady=ipad_y)
button_10 = Button(text="", command=lambda: set_button_press(button_10))
button_10.grid(column=1, row=0, ipadx=ipad_x, ipady=ipad_y)
button_11 = Button(text="", command=lambda: set_button_press(button_11))
button_11.grid(column=1, row=1, ipadx=ipad_x, ipady=ipad_y)
button_12 = Button(text="", command=lambda: set_button_press(button_12))
button_12.grid(column=1, row=2, ipadx=ipad_x, ipady=ipad_y)
button_20 = Button(text="", command=lambda: set_button_press(button_20))
button_20.grid(column=2, row=0, ipadx=ipad_x, ipady=ipad_y)
button_21 = Button(text="", command=lambda: set_button_press(button_21))
button_21.grid(column=2, row=1, ipadx=ipad_x, ipady=ipad_y)
button_22 = Button(text="", command=lambda: set_button_press(button_22))
button_22.grid(column=2, row=2, ipadx=ipad_x, ipady=ipad_y)
Label(text='Player_X:', justify="center").grid(column=0, row=3, ipadx=ipad_x, ipady=10)
Label(text='Draw:', justify="center").grid(column=1, row=3, ipadx=ipad_x, ipady=10)
Label(text='Player_O:', justify="center").grid(column=2, row=3, ipadx=ipad_x, ipady=10)
label_player_X = Label(text='0', justify=RIGHT)
label_player_X.grid(column=0, row=4, ipadx=ipad_x, ipady=10)
label_draw = Label(text='0', justify=LEFT)
label_draw.grid(column=1, row=4, ipadx=ipad_x, ipady=10)
label_player_O = Label(text='0', justify=LEFT)
label_player_O.grid(column=2, row=4, ipadx=ipad_x, ipady=10)
button_new_game = Button(text="New Game", command=clear_fields)
button_new_game.grid(column=0, row=5, columnspan=3, ipadx=35, ipady=10)

root.mainloop()