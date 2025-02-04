import random 
# ex1
"""
Используя функцию randrange() получите псевдослучайное четное число в пределах от 6 до 12.
Также получите число кратное пяти в пределах от 5 до 100.
`"""
# print(random.randrange(6, 13, 2))
# print(random.randrange(5, 101, 5))

# ex2 
"""
Напишите программу, которая запрашивает у пользователя границы диапазона и какое число: 
целое или дробное, он хочет получить. Выводит на экран подходящее случайное число.

Enter the number from: -3
Enter the number to: 10
Enter number '1' - integer or 2 - float: 2
-3.45
"""

# number_from = float(input("Enter the number from: "))
# number_to = float(input("Enter the number to: "))
# number_type = int(input("Enter number '1' - for integer or '2' for float: "))
# print(number_from, number_to, number_type)
# 
# number_random = random.random()*(number_to - number_from)+number_from
# if number_type  == 1: 
#     print(int(number_random))
# elif number_type == 2:
#     print(float(number_random))
# else: 
#     print(f"type '1' or '2'")


# ex3
# print(int(random.random()*(7-0)+0))
# print(int(random.random()*(30-10)+10))
# print(int(random.random()*(14)-7))
# print( int((random.random()*(10)+1)//2*2) )
# print( int((random.random()*(25))//3*3) )
# print( int((random.random()*(40-20)+20)//4*4) )
# print( int((random.random()*(40)-40)//5*5) )
# print( int((random.random()*(10+14)-14)//2*2) )
# генератор дробных чисел в диапазоне от 0 до 4.5 с шагом 0.5;
# print( random.random()*(4.5)//0.5*0.5 )
# print( random.random()*(45)//5*5/10 )
# генератор дробных чисел в диапазоне от 7 до 21 с шагом 0.25;
# print( (random.random()*(2100-700)+700)//20*25/100 )
# генератор дробных чисел в диапазоне от -2.5 до 2.5 с шагом 1.25;
# print( (random.random()*(250+250)-250)//125*125/100 )
# print( (random.random()*(250+250)-250)//125*125/100 )


# ex4 
from tkinter import *
from tkinter.ttk import *

# def calculate_random(x0, x1, y):
    # return random.random()*((x1-x0)+x0)//y*y
# fix inclide still doesnt work, checks and try linear if on 66-68 str


def check_user_input(number_from, number_to, number_step):
    warning = ''
    if not number_from.replace('.', '', 1).removeprefix('-').isdigit():
        warning=f"{warning} Warning in field from"
    if not number_to.replace('.', '', 1).removeprefix('-').strip().isdigit():
        warning=f"{warning} Fill up: 'Number to'"
    if not number_step.replace('.', '').replace('-', '').isdigit():
        warning=f"{warning} Fill up 'Step'"
    return warning


def generate_number():
    number_from = entry_from.get().replace(',', '.').strip()
    number_to = entry_to.get().replace(',','.')
    number_step = entry_step.get().replace(',','.')
    report_error = check_user_input(number_from, number_to, number_step)
    label_warning.config(text=report_error)
    if not report_error: 
        number_from, number_to, number_step = float(number_from), float(number_to), float(number_step)
        number_range = number_to - number_from + number_step
        number_random = (random.random()*number_range+number_from)//number_step*number_step
        label_result.config(text=f"Result: { str(number_random).removesuffix('.0') } ")


root=Tk()
Label(text = 'Random number generator').grid(column=1, columnspan=8, row=1)
Label(text = 'From: ').grid(column=1, row=2)
entry_from = Entry()
entry_from.insert(0, '5')
entry_from.grid(column=2, row=2)
Label(text = 'To: ').grid(column=3, row=2)
entry_to = Entry()
entry_to.insert(0, '10')
entry_to.grid(column=4, row=2)
Label(text = 'Step: ').grid(column=5, row=2)
entry_step = Entry()
entry_step.insert(0, '1')
entry_step.grid(column=6, row=2)
Button(text = '    Generate    \nrandom number' , command=generate_number ).grid(column=7, row=2)
label_result = Label(text='Result:   ')
label_result.grid(column=8, row=2)
label_warning= Label()
label_warning.grid(column=1, columnspan=7, row=3)
root.mainloop()