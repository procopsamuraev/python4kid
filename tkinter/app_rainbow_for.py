from tkinter import *

def display_red():
    entry_color_code.set('#ff0000')
    label.config(text='red', foreground='red')
    entry_color.config(background='red')


def display_orange():
    entry_color_code.set('#ff7d00')
    label.config(text='orange', foreground='orange')
    entry_color.config(background='orange')


def display_yellow():
    entry_color_code.set('#ffff00')
    label.config(text='yellow', foreground='yellow')
    entry_color.config(background='yellow')


def display_green():
    entry_color_code.set('#00ff00')
    label.config(text='green', foreground='green')
    entry_color.config(background='green')


def display_lightblue():
    entry_color_code.set('#007dff')
    label.config(text='lightblue', foreground='lightblue')
    entry_color.config(background='lightblue')


def display_blue():
    entry_color_code.set('#0000ff')
    label.config(text='blue', foreground='blue')
    entry_color.config(background='blue')


def display_purple():
    entry_color_code.set('#7d00ff')
    label.config(text='purple', foreground='purple')
    entry_color.config(background='purple')

def display_color(color, color_code):
    entry_color_code.set(color_code)
    label.config(text=color, foreground=color)
    entry_color.config(background=color)


list_colors = [
    ['red', '#ff0000', display_red],
    ['orange', '#ff7d00', display_orange],
    ['yellow', '#ffff00', display_yellow],
    ['green', '#00ff00', display_green], 
    ['lightblue', '#007dff', display_lightblue],
    ['blue', '#0000ff', display_blue],
    ['purple', '#7d00ff', display_purple]
]

root = Tk()
root.title("Colors")
label = Label(text="Color name", font=15, fg="black" )
label.pack()
entry_color_code = StringVar()
entry_color = Entry(textvariable=entry_color_code, justify="center", font=20, fg="black")
entry_color.pack()
entry_color_code.set("Color code")

for color_combo in list_colors: 
    color, color_code, display_function = color_combo
    Button(root, text=color, font=15, bg=color_code, command = display_function).pack(fill=X)

root.mainloop()
