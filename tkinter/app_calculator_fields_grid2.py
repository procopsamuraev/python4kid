from tkinter import *

error_general = "Enter numbers only"
error_zero = "Can't divide a number by 0"


# def sum_numbers():
#     result_sum.delete(0, "end")
#     value_clean_1 = value_sum_1.get().replace(" ", "").replace(",", ".")
#     value_clean_2 = value_sum_2.get().replace(" ", "").replace(",", ".")
#     number_1 = float(value_clean_1) if value_clean_1.removeprefix("-").replace(".", "", 1).isdigit() \
#         else result_sum.insert(0, error_message_general)
#     number_2 = float(value_clean_2) if value_clean_2.removeprefix("-").replace(".", "", 1).isdigit() \
#         else result_sum.insert(0, error_message_general)
#     result = number_1 + number_2
#     result_sum.insert(0, int(result)) if result.is_integer() \
#         else result_sum.insert(0, result)

def sum_numbers():
    result_sum.delete(0, "end")
    numbers=list()
    for value in [value_sum_1, value_sum_2]:
        value_clean = value.get().replace(" ", "").replace(",", ".")
        number = float(value_clean) if value_clean.removeprefix("-").replace(".", "", 1).isdigit() \
            else result_sum.insert(0, error_message_general)
        numbers.append(number)
    result = numbers[0] + numbers[1]
    result = int(result) if result.is_integer() else result
    result_sum.insert(0, str(result))


def subtract_numbers():
    result_subtract.delete(0, "end")
    value_clean_1 = value_subtract_1.get().replace(" ", "").replace(",", ".")
    value_clean_2 = value_subtract_2.get().replace(" ", "").replace(",", ".")
    number_1 = float(value_clean_1) if value_clean_1.removeprefix("-").replace(".", "", 1).isdigit() \
        else result_subtract.insert(0, error_message_general)
    number_2 = float(value_clean_2) if value_clean_2.removeprefix("-").replace(".", "", 1).isdigit() \
        else result_subtract.insert(0, error_message_general)
    result = number_1 - number_2
    result = int(result) if result.is_integer() else result
    result_subtract.insert(0, str(result))


def multiplication_numbers():
    result_multiplication.delete(0, "end")
    value_clean_1 = value_multiplication_1.get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = value_multiplication_2.get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    result = str(float(value_clean_1) * float(value_clean_2)) if number_1_true and number_2_true else error_general
    result_multiplication.insert(0, result.rstrip("0").removesuffix("."))


def exponentiation_numbers():
    result_exponentiation.delete(0, "end")
    value_clean_1 = value_exponentiation_1.get().replace(" ", "").replace(",", ".")
    value_clean_2 = value_exponentiation_2.get().replace(" ", "").replace(",", ".")
    number_1 = float(value_clean_1) if value_clean_1.removeprefix("-").replace(".", "", 1).isdigit() \
        else result_exponentiation.insert(0, error_message_general)
    number_2 = float(value_clean_2) if value_clean_2.removeprefix("-").replace(".", "", 1).isdigit() \
        else result_exponentiation.insert(0, error_message_general)
    result = number_1 ** number_2
    result = int(result) if result.is_integer() else result
    result_exponentiation.insert(0, str(result))


def division_numbers():
    result_division.delete(0, "end")
    value_clean_1 = value_division_1.get().replace(" ", "").replace(",", ".")
    value_clean_2 = value_division_2.get().replace(" ", "").replace(",", ".")
    number_1 = float(value_clean_1) if value_clean_1.removeprefix("-").replace(".", "", 1).isdigit() \
        else result_division.insert(0, error_message_general)
    number_2 = float(value_clean_2) if value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()  \
        else result_division.insert(0, error_message_general)
    if number_2 == 0.0:
        result_division.insert(0, error_message_zero) if number_2 == 0.0 else number_2
    else:
        result = number_1 / number_2
        result = int(result) if result.is_integer() else result
        result_division.insert(0, str(result))


def floor_division_numbers():
    result_floor_division.delete(0, "end")
    value_clean_1 = value_floor_division_1.get().replace(" ", "").replace(",", ".")
    value_clean_2 = value_floor_division_2.get().replace(" ", "").replace(",", ".")
    number_1 = float(value_clean_1) if value_clean_1.removeprefix("-").replace(".", "", 1).isdigit() \
        else result_floor_division.insert(0, error_message_general)
    number_2 = float(value_clean_2) if value_clean_2.removeprefix("-").replace(".", "", 1).isdigit() \
        else result_floor_division.insert(0, error_message_general)
    if number_2 == 0.0:
        result_floor_division.insert(0, error_message_zero) if number_2 == 0.0 else number_2
    else:
        result = number_1 // number_2
        result = int(result) if result.is_integer() else result
        result_floor_division.insert(0, str(result))


def modulus_numbers():
    result_modulus.delete(0, "end")
    value_clean_1 = value_modulus_1.get().replace(" ", "").replace(",", ".")
    value_clean_2 = value_modulus_2.get().replace(" ", "").replace(",", ".")
    number_1 = float(value_clean_1) if value_clean_1.removeprefix("-").replace(".", "", 1).isdigit() \
        else result_modulus.insert(0, error_message_general)
    number_2 = float(value_clean_2) if value_clean_2.removeprefix("-").replace(".", "", 1).isdigit() \
        else result_modulus.insert(0, error_message_general)
    if number_2 == 0.0:
        result_modulus.insert(0, error_message_zero) if number_2 == 0.0 else number_2
    else:
        result = number_1 % number_2
        result = int(result) if result.is_integer() else result
        result_modulus.insert(0, str(result))


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
result_sum = Entry(root, width=10, textvariable=value_result)
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
result_subtract = Entry(root, width=10, textvariable=value_result)
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
result_multiplication= Entry(root, width=10, textvariable=value_result)
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
result_exponentiation = Entry(root, width=10, textvariable=value_result)
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
result_division = Entry(root, width=10, textvariable=value_result)
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
result_floor_division = Entry(root, width=10, textvariable=value_result)
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
result_modulus = Entry(root, width=10, textvariable=value_result)
result_modulus.grid(column=4, row=row_num)

root.mainloop()
