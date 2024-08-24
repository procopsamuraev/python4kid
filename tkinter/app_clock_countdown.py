# ex.1
from tkinter import *
import time
'''
def show_time():
    show_moscow()
    show_current()
    show_countdown()

def show_moscow():
    time_moscow = f"Moscow time: {time.strftime('%H:%M:%S')}"
    label_moscow.config(text=time_moscow)


def show_current():
    time_current = f"Hour: {time.strftime('%H')} Minute: {time.strftime('%M')} Second: {time.strftime('%S')}"
    label_current.config(text=time_current)
    label_current.after(200, show_time)


def show_countdown():
    hours_left = 24 - int(time.strftime('%H'))
    minutes_left = 60 - int(time.strftime('%M'))
    seconds_left = 60 - int(time.strftime('%S'))
    time_countdown = f"Left: { hours_left } hours { minutes_left} Minutes { seconds_left} Seconds"
    label_countdown.config(text=time_countdown)


root = Tk()
frame_moscow = LabelFrame(text="Moscow time")
frame_moscow.pack(side="top")
label_moscow = Label(frame_moscow, width=50, font=('Fira Code', 12))
label_moscow.pack(fill="both", expand=1, side="left")

frame_current = LabelFrame(text="Current time")
frame_current.pack(side="top")
label_current = Label(frame_current, width=50, font=('Fira Code', 12))
label_current.pack(fill="both", expand=1, side="left")

frame_countdown = LabelFrame(text="Time until tomorrow")
frame_countdown.pack(side="top")
label_countdown = Label(frame_countdown, width=50, font=('Fira Code', 11))
label_countdown.pack(fill="both", expand=1, side="left")
'''
def show_time():
    time_moscow = f"Moscow time: {time.strftime('%H:%M:%S')}"
    label_moscow.config(text=time_moscow)
    time_current = f"Hour: {time.strftime('%H')} Minute: {time.strftime('%M')} Second: {time.strftime('%S')}"
    label_current.config(text=time_current)
    label_current.after(200, show_time)
    hours_left = 24 - int(time.strftime('%H'))
    minutes_left = 60 - int(time.strftime('%M'))
    seconds_left = 60 - int(time.strftime('%S'))
    time_countdown = f"Left: { hours_left } hours { minutes_left} Minutes { seconds_left} Seconds"
    label_countdown.config(text=time_countdown)


root = Tk()
frame_moscow = LabelFrame(text="Moscow time")
frame_moscow.pack(side="top")
label_moscow = Label(frame_moscow, width=50, font=('Fira Code', 12))
label_moscow.pack(fill="both", expand=1, side="left")

frame_current = LabelFrame(text="Current time")
frame_current.pack(side="top")
label_current = Label(frame_current, width=50, font=('Fira Code', 12), justify="left")
label_current.pack(fill="both", expand=1, side="left")

frame_countdown = LabelFrame(text="Time until tomorrow")
frame_countdown.pack(side="top")
label_countdown = Label(frame_countdown, width=50, font=('Fira Code', 11))
label_countdown.pack(fill="both", expand=1, side="left")


show_time()

show_time()
root.mainloop()
