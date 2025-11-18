# Напишите программу преобразования арабских целых чисел от 1 до 900 в римские.

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

def normalize_number(initial_string:str)->str:
    return initial_string.replace(' ', '')

def check_number(string_normalize:str)->bool:
    return string_normalize.isdigit() and int(string_normalize) <= 900

def convert_arabic_roman(number_arabic: int)-> str:
    digit_hundred = (number_arabic // 100) * 100
    digit_ten = ((number_arabic% 100)//10) * 10
    digit = number_arabic% 10
    return f"{dict_numbers[digit_hundred]}{dict_numbers[digit_ten]}{dict_numbers[digit]}"


number_string = '110'
number_normalized = normalize_number(number_string)
if check_number(number_normalized):
    print(number_normalized, ':', convert_arabic_roman(int(number_normalized)))
else:
    print('Vvedite 0< INT <900 ')
