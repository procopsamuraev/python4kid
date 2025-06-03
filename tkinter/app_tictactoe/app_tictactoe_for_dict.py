import tkinter
import pprint
from tkinter import *
from tkinter.ttk import *
from collections import defaultdict
turn = 'X'
size_field = 3
dict_combination = defaultdict(list)
"""
fix me disable buttons once winner
"""


def set_button(y, x):
    global turn
    message = f" {turn}-won .Press here for a new game"
    button_array[y][x].config(text=turn)
    fill_dictionary()
    winner = check_match()
    if winner:
        button_new_game.config(text=message)
        count_wins(winner)
        disable_buttons()
    turn = 'O' if turn == 'X' else 'X'
    label_turn.config(text=f"Next turn player: {turn}")


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


def fill_dictionary():
    dict_combination.clear()
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


def check_match()->str:
    winner = None
    counter_turns = 0
    for list_values in dict_combination.values():
        if len(list_values) != size_field: 
            continue
        if len(set(list_values)) == 1:
            winner = list_values[0]
            break
        elif len(list_values)==size_field:
            counter_turns += size_field
        if counter_turns == size_field * ( 2 * size_field + 2):
            winner = 'draw'
    return winner


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
        button = Button(command=lambda y=row, x=column: set_button(y, x))
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
