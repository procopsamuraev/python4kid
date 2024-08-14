# 1
# line = input("Enter anything: ")
# if line:
#     print("OK")
# if bool(line):
#      print("OK")


# 2
# line = input("Enter number: ")
# if int(line) > 0:
#     print("1")
# elif int(line) < 0:
#     print("-1")
# 0 : -1
# "" error

# 3 What time is it
# time_user = int(input("What time is it[0-23]?: "))
# # time_user = int(time_user)
# if 4 <= time_user <= 11:
#     print("Good morning")
# elif 12 <= time_user <= 16:
#     print("Good afternoon")
# elif 17 <= time_user <= 22:
#     print("Good evening")
# elif 23 == time_user or 0 <= time_user <= 3:
#     print("Good night!")
# else:
#     print("Enter should be in range 0-23")
#
# 0, 23 - Good night
# -1, 25 : False
# "sdf" : error


# kupi slona

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
    answer = input(f'{name_2} - ').capitalize()
    print(f'{message_generic} "{answer}", no ty {message_repeated}') if answer else print(f'{message_silent}')
    iteration += 1
# iteration could be replaced with just "i"

