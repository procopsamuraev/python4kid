# ex.2
from tkinter import *
import time


def adjust_hour(hour):
    hour = hour % 24 if hour >= 24 else hour
    return hour


def show_time():
    # calculate value of hour in UTC
    time_local = time.strftime('%H:%M:%S:%Z')
    # time_local = "05:15:01:+8" # testing
    hour_utc = int(time_local.split(":")[0]) - int(time_local.split(":")[-1])
    hour_utc = 24 + hour_utc if hour_utc < 0 else hour_utc
    minute = time_local.split(":")[1]
    second = time_local.split(":")[2]

    utc_offset = 3
    time_moscow = f"{adjust_hour(hour_utc + utc_offset)}:{minute}:{second}"
    label_moscow.config(text=time_moscow)
    utc_offset = 1
    time_london = f"{adjust_hour(hour_utc + utc_offset)}:{minute}:{second}"
    label_london.config(text=time_london)
    utc_offset = 9
    time_tokyo = f"{adjust_hour(hour_utc + utc_offset)}:{minute}:{second}"
    label_tokyo.config(text=time_tokyo)

    label_utc.after(500, show_time)

root = Tk()
# create but do not show a label
label_utc = Label(root)

frame_moscow = LabelFrame(text="Moscow time")
frame_moscow.pack(side="left")
label_moscow = Label(frame_moscow, width=10, font=('Fira Code', 13), bg='green')
label_moscow.pack(fill="both", expand=1, side="left")

frame_london = LabelFrame(text="London time")
frame_london.pack(side="right")
label_london = Label(frame_london, width=10, font=('Fira Code', 13), bg='green')
label_london.pack(fill="both", expand=1, side="right")

frame_tokyo = LabelFrame(text="Tokyo time")
frame_tokyo.pack(side="right")

label_tokyo = Label(frame_tokyo, width=10, font=('Fira Code', 13), bg='green', textvariable=)
label_tokyo.pack(fill="both", expand=1, side="right")


show_time()
root.mainloop()
