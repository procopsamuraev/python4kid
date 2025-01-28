from tkinter import *

# def display_color(color, color_code):
#     entry_color_code.set(color_code)
#     label.config(text=color, foreground=color_code)
#     entry_color.config(foreground="black", background=color)

# v4 static function
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
# v4


root = Tk()
root.title("Colors")
label = Label(text="Color name", font=15, fg="black" )
label.pack()
entry_color_code = StringVar()
entry_color = Entry(textvariable=entry_color_code, justify="center", font=20, fg="black")
entry_color.pack()
entry_color_code.set("Color code")

# v1
# list_colors  = ['red', 'orange', 'yellow', 'green', 'lightblue', 'blue', 'purple']
# list_color_codes  = ['#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#007dff', '#0000ff', '#7d00ff']
# 
# i = 0
# while i < 7:
#     color = list_colors[i]
#     color_code = list_color_codes[i]
#     Button(root, text=color, font=15, bg=color_code, command=lambda color=color, color_code=color_code: display_color(color, color_code)).pack(fill=X)
#     i = i + 1

# v2
# list_colors = ['red #ff0000', 'orange #ff7d00', 'yellow #ffff00', 'green #00ff00', 'lightblue #007dff', 'blue #0000ff', 'purple #7d00ff']
# 
# i = 0
# while i < 7:
#     color, color_code = list_colors[i].split()
#     Button(root, text=color, font=15, bg=color_code, command=lambda color=color, color_code=color_code: display_color(color, color_code)).pack(fill=X)
#     i = i + 1

# v3
# list_colors = ['red #ff0000', 'orange #ff7d00', 'yellow #ffff00', 'green #00ff00', 'lightblue #007dff', 'blue #0000ff', 'purple #7d00ff']
# for colors in list_colors:
#     color, color_code = colors.split()
#     Button(root, text=color, font=15, bg=color_code, command=lambda color=color, color_code=color_code: display_color(color, color_code)).pack(fill=X)


# v4
list_colors = ['red #ff0000', 'orange #ff7d00', 'yellow #ffff00', 'green #00ff00', 'lightblue #007dff', 'blue #0000ff', 'purple #7d00ff']
list_functions = [display_red, display_orange, display_yellow, display_green, display_lightblue, display_blue, display_purple]
i = 0
while i < len(list_colors):
    color, color_code = list_colors[i].split()
    color_function = list_functions[i]
    Button(root, text=color, font=15, bg=color_code, command=color_function).pack(fill=X)
    i = i + 1

root.mainloop()
