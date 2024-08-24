# ex.2
from tkinter import *
import time


def show_time():
    time_local = time.strftime('%H:%M:%S:%Z')
    # calculate value of hour in UTC
    hour_utc = int(time_local.split(":")[0]) - int(time_local.split(":")[-1])
    hour_utc = 24 + hour_utc if hour_utc < 0 else hour_utc
    minute = time_local.split(":")[1]
    second = time_local.split(":")[2]
    time_moscow = f"{hour_utc + 3}:{minute}:{second}"
    label_moscow.config(text=time_moscow)
    time_london = f"{hour_utc + 1}:{minute}:{second}"
    label_london.config(text=time_london)
    time_tokyo = f"{hour_utc + 9}:{minute}:{second}"
    label_tokyo.config(text=time_tokyo)
    label_tokyo.after(500, show_time)


root = Tk()
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
label_tokyo = Label(frame_tokyo, width=10, font=('Fira Code', 13), bg='green')
label_tokyo.pack(fill="both", expand=1, side="right")


show_time()
root.mainloop()
