# from datetime import datetime
import time
import datetime
from tkinter import *
from tkinter.ttk import *


quantity_timers = 5
list_timers = []

color_run = 'light green'
color_stop = 'pink'
color_zero = 'light grey'

# state
# 0 - zero
# 1- running
# 2 - stopped


def save_result_to_file(dict_timers: dict)->None:
    string_log = f"Timer #{dict_timers['name_timer']} started:{dict_timers['time_start']} finished: {dict_timers['time_stop']}\n"
    with open('app_sport_timer.log', 'a') as outfile:
        outfile.write(string_log)


def update_label_timer(dict_timer:dict, time_start:float)->None:
    label = dict_timer.get('label')
    state_timer = dict_timer.get('state')
    time_diff_s = time.time() - time_start
    time_diff = str(datetime.timedelta(seconds=time_diff_s)).split('.')[0]
    label.config(text=time_diff)
    if state_timer == 1:
        label.after(500, lambda: update_label_timer(dict_timer, time_start))


def control_timer(dict_timer: dict)->None:
    state_timer = dict_timer.get('state')
    label = dict_timer.get('label')

    if state_timer == 1:
        dict_timer.update({'state': 2, 'time_stop': time.time()})
        label.config(background=color_stop)
    elif state_timer == 2:
        label.config(background=color_zero, text='0:00:00')
        dict_timer['state'] = 0
        save_result_to_file(dict_timer)
    else:
        label.config(background=color_run)
        time_start = time.time()
        dict_timer.update({'state': 1, 'time_start': time_start})
        update_label_timer(dict_timer, time_start)


def control_timer_all()-> None:
    state_min = 2
    for dict_timer in list_timers:
        state_timer = dict_timer.get('state')
        state_min = state_timer if state_timer < state_min else state_min
    for dict_timer in list_timers:
        state_timer = dict_timer.get('state')
        if state_timer == state_min:
            control_timer(dict_timer)


def draw_label_timer(number:int)->Label:
    frame = LabelFrame(text=f"Timer {number+1}".title())
    frame.pack(side='left')
    label = Label(frame,  font=("Arial", 20), background=color_zero, text='0:00:00')
    label.pack(fill='both', expand=1)
    dict_timer = {'name_timer':number+1, 'label': label, 'state':0}
    list_timers.append(dict_timer)
    return dict_timer


root = Tk()
root.title("Sport Timers")

for index in range(quantity_timers):
    dict_timer = draw_label_timer(index)
    key = str(index+1)

    root.bind(key, lambda event, dict_timer=dict_timer: control_timer(dict_timer))

root.bind("<space>", lambda event: control_timer_all())
root.mainloop()

