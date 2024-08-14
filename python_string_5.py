#
name = "Bob"
city = "LA"
age = 28.86
# #print("This is Bob. Bob lives in LA. Bob is 28.86 years old.")
# # print("This is", name, ".", name, "lives in", city, ".", name, "is", age, "years old", ".")
# print("This is ", name, ". ", name, " lives in ", city, ". ", name, " is ", age, " years old.", sep="")
# # print("This is ", name, ". ", name, " lives in ", city, ". ", name, " is ", int(age), " years old.", sep="")
# # print("This is ", name, ". ", name, " lives in ", city, ". ", name, " is ", round(age), " years old.", sep="")
# # print("This is ", name, ". ", name, " lives in ", city, ". ", name, " is ", round(age, 0), " years old.", sep="")
# # print("11 - This is ", name, ". ", name, " lives in ", city, ". ", name, " is ", age, " years old.", sep="")
# # can concat only strings, not int
# print('This is ' + name + '. ' + name + ' lives in ' + city + '. ' + name + ' is ' + str(age) + ' years old.')
# # print('This is ' + name + '. ' + name + ' lives in ' + city + '. ' + name + ' is ' + str(int(age)) + ' years old.')
# # print('This is ' + name + '. ' + name + ' lives in ' + city + '. ' + name + ' is ' + str(round(age)) + ' years old.')
# # print('This is ' + name + '. ' + name + ' lives in ' + city + '. ' + name + ' is ' + str(round(age,1)) + ' years old.')
# # % string
# # print('This is %s . %s lives in %s. %s is %s years old.')
# print('This is %s. %s lives in %s. %s is %s years old.' % (name, name, city, name, age))
# # print('This is %s. %s lives in %s. %s is %i years old.' % (name, name, city, name, age))
# # print('This is %s. %s lives in %s. %s is %f years old.' % (name, name, city, name, age))
# # print('This is %s. %s lives in %s. %s is %.3f years old.' % (name, name, city, name, age))
print('This is %s. %s lives in %s. %s is %.2f years old.' % (name, name, city, name, age))
# # print('This is %s. %s lives in %s. %s is %.0f years old.' % (name, name, city, name, age))
# # format string
# # print('This is {}. {} lives in {}. {} is {} years old.')
# # print('This is {}. {} lives in {}. {} is {} years old.'.format(name, name, city, name, age))
# # print('This is {0}. {1} lives in {2}. {3} is {4} years old.'.format(name, name, city, name, age))
# # print('This is {4}. {1} lives in {2}. {4} is {4} years old.'.format(name, name, city, name, age))
# print('This is {0}. {0} lives in {1}. {0} is {2} years old.'.format(name, city, age))
# # print('This is {0}. {0} lives in {1}. {0} is {2} years old.'.format(name, city, int(age)))
# # print('This is {0}. {0} lives in {1}. {0} is {2:f} years old.'.format(name, city, age))
# # print('This is {0}. {0} lives in {1}. {0} is {2:.1f} years old.'.format(name, city, age))
print('This is {0}. {0} lives in {1}. {0} is {2:.0f} years old.'.format(name, city, age))
print('This is {name}. {name} lives in {city}. {name} is {age} years old.')
# # f-string
# print(f'This is {name}. {name} lives in {city}. {name} is {age} years old.')
# print(f'This is {name}. {name} lives in {city}. {name} is {int(age)} years old.')
# print(f'This is {name}. {name} lives in {city}. {name} is {age:f} years old.')
# print(f'This is {name}. {name} lives in {city}. {name} is {age:.0f} years old.')


