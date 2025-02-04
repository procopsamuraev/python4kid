# from tkinter import *
# 
# root = Tk()
# root.title("Calculator")
# 
# num = StringVar() # создадим переменную для отображения значений на табло калькулятора
# num.set(0)        # установим значение переменной равное 0
# # label = Entry(text=num, justify=RIGHT)
# # label.pack()
# 
# frame_entry=LabelFrame(root, text="1 row")
# frame_entry.pack()
# label = Entry(frame_entry, text=num, justify="right")
# label.pack()
# frame_numbers_1=LabelFrame(root, text="2 row")
# frame_numbers_1.pack()
# Button(frame_numbers_1, text=1).pack(side="left")
# Button(frame_numbers_1, text=2).pack(side="left")
# Button(frame_numbers_1, text=3).pack(side="left")
# Button(frame_numbers_1, text=4).pack(side="left")
# Button(frame_numbers_1, text=5).pack(side="left")
# frame_numbers_2=LabelFrame(root, text="3 row")
# frame_numbers_2.pack()
# Button(frame_numbers_2, text=6).pack(side="left")
# Button(frame_numbers_2, text=7).pack(side="left")
# Button(frame_numbers_2, text=8).pack(side="left")
# Button(frame_numbers_2, text=9).pack(side="left")
# Button(frame_numbers_2, text=0).pack(side="left")
# frame_operators=LabelFrame(root, text="4 row")
# frame_operators.pack()
# Button(frame_operators, text="+").pack(side="left")
# Button(frame_operators, text="-").pack(side="left")
# Button(frame_operators, text="*").pack(side="left")
# Button(frame_operators, text="/").pack(side="left")
# Button(frame_operators, text="=").pack(side="left")
# 
# 
# root.mainloop()


from tkinter import *

list_signs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', "="]

root = Tk()
root.title("Calculator")

num = StringVar() # создадим переменную для отображения значений на табло калькулятора
num.set(0)        # установим значение переменной равное 0
# Entry(text=num, justify="right").pack()

frame_entry = LabelFrame(root, text=row, justify='right').pack()
frame_entry.pack()

i = 0
while i < len(list_signs):
    print(i, list_signs[i], i%4, i//4)
    row = i//5+1
    column = i%5
    Button(text=list_signs[i]).grid(column=column, row=row, sticky=NSEW)
    i += 1


root.mainloop()