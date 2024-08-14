"""Напишите напишите программу, которая спрашивает "What day of week is it?" и выводит True - если название введенного дня существует, и False - если такого дня нет. Реализовать необходимо корректность проверки для любого типа ввода (sunday, Sunday, SUNDAY, SunDay и т.п) для любого дня недели."""

# day = input("Input day of the week : ").casefold().replace(" ", "")
# day = f" {day} "
# all_days = " monday tuesday sunday ".casefold()
# print(day in all_days)

# true:
#
# false: "space" and no i - "",
# month = input("What month is your vacation? Enter: ").casefold().replace(" ", "")
# month = f" {month} "
# all_months = " january february march april may june july august september october december ".casefold()
# result = month in all_months
# message = str(result).replace("True", "Why not").replace("False", "Incorrect month entered")
# message = str(result).replace("False", "Incorrect input, no such month")
# print(message)

"""4 Напишите напишите программу, которая просит "Enter your login to register: "

выводит "Congratulations! You are registered." при условии True - если такого имени нет.
выводит "This login already exists" при условии False - если название введенного имени существует,
реализовать необходимо корректность проверки для любого типа ввода (Log, lOG, LOG и т.п) для любого имени.
строка с исходными именами может быть следующая: "log, login, pass, password" и т.п."""

# login = input("Enter your login: ").casefold().replace(",", "").strip(" ")
# logins_db = ",log,login,password,"
# login = f",{login},"
# result = login not in logins_db
# print(str(result).replace("True", "Congratulations").replace("False", "Login Exists"))
#
# True: "sword", "in"
# False: " ", "","log"


#
# String check methods
#
""" 1  Напишите программу, которая будет определять характеристики строки. Программа запрашивает на ввод строку и далее определяет соответствие строки указанным параметрам:
состоит из цифр и разных букв,
только из разных букв,
только из цифр,
из строцных букв,
из прописных букв,
из пробелов,
строка заголовок """

current_string = "2222ssdfsssssss"
current_string = "AAA BBB 122"
current_string = " "
tabs = "\t\t\t"
# print(f'String "{current_string}" contains numbers and letters:\t{current_string.isalnum()}'),
# print(f'String "{current_string}" contains only letters:{tabs}{current_string.isalpha()}'),
# print(f'String "{current_string}" contains only number:{tabs}{current_string.isdecimal()}'),
# print(f'String "{current_string}" contains only lower:{tabs}{current_string.islower()}'),
# print(f'String "{current_string}" contains only upper:{tabs}{current_string.isupper()}'),
# print(f'String "{current_string}" contains only spaces:{tabs}{current_string.isspace()}')
# print(f'String "{current_string}" is formated as title:{tabs}{current_string.istitle()}')
# All False: ""

# 2


def exersize_2(current_string):
    print(f'String "{current_string}" are {str(current_string.isalnum()).replace("True","").replace("False","not ")}numbers and letters'),
    print(f'String "{current_string}" does {str(current_string.isalpha()).replace("True", "").replace("False", "not ")}contain only letters'),
    print(f'String "{current_string}" does {str(current_string.isdecimal()).replace("True", "").replace("False", "not ")}contains only number'),
    print(f'String "{current_string}" does {str(current_string.islower()).replace("True", "").replace("False", "not ")}contains only lower'),
    print(f'String "{current_string}" {str(current_string.isupper()).replace("True", "").replace("False", "not ")}contains upper case latters'),
    print(f'String "{current_string}" is {str(current_string.isspace()).replace("True", "").replace("False", "not ")}only spaces')
    print(f'String "{current_string}" is {str(current_string.istitle()).replace("True", "").replace("False", "not ")}formated as title')

# exersize_2(current_string)
list_strings = ("111", "1 UPPER","lower", "    ", "UPPERlower","Diffrent symblols 1", "")
list_strings=("111", "00", "1 000")
list_strings = ("AA", "A A", " AAA ") # A3 - false
list_strings = ("aa", "a a", " aaa ") # a3 - false
list_strings = (" ", " ", "   ")
list_strings = ("A3", "a3", "aA", " Aa3 ") # true for different symbols
list_strings = ("22", "avbdsd", "a2", " Aa3 ") # false

# list_strings = ("A3",)
# list_strings=("111",)
for user_string in list_strings:
    message = ""
    message += str(user_string.isspace()).replace("True", "only spaces.").replace("False", "")
    message += str(bool(user_string)).replace("True", "").replace("False", "is empty.")
    user_string1 = str(user_string).replace(" ", "")
    message += str(user_string1.isdigit()).replace("True", "contains only numbers.").replace("False", "")
    message += str(user_string1.isupper()).replace("True", "is upper case letters.").replace("False", "")
    message += str(user_string1.isalpha() and user_string1.islower()).replace("True", "is lower case letters.").replace("False", "")
    message += str(user_string1.isalnum() and not ( user_string1.isdigit() or user_string1.isupper() or user_string1.islower())).replace("True", "different symbols.").replace("False", "")
    # print((user_string1.isalpha(), user_string1.isdigit()),(user_string1.isupper(), user_string1.islower()))
    # message += str(bool(message)).replace("True", "").replace("False", "has no matches.") # ne bylo v zadache
    # print(f"The string '{user_string}' {message}")


list_strings = ("UPPER lower", "lower letter", "UPPER LETTER", "UP lower 123", "  ", "", )
for user_string in list_strings:
    message = ""
    message += str(not user_string.isspace()).replace("True", " not only spaces").replace("False","")
    user_string1 = str(user_string).replace(" ", "")
    message += str(user_string1.isdecimal()).replace("True", "").replace("False"," not only digits")
    message += str(not user_string1.isupper()).replace("True", " not upper").replace("False","")
    message += str(not user_string1.islower()).replace("True", " not lower").replace("False","")

    print(f"The string '{user_string}'{message}")

""" results:
The string 'HA' not only digits not lower not only spaces
The string '111' not upper not lower not only spaces
The string '1 UPPER' not only digits not lower not only spaces
The string 'lower' not only digits not upper not only spaces
The string '    ' not only digits not upper not lower
The string 'UPPERlower' not only digits not upper not lower not only spaces
The string 'UPPERlower 1' not only digits not upper not lower not only spaces
The string '' not only digits not upper not lower not only spaces
"""

# convert user input to int. if cant convert - error
# day = "1sd"
# check = str(day.isdecimal()).replace("True", day).replace("False","")
# print(bool(check))
#
# print(type(check))
# print(bool(day))
# message = print(str(bool(int((day))))
# print(1 < day and day < 12)