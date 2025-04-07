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
def show_time(label, offset):
    time_local = time.strftime('%H:%M:%S:%Z')
    hour, minute, second, tz = time_local.split(":")
    hour = (int(hour) - int(tz) + 24 + offset) % 24
    label.config(text=f"{str(hour).zfill(2)}:{minute}:{second}")
    label.after(500, lambda: show_time(label, offset))


def draw_clock(tz_frame, tz_label, utc):
    tz_frame = LabelFrame(text=f"{tz_label}")
    tz_frame.pack(side='left')
    tz_label = Label(tz_frame, width=10, font=('Fira Code', 13), bg='green')
    tz_label.pack(fill='both', expand=1)
    show_time(tz_label, utc)

root = Tk()
list_tz  = [['moscow', 3],  ['london', 0], ['tokyo', 5]] # tz, offset
tz = 0
while tz < len(list_tz):
    time_zone = list_tz[tz]
    draw_clock(f'frame_{list_tz[tz][0]}', f'label_{list_tz[tz][0]}', list_tz[tz][1] )
    draw_clock(f'frame_{list_tz[tz][0]}', f'label_{list_tz[tz][0]}', list_tz[tz][1] )
    tz +=1

root.mainloop()

