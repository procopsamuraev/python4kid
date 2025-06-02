# file_read = open("core_file/data.txt")
# print(file_read.read(10))
# print(file_read.read(2))
# print(file_read.read())
# print(file_read.read())
# print(type(file_read.read()))
# print(file_read.readline())
# print(file_read.readlines())
# for line in open('core_file/data.txt'):
    # print(line)
# numbers = []
# for line in open('core_file/data.txt'):
#     numbers.append(line.strip())
# print(numbers)
# 


# ex1
# list_numbers = []
# sum_numbers = 0
# for line in open('core_file/numbers_new.txt'):
#     line:str = line.split()
#     if line:
#         list_numbers.extend(line) if line else list_numbers
# 
# for number in list_numbers:
#     if number.replace('-', '').isdigit():
#         sum_numbers += int(number)
#     
# print(sum_numbers) # 1161
# 

# ex2
# list_numbers = []
# sum_numbers = 0
# for line in open('core_file/goods.txt'):
#     line = line.strip().split('-')[1:]
#     if line: 
#         list_numbers.extend(line) if line else list_numbers
# for number in list_numbers:
#     number = number.replace(' ', '').replace(',', '.')
#     if number.replace('.','').isdigit():
#         # print(float(number))
#         sum_numbers += float(number)
# print(round(sum_numbers, 2)) # 48340.98


# ex3 
list_questions=[]

for line in open('core_file/questions.txt'):
    line = line.strip()
    if line.startswith('.',1,2):
        print(line)