from tkinter import *

def add_text():
    text.insert(END, 'This is a new text!')

root = Tk()
text = Text(root) 
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack(expand=True, fill= 'both')
button = Button(text='Add', command=add_text)
button.pack()

root.mainloop()