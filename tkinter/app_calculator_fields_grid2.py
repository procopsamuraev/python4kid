from tkinter import *

def check_input(value_1, value_2):


def sum_numbers():
    if value_sum_1.get().isnumeric() and value_sum_2.get().isnumeric():
        result_sum.delete(0, "end")
        result_sum.insert(0, int(value_sum_1.get()) + int(value_sum_2.get()))
    else:
        result_sum.insert(0, "Error")


def subtract_numbers():
    if value_subtract_1.get().isnumeric() and value_subtract_2.get().isnumeric():
        result_subtract.delete(0, "end")
        result_subtract.insert(0, int(value_subtract_1.get()) - int(value_minus_2.get()))
    else:
        result_subtract.insert(0, "Error")


def multiplication_numbers():
   if value_multiplication_1.get().isnumeric() and value_multi_2.get().isnumeric():
       result_multi.delete(0, "end")
       result_multi.insert(0, int(value_multiplication_1.get()) * int(value_multi_2.get()))
   else:
       result_multi.insert(0, "Error")


def exponentiation_numbers():
   if value_stepen_1.get().isnumeric() and value_stepen_2.get().isnumeric():
       result_stepen.delete(0, "end")
       result_stepen.insert(0, int(value_stepen_1.get()) ** int(value_stepen_2.get()))
   else:
       result_stepen.insert(0, "Error")


def division_numbers():
    result_delenie.delete(0, "end")
    if value_delenie_1.get().isnumeric() and value_delenie_2.get().isnumeric() and (int(value_delenie_2.get()) > 0):
        result_delenie.insert(0, int(value_delenie_1.get()) / int(value_delenie_2.get()))
    else:
        result_delenie.insert(0, "Error")


def floor_division_numbers():
    result_c_delenie.delete(0, "end")
    if value_c_delenie_1.get().isnumeric() and value_c_delenie_2.get().isnumeric() and (int(value_c_delenie_2.get()) > 0):
        result_c_delenie.insert(0, int(value_c_delenie_1.get()) // int(value_c_delenie_2.get()))
    else:
        result_c_delenie.insert(0, "Error")


def modulus_numbers():
    result_ostatok.delete(0, "end")
    if value_ostatok_1.get().isnumeric() and value_ostatok_2.get().isnumeric() and (int(value_ostatok_2.get()) > 0):
        result_ostatok.insert(0, int(value_ostatok_1.get()) % int(value_ostatok_2.get()))
    else:
        result_ostatok.insert(0, "Error")


root = Tk()
root.title("Ex_1")

row_num = 0
value_sum_1 = StringVar()
field_sum_1 = Entry(root, width=5, textvariable=value_sum_1)
field_sum_1.grid(column=0, row=row_num)
label = Label(root, text="+")
label.grid(column=1, row=row_num)
value_sum_2 = StringVar()
field_sum_2 = Entry(root, width=5, textvariable=value_sum_2)
field_sum_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=sum_numbers)
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_sum = Entry(root, width=5, textvariable=value_result)
result_sum.grid(column=4, row=row_num)

row_num = 1
value_subtract_1 = StringVar()
field_subtract_1 = Entry(root, width=5, textvariable=value_subtract_1)
field_subtract_1.grid(column=0, row=row_num)
label = Label(root, text="-")
label.grid(column=1, row=row_num)
value_subtract_2 = StringVar()
field_subtract_2 = Entry(root, width=5, textvariable=value_subtract_2)
field_subtract_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=subtract_numbers)
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_subtract = Entry(root, width=5, textvariable=value_result)
result_subtract.grid(column=4, row=row_num)

row_num = 2
value_multiplication_1 = StringVar()
field_multiplication_1 = Entry(root, width=5, textvariable=value_multi_1)
field_multiplication_1.grid(column=0, row=row_num)
label = Label(root, text="*")
label.grid(column=1, row=row_num)
value_multiplication_2 = StringVar()
field_multiplication_2 = Entry(root, width=5, textvariable=value_multi_2)
field_multiplication_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=multiplication_numbers)
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_multi = Entry(root, width=5, textvariable=value_result)
result_multi.grid(column=4, row=row_num)

row_num = 3
value_stepen_1 = StringVar()
field_stepen_1 = Entry(root, width=5, textvariable=value_stepen_1)
field_stepen_1.grid(column=0, row=row_num)
label = Label(root, text="**")
label.grid(column=1, row=row_num)
value_stepen_2 = StringVar()
field_stepen_2 = Entry(root, width=5, textvariable=value_stepen_2)
field_stepen_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=exponentiation_numbers)
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_stepen = Entry(root, width=5, textvariable=value_result)
result_stepen.grid(column=4, row=row_num)

row_num = 4
value_delenie_1 = StringVar()
field_delenie_1 = Entry(root, width=5, textvariable=value_delenie_1)
field_delenie_1.grid(column=0, row=row_num)
label = Label(root, text="/")
label.grid(column=1, row=row_num)
value_delenie_2 = StringVar()
field_delenie_2 = Entry(root, width=5, textvariable=value_delenie_2)
field_delenie_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=division_number)
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_delenie = Entry(root, width=5, textvariable=value_result)
result_delenie.grid(column=4, row=row_num)

row_num = 5
value_c_delenie_1 = StringVar()
field_c_delenie_1 = Entry(root, width=5, textvariable=value_c_delenie_1)
field_c_delenie_1.grid(column=0, row=row_num)
label = Label(root, text="//")
label.grid(column=1, row=row_num)
value_c_delenie_2 = StringVar()
field_c_delenie_2 = Entry(root, width=5, textvariable=value_c_delenie_2)
field_c_delenie_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=floor_division_numbers)
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_c_delenie = Entry(root, width=5, textvariable=value_result)
result_c_delenie.grid(column=4, row=row_num)

row_num = 6
value_ostatok_1 = StringVar()
field_ostatok_1 = Entry(root, width=5, textvariable=value_ostatok_1)
field_ostatok_1.grid(column=0, row=row_num)
label = Label(root, text="%")
label.grid(column=1, row=row_num)
value_ostatok_2 = StringVar()
field_ostatok_2 = Entry(root, width=5, textvariable=value_ostatok_2)
field_ostatok_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=modulus_numbers)
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_ostatok = Entry(root, width=5, textvariable=value_result)
result_ostatok.grid(column=4, row=row_num)

root.mainloop()
