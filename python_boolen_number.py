"""
int + true
"""
# line = "0"
# print(line, line.replace(" ", "").isdigit())
# line = "1"
# print(line, line.replace(" ", "").isdigit())
# line = " 5 "
# print(line, line.replace(" ", "").isdigit())
# line = " 05 "
# print(line, line.replace(" ", "").isdigit())
# line = "1 000"
# print(line, line.replace(" ", "").isdigit())

# false
# line = "-1"
# print(line, line.replace(" ", "").isdigit())
# line= "1.9"
# print(line, line.replace(" ", "").isdigit())
# line= "-1.9"
# print(line, line.replace(" ", "").isdigit())
# line= ""
# print(line, line.replace(" ", "").isdigit())
# line= " "
# print(line, line.replace(" ", "").isdigit())
# line= "a"
# print(line, line.replace(" ", "").isdigit())
# line= "/"
# print(line, line.replace(" ", "").isdigit())
# line= "5a"
# print(line, line.replace(" ", "").isdigit())


"""
int - true
"""


# def check_line(line_check):
#     line_check = line_check.replace(" ", "")
#     return line_check.find("-", 0, 1) == 0 and line_check.replace("-", "", 1).isdigit()


# line = "-1"
# print(line, check_line(line))
# line = "- 5 "
# print(line, check_line(line))
# line = " -05 "
# print(line, check_line(line))
# line = "-1 000"
# print(line, check_line(line))

'''
int - false
'''
# line = "+1"
# print(line, check_line(line))
# line = "1.9"
# print(line, check_line(line))
# line = "-1.9"
# print(line, check_line(line))
# line = ""
# print(line, check_line(line))
# line = " "
# print(line, check_line(line))
# line = "a"
# print(line, check_line(line))
# line = "/"
# print(line, check_line(line))
# line = "5a"
# print(line, check_line(line))
# line = "--5"
# print(line, check_line(line))
# line = "5-"
# print(line, check_line(line))
# line = "-5-"
# print(line, check_line(line))
# line = "5-2"
# print(line, check_line(line))

'''
float positive
'''

"""
def check_line(line_check: str):
    line_check = line_check.replace(" ", "")
    # return line_check.find(".") != -1 and line_check.replace(".", "", 1).isdigit()
    return (line_check.find(".") != -1 or line_check.find(",") != -1) and line_check.replace(".", "", 1).replace(".", "", 1).isdigit()


print("### float + true")
line = ".3"
print(line, check_line(line))
line = ",3"
print(line, check_line(line))
line = "3."
print(line, check_line(line))
line = "1.3"
print(line, check_line(line))
line = " 5.2 "
print(line, check_line(line))
line = " 05. 2 "
print(line, check_line(line))
line = "1 000.2"
print(line, check_line(line))


# float + false
print("### float + false")
line = ".,3"
print(line, check_line(line))
line = "-1.0"
print(line, check_line(line))
line = "1"
print(line, check_line(line))
line = ".1."
print(line, check_line(line))
line = "..1"
print(line, check_line(line))
line = " "
print(line, check_line(line))
line = "."
print(line, check_line(line))
line = ""
print(line, check_line(line))
line = "a"
print(line, check_line(line))
line = "/"
print(line, check_line(line))
line = "5a"
print(line, check_line(line))
"""
'''
float  negative
'''

"""
def check_line(line_check:str):
    line_check = line_check.replace(" ", "")
    # return line_check.find("-", 0, 1) == 0 and line_check.find(".") != -1 and line_check.replace("-", "", 1).replace(".", "", 1).isdigit()
    return line_check.startswith("-") and line_check.count(".") == 1 and line_check.replace("-", "", 1).replace(".", "").isdigit()


print("### float - true")
line = "-.3"
print(line, check_line(line))
line = "-3."
print(line, check_line(line))
line = "-1.3"
print(line, check_line(line))
line = " -5.2 "
print(line, check_line(line))
line = "- 05. 2 "
print(line, check_line(line))
line = "-1 000.2"
print(line, check_line(line))


print("### float - false")
line = "1.0"
print(line, check_line(line))
line = "1"
print(line, check_line(line))
line = ".1."
print(line, check_line(line))
line = "..1"
print(line, check_line(line))
line = " "
print(line, check_line(line))
line = "a"
print(line, check_line(line))
line = "/"
print(line, check_line(line))
line = "5a"
print(line, check_line(line))
"""

