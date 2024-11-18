import tkinter
from tkinter import *
from tkinter.ttk import *

turn = 1


def set_button_press(button):
    global turn
    buttons_combinations = [button_00, button_10, button_11, button_01]
    # field_empty_true = not str(button.cget('text')).isalnum()
    if not str(button.cget('text')).isalnum():
        button.config(text='X') if turn % 2 != 0 else button.config(text='O')
        turn = turn + 1

        buttons_combinations.remove(button)
        for buttons in buttons_combinations:
            check_winner(button, buttons)


def clear_fields():
    for button in button_00, button_10, button_11, button_01:
        button.config(text='')


def check_winner(button1, button2):
    if button1.cget('text') == button2.cget('text'):
        print(f"{button1.cget('text')}-Won!")



root = Tk()
root.title('TicTac v0.9')
button_00 = Button(text="", command=lambda: set_button_press(button_00))
button_00.grid(column=0, row=0, ipadx=80, ipady=100)
button_01 = Button(text="", command=lambda: set_button_press(button_01))
button_01.grid(column=0, row=1, ipadx=80, ipady=100)
button_10 = Button(text="", command=lambda: set_button_press(button_10))
button_10.grid(column=1, row=0, ipadx=80, ipady=100)
button_11 = Button(text="", command=lambda: set_button_press(button_11))
button_11.grid(column=1, row=1, ipadx=80, ipady=100)
button_new_game = Button(text="New Game", command= clear_fields)
button_new_game.grid(columnspan=2, row=2,ipadx=200, ipady=10)

root.mainloop()