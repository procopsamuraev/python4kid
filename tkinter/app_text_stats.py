from curses.ascii import isalnum
from tkinter import *
from tkinter import messagebox
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
        # if self.state_timer == 1:
            # self.control_timer(0)

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
    list_char_end_sentence = ['.', ';', '!', '?', '\n' ]
    string_text = f"{str(text.get("1.0", END))}\n"
    char_previous = ''
    count_sentences_paragraph, number_paragraph, count_words = 0, 0, 0
    sum_sentences_start, sum_sentences_main, sum_sentences_end, _sum_sentences_end, sum_sentences_total = 0, 0, 0, 0, 0

    for char in string_text:
        word_end_true = not char.isalnum()  and char_previous.isalnum()
        sentence_end_true = char in list_char_end_sentence and char_previous not in list_char_end_sentence and char_previous
        paragraph_end_true = char == '\n' and count_sentences_paragraph
        count_words += 1 if word_end_true else 0

        if sentence_end_true:
            count_sentences_paragraph += 1
            sum_sentences_total += 1
            if number_paragraph == 0:
               sum_sentences_start += 1
            elif number_paragraph == 1:
                _sum_sentences_end = 0
            else:
                _sum_sentences_end += 1

        if paragraph_end_true:
            number_paragraph += 1 if count_sentences_paragraph else 0
            count_sentences_paragraph = 0
            _sum_sentences_end = 0
        sum_sentences_end = _sum_sentences_end if _sum_sentences_end else sum_sentences_end
        char_previous = char
    sum_sentences_main = sum_sentences_total - sum_sentences_end - sum_sentences_start

    update_status(count_words, sum_sentences_total, sum_sentences_start, sum_sentences_main, sum_sentences_end)
    timer.state_timer = 1
    timer.control_timer()
    set_result()


def update_status( count_words, sum_sentences_total, sum_sentences_start, sum_sentences_main,sum_sentences_end )->None:
    label_written_sentence_start.config(text=f"Written start sentences: {sum_sentences_start}")
    label_written_sentence_main.config(text=f"Written main sentences: {sum_sentences_main}")
    label_written_sentence_end.config(text=f"Written end sentences: {sum_sentences_end}")
    label_written_words.config(text=f"Written words: { count_words }")
    label_written_sentences.config(text=f"Written sentences: {sum_sentences_total}")

def show_warning_popup(string_warning:str)->None:
    messagebox.showwarning(title="Warning", message=f"Warning: {string_warning}")

def get_task():
    length_sentence = entry_sentence_len.get()
    words_min = entry_min_words.get()
    words_max= entry_max_words.get()
    # check user input data:
    # for user_input in [ length_sentence, words_min, words_max ]:
    #     print(user_input)
    #     if user_input.isdigit():
    #         user_input = int(user_input)
    #     else:
    #         show_warning_popup(f"Please enter only INT in {user_input}")
    if length_sentence.isdigit():
        length_sentence = int(length_sentence)
    else:
        show_warning_popup(f"Please enter INT in {length_sentence}")
    if words_min.isdigit():
        words_min = int(words_min)
    else:
        show_warning_popup(f"Please enter INT in {words_min}")
    if words_max.isdigit():
        words_max = int(words_max)
    else:
        show_warning_popup(f"Please enter INT in {words_max}")

    if words_min > words_max:
        show_warning_popup(f"Max should be > Min")

    number_sentences_min = words_min // length_sentence
    number_sentences_max = words_max // length_sentence
    number_sentences_other_min = number_sentences_min // 4
    number_sentences_other_max = number_sentences_max // 4
    number_sentences_main_min = number_sentences_min - 2 * number_sentences_other_min
    number_sentences_main_max = number_sentences_max - 2 * number_sentences_other_min
    label_sentence_start.config(text=f"Number of start sentences: {number_sentences_other_min}-{number_sentences_other_max}")
    label_sentence_main.config(text=f"Number of main sentences: {number_sentences_main_min}-{number_sentences_main_max}")
    label_sentence_end.config(text=f"Number of end sentences: {number_sentences_other_min}-{number_sentences_other_max}")

def set_result():
    count_written_words =  int(label_written_words.cget('text').split(':')[-1])
    words_max = int(entry_max_words.get())
    words_min = int(entry_min_words.get())
    if count_written_words > words_max:
        str_result = 'Over'
        timer.state_timer = 2
        timer.control_timer()
    elif count_written_words >= words_min:
        str_result = 'Done'
        timer.state_timer = 2
        timer.control_timer()
    else:
        str_result = 'Less'

    label_result.config(text=f"Result: {str_result}")



def set_time():
    pass

def control_timer():
    pass


root = Tk()
root.title('Literary note')

text = Text(wrap=WORD, width=30)
# text_sample = "What is Lorem Ipsum?\nLorem Ipsum is! simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.\nWhere does it come from?\nThis is the end paragraph! Have 3 sentences... Really"
# text_sample = "What is Lorem Ipsum?\nLorem Ipsum is!!!"
text_sample = "1. 2. 3.\n1. 2. 3. 4. 5.\n1. 2."
text.insert(INSERT, text_sample)
text.pack(fill='x')
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
timer=Timer(master=frame_result)
# label_time_spent = Label(frame_result, text='Spent time: 00:00:00')
# label_time_spent.pack(fill=X)
label_result = Label(frame_result, text="Result: Less.../Ready!/Much...")
label_result.pack(fill=X)

# root.bind('<Key>', lambda event: get_status())
text.bind('<Key>', lambda event: get_status())
frame_task.bind('<Leave>', lambda event: get_task())
root.bind('<Return>', lambda event: get_task())
# root.bind('<Key>', lambda event: get_task())


root.mainloop()