'''
int positive/negative 
'''
"""
def check_line(line_check):
    line_check = line_check.replace(" ", "")
    # return line_check.find("-", 1) == -1 and line_check.replace("-", "", 1).isdigit()
    return line_check.find("-") < 1 and line_check.replace("-", "", 1).isdigit()


print("### int +- true")
line = "1"
print(line, check_line(line))
line = "-1"
print(line, check_line(line))
line = " 5 "
print(line, check_line(line))
line = "- 5 "
print(line, check_line(line))
line = " 05 "
print(line, check_line(line))
line = " -05 "
print(line, check_line(line))
line = "1 000"
print(line, check_line(line))
line = "-1 000"
print(line, check_line(line))

print("### int +- false")
line = "1.9"
print(line, check_line(line))
line = "-1.9"
print(line, check_line(line))
line = ""
print(line, '""', check_line(line))
line = " "
print(line, '" "', check_line(line))
line = "a"
print(line, check_line(line))
line = "/"
print(line, check_line(line))
line = "5a"
print(line, check_line(line))
line = "--5"
print(line, check_line(line))
line = "5-"
print(line, check_line(line))
line = "-5-"
print(line, check_line(line))
line = "5-2"
print(line, check_line(line))
"""
'''
float positive/negative
'''

"""
def check_line(line_check:str):
    line_check = line_check.replace(" ", "")
    return line_check.find("-", 1) == -1 and line_check.find(".") != -1 and line_check.replace("-", "", 1).replace(".", "", 1).isdigit()


print("### float +- true")
line = ".3"
print(line, check_line(line))
line = "3."
print(line, check_line(line))
line = "1.3"
print(line, check_line(line))
line = " 5.2 "
print(line, check_line(line))
line = " 05. 2 "
print(line, check_line(line))
line = "1 000.2"
print(line, check_line(line))
line = "-.3"
print(line, check_line(line))
line = "-3."
print(line, check_line(line))
line = "-1.3"
print(line, check_line(line))
line = " -5.2 "
print(line, check_line(line))
line = "- 05. 2 "
print(line, check_line(line))
line = "-1 000.2"
print(line, check_line(line))

print("### float +- false")
print(line, check_line(line))
line = "1"
print(line, check_line(line))
line = ".1."
print(line, check_line(line))
line = "..1"
print(line, check_line(line))
line = " "
print(line, check_line(line))
line = "a"
print(line, check_line(line))
line = "/"
print(line, check_line(line))
line = "5a"
print(line, check_line(line))
line = "1"
print(line, check_line(line))
line = "-1"
print(line, check_line(line))
line = " 5 "
print(line, check_line(line))
line = "- 5 "
print(line, check_line(line))
line = " 05 "
print(line, check_line(line))
line = " -05 "
print(line, check_line(line))
line = "1 000"
print(line, check_line(line))
line = "-1 000"
print(line, check_line(line))
"""
'''
int/float positive
'''

"""
def check_line(line_check):
    line_check = line_check.replace(" ", "")
    return line_check.replace(".", "", 1).isdigit()


print("### int/float + true")
line = "1"
print(line, check_line(line))
line = " 5 "
print(line, check_line(line))
line = " 05 "
print(line, check_line(line))
line = "00.5 "
print(line, check_line(line))
line = "1 000"
print(line, check_line(line))
line = ".3"
print(line, check_line(line))
line = "3."
print(line, check_line(line))
line = "1.3"
print(line, check_line(line))
line = " 5.2 "
print(line, check_line(line))
line = " 05. 2 "
print(line, check_line(line))
line = "1 000.2"
print(line, check_line(line))

print("### int/float + false")
line = "-1"
print(line, check_line(line))
line= "-1.9"
print(line, check_line(line))
line= ""
print(line, check_line(line))
line= " "
print(line, check_line(line))
line= "a"
print(line, check_line(line))
line= "/"
print(line, check_line(line))
line= "5a"
print(line, check_line(line))
line = "-1"
print(line, check_line(line))
line = "- 5 "
print(line, check_line(line))
line = " -05 "
print(line, check_line(line))
line = "-1 000"
print(line, check_line(line))
line = "-.3"
print(line, check_line(line))
line = "-3."
print(line, check_line(line))
line = "-1.3"
print(line, check_line(line))
line = " -5.2 "
print(line, check_line(line))
line = "- 05. 2 "
print(line, check_line(line))
line = "-1 000.2"
print(line, check_line(line))
"""
"""
int/float negative 
"""

