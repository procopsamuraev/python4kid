from tkinter import *
from tkinter.ttk import *
import time
import datetime

class Timer:
    def __init__(self, master: Tk = None, state: int = 1) -> None:
        self.time_start = 0
        self.time_stop = 0
        self.state_timer = state
        self.color_run = 'light green'
        self.color_stop = 'pink'
        self.color_zero = 'light grey'
        self.label = Label(master,  text='Spent Time: 0:00:00')
        self.label.pack(fill='x')

    def update_label_timer(self)->None:
        time_diff = datetime.timedelta(seconds=time.time() - self.time_start)
        self.label.config(text=f"Spent Time: {str(time_diff).split('.')[0]}")
        if self.state_timer == 1:
            self.label.after(500, lambda: self.update_label_timer())

    def control_timer(self)->None:
        if not self.time_start:
            self.time_start = time.time()
        if self.state_timer == 2:
            self.label.config(background=self.color_stop)
            # self.state_timer = 2
        elif self.state_timer == 0:
            self.label.config(background=self.color_zero, text='0:00:00')
            # self.state_timer = 0
        else:
            self.label.config(background=self.color_run)
            self.state_timer = 1
            self.update_label_timer()


def get_status():
    condition_words =  0
    words_min_limit = entry_min_words.get()
    words_max_limit = entry_max_words.get()
    length_sentence = entry_sentence_len.get()

    string_text = text.get("1.0", END).strip()
    sum_words = len(string_text.split())
    sum_sentences = string_text.replace('!','.').replace('?', '.').replace('...', '.').count('.')
    label_written_words.config(text=f"Written words: {sum_words}")
    label_written_sentences.config(text=f"Written sentences: {sum_sentences}")
    timer.state_timer = 1
    timer.control_timer()



def get_task():
    pass

def set_result():
    pass

def set_time():
    pass

def control_timer():
    pass
# def update_label_timer(dict_timer, time_start):


root = Tk()
root.title('Literary note')

text = Text(wrap=WORD, width=30)
text.pack(side=LEFT, expand=1, fill=BOTH)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

frame_right = Frame()
frame_right.pack(side=LEFT, fill=Y)


frame_task = LabelFrame(frame_right, text='Task:')
frame_task.pack(fill=X)

Label(frame_task, text='Min words:').pack()
entry_min_words = Entry(frame_task, justify=RIGHT)
entry_min_words.insert(END, 70)
entry_min_words.pack(fill=X)

Label(frame_task, text='Max words:').pack()
entry_max_words = Entry(frame_task, justify=RIGHT)
entry_max_words.insert(END, 90)
entry_max_words.pack(fill=X)

Label(frame_task, text='Number of words in a sentence:').pack()
entry_sentence_len = Entry(frame_task, justify=RIGHT)
entry_sentence_len.insert(END, 7)
entry_sentence_len.pack(fill=X)

label_sentence_start = Label(frame_task, text="Number of start sentences: 2 - 3")
label_sentence_start.pack(fill=X)
label_sentence_main = Label(frame_task, text="Number of main sentences: 5 - 7")
label_sentence_main.pack(fill=X)
label_sentence_end = Label(frame_task, text="Number of end sentences: 2 - 3")
label_sentence_end.pack(fill=X)


frame_status = LabelFrame(frame_right, text='Status:')
frame_status.pack(fill=X)
label_written_words = Label(frame_status, text='Written words: 0')
label_written_words.pack(fill=X)
label_written_sentences = Label(frame_status, text='Written sentences: 0')
label_written_sentences.pack(fill=X)

label_written_sentence_start = Label(frame_status, text="Written start sentences: 0")
label_written_sentence_start.pack(fill=X)
label_written_sentence_main = Label(frame_status, text="Written main sentences: 0")
label_written_sentence_main.pack(fill=X)
label_written_sentence_end = Label(frame_status, text="Written end sentences: 0")
label_written_sentence_end.pack(fill=X)


frame_result = LabelFrame(frame_right, text='Result:')
frame_result.pack(fill=X)
timer=Timer(master=frame_result, state=0)
# label_time_spent = Label(frame_result, text='Spent time: 00:00:00')
# label_time_spent.pack(fill=X)
label_result = Label(frame_result, text="Result: Less.../Ready!/Much...")
label_result.pack(fill=X)

root.bind('<Key>', lambda event: get_status())

root.mainloop()