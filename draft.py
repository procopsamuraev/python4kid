# a="1+123222=122"
# time_now = datetime.datetime()
# b=a.split("=").split("+")
# print(a.rsplit("=")[0])
# print(len(b))
# string = "1.59090"
string = "1500.55"
year = "1500.5"
# delimiters = ["+", "-", "*"]
# for delimiter in delimiters:
#     string = " ".join(string.split(delimiter))
# result = string.split()
# for numbers in result:
#     numbers = 1 if numbers.isdigit() else false
# if string.find("/"):
    # print(string.split('/')[1].replace("0","").strip("1234567890"))
    # a=string.split('/')[1].lstrip("0")
    # print(f"{a=}")
    # if a:
        # print(a.a[0].isdigit())
# print(a)
# print(f'{result=}')
# print(len(result))
# print(list(string))
# print(tuple(string))
# print(  not string[string.find('.')+1:].rstrip('0').replace('5', '', 1) if string.find('.') !=-1 else string.replace('.', '').isdigit() )
# print( not string.rsplit('.', )[-1].rstrip('0').replace('5', '', 1 ))
# print( not year[year.find('.')+1:].rstrip('0').replace('5', '', 1))
# Import package and it's modules 

# array = [
#   [0,1,2],
#   [2,1,2],
#   [0,1,0],
#  ] 
# for index_row, row in enumerate(array):
#     current_value = 0 
#     count_in_row = 0
#     for index_column, element in enumerate(row):
#         if index_column == 0 and  current_value == element and current_value: 
#             count_in_column +=1
#             current_value == element
        

# array_1d = [1,0,2,1,1, 1]
# # array_1d = [1,1,1,1,1]
# # array_1d = [2,2]
# flag = 0 
# current_value = array_1d[0]       
# for item in array_1d: 
#     if item and item != current_value:
#         break
#     else:
#         flag = item
#     current_value = item
# 
# print(flag)

# array_1d = [[1,1],[0,1],[2,2]]
# array_1d = [[1,1],[0,1],[2,1]]
# array_1d = [[0,1],[0,1],[0,1]]
array_1d = [[0,1],[0,2],[0,1]]

# array_1d = [[1],[1],[1]]
# flag = 0 
# current_value = array_1d[0][0]       
# for item in array_1d: 
#     if item[0] and item[0] != current_value :
#         break
#     else:
#         flag = item[0]
#     current_value = item[0]
# 
# print(flag)
# 
# flag = 0 
# current_value = array_1d[0][1]       
# for item in array_1d: 
#     if item[1] and item[1] != current_value :
#         break
#     else:
#         flag = item[1]
#     current_value = item[1]

# for x in range(len(array_1d[0])):
#     flag = 0 
#     current_value = array_1d[x][0]       
#     for item in array_1d: 
#         if item[x] and item[x] != current_value:
#             break
#         else:
#             flag = item[x]
#         current_value = item[x]
#     print(flag)


#import operator
#
#
#def sum_number(a,b):
#    return a+b
#
#def calculate(a,b, func):
#    return func(a,b)
#
#print(calculate(4,5, sum_number))
#print(calculate(4,5, operator.sub))
## Sample dictionary
#sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
a,b,c = 1,2,35
print(a,b,c)
list_numbers  = [a,b,c]
print(list_numbers)
print(*list_numbers)
a,b,c = [3,7,19]
print(a,b,c)
# a,b,c = *list_numbers
print(a,b,c)