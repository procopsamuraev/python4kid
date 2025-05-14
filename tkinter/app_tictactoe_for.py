import tkinter
from tkinter import *
from tkinter.ttk import *
turn = 'X'
size_field = 3

"""
fixme - dynamic version

"""


def set_button(y, x):
    global turn
    if not str(button_array[y][x].cget('text')).isalnum() and str(button_new_game.cget('text')) == "New Game":
        button_array[y][x].config(text=turn)
        check_match_row()
        check_match_column()
        # print(turn)
        turn = 'O' if turn == 'X' else 'X'
        label_turn.config(text=f"Next turn player: {turn}")


def clear_fields():
    for line in button_array:
        for button in line:
            button.config(text='')
    button_new_game.config(text='New Game')


flag_diag_back = 0
flag_diag_forward = 0


def check_match_row():
    draw = 0
    message = f" {turn}-won \nPress here for\na new game"
    for index_row, row in enumerate(button_array):
        current_value = row[0].cget('text')
        flag = 0
        for index_column, button in enumerate(row):
            if button.cget('text') != current_value:
                flag = 0
                # continue
            else:
                flag = button.cget('text')

            if index_column - index_row == 0:
                print('diag')
                if button.cget('text') != button_array[0][0].cget('text'):
                    flag_diag = 0
                else:
                    flag_diag = button.cget('text')
            
            if index_column + index_row + 1 == size_field:
                print('diagfwd')
                if button.cget('text') != button_array[0][-1].cget('text'):
                    flag_diag_forward = 0
                else:
                    flag_diag_forward = button.cget('text')

        if flag:
            print('row', flag)
            break
        if flag_diag or flag_diag_forward:
            print('diag', flag_diag)

    if flag or flag_diag:
        button_new_game.config(text=message)
        count_wins(turn)
    elif draw == 3:
        message = f" Draw\nPress here for\na new game"
        button_new_game.config(text=message)
        count_wins('draw')


def check_match_column():
    draw = 0
    message = f" {turn}-won \nPress here for\na new game"
    for column in range(len(button_array)):
        flag = 0
        current_value = button_array[0][column].cget('text')
        for index_column, row in enumerate(button_array):
            if row[column].cget('text') != current_value:
                flag = 0
                continue
            else:
                flag = row[column].cget('text')
        if flag:
            print('column', flag)
            break

    if flag:
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
