# a = [12, 3.85, "black", -4]
# print(a)
# a.append('wood')
# print(a)                # [12, 3.85, 'black', -4, 'wood']
# 
# a.insert(1, 'circle')
# print(a)                # 12, 'circle', 3.85, 'black', -4, 'wood']
# 
# a.remove(-4)
# print(a)                # [12, 'circle', 3.85, 'black', 'wood']
# 
# print(a.pop())          # 'wood'
# print(a)                # [12, 'circle', 'black', -4]
# print(a.pop(2))         # '3.85'
# print(a)                # [12, 'circle', 'black']
# dir(list)


# ex1
# three_numbers=[]
# three_numbers.append(float(input("Enter 1st num:")))
# three_numbers.append(float(input("Enter 2nd num:")))
# three_numbers.append(float(input("Enter 3rd num:")))
# print(three_numbers)
# print(f"Sum: {sum(three_numbers)}")
# print(f"Max: {max(three_numbers)}")
# print(f"Min: {min(three_numbers)}")


# ex2
# a, b  = 54, 87
# two_numbers = []
# two_numbers.append(a)
# two_numbers.append(b)
# print(f"Sum of {a} and {b} = {sum(two_numbers)}")
# print(f"Max of {a} and {b} = {max(two_numbers)}")
# print(f"Mim of {a} and {b} = {min(two_numbers)}")


# ex3

# import random
# list_of_numbers = []
# i = 0
# while i < 30:
#     list_of_numbers.append(random.randint(0,99))
#     i += 1
# print(f"Original:\n{list_of_numbers[0:9]}\n{list_of_numbers[10:19]}\n{list_of_numbers[20:29]}")
# list_of_numbers.sort()
# print(f"Sorted:\n{list_of_numbers[0:9]}\n{list_of_numbers[10:19]}\n{list_of_numbers[20:29]}")


# fix methods of lists
list_test = ['n1', 'n2', 'n3', 'n4']
# list_test.append('n5')
# list_test.clear()
# b = list_test.copy()
# print(b)
# print(list_test.count('n1')) 
list_test.extend('bbb')
# ['n1', 'n2', 'n3', 'n4', 'b', 'b', 'b']
# print(list_test.index('b'))
list_test.insert(4, 'a')
# ['n1', 'n2', 'n3', 'n4', 'a', 'b', 'b', 'b']
print(list_test.pop(4))
#a
# ['n1', 'n2', 'n3', 'n4', 'b', 'b', 'b'] 
list_test.remove('b')
# ['n1', 'n2', 'n3', 'n4', 'b', 'b']
list_test.reverse()
# ['b', 'b', 'n4', 'n3', 'n2', 'n1']
list_test.sort()
list_test.count
# ['b', 'b', 'n1', 'n2', 'n3', 'n4']
print(list_test)