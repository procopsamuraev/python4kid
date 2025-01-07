from tkinter import *
"""
2nd solution is to work with string 
replace 1000 with calculated value
"""

def get_status():
    line_len = len(text.get(0.0, END))
    # number_lines = text.index('end-1c').split('.')[0]
    number_lines = int(text.index('end').split('.')[0]) - 1
    number_line, number_symbol = text.index('insert').split('.')
    line_status = f"Symblols: {line_len} | Lines: {number_lines} | Line: {number_line} | Symbol: {number_symbol}".expandtabs()
    label.config(text=line_status)


def backspace_text():
    char, line = text.index('insert').split('.')
    if line=='0' and char>'0': 
        index0=f"{int(char)-1}.1000" #1000 should be replaced to the last symbol on string-1
    else: 
        index0=f"{char}.{int(line)-1}"
    print(index0)
    text.delete(index0, f"{char}.{line}")


root = Tk()
text = Text(root, width=70, height=10) 
text.insert(INSERT, "Some Text....some more text....end more..\n.........\n.............12345678911232sssssssssssssssssssssss")
text.pack(expand=1, fill='both')
frame_button = LabelFrame(text='', border=0, width=100)
frame_button.pack(expand=1, fill='x')
Button(frame_button, text='<- BackSpace', command=backspace_text).pack(side=LEFT)
Button(frame_button, text='Get Status', command=get_status).pack(side=LEFT)
label = Label(frame_button, justify=CENTER, text='')
label.pack(expand=1, fill='x', )
get_status


root.mainloop()