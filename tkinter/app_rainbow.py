from tkinter import *

//
// while only 1 level list can. 
//
def change_color(color, color_code):
    print(f'{color}:{color_code}')
    text_code.set(color_code)
    label.config(text=color, foreground=color)
    entry.config(foreground="black", background=color)


root = Tk()
root.title("Colors")
label = Label(text="Color name", font=20, fg="black" )
label.pack()
text_code = StringVar()
entry = Entry(textvariable=text_code, justify="center", font=20, fg="black")
entry.pack()
text_code.set("Color code")

# creating buttons
color = "red"
color_code = "#ff0000"
# button_red = Button(root, text="1", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
button = Button(root, text="1", font=20, bg="#ff0000", command=lambda: change_color("red", "#ff0000"))
button.pack(fill=X)
color = "orange"
color_code = "#ff7d00"
button = Button(root, text="2", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
button.pack(fill=X)
color = "yellow"
color_code = "#ffff00"
button = Button(root, text="3", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
button.pack(fill=X)
color = "green"
color_code = "#00ff00"
button = Button(root, text="4", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
button.pack(fill=X)
color = "lightblue"
color_code = "#007dff"
button = Button(root, text="5", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
button.pack(fill=X)
color = "blue"
color_code = "#0000ff"
button = Button(root, text="6", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
button.pack(fill=X)
color = "purple"
color_code = "#7d00ff"
button = Button(root, text="7", font=20, bg=color_code, command=lambda color_temp=color, color_code_temp=color_code: change_color(color_temp, color_code_temp))
button.pack(fill=X)

root.mainloop()
