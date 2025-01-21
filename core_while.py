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

import random
uniq_line = set()

while len(uniq_line) < 5:
    uniq_line.add(random.randrange(-2, 3))
    # exit()

print(uniq_line)