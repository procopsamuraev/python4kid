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
# def print_console(row_number):
#     label_phone_value.set(f"{rb_var.get()}")
#     label_phone.grid(row=row_number,column=2)
# 
# 
# root = Tk()
# rb_var = StringVar()
# Label(text='Please select a name to show the phone number:').grid(column=1, row=1, columnspan=2)
# Radiobutton(text='Pit', variable=rb_var, value='+722', command=lambda row_number=2:  print_console(row_number)).grid(column=1, row=2, sticky=W)
# Radiobutton(text='Bob', variable=rb_var, value='+823', command=lambda row_number=3: print_console(row_number)).grid(column=1, row=3, sticky=W )
# Radiobutton(text='Garry', variable=rb_var, value='+9123', command=lambda row_number=4: print_console(row_number)).grid(column=1, row=4, sticky=W)
# label_phone_value = StringVar()
# label_phone = Label(textvariable=label_phone_value)
# root.mainloop()

#
# ex 3
# 

# def check_answer():
#     if rb_var.get()=='3' and line_input.get().strip().lower() =='correct':
#         line_value.set("Your answer is correct!") 
#     else:
#         line_value.set('Error')
# 
# 
# root = Tk()
# rb_var = StringVar()
# Label(text='Choose correct spelling in russian lang').grid(column=1, row=1, columnspan=3)
# Radiobutton(text='pastolku, paskolku', variable=rb_var, value='1').grid(column=1, row=2, sticky=W)
# Radiobutton(text='vilka, tarelka', variable=rb_var, value='2').grid(column=1, row=3, sticky=W )
# Radiobutton(text='Your version:', variable=rb_var, value='3').grid(column=1, row=4, sticky=W)
# line_input=StringVar()
# Entry(textvariable=line_input).grid(column=2, row=4, sticky=W)
# Button(text='Check', command=check_answer).grid(column=2, row=5)
# 
# line_value = StringVar()
# Label(textvariable=line_value).grid(row=6, column=2)
# 
# 
# root.mainloop()