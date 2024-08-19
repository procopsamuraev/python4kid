# Ex 1,2
"""
from tkinter import *

root = Tk()

frame_header = Frame()
frame_header.pack(fill="x")
button_file = Button(frame_header, width=3, height=1, text="File")
button_file.pack(side="left", fill="x" ,expand=1)
button_view = Button(frame_header, width=3, height=1, text="View")
button_view.pack(side="left", fill="x", expand=1)
button_about = Button(frame_header, width=3, height=1, text="About")
button_about.pack(side="left", fill="x", expand=1)

frame_top = Frame(root)
frame_top.pack()
label_1 = Label(frame_top, width=9, height=4, bg="yellow", text="1")
label_1.pack(side="left")
label_2 = Label(frame_top, width=9, height=4, bg="orange", text="2")
label_2.pack(side="right")

frame_bottom = Frame(root)
frame_bottom.pack()
label_3 = Label(frame_bottom, width=9, height=4, bg="lightgreen", text="3")
label_3.pack(side="left")
label_4 = Label(frame_bottom, width=9, height=4, bg="lightblue", text="4")
label_4.pack(side="right")

frame_footer = Frame()
frame_footer.pack()
label_5 = Label(frame_footer, width=9, height=4, bg="red", text="5")
label_5.pack(side="left")
label_6 = Label(frame_footer, width=9, height=4, bg="brown", text="6")
label_6.pack(side="right")

if __name__ == '__main__':
    root.mainloop()
"""

# Ex3
'''
from tkinter import *
root = Tk()
frame_top = Frame()
frame_top.pack(side="top", fill="x")
button_top_left = Button(frame_top, width=9, text="Top Left")
button_top_left.pack(side="left")
button_top_right = Button(frame_top, width=9, text="Top Right")
button_top_right.pack(side="right")

frame_bottom = Frame()
frame_bottom.pack(fill="x", side="bottom")
button_bottom_left = Button(frame_bottom, width=9, text="Bottom Left")
button_bottom_left.pack(side="left")
button_bottom_right  = Button(frame_bottom, width=9, text="Bottom Right")
button_bottom_right.pack(side="right")
root.mainloop()
'''