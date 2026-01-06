# Напишите программу преобразования арабских целых чисел от 1 до 900 в римские.
#

list_operators = ['+', '-', '=']
# list_numbers_roman=['', '1', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', '10', '11', '12', '13', '14l', 15', '16', '17', '18'   19 '20',  '20', '21', '22l', '23', 24', '25', '26',   27' ]
# list_100_roman= ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C',  'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM' ]
list_roman_hundreds = ['C',  'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM' ]
list_roman_tens = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', ]
list_roman_units = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

# list_all_roman = []

list_test_string = [
    'II + XIV', 'XVII - XIV', 'LI - xx + v', 'i+X-v+xx', 'ix - x + xL - xv',
    'XX +', '-i', 'VV + XX', 'IIII - + X', 'I + X -', 'IV+IX', '', ' ', '1']


class NumberRoman:
    def __init__(self, string: str = ''):
        self.roman_number = roman_




def convert_arabic(number_arabic: int)-> str:
    digit_hundred = (number_arabic // 100)
    digit_ten = ((number_arabic % 100)//10)
    digit = number_arabic % 10
    digit_hundred_roman = list_numbers_roman[digit_hundred+18] if digit_hundred else ''
    digit_ten_roman = list_numbers_roman[digit_ten+9] if digit_ten else ''
    digit_roman = list_numbers_roman[digit]
    return f"{digit_hundred_roman}{digit_ten_roman}{digit_roman}"


def normalize_string(string:str)-> str:
   string_normalized = string.replace(' ', '').upper()
   string_normalized = string_normalized.replace('+', ' + ')
   string_normalized = string_normalized.replace('-', ' - ')
   string_normalized = string_normalized.removeprefix(' ').removeprefix(' ')
   return string_normalized


def convert_roman(roman: str) -> int:
    digit, digit_ten, digit_hundred = 0, 0, 0
    roman_word = ''
    for index, roman_symbol in enumerate(roman):
        roman_word += roman_symbol
        if roman_word not in list_numbers_roman:
            roman_word = roman_symbol
        index_list = list_numbers_roman.index(roman_word)
        if index_list < 10:
            digit = index_list
        elif index_list < 19:
            digit_ten = (index_list-9)*10
        else:
            digit_hundred = (index_list-18) * 100
    return digit+digit_ten+digit_hundred



def test_convert_all_arabic_roman() -> list:
    number = 0
    list_all_roman = []
    while number < 900:
        roman_number = convert_arabic(number)
        list_all_roman.append(roman_number)
        # int_number = convert_roman(roman_number)
        # print(number, str_roman, int_number)
        # if number != int_number:
        #     print(number, roman_number, int_number)
        #     return False
        number += 1
    return list_all_roman


def check_roman_example(example:str, list_all_roman)->bool:
    list_ = example.split()
    if len(list_) < 3:
        print('debug: not enough elements to do calculation')
        return False
    for index, element in enumerate(list_):
        start_true = index==0 and element.isalpha()
        end_true = index == len(list_)-1 and element.isalpha()
        number_true = index % 2 == 0 and element in list_all_roman
        operator_true = index % 2 == 1 and element in list_operators
        if not (number_true or operator_true) or not start_true or not end_true:
            return False
    return True


def main():
    list_all_roman = test_convert_all_arabic_roman()

    for string_example in list_test_string:
        normalized_example = normalize_string(string=string_example)
        if not check_roman_example(example=normalized_example,list_all_roman=list_all_roman):
            print(f"Not a good example: {string_example=}")
            continue

        list_string_roman:list = normalized_example.split()

        string_result = ''
        for element in list_string_roman:
            if element.isalpha():
                element = convert_roman(element)
            string_result += str(element)
        result_int = eval(string_result)
        result_roman = convert_arabic(result_int)
        print(f"{string_example} {string_result=} = {result_int} = {result_roman}")

if __name__ == '__main__':
    main()