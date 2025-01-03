from tkinter import *


def get_status():
    line_len = len(text.get(0.0, END))
    # number_lines = text.index('end-1c').split('.')[0]
    number_lines = int(text.index('end').split('.')[0]) - 1
    line_number, symbol_number = text.index('insert').split('.')
    line_status = f"Symblols: {line_len} | Lines: {number_lines} | Line: {line_number} | Symbol: {symbol_number}".expandtabs()
    label.config(text=line_status)


def backspace():
    a, b = text.index('insert').split('.')
    if b=='0' and a>'0': 
        index0=f"{int(a)-1}.1000" #1000 should be replaced to the last symbol on string-1
    else: 
        index0=f"{a}.{int(b)-1}"
    print(index0)
    text.delete(index0, f"{a}.{b}")


root = Tk()
text = Text(root) 
text.insert(INSERT, "Some Text....some more text....end more..\n.........\n.............12345678911232sssssssssssssssssssssss")
text.pack(expand=1, fill='both')
frame_button = LabelFrame(text='', border=0, width=100)
frame_button.pack(expand=1, fill='x')
button = Button(frame_button, text='<- BackSpace', command=backspace)
button.pack(side=LEFT)
button = Button(frame_button, text='Get Status', command=get_status)
button.pack(side=LEFT)
label = Label(frame_button, justify=CENTER, text='')
label.pack(expand=1, fill='x', )
get_status


root.mainloop()