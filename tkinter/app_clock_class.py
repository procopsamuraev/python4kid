from tkinter import *
import time 
"""
show diffirent city clocks
Limitiations =  accepts only int as  utc time, no  fractional.
add 
"""

LIST_CLOCKS:list[list[str|int]] = [['moscow', 3],  ['london', 0], ['tokyo', 5]] # city, utc zone

class ClockZone:
    background_clock='lightgreen'
    def __init__(self,master: Tk = None, city: str = '', utc_zone: float = 0 ) ->  None:
        self.master = master
        self.city = city
        self.utc_zone = utc_zone
        self.frame = LabelFrame(self.master, text=f"{self.city.title()} Time")
        self.frame.pack(side='left')
        self.label = Label(self.frame, bg=self.__class__.background_clock)
        self.label.pack(fill='both', expand=1)
        self.update_time()
    
    def update_time(self) -> None:
        self.frame.configure(text=f"{self.city.title()} Time")
        hour, minute, second, tz = time.strftime('%H:%M:%S:%Z').split(':')
        hour = (int(hour) - int(tz) + 24 + self.utc_zone) % 24
        self.label.config(text=f"{str(hour).zfill(2)}:{minute}:{second}", background=self.__class__.background_clock)
        self.label.after(500, self.update_time)


root = Tk()
for city, tz in LIST_CLOCKS:
    #if  city == 'moscow':
    #    clock = ClockZone()
    #    clock.background_clock = 'orange'
    #    ClockZone.background_clock = 'pink'
    #    print(clock.__dict__)
    clock = ClockZone()
    clock.city = city
    clock.utc_zone = tz
    # print(clock.__dict__)
root.mainloop()

# 3 independent windows
# for city, tz in LIST_CLOCKS:
#     root = Tk()
#     clock = ClockZone(root)
#     clock.city = city
#     clock.utc_zone = tz
#
# root.mainloop()

