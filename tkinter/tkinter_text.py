from tkinter import *

text_buffer = ''
def add_text():
    text.insert(END, 'This is a new text!')


def copy_all():
    global text_buffer
    text_buffer = text.get(0.0, END)


def copy_selected():
    global text_buffer
    text_buffer = text.selection_get()
 

def delete():
    text.delete(SEL_FIRST, SEL_LAST)


def cut():
    copy_selected()
    delete()
    

def paste_buffer():
    global text_buffer
    text.insert(INSERT, text_buffer)
    

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
button_copy_selected = Button(frame_button, text='Copy', command=copy_selected)
button_copy_selected.pack(side=LEFT)
button_cut= Button(frame_button, text='Cut', command=cut)
button_cut.pack(side=LEFT)
button_paste_buffer = Button(frame_button, text='Paste', command=paste_buffer)
button_paste_buffer.pack(side=LEFT)


root.mainloop()