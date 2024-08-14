# number_1 = 14
# number_2 = -10
# number_3 = 12.5
# result = number_2 + number_3
# print('1\tM', 5 + 7)
# print('2\tL', number_1 < 7)
# print('3\tL', number_1 - number_2 > number_3)
# print('4\tM', -8 + number_1)
# print('5\tM', number_2 - number_3)
# print('6\tL', number_1 >= 14)
# print('7\tL', result != 4)
# print('8\tM', result - number_3)
# print('9\tM', 4 + number_2)
# print('10\tL', result + 10 == - number_2)


# number_1 = "14"
# number_2 = -10
# number_3 = 12.5
# result = number_2 + number_3
# print(5 > 7)
# # print(number_1 - number_2 > number_3)
# # print(- 8 <= number_1)
# print(number_2 != number_3)
# # print(number_1 >= 14)
# print(result != 4)
# # print(result < number_1)
# # print("4" > number_2)
# print(result + 10 == - number_2)
# print(number_1 == - number_2 + 4)


#4
# input_year = input("Enter year: ")
# print("Year is", 2024 == int(input_year))


#5
# input_1 = input("Enter 1st number: ")
# input_2 = input("Enter 2nd number: ")
# print("Is the 1st number more then the 2nd number:", int(input_1)>int(input_2))


#7
# input_1 = input("Enter 1st number,positive: ")
# input_2 = input("Enter 2nd number, negative: ")
# input_3 = input(f"Enter your answer {input_1}+{input_2}: ")
# result = int(input_1)+int(input_2)
# print("Answer:", result == int(input_3), "Correct value is:", result)

# print('15' <= '17')     # True
# print('5' > '7')        # False
# print('15' > '7')       # False
# print('415' > '45')     # False
# print('75' > '48')      # True
# print('1' <= 's')       # True
# print('a' >= 'b')       # False
# print('b' != 'B')       # True
# print('LOL' == 'lol')

# for i in range(1106):
#     if chr(i).isprintable():
#         print(chr(i), end='')


for i in range(206):
    if chr(i).isprintable():
        print(f'{i} {chr(i)}\t\t{i+150} {chr(i+150)}\t\t{i+300} {chr(i+300)}'
              f'\t\t{i+450} {chr(i+450)}\t\t{i+600} {chr(i+600)}'
              f'\t\t{i+750} {chr(i+750)}\t\t{i+900} {chr(i+900)}')