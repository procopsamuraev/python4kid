# from tkinter import *
# 
# list_signs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', "="]
# 
# root = Tk()
# root.title("Calculator")
# 
# num = StringVar() # создадим переменную для отображения значений на табло калькулятора
# num.set(0)        # установим значение переменной равное 0
# 
# entry = Entry(text=num).place(x=0, y=0)
# i = 0
# while i < len(list_signs):
#     # print(i, list_signs[i], i%4, i//4)
#     row = i//5+1
#     column = i%5
#     print(row, column)
#     Button(text=list_signs[i]).place(x=column*35, y=row*35)
#     i += 1
# 
# 
# root.mainloop()

# double while

from tkinter import *
list_signs = [['1', '2', '3', '4', '5'], ['6', '7', '8', '9', '0'], ['+', '-', '*', '/', "="]]
root = Tk()
root.title('Calculator')

Entry(text='').place(x=0, y=0)
row = 0
while row < len(list_signs):
    column = 0
    while column < len(list_signs[row]):
        Button(text=list_signs[row][column]).place(x=column*35, y=row*35)
        column += 1
    row +=1
root.mainloop() 
