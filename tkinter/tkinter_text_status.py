from tkinter import *
"""
2nd solution is to work with string 
replace 1000 with calculated value
"""

def get_status():
    line_len = len(text.get(0.0, END))
    # number_lines = text.index('end-1c').split('.')[0]
    number_lines = int(text.index('end').split('.')[0]) - 1
    line_number, symbol_number = text.index('insert').split('.')
    line_status = f"Symblols: {line_len} | Lines: {number_lines} | Line: {line_number} | Symbol: {symbol_number}"
    label.config(text=line_status)


def get_status2():
    text_all = text.get(0.0, END)
    size_text =  len(text_all)
    print(text_all)
    number_lines = text_all.count('\n')
    line_number, symbol_number = text.index('insert').split('.')
    line_status2 = f"Symblols: {size_text} | Lines: {number_lines} | Line: {line_number} | Symbol: {symbol_number}"
    label2.config(text=line_status2)


def backspace_text():
    number_line, number_char = text.index('insert').split('.')
    size_upper_line = len(text.get(0.0, END).split('\n')[int(number_line)-2])
    if number_char =='0' and number_line >'0':
        index0=f"{int(number_line)-1}.{size_upper_line}" 
    else: 
        index0=f"{number_line}.{int(number_char)-1}"
    # print(index0)
    text.delete(index0, f"{number_line}.{number_char}")


root = Tk()
text = Text(root, width=70, height=10) 
text.insert(INSERT, "Some Text....some more text....end more..\n.........\n.............12345678911232sssssssssssssssssssssss")
text.pack(expand=1, fill='both')
frame_button = LabelFrame(text='', border=0, width=100)
frame_button.pack(expand=1, fill='x')
frame_button2 = LabelFrame(text='', border=0, width=100)
frame_button2.pack(expand=1, fill='x')
Button(frame_button, text='<- BackSpace', command=backspace_text).pack(side=LEFT)
Button(frame_button, text='Get Status v1', command=get_status).pack(side=LEFT)
Button(frame_button2, text='Get Status v2', command=get_status2).pack(side=LEFT)
label = Label(frame_button, justify=CENTER, text='')
label.pack(expand=1, fill='x', )
label2 = Label(frame_button2, justify=CENTER, text='')
label2.pack(expand=1, fill='x', )
get_status
get_status2


root.mainloop()