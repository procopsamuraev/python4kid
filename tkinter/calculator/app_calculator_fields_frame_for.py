from tkinter import *            
error = "Enter numbers only0"
error_zero = "Enter numbers only and not 0"

# list_signs = ['+', '-', '*', '**', '/','//', '%']
# list_descriptions = ['Sum', 'Subtract', 'Multiplication', 'Exponentiation', 'Division', 'Floor Division', 'Modulus']
list_signs = ['+ Sum', '- Subtract', '* Multiplication', '** Exponentiation', '/ Division','// Floor_Division', '% Modulus']
list_signs = ['+ Sum', '+ Sum']


def sum_numbers(row):
    index_element = row*3
    value_clean_1 = list_widgets[index_element].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[index_element+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    result = str(float(value_clean_1) + float(value_clean_2)) if number_1_true and number_2_true else error
    list_widgets[index_element+2].delete(0, END)
    list_widgets[index_element+2].insert(0, result.rstrip("0").removesuffix("."))


def subtract_numbers(row):
    index_element = row*3
    value_clean_1 = list_widgets[index_element].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[index_element+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    result = str(float(value_clean_1) - float(value_clean_2)) if number_1_true and number_2_true else error
    list_widgets[index_element+2].delete(0, END)
    list_widgets[index_element+2].insert(0, result.rstrip("0").removesuffix("."))


def multiplication_numbers(row):       
    index_element = row*3
    value_clean_1 = list_widgets[index_element].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[index_element+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    numbers_true = number_1_true and number_2_true
    result = str(float(value_clean_1) * float(value_clean_2)) if numbers_true else error
    list_widgets[index_element+2].delete(0, END)
    list_widgets[index_element+2].insert(0, result.rstrip("0").removesuffix("."))


def exponentiation_numbers(row):
    index_element = row*3
    value_clean_1 = list_widgets[index_element].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[index_element+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    numbers_true = number_1_true and number_2_true
    result = str(float(value_clean_1) ** float(value_clean_2)) if numbers_true else error
    list_widgets[index_element+2].delete(0, "end")                                                 
    list_widgets[index_element+2].insert(0, result.rstrip("0").removesuffix("."))
                                                                                           

def division_numbers(row):       
    index_element = row*3
    value_clean_1 = list_widgets[index_element].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[index_element+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    numbers_true = number_1_true and number_2_true and int(value_clean_2) != 0
    result = str(float(value_clean_1) / float(value_clean_2)) if numbers_true else error_zero
    list_widgets[index_element+2].delete(0, "end")                                                       
    list_widgets[index_element+2].insert(0, result.rstrip("0").removesuffix("."))
                                             
                                             
def floor_division_numbers(row):                                                              
    index_element = row*3
    value_clean_1 = list_widgets[index_element].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[index_element+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit() 
    numbers_true = number_1_true and number_2_true and int(value_clean_2) != 0
    result = str(float(value_clean_1) // float(value_clean_2)) if numbers_true else error_zero
    list_widgets[index_element+2].delete(0, "end")                                                       
    list_widgets[index_element+2].insert(0, result.rstrip("0").removesuffix("."))
                                             
                                                                                           
def modulus_numbers(row):                                                                     
    index_element = row*3
    value_clean_1 = list_widgets[index_element].get().replace(" ", "").replace(",", ".")
    number_1_true = value_clean_1.removeprefix("-").replace(".", "", 1).isdigit()
    value_clean_2 = list_widgets[index_element+1].get().replace(" ", "").replace(",", ".")
    number_2_true = value_clean_2.removeprefix("-").replace(".", "", 1).isdigit()
    number_2_zero = value_clean_2.find("0") != -1 and len(value_clean_2.removeprefix("-").strip("0")) < 2
    numbers_true = number_1_true and number_2_true and not number_2_zero
    result = str(float(value_clean_1) % float(value_clean_2)) if numbers_true else error_zero
    list_widgets[index_element+2].delete(0, "end")                                                       
    list_widgets[index_element+2].insert(0, result.rstrip("0").removesuffix("."))


root = Tk()
root.title("Ex_1.1")
list_functions = {'+':sum_numbers, '-':subtract_numbers,'*': multiplication_numbers, '**':exponentiation_numbers, '/':division_numbers, '//':floor_division_numbers, '%':modulus_numbers}
list_widgets = [] 

for index in range(len(list_signs)):
    sign_operation = list_signs[index].split()[0]
    sign_description = list_signs[index].split()[-1]
    frame = LabelFrame(text=sign_description)
    frame.pack(side='top')
    entry = Entry(frame, width=5)
    entry.pack(side=LEFT)
    list_widgets.append(entry)
    Label(frame, text=sign_operation).pack(side=LEFT)
    entry = Entry(frame, width=5)
    entry.pack(side=LEFT)
    list_widgets.append(entry)
    Button(frame, text='=', command= lambda row = index :list_functions.get(sign_operation)(row)).pack(side=LEFT)
    entry = Entry(frame, width=10)
    entry.pack(side=LEFT)
    list_widgets.append(entry)

root.mainloop()
