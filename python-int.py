# print(2 + 3)
# print(3 - 2)
# print(2 * 3)
# print("4: - stepen", 3 ** 2)  # что делает операция "**"?
# print(3 / 2)
# print("6:max celochislenoe delenie", 12 // 2)  # что делает операция "//"?
# print("7:ostatok ot deleniya", 11 % 2)


# find appt floor by appt num
# limited etajey and zaidy na 1st etege mojem uvidet colvo kvartir na etage
# kak znaya num of kvartiry naity etag i podjezd
appt_num = 1
floor_lobby = 8  # kol-vo erajey v podjezde
appt_floor = 4  # kol-vo appt na etaje


floor_n = appt_num//appt_floor  # nahodim bezontositelny etaj withour accounts lobbies and limit to 8
if appt_num%appt_floor != 0:
    floor_n = floor_n + 1
# print(f'{floor_n = }')
our_lobby = floor_n // floor_lobby
if floor_n % floor_lobby !=0:
    our_lobby = our_lobby + 1
# print(f'{our_lobby = }')
our_floor = floor_n - ( our_lobby -1)* floor_lobby
print(f'{appt_num = }\n\t{our_lobby = }\n\t{our_floor = }')

print(f'Lobby:{(appt_num-1)//(floor_lobby*appt_floor)+1}')