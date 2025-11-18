# Напишите программу преобразования арабских целых чисел от 1 до 900 в римские.
from calculator_roman import list_numbers_roman

dict_numbers = {
    0: '',
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC',
    100: 'C',
    200: 'CC',
    300: 'CCC',
    400: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM',
}
for value in 'VIII':
    V in list_numbers_roman
    if true:
        int = 5
    VI




VIII

# list_numbers_roman=['', '', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', '11', '12', '13', '14l', 15', '16', '17',   '18','19',  '20', '21', '22l', '23', 24', '25', '26',   27' ]
list_numbers_roman= ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC','C',  'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM' ]

def normalize_number(initial_string:str)->str:
    return initial_string.replace(' ', '')

def check_number(string_normalize:str)->bool:
    return string_normalize.isdigit() and int(string_normalize) <= 900

def convert_arabic_roman(number_arabic: int)-> str:
    digit_hundred = (number_arabic // 100)
    digit_ten = ((number_arabic % 100)//10)
    digit = number_arabic % 10
    # print(digit_hundred, digit_ten, digit)
    digit_hundred_roman = list_numbers_roman[digit_hundred+18] if digit_hundred else ''
    digit_ten_roman = list_numbers_roman[digit_ten+9] if digit_ten else ''
    digit_roman = list_numbers_roman[digit]
    return f"{digit_hundred_roman}{digit_ten_roman}{digit_roman}"


XI 10+1
VI
CCXI

def convert_roman_arabic(string_roman: str) -> int:
    number_arabic = 0
    while string_roman:
        string_roman_part = string_roman
        while string_roman_part:
            if string_roman_part in list_numbers_roman:
                index_arabic = list_numbers_roman.index(string_roman_part)
                # print(index_arabic)
                number_arabic += index_arabic % 9 * 10 ** (index_arabic//9)
                # print(f"{number_arabic}")
                string_roman = string_roman.removeprefix(string_roman_part)
                string_roman_part=''
            else:
                string_roman_part = string_roman_part[:-1]
    return number_arabic

for roman in list_numbers_roman:
    print(convert_roman_arabic(roman))

list_string = ['123', '1', '12 ', '44','46', '  99', '801', '901', 'oo1', '-1', ' ', '', ]
for string_number in list_string:
    number_normalized = normalize_number(string_number)
    if check_number(number_normalized):
        number_in_roman = convert_arabic_roman(int(number_normalized))
        print(f"list: {number_normalized}: {convert_arabic_roman(int(number_normalized))}")
    else:
        print('E: Incorrect input. Vvedite 0< INT <900 in arabic')

        LI - xx + v =  51-20+5
        for