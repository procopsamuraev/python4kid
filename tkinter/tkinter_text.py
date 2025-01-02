from tkinter import *

text_buffer = ''
def add_text():
    text.insert(END, 'This is a new text!')


def copy_all():
    global text_buffer
    text_buffer = text.get(0.0, END)


def paste_buffer():
    global text_buffer
    text.insert(INSERT, text_buffer)
    

root = Tk()
text = Text(root) 
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack(expand=True, fill= 'both')
# button = Button(text='Add', command=add_text)
button_copy_all = Button(text='Copy all', command=copy_all)
button_copy_all.pack(side=LEFT)
button_paste_buffer = Button(text='Paste', command=paste_buffer)
button_paste_buffer.pack(side=RIGHT)


root.mainloop()