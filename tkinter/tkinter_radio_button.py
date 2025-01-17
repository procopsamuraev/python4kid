from tkinter import *
from tkinter.ttk import *

# ex1


# def print_console():
#     # label_value.set(f"Choosen {rb_var.get()} radiobutton")
#     pass
# 
# 
# root = Tk()
# rb_var = StringVar()
# Label(text='Look at the working program').pack()
# # label.pack()
# Radiobutton(text='the first', variable=rb_var, value='1', command=print_console).pack(anchor=W)
# Radiobutton(text='the second', variable=rb_var, value='2', command=print_console).pack(anchor=W)
# Radiobutton(text='the third', variable=rb_var, value='3', command=print_console).pack(anchor=W)
# Radiobutton(text='the fourth', variable=rb_var, value='4', command=print_console).pack(anchor=W)
# # label_value = StringVar()
# # label_value.set('Choosen ... radiobutton')
# Label(textvariable=rb_var).pack()
# root.mainloop()



# ex 2 
# //fix
# chosen should show on the user line - dynamic position
# def print_console():
#     label_value.set(f"Choosen {rb_var.get()} phone number")
# 
# 
# root = Tk()
# rb_var = StringVar()
# Label(text='Choose name:').grid(column=1, row=1, columnspan=1)
# Radiobutton(text='Pit', variable=rb_var, value='+722', command=print_console).grid(column=1, row=2)
# Radiobutton(text='Bob', variable=rb_var, value='+823', command=print_console).grid(column=1, row=3 )
# Radiobutton(text='Garry', variable=rb_var, value='+9123', command=print_console).grid(column=1, row=4)
# label_value = StringVar()
# label_value.set('Choosen ... radiobutton')
# Label(textvariable=label_value).grid(row=2, rowspan=3, column=2)
# root.mainloop()


# ex 3
# 

def check_answer():
    if rb_var.get()=='3' and input_user.get().strip().lower() =='pravilno':
        line_value.set("Correct") 
    else:
        line_value.set('Error')


root = Tk()
rb_var = StringVar()
Label(text='Choose correct spelling in russian lang').grid(column=1, row=1, columnspan=3)
Radiobutton(text='pastolku, paskolku', variable=rb_var, value='1').grid(column=1, row=2, sticky=W)
Radiobutton(text='vilka, tarelka', variable=rb_var, value='2').grid(column=1, row=3, sticky=W )
Radiobutton(text='your version:', variable=rb_var, value='3').grid(column=1, row=4, sticky=W)
Button(text='Check', command=check_answer).grid(column=2, row=5)

line_input=StringVar()
Entry(textvariable=line_input).grid(column=2, row=4, sticky=W)

line_value = StringVar()
Label(textvariable=line_value).grid(row=6, column=2)


root.mainloop()