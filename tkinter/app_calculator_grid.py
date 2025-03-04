# from tkinter import *
# 
# root = Tk()
# root.title("Calculator")
# 
# num = StringVar() # создадим переменную для отображения значений на табло калькулятора
# num.set(0)        # установим значение переменной равное 0
# 
# entry = Entry(text=num, justify="right").grid(column=0, row=0, columnspan=5)
# 
# Button(text=1).grid(column=0, row=1, sticky=NSEW)
# Button(text=2).grid(column=1, row=1, sticky=NSEW)
# Button(text=3).grid(column=2, row=1, sticky=NSEW)
# Button(text=4).grid(column=3, row=1, sticky=NSEW)
# Button(text=5).grid(column=4, row=1, sticky=NSEW)
# 
# Button(text=6).grid(column=0, row=2, sticky=NSEW)
# Button(text=7).grid(column=1, row=2, sticky=NSEW)
# Button(text=8).grid(column=2, row=2, sticky=NSEW)
# Button(text=9).grid(column=3, row=2, sticky=NSEW)
# Button(text=0).grid(column=4, row=2, sticky=NSEW)
# 
# Button(text="+").grid(column=0, row=3, sticky=NSEW)
# Button(text="-").grid(column=1, row=3, sticky=NSEW)
# Button(text="*").grid(column=2, row=3, sticky=NSEW)
# Button(text="/").grid(column=3, row=3, sticky=NSEW)
# Button(text="=").grid(column=4, row=3, sticky=NSEW)
# 
# 
# root.mainloop()


from tkinter import *

list_signs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', "="]

root = Tk()
root.title("Calculator")

num = StringVar() # создадим переменную для отображения значений на табло калькулятора
num.set(0)        # установим значение переменной равное 0

entry = Entry(text=num, justify="right").grid(column=0, row=0, columnspan=5)
i = 0
while i < len(list_signs):
    row = i//5+1
    column = i%5
    # print(i, row, column)
    Button(text=list_signs[i]).grid(column=column, row=row, sticky=NSEW)
    i += 1


root.mainloop()