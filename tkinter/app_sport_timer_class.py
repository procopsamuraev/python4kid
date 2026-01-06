# from datetime import datetime
import time
import datetime
from tkinter import *
from tkinter.ttk import *

quantity_timers = 3
list_timers = []


# timer states:
# 0 - zero
# 1- running
# 2 - stopped

class Timer:
    def __init__(self, master: Tk = None, number: int = 0) -> None:
        self.time_start = 0
        self.time_stop = 0
        self.state_timer = 0
        self.color_run = 'light green'
        self.color_stop = 'pink'
        self.color_zero = 'light grey'
        frame = LabelFrame(text=f"Timer {number}".title())
        frame.pack(side='left')
        self.label = Label(frame,  font=("Arial", 20), background=self.color_zero, text='0:00:00')
        self.label.pack(fill='both', expand=1)
        master.bind(str(number), lambda event: self.control_timer())

    def update_label_timer(self)->None:
        time_diff = datetime.timedelta(seconds=time.time() - self.time_start)
        self.label.config(text=str(time_diff).split('.')[0])
        if self.state_timer == 1:
            self.label.after(500, lambda: self.update_label_timer())

    def control_timer(self)->None:
        if self.state_timer == 1:
            self.label.config(background=self.color_stop)
            self.state_timer = 2
        elif self.state_timer == 2:
            self.label.config(background=self.color_zero, text='0:00:00')
            self.state_timer = 0
        else:
            self.label.config(background=self.color_run)
            self.state_timer = 1
            self.time_start = time.time()
            self.update_label_timer()


def control_timer_all()-> None:
   state_min = 2
   for timer_ in list_timers:
       state_timer = timer_.state_timer
       state_min = state_timer if state_timer < state_min else state_min
   for timer_ in list_timers:
       state_timer = timer_.state_timer
       if state_timer == state_min:
           timer_.control_timer()


root = Tk()
root.title("Sport Timers")

for number_timer in range(quantity_timers):
    timer = Timer(master=root, number=number_timer+1)
    list_timers.append(timer)

root.bind("<space>", lambda event: control_timer_all())
root.mainloop()

