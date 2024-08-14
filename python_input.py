# user_name = input("Your name: ")
# user_last_name = input("Your last name: ")
# print("You are welcome {0} {1}." .format(user_name, user_last_name))

input_1 = input("Enter 1st number: ")
input_2 = input("Enter 2nd number: ")
input_3 = input("Enter 3rd number: ")
input_4 = input("Enter 4th number: ")

for user_input in input_1, input_2, input_3, input_4:
    if user_input.isdigit():
        user_input = int(user_input) # why didnt work?
    else:
        print(user_input + " - Wrong input,  input should be digits only")
        break
sum12 = int(input_1) + int(input_2)
sum34 = int(input_3) + int(input_4)
print("Sum input_1 and input_2 = " + str(sum12))
print("Sum input_3 and input_4 = " + str(sum34))
print("Division of sums equals", sum12/sum34)