# line_0 = "This is Bob. Bob lives in LA. Bob is 28.86 years old."
# line_1 = "This is ", name, ". ", name, " lives in ", city, ". ", name, " is ", age, " years old."  # use only on print
# line_2 = 'This is ' + name + '. ' + name + ' lives in ' + city + '. ' + name + ' is ' + str(age) + ' years old.'  # not recommended to use! at all!
# line_3 = 'This is %s. %s lives in %s. %s is %s years old.' % (name, name, city, name, age)
# line_4 = 'This is {0}. {0} lives in {1}. {0} is {2} years old.'.format(name, city, age)
# line_5 = f'This is {name}. {name} lives in {city}. {name} is {age} years old.'  # best practise
# print(line_0)
# print(line_1)
# print(line_2)
# print(line_3)
# print(line_4)
# print(line_5)
# del line_5  # manual memory clean memory
# line_5 = f'{line_3} {line_4}'
# print(line_5)


# home work
# write letter to "ded moros" with all 5 methods.
# age = 33.5
# year = 2000
# gift = "bicycle"
# print("Dear Ded Moroz, I am 33.5 years old. I would like to a bicycle for the New Year 2000.")
# # print("Dear Ded Moroz, I am", age, "years old. I would like to a", gift , " for the New year", year, ".")
# # print("Dear Ded Moroz, I am ", age, " years old. I would like to a ", gift , " for the New year ", year, ".",sep = "")
# # print("Dear Ded Moroz, I am ", int(age), " years old. I would like to a ", gift , " for the New year ", year, ".",sep = "")
# # print("Dear Ded Moroz, I am ", round(age,0), " years old. I would like to a ", gift , " for the New year ", year, ".",sep = "")
# # print("Dear Ded Moroz, I am ", str(int(age)), " years old. I would like to a ", gift , " for the New year ", year, ".",sep = "")
# # print("Dear Ded Moroz, I am " + str(age) + " years old. I would like to a " + gift + " for the New year " + str(year) +".")
# # print("Dear Ded Moroz, I am " + str(int(age)) + " years old. I would like to a " + gift + " for the New year " + str(round(year,-5)) +".")
# # print("Dear Ded Moroz, I am %s years old. I would like to a %s for the New year %s." % (age, gift, year))
# # print("Dear Ded Moroz, I am %i years old. I would like to a %s for the New year %f." % (age, gift, year))
# # print("Dear Ded Moroz, I am {} years old. I would like to a {} for the New year {}.")
# # print('Dear Ded Moroz, I am {} years old. I would like to a {} for the New year {}.'. format(age, year, gift))
# # print('Dear Ded Moroz, I am {0} years old. I would like to a {1} for the New year {2}.'. format(age, year, gift))
# # print('Dear Ded Moroz, I am {0:f} years old. I would like to a {1} for the New year {2}.'. format(age, year, gift))
# # print('Dear Ded Moroz, I am {age} years old. I would like to a {gift} for the New year {year}.')
# # print('Dear Ded Moroz, I am {age} years old. I would like to a {gift} for the New year {year}.')
# # print(f'Dear Ded Moroz, I am {age:f} years old. I would like to a {gift} for the New year {year}.')
# # print(f'Dear Ded Moroz, I am {age:.0f} years old. I would like to a {gift} for the New year {year}.')
# # print(f'Dear Ded Moroz, I am {int(age)} years old. I would like to a {gift} for the New year {year}.')
# line_print = "Dear Ded Moroz, I am", age, "years old. I would like to a", gift , " for the New year", year, "."
# line_concat = "Dear Ded Moroz, I am " + str(age) + " years old. I would like to a " + gift + " for the New year " + str(year) + "."
# line_procent = "Dear Ded Moroz, I am %s years old. I would like to a %s for the New year %s." % (age, gift, year)
# line_figures = 'Dear Ded Moroz, I am {} years old. I would like to a {} for the New year {}.'. format(age, gift, year)
# line_fformat = f'Dear Ded Moroz, I am {age} years old. I would like to a {gift} for the New year {year}.'
# print(line_print)
# print(line_concat)
# print(line_procent)
# print(line_figures)
# print(line_fformat)


city = "Msk"
year = 1988
print(city, year)
print(f'city = {city} year = {year}')
print(f'{city = } {year = }')
print([city, year])

city = "Msk 1988"
year = ""
print(city, year)
print(f'city={city} year={year}')
print(f'{city = } {year = }')
print([city, year])  # array, list
print((city, year))  # tuple

