# ex 1 

# exponenta = 0
# number = 2
# while exponenta <= 15: 
#     print(number**exponenta)
#     exponenta = exponenta + 1



# ex 2 

# import random
# line = ''
# counter = 0
# 
# while counter < 6:
#     line= f"{line}{random.randrange(0,7)} {random.randrange(0,7)}, "
#     counter += 1
# print(line.strip(' ,'))


# ex 3 

# import random
# uniq_line = set()
# 
# while len(uniq_line) < 5:
#     # uniq_line.add(random.randrange(-2, 3))
#     uniq_line.add(random.randint(-2, 3))
#     # exit()
# 
# print(uniq_line)

# ex 3 v2
# import random
# uniq_line = []
# while len(uniq_line) < 5:
#     random_number = random.randint(-2, 3)
#     uniq_line.append(random_number) if not uniq_line.count(random_number) else None
# print(uniq_line)

# ex. 4
# total = 100
# while total > 0:
#     n = int(input("Pls input number: "))
#     if total - n >= 0:
#         total = total - n
#     else:
#         print("Cant do operation")
#         break
#     print(total)
# print("Reached the limit")

# ex 4.1
# total = 100
# user_number = 0
# 
# while total - user_number >= 0:
#     total = total - user_number
#     print(total)
#     user_number = int(input("Pls input number: "))
# print("Operation is failed. Total should be positive")
u