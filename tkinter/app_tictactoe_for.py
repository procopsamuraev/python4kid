import tkinter
import pprint
from tkinter import *
from tkinter.ttk import *
from collections import defaultdict
turn = 'X'
size_field = 3
dict_combination = defaultdict(list)
"""
make a 3 function - seperate for diag
2. make a collection of row, column, and diag

"""


def set_button(y, x):
    global turn
    message = f" {turn}-won \nPress here for\na new game"
    if not str(button_array[y][x].cget('text')).isalnum() and str(button_new_game.cget('text')) == "New Game":
        button_array[y][x].config(text=turn)
        winner_row_diag = check_match_row()
        winner_column = check_match_column()
        if winner_row_diag or winner_column: 
            button_new_game.config(text=message)
            count_wins(turn)
        turn = 'O' if turn == 'X' else 'X'
        label_turn.config(text=f"Next turn player: {turn}")


def clear_fields():
    for line in button_array:
        for button in line:
            button.config(text='')
    button_new_game.config(text='New Game')


def check_match_row():
    list_combinations = []
    winner = None
    flag_diag_back = None
    flag_diag_forward = None
    for index_row, row in enumerate(button_array):
        current_value = row[0].cget('text')
        flag_row = None
        list_row=[]
        for index_column, button in enumerate(row):
            value_button:str = button.cget('text')
            if value_button.isalnum():
                row_name= f"row_{row}"
                dict_combination[row_name].append(button.cget('text'))
            list_row.extend(button.cget('text')) if button.cget('text') else list_row
            # row check
            if current_value.isalnum() and button.cget('text') == current_value and flag_row != 0:
                flag_row = button.cget('text')
            else:
                flag_row = 0
            # back diagonal check
            diagonal_back_true = index_column - index_row ==0
            if diagonal_back_true and flag_diag_back !=0:
                if button.cget('text') == button_array[0][0].cget('text'):
                    flag_diag_back = button.cget('text')
                else:
                    flag_diag_back = 0
            # forward diagonal check  
            if index_column + index_row + 1 == size_field:
                if button.cget('text') == button_array[0][-1].cget('text') and flag_diag_forward !=0:
                    flag_diag_forward = button.cget('text')
                else:
                    flag_diag_forward = 0
        list_combinations.append(list_row)
        if flag_row:
            break

    if flag_row:
        winner = flag_row
    elif flag_diag_back: 
        winner = flag_diag_back
    elif flag_diag_forward: 
        winner = flag_diag_forward
    
    pprint.pprint(dict_combination)
    return winner


def check_match_column():
    winner = None
    for column in range(len(button_array)):
        flag_column = None
        current_value = button_array[0][column].cget('text')
        for row in button_array:
            if row[column].cget('text') == current_value and flag_column != 0:
                flag_column = current_value
            else:
                flag_column = 0
                continue
        if flag_column:
            winner = flag_column
    return winner


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
root.title('TicTacToe v2.0')
ipad_x = 40
ipad_y = 60
label_turn = Label(text=f'The player: {turn} start the game')
label_turn.grid(column=0,columnspan=3, row=6)


button_array = []

for row in range(size_field):
    row_buttons = []
    for column in range(size_field):
        button = Button(command=lambda y=row, x=column: set_button(y, x))
        button.grid(column=column, row=row, ipadx=ipad_x, ipady=ipad_y)
        row_buttons.append(button)
    button_array.append(row_buttons)

Label(text='Player_X:', justify="center").grid(column=0, row=size_field, ipadx=ipad_x, ipady=10)
Label(text='Draw:', justify="center").grid(column=1, row=size_field, ipadx=ipad_x, ipady=10)
Label(text='Player_O:', justify="center").grid(column=2, row=size_field, ipadx=ipad_x, ipady=10)
label_player_X = Label(text='0', justify=RIGHT)
label_player_X.grid(column=0, row=size_field+1, ipadx=ipad_x, ipady=10)
label_draw = Label(text='0', justify=LEFT)
label_draw.grid(column=1, row=size_field+1, ipadx=ipad_x, ipady=10)
label_player_O = Label(text='0', justify=LEFT)
label_player_O.grid(column=2, row=size_field+1, ipadx=ipad_x, ipady=10)
button_new_game = Button(text="New Game", command=clear_fields)
button_new_game.grid(column=0, row=size_field+2, columnspan=3, ipadx=35, ipady=10)

root.mainloop()
