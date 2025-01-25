from tkinter import *

def display_color(color, color_code):
    entry_color_code.set(color_code)
    label.config(text=color, foreground=color_code)
    entry_color.config(foreground="black", background=color)


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

root.mainloop()
