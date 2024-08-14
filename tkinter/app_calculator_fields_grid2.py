from tkinter import *


def sum_numbers():
    if value_sum_1.get().isnumeric() and value_sum_2.get().isnumeric():
        result_sum.delete(0, "end")
        result_sum.insert(0, int(value_sum_1.get()) + int(value_sum_2.get()))
    else:
        result_sum.insert(0, "Error")


def subtract_numbers():
    if value_subtract_1.get().isnumeric() and value_subtract_2.get().isnumeric():
        result_subtract.delete(0, "end")
        result_subtract.insert(0, int(value_subtract_1.get()) - int(value_subtract_2.get()))
    else:
        result_subtract.insert(0, "Error")


def multiplication_numbers():
   if value_multiplication_1.get().isnumeric() and value_multiplication_2.get().isnumeric():
       result_multi.delete(0, "end")
       result_multi.insert(0, int(value_multiplication_1.get()) * int(value_multiplication_2.get()))
   else:
       result_multi.insert(0, "Error")


def exponentiation_numbers():
   if value_exponentiation_1.get().isnumeric() and value_exponentiation_2.get().isnumeric():
       result_exponentiation.delete(0, "end")
       result_exponentiation.insert(0, int(value_exponentiation_1.get()) ** int(value_exponentiation_2.get()))
   else:
       result_exponentiation.insert(0, "Error")


def division_numbers():
    result_division.delete(0, "end")
    if value_division_1.get().isnumeric() and value_division_2.get().isnumeric() and (int(value_division_2.get()) > 0):
        result_division.insert(0, int(value_division_1.get()) / int(value_division_2.get()))
    else:
        result_division.insert(0, "Error")


def floor_division_numbers():
    result_floor_division.delete(0, "end")
    if value_floor_division_1.get().isnumeric() and value_floor_division_2.get().isnumeric() and (int(value_floor_division_2.get()) > 0):
        result_floor_division.insert(0, int(value_floor_division_1.get()) // int(value_floor_division_2.get()))
    else:
        result_floor_division.insert(0, "Error")


def modulus_numbers():
    result_modulus.delete(0, "end")
    if value_modulus_1.get().isnumeric() and value_modulus_2.get().isnumeric() and (int(value_ostatok_2.get()) > 0):
        result_modulus.insert(0, int(value_modulus_1.get()) % int(value_ostatok_2.get()))
    else:
        result_modulus.insert(0, "Error")


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
field_multiplication_1 = Entry(root, width=5, textvariable=value_multiplication_1)
field_multiplication_1.grid(column=0, row=row_num)
label = Label(root, text="*")
label.grid(column=1, row=row_num)
value_multiplication_2 = StringVar()
field_multiplication_2 = Entry(root, width=5, textvariable=value_multiplication_2)
field_multiplication_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=multiplication_numbers)
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_multiplication= Entry(root, width=5, textvariable=value_result)
result_multiplication.grid(column=4, row=row_num)

row_num = 3
value_exponentiation_1 = StringVar()
field_exponentiation_1 = Entry(root, width=5, textvariable=value_exponentiation_1)
field_exponentiation_1.grid(column=0, row=row_num)
label = Label(root, text="**")
label.grid(column=1, row=row_num)
value_exponentiation_2 = StringVar()
field_exponentiation_2 = Entry(root, width=5, textvariable=value_exponentiation_2)
field_exponentiation_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=exponentiation_numbers)
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_exponentiation = Entry(root, width=5, textvariable=value_result)
result_exponentiation.grid(column=4, row=row_num)

row_num = 4
value_division_1 = StringVar()
field_division_1 = Entry(root, width=5, textvariable=value_division_1)
field_division_1.grid(column=0, row=row_num)
label = Label(root, text="/")
label.grid(column=1, row=row_num)
value_division_2 = StringVar()
field_division_2 = Entry(root, width=5, textvariable=value_division_2)
field_division_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=division_numbers)
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_division = Entry(root, width=5, textvariable=value_result)
result_division.grid(column=4, row=row_num)

row_num = 5
value_floor_division_1 = StringVar()
field_floor_division_1 = Entry(root, width=5, textvariable=value_floor_division_1)
field_floor_division_1.grid(column=0, row=row_num)
label = Label(root, text="//")
label.grid(column=1, row=row_num)
value_floor_division_2 = StringVar()
field_floor_division_2 = Entry(root, width=5, textvariable=value_floor_division_2)
field_floor_division_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=floor_division_numbers)
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_floor_division = Entry(root, width=5, textvariable=value_result)
result_floor_division.grid(column=4, row=row_num)

row_num = 6
value_modulus_1 = StringVar()
field_modulus_1 = Entry(root, width=5, textvariable=value_modulus_1)
field_modulus_1.grid(column=0, row=row_num)
label = Label(root, text="%")
label.grid(column=1, row=row_num)
value_modulus_2 = StringVar()
field_modulus_2 = Entry(root, width=5, textvariable=value_modulus_2)
field_modulus_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=modulus_numbers)
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_modulus = Entry(root, width=5, textvariable=value_result)
result_modulus.grid(column=4, row=row_num)

root.mainloop()
