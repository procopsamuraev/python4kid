import tkinter
from tkinter import *
from tkinter.ttk import *
turn = 'X'

"""
"""


def set_button(i, j):
    global turn
    if not str(button_array[i][j].cget('text')).isalnum() and str(button_new_game.cget('text')) == "New Game":
        button_array[i][j].config(text=turn)
        check_winner()
        turn = 'O'if turn == 'X' else 'X'
        label_turn.config(text=f"Next turn player: {turn}")


def clear_fields():
    for line in button_array:
        for button in line:
            button.config(text='')
    button_new_game.config(text='New Game')


def check_winner():
    winner = 0
    draw = 0
    message=f" {turn}-won \nPress here for\na new game"
    winner += 1 if button_array[0][0].cget('text') == button_array[1][1].cget('text') == button_array[2][2].cget('text') != '' else winner
    winner += 1 if button_array[2][0].cget('text') == button_array[1][1].cget('text') == button_array[0][2].cget('text') != '' else winner
    for i in  range(3):
        winner += 1 if button_array[i][0].cget('text') == button_array[i][1].cget('text') == button_array[i][2].cget('text') != '' else winner 
        winner += 1 if button_array[0][i].cget('text') == button_array[1][i].cget('text') == button_array[2][i].cget('text') != '' else winner 
        draw  += 1 if button_array[i][0].cget('text') and button_array[i][1].cget('text') and button_array[i][2].cget('text') != '' else draw
    if winner: 
        button_new_game.config(text=message)
        count_wins(turn)
    elif draw == 3:
        message=f" Draw\nPress here for\na new game"
        button_new_game.config(text=message)
        count_wins('draw')


def count_wins(player):
    if player == 'X':
        count = int(label_player_X.cget('text'))
        label_player_X.config(text=str(count+1))
    elif player == 'O':
        count = int(label_player_O.cget('text'))
        label_player_O.config(text=str(count+1))
    elif player == 'draw':
        count = int(label_draw.cget('text'))
        label_draw.config(text=str(count+1))


root = Tk()
root.title('TicTacToe v1.12')
ipad_x = 40
ipad_y = 60
label_turn=Label(text=f'The player: {turn} start the game')
label_turn.grid(column=0,columnspan=3, row=6)


button_array = [
    [0, 0, 0], 
    [0, 0, 0],
    [0, 0, 0]
    ]

for i in range(3):
    for j in range(3):
        button_array[i][j] = Button(command = lambda y = j, x = i : set_button(x, y))
        button_array[i][j].grid(column = i, row = j, ipadx=ipad_x, ipady=ipad_y)
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