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
# ]
# print(list_2d[0][0],list_2d[1][0])
# print(list_2d[0][1],list_2d[1][1])
# print(list_2d[0][2],list_2d[1][2])
# index = 0
# while index < len(list_2d[0]):
#     print(list_2d[0][index], list_2d[1][index])
#     index += 1  
# 
# for index in range(len(list_2d[0])):
    # print(list_2d[0][index], list_2d[1][index])

# for number list_2d:

#
#ex1
#
# list_numbers=[]
# for number in range(-20, 20, 3):
#     list_numbers.append(number)
# print(list_numbers) # [-20, -17, -14, -11, -8, -5, -2, 1, 4, 7, 10, 13, 16, 19]
# 
#ex2
# list_2 = list(range(0,100, 17))
# print(list_2) # [0, 17, 34, 51, 68, 85]

#ex3
# list_ex3 = [-2, -8, 0, 3, 100, -4]
# count_negative = 0 
# for number in list_ex3:
#     if number < 0:
#         count_negative += 1 
#         #if number < 0 else count_negative
# print(list_ex3, count_negative)

#ex4
# list_words=['yes', 'no', 'maybe', 'ok', 'what']
# list_count_alpha = []
# for word in list_words:
#     list_count_alpha.append(len(word))
# print(f"{list_words}\n{list_count_alpha}")

#ex5

#Q from tkinter import *
#Q list_eng = ['yes', 'no', 'maybe', 'ok', 'what']
#Q list_rus = ["да", "нет", "наверно", "ок", "что"]
#Q list_buttons = []
#Q 
#Q def translate_button(index):
#Q     text=list_rus[index]
#Q     list_buttons[index].config(text=text)
#Q 
#Q root = Tk()
#Q root.title("for loop ex5")
#Q for index in range(len(list_eng)):
#Q     text=list_eng[index]
#Q     button = Button(root, text=text, command=lambda index=index: translate_button(index))
#Q     button.pack()
#Q     list_buttons.append(button)
#Q root.mainloop()
#Q 