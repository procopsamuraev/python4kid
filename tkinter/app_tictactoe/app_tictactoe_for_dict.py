import tkinter
import pprint
from tkinter import *
from tkinter.ttk import *
from collections import defaultdict
turn = 'X'
count_turn = 0
size_field = 3
# dict_combination = defaultdict(list)
# flag = True

def set_button(button):
    global turn, flag
    if button.cget('text'):
        return
    button.config(text=turn)
    check_match()
    turn = 'O' if turn == 'X' else 'X'
    label_turn.config(text=f"Next turn player: {turn}")
    # flag = not flag


def disable_buttons():
    for row in button_array:
        for button in row: 
            button.config(state=DISABLED)


def clear_fields():
    for row in button_array:
        for button in row:
            button.config(text='')
            button.config(state=ON)
    button_new_game.config(text='New Game')


def fill_combinations()->dict:
    dict_combination = defaultdict(list)
    for index_row, row in enumerate(button_array):
        for index_column, button in enumerate(row):
            value_button = button.cget('text')
            if not value_button.isalnum():
                continue
            dict_combination[f"row_{index_row}"].append(value_button)
            dict_combination[f"col_{index_column}"].append(value_button)
            diagonal_back_true = index_column - index_row == 0
            if diagonal_back_true:
                dict_combination['diagonal_back'].append(value_button)
            diagonal_forward_true = index_column + index_row + 1 == size_field
            if diagonal_forward_true:
                dict_combination['diagonal_forward'].append(value_button)
    return dict_combination

def check_match():
    global count_turn
    count_turn += 1
    dict_combinations = fill_combinations()
    winner = ''
    for list_values in dict_combinations.values():
        if len(list_values) == size_field and len(set(list_values)) == 1:
            winner = turn
    
    winner = 'draw' if count_turn == size_field*size_field else winner
    if winner:
        button_new_game.config(text=f"{winner} won. Click here for a new game")
        count_wins(winner)
        disable_buttons()
        count_turn = 0


def count_wins(player):
    label = dict_count_wins.get(player)
    count = int(label.cget('text'))
    label.config(text=str(count+1))


root = Tk()
root.title('TicTacToe v2.0')
ipad_x = 40
ipad_y = 60


button_array = []
for row in range(size_field):
    row_buttons = []
    for column in range(size_field):
        button = Button()
        button.config(command=lambda button_=button: set_button(button_))
        button.grid(column=column, row=row, ipadx=ipad_x, ipady=ipad_y)
        row_buttons.append(button)
    button_array.append(row_buttons)

dict_count_wins = {}
Label(text='Player_X:', justify="center").grid(column=0, row=size_field)
Label(text='Draw:', justify="center").grid(column=0, row=size_field+1)
Label(text='Player_O:', justify="center").grid(column=0, row=size_field+2)
label = Label(text='0', justify=LEFT)
label.grid(column=1, row=size_field)
dict_count_wins.update({'X': label})
label = Label(text='0', justify=LEFT)
label.grid(column=1, row=size_field+1)
dict_count_wins.update({'draw': label})
label = Label(text='0', justify=LEFT)
label.grid(column=1, row=size_field+2)
dict_count_wins.update({'O': label})

button_new_game = Button(text="New Game", command=clear_fields)
button_new_game.grid(column=0, row=size_field+3, columnspan=size_field)
label_turn = Label(text=f'The player: {turn} start the game')
label_turn.grid(column=0,columnspan=size_field, row=size_field+4)

root.mainloop()
