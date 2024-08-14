line = "String and not string. And one more string."
# line = "34"
# line = "AAA"
# print(f'{line = }')
# print(f'{line.upper() = }')
# print(f'{line.capitalize() = }')
# print(f'{line.swapcase() = }')
# print(f'{line.lower() = }')
# print(f'{line.casefold() = }')
# print(f'{line.title() = }')

# print(f'{line = }')
# print(f'{line.center(50) = }')
# print(f'{line.center(10) = }')
# print(f'{line.center(0) = }')
# print(f'{line.center(-10) = }')
# print(f"{line.center(50,'#') = }")
# print(f"{line.center(50,' ') = }")
# print(f'{line.ljust(50) = }')
# print(f'{line.ljust(-1) = }')
# print(f'{line.ljust(0) = }')
# print(f'{line.ljust(50,"#") = }')
# print(f'{line.rjust(50) = }')
# print(f'{line.rjust(50,"!") = }')
# print(f'{line = }')
# line1 = "\t1\t22\t333\t4444\t5"
# line2 = "0\t11\t222\t3333\t44444\t5"
# print(line1)
# print(line2)
# print(line1.expandtabs())
# print(line2.expandtabs())
# print(line1.expandtabs(15))
# print(line2.expandtabs(15))
# print(line1.expandtabs(0))
# print(line1.expandtabs(1))
# print(line1.expandtabs(-1))

print(f'{line = }')
# print(f'{line.zfill(50) = }')
# issledovat samostoyatelno
# print(f'{line.count("tring") = }')
# print(f'{line.count("String",10) = }')
# print(f'{line.count("String",0, 1) = }')
# print(f'{line.count("") = }')
# print(f'{line.count(" ") = }')
# print(f'{line.replace("String", "string") = }')
# print(f'{line.replace("string", "not string", 1) = }')
# print(f'{line.index("S") = }') # if not find will failure
# print(f'{line.index("s") = }')
# print(f'{line.strip("String.") = }')
# print(f'{line.rsplit(" ",1) = }')
# print(f'{line.lstrip("S",1) = }')
# print(f'{line.split(" ",1) = }')
# print(f'{"#".join(line) = }')
# print(f'{line.join("1 2") = }')
# print(f'{line.find("not") = }') # if not find just -1

print(f'{line = }')


# print diff between lower and casefold
# import sys
# import unicodedata as ud
#
# print("Unicode version:", ud.unidata_version, "\n")
# total = 0
# for codepoint in map(chr, range(sys.maxunicode)):
#     lower, casefold = codepoint.lower(), codepoint.casefold()
#     if lower != casefold:
#         total += 1
#         for conversion, converted in zip(
#             ("orig", "lower", "casefold"),
#             (codepoint, lower, casefold)
#         ):
#             print(conversion, [ud.name(cp) for cp in converted], converted)
#         print()
# print("Total differences:", total)
