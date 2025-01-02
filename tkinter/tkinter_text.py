from tkinter import *

text_buffer = ''


def add_text():
    text.insert(END, 'This is a new text!')


def copy_all():
    global text_buffer
    text_buffer = text.get(0.0, END)


def copy():
    if text.tag_ranges('sel'):
        return text.selection_get()
    else: 
        None
    

def delete():
    text.delete(SEL_FIRST, SEL_LAST) if text.tag_ranges('sel') else None


def cut():
    global text_buffer
    text_buffer = copy()
    if text_buffer:
        delete()
    

def paste():
    global text_buffer
    text.insert(INSERT, text_buffer) if text_buffer else None


def caps():
    cut()
    text.insert(INSERT, text_buffer.capitalize()) if text_buffer else None


def lower():
    cut()
    text.insert(INSERT, text_buffer.lower()) if text_buffer else None


def upper():
    cut()
    text.insert(INSERT, text_buffer.upper()) if text_buffer else None


def title():
    cut()
    text.insert(INSERT, text_buffer.title()) if text_buffer else None



root = Tk()
text = Text(root) 
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack(expand=True, fill= 'both')
frame_button = LabelFrame(text='', border=0)
frame_button.pack()
# button = Button(text='Add', command=add_text)
button_copy_all = Button(frame_button, text='Copy all', command=copy_all)
button_copy_all.pack(side=LEFT)
button_copy = Button(frame_button, text='Copy', command=copy)
button_copy.pack(side=LEFT)
button_cut= Button(frame_button, text='Cut', command=cut)
button_cut.pack(side=LEFT)
button_paste_buffer = Button(frame_button, text='Paste', command=paste)
button_paste_buffer.pack(side=LEFT)
button = Button(frame_button, text='Capitalize', command=caps)
button.pack(side=LEFT)
button = Button(frame_button, text='Lower', command=lower)
button.pack(side=LEFT)
button = Button(frame_button, text='Upper', command=upper)
button.pack(side=LEFT)
button = Button(frame_button, text='Title', command=title)
button.pack(side=LEFT)


root.mainloop()