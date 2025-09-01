from tkinter import *


def display_color(_desc, color):
    label.config(text=_desc)
    entry_color_code.set(color)
    entry_color.config(background=color)



list_colors = [
    ['red', '#ff0000'],
    ['orange', '#ff7d00'],
    ['yellow', '#ffff00'],
    ['green', '#00ff00'], 
    ['lightblue', '#007dff'],
    ['blue', '#0000ff'],
    ['purple', '#7d00ff']
]

root = Tk()
root.title("Colors")
label = Label(text="Color name", font=15, fg="black" )
label.pack()
entry_color_code = StringVar()
entry_color = Entry(textvariable=entry_color_code, justify="center", font=20, fg="black")
entry_color.pack()
entry_color_code.set("Color code")

for index, color_combo in enumerate(list_colors): 
    Button(root, text=index, font=15, bg=color_combo[1], command = lambda _params = color_combo :display_color(*_params)).pack(fill=X)

root.mainloop()
