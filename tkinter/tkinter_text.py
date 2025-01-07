"""
fix me
make small screen text
"""

from tkinter import *

text_buffer = ''


def add_text():
    text.insert(END, 'This is a new text!')


def copy_all():
    global text_buffer
    text_buffer = text.get(0.0, END)


def copy_text():
    global text_buffer
    try:
        text_buffer = text.selection_get()
    except TclError:
        pass
        

def delete():
    text.delete(SEL_FIRST, SEL_LAST) if text.tag_ranges('sel') else None


def cut():
    # global text_buffer
    copy_text()
    delete()
    

def paste():
    # global text_buffer
    text.insert(INSERT, text_buffer) if text_buffer else None


def capitalize_text():
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
text = Text(root, width=10, height=2) 
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack(expand=True, fill= 'both')
frame_button = LabelFrame(text='', border=0)
frame_button.pack()
# button = Button(text='Add', command=add_text)
Button(frame_button, text='Copy all', command=copy_all).pack(side=LEFT)
Button(frame_button, text='Copy', command=copy_text).pack(side=LEFT)
Button(frame_button, text='Cut', command=cut).pack(side=LEFT)
Button(frame_button, text='Paste', command=paste).pack(side=LEFT)
Button(frame_button, text='Capitalize', command=capitalize_text).pack(side=LEFT)
Button(frame_button, text='Lower', command=lower).pack(side=LEFT)
Button(frame_button, text='Upper', command=upper).pack(side=LEFT)
Button(frame_button, text='Title', command=title).pack(side=LEFT)

root.mainloop()