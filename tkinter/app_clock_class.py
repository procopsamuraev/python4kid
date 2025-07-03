from tkinter import *
import time 

LIST_CLOCKS = [['moscow', 3],  ['london', 0], ['tokyo', 5]] # city, utc zone

class ClockWorld: 
    def __init__(self, city: str, utc_zone: float) ->  None:
        self.city = city
        self.utc_zone = utc_zone
        self.frame = LabelFrame(text=f"{self.city.title()} Time")
        self.frame.pack(side='left')
        self.label = Label(self.frame, bg='green')
        self.label.pack(fill='both', expand=1)
        self.update_time()
    
    def update_time(self) -> None:
        hour, minute, second, tz = time.strftime('%H:%M:%S:%Z').split(':')
        hour = (int(hour) - int(tz) + 24 + self.utc_zone) % 24
        self.label.config(text=f"{str(hour).zfill(2)}:{minute}:{second}")
        self.label.after(500, self.update_time)


root = Tk()
for clock in LIST_CLOCKS:
    ClockWorld(*clock)

root.mainloop()

