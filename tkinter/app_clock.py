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

tick()
root.mainloop()
