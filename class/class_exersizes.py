class Box:
    width_class = 1
    length_class = 3
    height_class = 5


box_1 = Box()
box_1.length_class = 15
# print(box_1, box_1.width_class, box_1.length_class, box_1.height_class)
box_2 = Box()
# print(box_2, box_2.width_class, box_2.length_class, box_2.height_class)
box_3 = Box()
# print(box_3, box_3.width_class, box_3.length_class, box_3.height_class)

# Box.width_class = 77
# box_3.height_class = 33
print(f"{box_1=}, {box_1.width_class=} {box_1.length_class=}, {box_1.height_class=}")
print(f"{box_2=}, {box_2.width_class=} {box_2.length_class=}, {box_2.height_class=}")
print(f"{box_3=}, {box_3.width_class=} {box_3.length_class=}, {box_3.height_class=}")

box_4 = Box()
print(f"{box_4=}, {box_4.width_class=} {box_4.length_class=}, {box_4.height_class=}")