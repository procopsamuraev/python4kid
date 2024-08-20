# ex.1
from tkinter import *
import time


def tick():
    time2 =  time.strftime('%H:%M:%S')
    clock.config(text=time2)
    clock.after(200, tick)


root = Tk()
clock = Label(root, font=('times', 20, 'bold'), bg='green')
clock.pack(fill="both",expand=1)

frame_moscow = LabelFrame(text="Moscow time")
frame_moscow.pack(side="top")
clock = Label(frame_moscow, width=20, font=('times', 20, 'bold'))
clock.pack(fill="both", expand=1, side="left")

frame_current= LabelFrame(text="Current time")
frame_current.pack(side="top")

tick()
root.mainloop()
