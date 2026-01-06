# from tkinter import *
# from tkinter.ttk import *
# 
# def change(event):
#     b['text'] = 'Thanks for your click. ;)'
# 
# def change2(event):
#     b['text'] = 'Thanks for your click Enter. ;)'
# 
# root = Tk()
# 
# b = Button(text='Click me!')
# b.bind('<Button-1>', change)
# b.bind('<Return>', change2)
# b.pack()
# 
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def font1(event):
#     l['font'] = "Verdana"
#
# def font2(event):
#     l['font'] = "Times"
#
# root = Tk()
#
# l = Label(text="Hello World")
# l.bind('<Button-1>', font1)  # ЛКМ
# l.bind('<Button-3>', font2)  # ПКМ
# l.pack()
#
# root.mainloop()

# from tkinter import *
#
# def changeFont(font):
#     l['font'] = font
#
# root = Tk()
# l = Label(text="Hello World")
# l.pack()
# Button(text="Verdana", command=lambda f="Verdana": changeFont(f)).pack()
# Button(text="Times", command=lambda f="Times": changeFont(f)).pack()
#
# root.mainloop()

# #ex1
# from tkinter import *
#
# def move_to_listbox(event):
#     text = entry.get().strip()
#     index_listbox_selected = listbox.curselection()
#     if not text:
#         return
#     if index_listbox_selected:
#         listbox.delete(index_listbox_selected)
#         listbox.insert(index_listbox_selected, text)
#     else:
#         listbox.insert(END, text)
#     entry.delete(0, END)
#
#
# def delete_from_listbox(event):
#     selected=listbox.curselection()
#     listbox.delete(selected)
#
# def copy_to_entry(event):
#     index = listbox.curselection()
#     entry.delete(0, END)
#     entry.insert(0, listbox.get(index))


# root = Tk()
# entry = Entry(root)
# entry.pack()
# entry.bind("<Return>", move_to_listbox)
#
# listbox=Listbox(root)
# listbox.pack()
# listbox.bind("<Delete>", delete_from_listbox)
# listbox.bind("<Double-Button-1>", copy_to_entry)
#
# root.mainloop()


#ex2
# from tkinter import *
#
# def change_label_color(event):
#     label.configure(background='#fff')
#
# def change_font_color(event):
#     label.configure(fg='#fff')
#
# root = Tk()
# label = Label(root, text='Click to change color')
# label.pack(fill='both', expand=True)
# label.bind('<Button-1>', change_label_color)
# label.bind('<Button-3>', change_font_color)
#
# root.mainloop()
