from tkinter import *            
error = "Enter numbers only0"
error_zero = "Enter numbers only and not 0"


def sum_numbers():
    i = 0
    value_clean_1 = list_widgets[i].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[i+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    result = str(float(value_clean_1) + float(value_clean_2)) if number_1_true and number_2_true else error
    list_widgets[i+2].delete(0, END)
    list_widgets[i+2].insert(0, result.rstrip("0").removesuffix("."))


def subtract_numbers():
    i = 3
    value_clean_1 = list_widgets[i].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[i+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    result = str(float(value_clean_1) - float(value_clean_2)) if number_1_true and number_2_true else error
    list_widgets[i+2].delete(0, END)
    list_widgets[i+2].insert(0, result.rstrip("0").removesuffix("."))


def multiplication_numbers():       
    i = 6
    value_clean_1 = list_widgets[i].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[i+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    numbers_true = number_1_true and number_2_true
    result = str(float(value_clean_1) * float(value_clean_2)) if numbers_true else error
    list_widgets[i+2].delete(0, END)
    list_widgets[i+2].insert(0, result.rstrip("0").removesuffix("."))


def exponentiation_numbers():
    i = 9
    value_clean_1 = list_widgets[i].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[i+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    numbers_true = number_1_true and number_2_true
    result = str(float(value_clean_1) ** float(value_clean_2)) if numbers_true else error
    list_widgets[i+2].delete(0, "end")                                                 
    list_widgets[i+2].insert(0, result.rstrip("0").removesuffix("."))
                                                                                           
                                                                                           
def division_numbers():       
    i =  12
    value_clean_1 = list_widgets[i].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[i+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    numbers_true = number_1_true and number_2_true and int(value_clean_2) != 0
    result = str(float(value_clean_1) / float(value_clean_2)) if numbers_true else error_zero
    list_widgets[i+2].delete(0, "end")                                                       
    list_widgets[i+2].insert(0, result.rstrip("0").removesuffix("."))
                                             
                                             
def floor_division_numbers():                                                              
    i = 15
    value_clean_1 = list_widgets[i].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[i+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit() 
    numbers_true = number_1_true and number_2_true and int(value_clean_2) != 0
    result = str(float(value_clean_1) / float(value_clean_2)) if numbers_true else error_zero
    list_widgets[i+2].delete(0, "end")                                                       
    list_widgets[i+2].insert(0, result.rstrip("0").removesuffix("."))
                                             
                                                                                           
def modulus_numbers():                                                                     
    i = 18
    value_clean_1 = list_widgets[i].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[i+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    number_2_zero = value_clean_2.find("0") != -1 and len(value_clean_2.removeprefix("-").strip("0")) < 2
    numbers_true = number_1_true and number_2_true and not number_2_zero
    result = str(float(value_clean_1) % float(value_clean_2)) if numbers_true else error_zero
    list_widgets[i+2].delete(0, "end")                                                       
    list_widgets[i+2].insert(0, result.rstrip("0").removesuffix("."))


root = Tk()
root.title("Ex_1")
list_signs = ['+', '-', '*', '**', '/','//', '%']
list_functions = [sum_numbers, subtract_numbers, multiplication_numbers, exponentiation_numbers, division_numbers, floor_division_numbers, modulus_numbers]
list_widgets = [] 

i = 0
while i < len(list_signs):
    entry = Entry(root, width=5)
    entry.grid(column=0, row=i)
    list_widgets.append(entry)
    Label(root, text=list_signs[i]).grid(column=1, row=i)
    entry = Entry(root, width=5)
    entry.grid(column=2, row=i)
    list_widgets.append(entry)
    Button(root, text='=', command=list_functions[i]).grid(column=3, row=i)
    entry = Entry(root, width=10)
    entry.grid(column=4, row=i)
    list_widgets.append(entry)
    i += 1

root.mainloop()
