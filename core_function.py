# 3
"""
def func_a():
    print("Step 7", end=" ")

def func_b():
    print("Step 3", end=" ")

def func_c():
    print("Step 4", end=" ")

def func_d():
    print("Step 1", end=" ")

def func_e():
    print("Step 6", end=" ")

func_d()
# print(func_d)
# print(func_e)
print("Step 2", end=" ")
func_b()
func_c()
print("Step 5", end=" ")
func_e()
func_a()

#5 sdelat
"""

"""
# kupi slona

def make_conversation():
    answer = input(f'{name_2} - ').capitalize()
    return f'{message_generic} "{answer}", no ty {message_repeated}' if answer else f'{message_silent}'


name_1 = input("Please, enter the 1st person's name: ").strip().title()
name_2 = input("Please, enter the 2nd person's name: ").strip().title()
exit("Names should not be empty") if not (name_1 and name_2) else None
# exit("Names should not be empty") if not name_1 or not name_2 else None
name_1 = f'{name_1}:'
name_2 = f'{name_2}:'
padding = len(name_1) if len(name_1) >= len(name_2) else len(name_2)
message_repeated = f'kupi slona!'
message_generic = f'{name_1.ljust(padding)} - Everyone says:'
message_silent = f'{name_1.ljust(padding)} - Everyone is silent, but you {message_repeated}'

print(f'{name_1.ljust(padding)} - {message_repeated.title()}')
iteration = 0
while iteration < 5:
    print(make_conversation())
    iteration += 1
# iteration could be replaced with just "i"

"""


# 7  Order if the function doesnt matter -  as long as they defined before function call


def negative(n):
    print("Negative")


def test():
    number_int = input("Enter integer: ")
    exit("Zero is not positive and not negative") if int(number_int) == 0 else None
    positive(number_int) if int(number_int) > 0 else negative(number_int)


def positive(n):
    print("Positive")


test()
