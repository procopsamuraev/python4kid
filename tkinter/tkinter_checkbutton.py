# ex 1 
from tkinter import *
from tkinter.ttk import *


# def check_answers():
#     a1,a2,a3,a4 = int(ch_var1.get()), int(ch_var2.get()), int(ch_var3.get()), int(ch_var4.get())
#     if a1 and a3 and a4 and not a2: 
#         label_result.config(text='Correct')
#     elif (a1 or a3 or a4) and not a2: 
#         label_result.config(text='Almost correct')
#     elif a2: 
#         label_result.config(text='Not correct')
#     else: 
#         label_result.config(text='Please choose one or more options')
#     print(a1,a2,a3,a4) 
# 
# 
# root = Tk()
# Label(text="How much is 1+1?").pack(anchor=N)
# ch_var1 = StringVar()
# ch_var1.set(0)
# Checkbutton(text="11, for strings", variable=ch_var1, onvalue=1, offvalue=0).pack(anchor=W)
# 
# ch_var2 = StringVar()
# ch_var2.set(0)
# Checkbutton(text="5 with margin", variable=ch_var2, onvalue=1, offvalue=0).pack(anchor=W)
# 
# ch_var3 = StringVar()
# ch_var3.set(0)
# Checkbutton(text="10 for 2x systems", variable=ch_var3, onvalue=1, offvalue=0).pack(anchor=W)
# 
# ch_var4 = StringVar()
# ch_var4.set(0)
# Checkbutton(text="2 fo 10x systems", variable=ch_var4, onvalue=1, offvalue=0).pack(anchor=W)
# 
# Button(text="Check", command=check_answers).pack(anchor=N)
# 
# label_result = Label(text='Choose correct options')
# label_result.pack(anchor=N)

#
# ex 2
#

# def print_selected():
#     text.delete(1.0, END)
#     a1,a2,a3,a4,a5 = ch_var1.get(), ch_var2.get(), ch_var3.get(), ch_var4.get(), ch_var5.get()
#     text_to_insert = f"{a1}, {a2}, {a3}, {a4}, {a5}".replace(', .', '.').strip(' ,').replace(' ,','')
#     text_to_insert = f"{text_to_insert}." if len(text_to_insert)>1 else f""
#     text.insert(END, text_to_insert)
#     
# 
# root = Tk()
# Label(text="choose:").grid(row=1, column=1)
# ch_var1 = StringVar()
# ch_var1.set('')
# Checkbutton(text="black", variable=ch_var1, onvalue='black', offvalue='').grid(column=1, row=2, sticky=W)
# ch_var2 = StringVar()
# ch_var2.set('')
# Checkbutton(text="green", variable=ch_var2, onvalue='green', offvalue='').grid(column=1, row=3, sticky=W)
# ch_var3 = StringVar()
# ch_var3.set('')
# Checkbutton(text="blue", variable=ch_var3, onvalue='blue', offvalue='').grid(column=1, row=4, sticky=W)
# ch_var4 = StringVar()
# ch_var4.set('')
# Checkbutton(text="red", variable=ch_var4, onvalue='red', offvalue='').grid(column=1, row=5, sticky=W)
# ch_var5 = StringVar()
# ch_var5.set('')
# Checkbutton(text="white", variable=ch_var5, onvalue='white', offvalue='').grid(column=1, row=6, sticky=W)
# 
# Button(text="Print", command=print_selected).grid(column=1, row=7, sticky=W)
# 
# text = Text(root, width=25)
# text.grid(column=2, row=1, rowspan=7, sticky=N)
# 
# 

def check_answer():
    correct_answer = ch_var4.get() and (ch_var4_input.get() == '7' or ch_var4_input.get() == '8')
    if ch_var1.get() or ch_var2.get() or ch_var3.get():
        label_result.config(text='Not correct')
    elif correct_answer:
        label_result.config(text='Correct')
    else:
        label_result.config(text='Chose one or more and full up field')


root = Tk()

Label(text='how much is 2+2?').grid(row=1, column=1)
ch_var1 = IntVar()
ch_var1.set(0)
Checkbutton(text='3', variable=ch_var1, onvalue=3, offvalue=0).grid(column=1, row=2, sticky=W)
ch_var2 = IntVar()
ch_var2.set(0)
Checkbutton(text='5', variable=ch_var2, onvalue=5, offvalue=0).grid(column=1, row=3, sticky=W)
ch_var3 = IntVar()
ch_var3.set(0)
Checkbutton(text='4', variable=ch_var3, onvalue=4, offvalue=0).grid(column=1, row=4, sticky=W)
ch_var4 = IntVar()
ch_var4.set(0)
Checkbutton(text='Own version:', variable=ch_var4, offvalue=0, onvalue=1).grid(column=1, row=5, sticky=W)
ch_var4_input=StringVar()
ch_var4_input.set('')
entry_chech_button = Entry(textvariable=ch_var4_input, width=5).grid(column=2, row=5, padx=3)
Button(text='Check', command=check_answer).grid(column=1, row=6, sticky=N)
label_result = Label(text='Chose one or more')
label_result.grid(column=1, row=7, columnspan=2)


root.mainloop()