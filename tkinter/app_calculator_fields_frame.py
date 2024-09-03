from tkinter import *            
error = "error"


def calculation_numbers(number_1, number_2, operation, value_result):
    value_clean_1 = number_1.get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = number_2.get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    if operation == "+":
        result = str(float(value_clean_1) + float(value_clean_2)) if number_1_true and number_2_true else error
    elif operation == "-":
        result = str(float(value_clean_1) - float(value_clean_2)) if number_1_true and number_2_true else error
    elif operation == "*":
        result = str(float(value_clean_1) * float(value_clean_2)) if number_1_true and number_2_true else error
    elif operation == "**":
        result = str(float(value_clean_1) ** float(value_clean_2)) if number_1_true and number_2_true else error
    elif operation == "/":
        number_2_zero = value_clean_2.find("0") != -1 and len(value_clean_2.removeprefix("-").strip("0")) < 2
        number_2_true = number_2_true and not number_2_zero
        result = str(float(value_clean_1) / float(value_clean_2)) if number_1_true and number_2_true else error
    elif operation == "//":
        number_2_zero = value_clean_2.find("0") != -1 and len(value_clean_2.removeprefix("-").strip("0")) < 2
        number_2_true = number_2_true and not number_2_zero
        result = str(float(value_clean_1) // float(value_clean_2)) if number_1_true and number_2_true else error
    elif operation == "%":
        number_2_zero = value_clean_2.find("0") != -1 and len(value_clean_2.removeprefix("-").strip("0")) < 2
        number_2_true = number_2_true and not number_2_zero
        result = str(float(value_clean_1) % float(value_clean_2)) if number_1_true and number_2_true else error
    value_result.set(result.rstrip("0").removesuffix("."))


"""
def sum_numbers():
    value_clean_1 = value_sum_1.get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = value_sum_2.get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    result = str(float(value_clean_1) + float(value_clean_2)) if number_1_true and number_2_true else error
    value_result_sum.set(result.rstrip("0").removesuffix("."))

                                             
def subtract_numbers():             
    result_subtract.delete(0, "end")                                                       
    value_clean_1 = value_subtract_1.get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = value_subtract_2.get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    numbers_true = number_1_true and number_2_true
    result = str(float(value_clean_1) - float(value_clean_2)) if numbers_true else error
    result_subtract.insert(0, result.rstrip("0").removesuffix("."))

                                             
def multiplication_numbers():       
    result_multiplication.delete(0, "end")                                                 
    value_clean_1 = value_multiplication_1.get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = value_multiplication_2.get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    numbers_true = number_1_true and number_2_true
    result = str(float(value_clean_1) * float(value_clean_2)) if numbers_true else error
    result_multiplication.insert(0, result.rstrip("0").removesuffix("."))
                                                                                           
                                             
def exponentiation_numbers():
    result_exponentiation.delete(0, "end")                                                 
    value_clean_1 = value_exponentiation_1.get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = value_exponentiation_2.get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    numbers_true = number_1_true and number_2_true
    result = str(float(value_clean_1) ** float(value_clean_2)) if numbers_true else error
    result_exponentiation.insert(0, result.rstrip("0").removesuffix("."))


def division_numbers():       
    result_division.delete(0, "end")                                                       
    value_clean_1 = value_division_1.get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = value_division_2.get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    numbers_true = number_1_true and number_2_true and int(value_clean_2) != 0
    result = str(float(value_clean_1) / float(value_clean_2)) if numbers_true else error_zero
    result_division.insert(0, result.rstrip("0").removesuffix("."))
                                             
                                             
def floor_division_numbers():                                                              
    result_floor_division.delete(0, "end")
    value_clean_1 = value_floor_division_1.get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = value_floor_division_2.get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit() 
    numbers_true = number_1_true and number_2_true and int(value_clean_2) != 0
    result = str(float(value_clean_1) / float(value_clean_2)) if numbers_true else error_zero
    result_floor_division.insert(0, result.rstrip("0").removesuffix("."))
                                             
                                                                                           
def modulus_numbers():                                                                     
    result_modulus.delete(0, "end")
    value_clean_1 = value_modulus_1.get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = value_modulus_2.get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    number_2_zero = value_clean_2.find("0") != -1 and len(value_clean_2.removeprefix("-").strip("0")) < 2
    numbers_true = number_1_true and number_2_true and not number_2_zero
    # line_check.removeprefix("-").replace(".", "", 1).replace("0", "", line_check.count("0") - 1) == "0"
    result = str(float(value_clean_1) % float(value_clean_2)) if numbers_true else error_zero
    result_modulus.insert(0, result.rstrip("0").removesuffix("."))
"""

root = Tk()
root.title("Ex_1")



frame_sum = LabelFrame(text="Sum")
frame_sum.pack(side="top")
value_sum_1 = StringVar()
field_sum_1 = Entry(frame_sum, width=5, textvariable=value_sum_1)
field_sum_1.pack(side="left")
label_field_sum = Label(frame_sum, text="+")
label_field_sum.pack(side="left")
value_sum_2 = StringVar()
field_sum_2 = Entry(frame_sum, width=5, textvariable=value_sum_2)
field_sum_2.pack(side="left")
button_sum = Button(frame_sum, text="=", command= lambda: calculation_numbers(value_sum_1, value_sum_2, "+", value_result_sum))
button_sum.pack(side="left")
value_result_sum = StringVar()
entry_result_sum = Entry(frame_sum, width=10, textvariable=value_result_sum)
entry_result_sum.pack(side="left")

frame_subtract = LabelFrame(text="Subtract")
frame_subtract.pack(side="top")
value_subtract_1 = StringVar()
field_subtract_1 = Entry(frame_subtract, width=5, textvariable=value_subtract_1)
field_subtract_1.pack(side="left")
label = Label(frame_subtract, text="-")
label.pack(side="left")
value_subtract_2 = StringVar()
field_subtract_2 = Entry(frame_subtract, width=5, textvariable=value_subtract_2)
field_subtract_2.pack(side="left")
button_subtract = Button(frame_subtract, text="=", command=lambda: calculation_numbers(value_subtract_1, value_subtract_2, "-", value_result_subtract))
button_subtract.pack(side="left")
value_result_subtract = StringVar()
entry_result_subtract = Entry(frame_subtract, width=10, textvariable=value_result_subtract)
entry_result_subtract.pack(side="left")

frame_multiplication = LabelFrame(text="Multiplication")
frame_multiplication.pack(side="top")
value_multiplication_1 = StringVar()
field_multiplication_1 = Entry(frame_multiplication, width=5, textvariable=value_multiplication_1)
field_multiplication_1.pack(side="left")
label = Label(frame_multiplication, text="*")
label.pack(side="left")
value_multiplication_2 = StringVar()
field_multiplication_2 = Entry(frame_multiplication, width=5, textvariable=value_multiplication_2)
field_multiplication_2.pack(side="left")
button_multiplication = Button(frame_multiplication, text="=", command=lambda: calculation_numbers(value_multiplication_1, value_multiplication_2, "*", value_result_multiplication))
button_multiplication.pack(side="left")
value_result_multiplication = StringVar()
entry_result_multiplication= Entry(frame_multiplication, width=10, textvariable=value_result_multiplication)
entry_result_multiplication.pack(side="left")

frame_exponentiation = LabelFrame(text="Exponentiation" )
frame_exponentiation.pack(side="top")
value_exponentiation_1 = StringVar()
field_exponentiation_1 = Entry(frame_exponentiation, width=5, textvariable=value_exponentiation_1)
field_exponentiation_1.pack(side="left")
label = Label(frame_exponentiation, text="**")
label.pack(side="left")
value_exponentiation_2 = StringVar()
field_exponentiation_2 = Entry(frame_exponentiation, width=5, textvariable=value_exponentiation_2)
field_exponentiation_2.pack(side="left")
button_equal = Button(frame_exponentiation, text="=", command=lambda: calculation_numbers(value_exponentiation_1, value_exponentiation_2, "**", value_result_exponentiation))
button_equal.pack(side="left")
value_result_exponentiation = StringVar()
result_exponentiation = Entry(frame_exponentiation, width=10, textvariable=value_result_exponentiation)
result_exponentiation.pack(side="left")

frame_division = LabelFrame(text="Division")
frame_division.pack(side="top")
value_division_1 = StringVar()
field_division_1 = Entry(frame_division, width=5, textvariable=value_division_1)
field_division_1.pack(side="left")
label = Label(frame_division, text="/")
label.pack(side="left")
value_division_2 = StringVar()
field_division_2 = Entry(frame_division, width=5, textvariable=value_division_2)
field_division_2.pack(side="left")
button_equal = Button(frame_division, text="=", command=lambda: calculation_numbers(value_division_1, value_division_2, "/", value_result_division))
button_equal.pack(side="left")
value_result_division = StringVar()
result_division = Entry(frame_division, width=10, textvariable=value_result_division)
result_division.pack(side="left")

frame_floor_division = LabelFrame(text="Floor Division")
frame_floor_division.pack(side="top")
value_floor_division_1 = StringVar()
field_floor_division_1 = Entry(frame_floor_division, width=5, textvariable=value_floor_division_1)
field_floor_division_1.pack(side="left")
label = Label(frame_floor_division, text="//")
label.pack(side="left")
value_floor_division_2 = StringVar()
field_floor_division_2 = Entry(frame_floor_division, width=5, textvariable=value_floor_division_2)
field_floor_division_2.pack(side="left")
button_equal = Button(frame_floor_division, text="=", command=lambda: calculation_numbers(value_floor_division_1, value_floor_division_2, "//", value_result_floor_division))
button_equal.pack(side="left")
value_result_floor_division = StringVar()
result_floor_division = Entry(frame_floor_division, width=10, textvariable=value_result_floor_division)
result_floor_division.pack(side="left")

frame_modulus = LabelFrame(text="Modulus")
frame_modulus.pack(side="top")
value_modulus_1 = StringVar()
field_modulus_1 = Entry(frame_modulus, width=5, textvariable=value_modulus_1)
field_modulus_1.pack(side="left")
label = Label(frame_modulus, text="%")
label.pack(side="left")
value_modulus_2 = StringVar()
field_modulus_2 = Entry(frame_modulus, width=5, textvariable=value_modulus_2)
field_modulus_2.pack(side="left")
button_equal = Button(frame_modulus, text="=", command=lambda: calculation_numbers(value_modulus_1, value_modulus_2, "%", value_result_modulus))
button_equal.pack(side="left")
value_result_modulus = StringVar()
result_modulus = Entry(frame_modulus, width=10, textvariable=value_result_modulus)
result_modulus.pack(side="left")

root.mainloop()
