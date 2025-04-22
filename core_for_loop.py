# print(range(5))
# print(list(range(0)))
# print(list(range(5)))
# print(list(range(-5, 5)))
# print(list(range(-5, 5, 3))) # [-5, -2, 1, 4]
# print(list(range(-9, 0, 2))) # [-9, -7, -5, -3, -1]
# print(list(range(-1, -10, -2))) # [-1, -3, -5, -7, -9] 
# print(list(range(-10, -1, -2))) # []
##
# for i in range(5):
#    print(i)
# for i in range(0):
#     print(i)
# for i in []:
#     print(i)
# for i in [1,2,3]:
    # print(i)
# list_numbers = [1,2,3]
# for i in list_numbers:
#    print(i)
# list_numbers = [1,2,3]
# for i in range(3):
#     print(list_numbers[i])
# list_numbers = [1,2,3,4,10,12]
# for index in range(len(list_numbers)):
#     print(list_numbers[index])
#
# list_numbers = [1,2,3,4,10,12]
# for number in list_numbers: 
#    print(number)


# string = '1a2b3c'
# list_chars = []
# for char in string:
#     list_chars.append(char)
# print(list_chars)
# # or
# list_chars= list(string)
# print(list_chars)

list_2d=[
    [1, 2 ,3],
    ['a', 'b', 'c']
]
# print(list_2d[0][0],list_2d[1][0])
# print(list_2d[0][1],list_2d[1][1])
# print(list_2d[0][2],list_2d[1][2])
# index = 0
# while index < len(list_2d[0]):
#     print(list_2d[0][index], list_2d[1][index])
#     index += 1  
# 
# for index in range(len(list_2d[0])):
#     print(list_2d[0][index], list_2d[1][index])
index=0
for line in list_2d: 
    print(line[index])
    index += 1

