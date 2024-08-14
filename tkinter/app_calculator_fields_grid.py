from tkinter import *


def calculation(operation):
    if operation == "+":
        if value_sum_1.get().isdigit() and value_sum_2.get().strip("-").isdigit():
            result_sum.delete(0, "end")
            result_sum.insert(0, int(value_sum_1.get()) + int(value_sum_2.get()))
        else:
            result_sum.insert(0, "Error")
    elif operation == "-":
        if value_minus_1.get().isdigit() and value_minus_2.get().isdigit():
            result_minus.delete(0, "end")
            result_minus.insert(0, int(value_minus_1.get()) - int(value_minus_2.get()))
        else:
            result_minus.insert(0, "Error")
    elif operation == "*":
        if value_multi_1.get().isdigit() and value_multi_2.get().isdigit():
            result_multi.delete(0, "end")
            result_multi.insert(0, int(value_multi_1.get()) * int(value_multi_2.get()))
        else:
            result_multi.insert(0, "Error")
    elif operation == "**":
        if value_stepen_1.get().isdigit() and value_stepen_2.get().isdigit():
            result_stepen.delete(0, "end")
            result_stepen.insert(0, int(value_stepen_1.get()) ** int(value_stepen_2.get()))
        else:
            result_stepen.insert(0, "Error")
    elif operation == "/":
        result_delenie.delete(0, "end")
        if value_delenie_1.get().isdigit() and value_delenie_2.get().isdigit() and (int(value_delenie_2.get()) > 0):
            result_delenie.insert(0, int(value_delenie_1.get()) / int(value_delenie_2.get()))
        else:
            result_delenie.insert(0, "Error")
    elif operation == "//":
        result_c_delenie.delete(0, "end")
        if value_c_delenie_1.get().isdigit() and value_c_delenie_2.get().isdigit() and (int(value_c_delenie_2.get()) > 0):
            result_c_delenie.insert(0, int(value_c_delenie_1.get()) // int(value_c_delenie_2.get()))
        else:
            result_c_delenie.insert(0, "Error")
    elif operation == "%":
        result_ostatok.delete(0, "end")
        if value_ostatok_1.get().isdigit() and value_ostatok_2.get().isdigit() and (int(value_ostatok_2.get()) > 0):
            result_ostatok.insert(0, int(value_ostatok_1.get()) % int(value_ostatok_2.get()))
        else:
            result_ostatok.insert(0, "Error")

# operations_list = [
#     {"name": "sum", "symbol": "+"},
#     {"name": "minus", "symbol": "-"},
#     {"name": "multiplication", "symbol": "*"},
# ]

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
button_equal = Button(root, text="=", command=lambda operation="+": calculation(operation))
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_sum = Entry(root, width=5, textvariable=value_result)
result_sum.grid(column=4, row=row_num)

row_num = 1
value_minus_1 = StringVar()
field_minus_1 = Entry(root, width=5, textvariable=value_minus_1)
field_minus_1.grid(column=0, row=row_num)
label = Label(root, text="-")
label.grid(column=1, row=row_num)
value_minus_2 = StringVar()
field_minus_2 = Entry(root, width=5, textvariable=value_minus_2)
field_minus_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=lambda operation="-": calculation(operation))
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_minus = Entry(root, width=5, textvariable=value_result)
result_minus.grid(column=4, row=row_num)

row_num = 2
value_multi_1 = StringVar()
field_multi_1 = Entry(root, width=5, textvariable=value_multi_1)
field_multi_1.grid(column=0, row=row_num)
label = Label(root, text="*")
label.grid(column=1, row=row_num)
value_multi_2 = StringVar()
field_multi_2 = Entry(root, width=5, textvariable=value_multi_2)
field_multi_2.grid(column=2, row=row_num)
button_equal = Button(root, text="=", command=lambda operation="*": calculation(operation))
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
button_equal = Button(root, text="=", command=lambda operation="**": calculation(operation))
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
button_equal = Button(root, text="=", command=lambda operation="/": calculation(operation))
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
button_equal = Button(root, text="=", command=lambda operation="//": calculation(operation))
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
button_equal = Button(root, text="=", command=lambda operation="%": calculation(operation))
button_equal.grid(column=3, row=row_num)
value_result = StringVar()
result_ostatok = Entry(root, width=5, textvariable=value_result)
result_ostatok.grid(column=4, row=row_num)

root.mainloop()
