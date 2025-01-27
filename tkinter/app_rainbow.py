from tkinter import *

# def change_color(color, color_code):
#     print(f'{color}:{color_code}')
#     text_code.set(color_code)
#     label.config(text=color, foreground=color)
#     entry.config(foreground="black", background=color)
# 
# 
# root = Tk()
# root.title("Colors")
# label = Label(text="Color name", font=20, fg="black" )
# label.pack()
# text_code = StringVar()
# entry = Entry(textvariable=text_code, justify="center", font=20, fg="black")
# entry.pack()
# text_code.set("Color code")
# 
# # creating buttons
# color = "red"
# color_code = "#ff0000"
# # button_red = Button(root, text="1", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
# button = Button(root, text="1", font=20, bg="#ff0000", command=lambda: change_color("red", "#ff0000"))
# button.pack(fill=X)
# color = "orange"
# color_code = "#ff7d00"
# button = Button(root, text="2", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
# button.pack(fill=X)
# color = "yellow"
# color_code = "#ffff00"
# button = Button(root, text="3", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
# button.pack(fill=X)
# color = "green"
# color_code = "#00ff00"
# button = Button(root, text="4", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
# button.pack(fill=X)
# color = "lightblue"
# color_code = "#007dff"
# button = Button(root, text="5", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
# button.pack(fill=X)
# color = "blue"
# color_code = "#0000ff"
# button = Button(root, text="6", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
# button.pack(fill=X)
# color = "purple"
# color_code = "#7d00ff"
# button = Button(root, text="7", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
# button.pack(fill=X)
# 
# root.mainloop()

# static version
def display_red():
    text_code.set('#ff0000')
    label.config(text='red', foreground='red')
    entry.config(background='red')


def display_orange():
    text_code.set('#ff7d00')
    label.config(text='orange', foreground='orange')
    entry.config(background='orange')


def display_yellow():
    text_code.set('#ffff00')
    label.config(text='yellow', foreground='yellow')
    entry.config(background='yellow')


def display_green():
    text_code.set('#00ff00')
    label.config(text='green', foreground='green')
    entry.config(background='green')


def display_lightblue():
    text_code.set('#007dff')
    label.config(text='lightblue', foreground='lightblue')
    entry.config(background='lightblue')


def display_blue():
    text_code.set('#0000ff')
    label.config(text='blue', foreground='blue')
    entry.config(background='blue')


def display_purple():
    text_code.set('#7d00ff')
    label.config(text='purple', foreground='purple')
    entry.config(background='purple')


root = Tk()
root.title("Colors")
label = Label(text="Color name", font=20, fg="black" )
label.pack()
text_code = StringVar()
entry = Entry(textvariable=text_code, justify="center", font=20, fg="black")
entry.pack()
text_code.set("Color code")

Button(root, text="1", font=20, bg="#ff0000", command=display_red).pack(fill=X)
Button(root, text="2", font=20, bg="#ff7d00", command=display_orange).pack(fill=X)
Button(root, text="3", font=20, bg="#ffff00", command=display_yellow).pack(fill=X)
Button(root, text="4", font=20, bg="#00ff00", command=display_green).pack(fill=X)
Button(root, text="5", font=20, bg="#007dff", command=display_lightblue).pack(fill=X)
Button(root, text="6", font=20, bg="#0000ff", command=display_blue).pack(fill=X)
Button(root, text="7", font=20, bg="#7d00ff", command=display_purple).pack(fill=X)


root.mainloop()
