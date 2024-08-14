# ex 1
# from tkinter import *
#
# root = Tk()
# root.geometry("400x400")
# button_top_left = Button(text="top left")
# button_top_left.place(x=0, y=0)
# button_bottom_left = Button(text="bottom left")
# button_bottom_left.place(x=0, y=370)
# button_top_right = Button(text="top right")
# button_top_right.place(x=315, y=0)
# button_bottom_right = Button(text="bottom right")
# button_bottom_right.place(x=300, y=370)
#
# button_center = Button(text="Center")
# button_center.place(x=180, y=185)
#
# root.mainloop()


# # ex 2
# from tkinter import *
#
# root = Tk()
# root.geometry("600x300")
# button_top = Button(text="top")
# button_top.place(relx=.47, rely=0)
# button_bottom = Button(text="bottom")
# button_bottom.place(relx=.45, rely=.90)
# button_right = Button(text="right")
# button_right.place(relx=.9, rely=.45)
# button_left = Button(text="left")
# button_left.place(relx=0, rely=0.45)
# button_center = Button(text="Center")
# button_center.place(relx=.45, rely=.45)
#
# root.mainloop()


# ex 3
from tkinter import *


# def move_button():
#     global x, y
#     if x == 0.5 and y == 0.0:
#         button.place(relx="1.0", rely="0.5", anchor="e")
#     elif x == 1.0 and y == 0.5:
#         x = x - 0.5
#         y = y + 0.5
#         a = "s"
#     elif x == 0.5 and y == 1.0:
#         x = x - 0.5
#         y = y - 0.5
#         a = "w"
#     elif x == 0.0 and y == 0.5:
#         x = x + 0.5
#         y = y - 0.5
#         a = "n"
#     print(button["text"])
#     button.place(relx=x, rely=y, anchor=a)

def move_button():
    if button["text"] == "top":
        button.config(text="right")
        button.place(relx=1.0, rely=0.5, anchor="e")
    elif button["text"] == "right":
        button.config(text="bottom")
        button.place(relx=0.5, rely=1, anchor="s")
    elif button["text"] == "bottom":
        button.config(text="left")
        button.place(relx=0, rely=0.5, anchor="w")
    elif button["text"] == "left":
        button.config(text="top")
        button.place(relx=.5, rely=0, anchor="n")


root = Tk()
root.geometry("200x100")
x = 0.5
y = 0.0
button = Button(text="top", command=move_button)
button.place(relx=x, rely=y, anchor="n") # top
# button.place(relx=1, rely=0.5, anchor="e") # right
# button.place(relx=0.5, rely=1, anchor="s") # bottom
# button.place(relx=0, rely=0.5, anchor="w") # left

root.mainloop()