'''
def check_line(line_check):
    line_check = line_check.replace(" ", "")
    return line_check.find("-", 0, 1) == 0 and line_check.replace("-", "", 1).replace(".", "", 1).isdigit()


print("### int/float - true")
line = "-1"
print(line, check_line(line))
line = "- 5 "
print(line, check_line(line))
line = " -05 "
print(line, check_line(line))
line = "-1 000"
print(line, check_line(line))
line = "-.3"
print(line, check_line(line))
line = "-3."
print(line, check_line(line))
line = "-1.3"
print(line, check_line(line))
line = " -5.2 "
print(line, check_line(line))
line = "- 05. 2 "
print(line, check_line(line))
line = "-1 000.2"
print(line, check_line(line))


print("### int/float - false")
line = "+1"
print(line, check_line(line))
line = "1.9"
print(line, check_line(line))
line = "-1.9"
print(line, check_line(line))
line = ""
print(line, check_line(line))
line = " "
print(line, check_line(line))
line = "a"
print(line, check_line(line))
line = "/"
print(line, check_line(line))
line = "5a"
print(line, check_line(line))
line = "--5"
print(line, check_line(line))
line = "5-"
print(line, check_line(line))
line = "-5-"
print(line, check_line(line))
line = "5-2"
print(line, check_line(line))
line = "1.0"
print(line, check_line(line))
line = "1"
print(line, check_line(line))
line = ".1."
print(line, check_line(line))
line = "..1"
print(line, check_line(line))
line = " "
print(line, check_line(line))
line = "a"
print(line, check_line(line))
line = "/"
print(line, check_line(line))
line = "5a"
print(line, check_line(line))
'''
"""
number
"""

'''
def check_line(line_check:str):
    line_check = line_check.replace(" ", "")
    # return line_check.find("-", 0, 1) == 0 and line_check.replace("-", "", 1).replace(".", "", 1).isdigit()
    # return line_check.find("-")< 1 and line_check.replace("-", "", 1).replace(".", "", 1).isdigit()
    return line_check.removeprefix("-").replace(".", "", 1).isdigit()


line = "-1"
print(line, check_line(line))
line = "- 5 "
print(line, check_line(line))
line = " -05 "
print(line, check_line(line))
line = "-1 000"
print(line, check_line(line))
line = "-.3"
print(line, check_line(line))
line = "-3."
print(line, check_line(line))
line = "-1.3"
print(line, check_line(line))
line = " -5.2 "
print(line, check_line(line))
line = "- 05. 2 "
print(line, check_line(line))
line = "-1 000.2"
print(line, check_line(line))
line = "1"
print(line, check_line(line))
line = " 5 "
print(line, check_line(line))
line = " 05 "
print(line, check_line(line))
line = "00.5 "
print(line, check_line(line))
line = "1 000"
print(line, check_line(line))
line = ".3"
print(line, check_line(line))
line = "3."
print(line, check_line(line))
line = "1.3"
print(line, check_line(line))
line = " 5.2 "
print(line, check_line(line))
line = " 05. 2 "
print(line, check_line(line))
line = "1 000.2"
print(line, check_line(line))
'''

"""
Check if string contains only Aa or special symbols eg.
"""

"""
def check_line(line_check):
    # return line_check.lower().find("a") != -1 and not line_check.lower().replace("a", "").islower()
    # return line_check.lower().find("a") != -1 and not line_check.lower().replace("a", "").isalpha()
    return line_check.lower().find("a") != -1 and not line_check.strip("Aa,.- ")


print("### true")
line = "AaaaA"
print(line, check_line(line))
line = "AaaaA..?aaAAA1"
print(line, check_line(line))

print("### false")
line = "BAaaaA..?aaAAA1"
print(line, check_line(line))
line = "1%"
print(line, check_line(line))
line = ""
print(line, check_line(line))
line = " "
print(line, check_line(line))
"""

# Check if string contains only 0
def check_line(line_check):
    line_check = line_check.replace(" ", "")
    # return line_check.find("0") != -1 and line_check.find("-", 1) == -1 and line_check.replace(".", "", 1).replace("-", "", 1).replace("0", " ").isspace()
    # return line_check.find("0") != -1 and len(line_check.removeprefix("-").strip("0")) < 2
    # return  line_check.count("0") > 0 and len(line_check.removeprefix("-").strip(".0")) == 0
    return line_check.removeprefix("-").replace(".", "", 1).replace("0", "", line_check.count("0") - 1) == "0"

print("#### True ####")
line = " 00 0000"
print(line, check_line(line))
line = " 00.0000"
print(line, check_line(line))
line = " -0.0 0 "
print(line, check_line(line))
print("#### False ####")
line = " 0001A "
print(line, check_line(line))
line = " 0.0.0"
print(line, check_line(line))
line = "0-00 "
print(line, check_line(line))
line = " "
print(line, check_line(line))
line = ""
print(line, check_line(line))