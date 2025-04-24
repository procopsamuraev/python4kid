# ex.2
# from tkinter import *
# import time
# 
# 
# def show_time(label, offset):
#     time_local = time.strftime('%H:%M:%S:%Z')
#     hour, minute, second, tz = time_local.split(":")
#     hour = (int(hour) - int(tz) + 24 + offset) % 24
#     label.config(text=f"{str(hour).zfill(2)}:{minute}:{second}")
#     label.after(500, lambda: show_time(label, offset))
# 
# root = Tk()
# frame_moscow = LabelFrame(text="Moscow time")
# frame_moscow.pack(side="left")
# label_moscow = Label(frame_moscow, width=10, font=('Fira Code', 13), bg='green')
# label_moscow.pack(fill="both", expand=1, side="left")
# show_time(label_moscow, 3)
# 
# frame_london = LabelFrame(text="London time")
# frame_london.pack(side="right")
# label_london = Label(frame_london, width=10, font=('Fira Code', 13), bg='green')
# label_london.pack(fill="both", expand=1, side="right")
# show_time(label_london, 0)
# 
# frame_tokyo = LabelFrame(text="Tokyo time")
# frame_tokyo.pack(side="right")
# label_tokyo = Label(frame_tokyo, width=10, font=('Fira Code', 13), bg='green')
# label_tokyo.pack(fill="both", expand=1, side="right")
# show_time(label_tokyo, 5)
# 
# root.mainloop()


# while
from tkinter import *
import time 
list_clocks  = [['time moscow', 3],  ['time london', 0], ['time tokyo', 5]] # clocks, offset


def show_time(label, offset):
    hour, minute, second, tz = time.strftime('%H:%M:%S:%Z').split(':')
    hour = (int(hour) - int(tz) + 24 + offset) % 24
    label.config(text=f"{str(hour).zfill(2)}:{minute}:{second}")
    label.after(500, lambda: show_time(label, offset))


def draw_clock(name_utc):
    name_frame, utc = name_utc
    frame = LabelFrame(text=f"{name_frame}".title())
    frame.pack(side='left')
    label = Label(frame, font=('Fira Code', 13), bg='green')
    label.pack(fill='both', expand=1)
    show_time(label, utc)


root = Tk()

# while
# index = 0
# while index < len(list_clocks):
#     draw_clock(list_clocks[index])
#     index += 1

# for loop
for index in range(len(list_clocks)):
    draw_clock(list_clocks[index])


root.mainloop()

