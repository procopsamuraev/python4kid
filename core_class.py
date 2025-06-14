# class B:
#     n = 5
#     def adder(self, v):
#         return v + self.n
#     
# # print(B.n)
# # print(B.adder(4))
# 
# l = B()
# print(l.n)
# print(l.adder(100))

# class User:
#     def setName(self, n):
#         self.name = n
#     def getName(self):
#         try:
#             return self.name
#         except:
#             return "No name"
# 
# first = User()
# second = User()
# first.setName("Bob")
# print(first.getName())              # Bob
# print(second.getName())             # No name

# class Animal:
#     kind = ''
#     name = ''
#     hp = 0
#     
#     def eat(self):
#         self.hp +=10
#     
#     def live(self, n):
#         self.hp -= n
# 
#     def gethp(self):
#         if self.hp > 0:
#             return self.hp
#         else: 
#             return "I am hungry..."
# 
# cat = Animal()
# cat.kind = 'cat'
# cat.name = 'Murz'
# dog = Animal()
# dog.kind = 'dog'
# dog.name = 'Sharik'
# print("I like my {} {}!".format(cat.kind, cat.name))
# print(cat.gethp())
# cat.eat()
# print(cat.gethp())
# cat.live(7)
# print(cat.gethp())
# 
# print("I like my {} {}!".format(dog.kind, dog.name))

# class Car():
#     brand = ''
#     model = ''
#     year = 2000
#     color = ''
#     def get_detail(self):
#         return self.brand, self.model, self.year, self.color
# 
# 
# car_one = Car()
# car_one.brand = 'Toyota'
# car_one.model = 'Supra'
# car_one.color = 'black'
# 
# print(car_one.get_detail())

# 
# """
# Используя библиотеку tkinter и Canvas. Нарисовать 3 коробки на холсте с помощью задания 
# координат и размеров через переменные.
# """
# import tkinter as tk
# 
# # Создаем окно
# root = tk.Tk()
# root.title("Три коробки на Canvas")
# 
# # Создаем холст
# canvas_width = 400
# canvas_height = 300
# canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
# canvas.pack()
# 
# # Параметры коробок
# # Коробка 1
# x1_1, y1_1 = 50, 50
# width1, height1 = 100, 60
# 
# # Коробка 2
# x2_1, y2_1 = 200, 70
# width2, height2 = 80, 120
# 
# # Коробка 3
# x3_1, y3_1 = 120, 180
# width3, height3 = 140, 50
# 
# # Рисуем коробки
# canvas.create_rectangle(x1_1, y1_1, x1_1 + width1, y1_1 + height1, fill="lightblue", outline="black")
# canvas.create_rectangle(x2_1, y2_1, x2_1 + width2, y2_1 + height2, fill="lightgreen", outline="black")
# canvas.create_rectangle(x3_1, y3_1, x3_1 + width3, y3_1 + height3, fill="salmon", outline="black")
# 
# # Запуск главного цикла
# root.mainloop()

# """
# Используя библиотеку tkinter и Canvas. Нарисовать 3 коробки на холсте
# с помощью задания координат и размеров через список.
# """
# import tkinter as tk
# root = tk.Tk()
# root.title('3 box_list')
# 
# canvas = tk.Canvas(root, width=400, height=300, bg="lightgrey")
# canvas.pack()
# # x, y , w , h 
# boxes = [
# [10, 20, 30, 30, 'salmon'], 
# [70, 100, 100, 20, 'red'], 
# [100, 200, 34, 70, 'yellow']
#]
# for box in boxes:
#     x, y, w, h, color = box
#     print(x)
#     canvas.create_rectangle(x, y, x+w, y+h, fill=color, outline='black')
# 
# root.mainloop()

"""
Используя библиотеку tkinter и Canvas. Нарисовать 3 коробки на холсте
с помощью задания координат и размеров через словарь.
"""

# import tkinter as tk
# root = tk.Tk()
# root.title('3 box_list')
# 
# canvas = tk.Canvas(root, width=400, height=300, bg="lightgrey")
# canvas.pack()
# # x, y , w , h 
# boxes:list[dict] = [
#     {'x':10, 'y':20, 'w':30, 'h':30, 'color':'salmon'},
#     {'x':70, 'y':100, 'w':100, 'h':20, 'color':'red'},
#     {'x':100, 'y':200, 'w':34, 'h':70, 'color':'yellow'},
# ]
# 
# for box in boxes:
#     x, y, w, h, color = box
#     x = box.get('x')
#     y = box.get('y')
#     w = box.get('w')
#     h = box.get('h')
#     color = box.get('color')
#     canvas.create_rectangle(x, y, x+w, y+h, fill=color, outline='black')
# 
# root.mainloop()

"""
Используя библиотеку tkinter и Canvas. Нарисовать 3 коробки на холсте c 
помощью задания координат и размеров через класс.
"""

import tkinter as tk
root = tk.Tk()
root.title('3 box_list')

canvas = tk.Canvas(root, width=400, height=300, bg="lightgrey")
canvas.pack()

class Box:
    x = 10
    y = 20
    width = 30
    height = 30
    color = 'salmon'
# x, y , w , h 
# boxes:list[dict] = [
    # {'x':10, 'y':20, 'w':30, 'h':30, 'color':'salmon'},
    # {'x':70, 'y':100, 'w':100, 'h':20, 'color':'red'},
    # {'x':100, 'y':200, 'w':34, 'h':70, 'color':'yellow'},
# ]

# for box in boxes:
#     x, y, w, h, color = box
#     x = box.get('x')
#     y = box.get('y')
#     w = box.get('w')
#     h = box.get('h')
#     color = box.get('color')
box1 = Box()
box2 = Box()
box3 = Box()
box2.x, box2.y, box2.width, box2.height, box2.color = 70, 100, 100, 20, 'red'
box3.x, box3.y, box3.width, box3.height, box3.color = 100, 200, 34, 70, 'yellow'
canvas.create_rectangle(box1.x, box1.y, box1.x+box1.width, box1.y+box1.height, fill=box1.color, outline='black')
canvas.create_rectangle(box2.x, box2.y, box2.x+box2.width, box2.y+box2.height, fill=box2.color, outline='black')
canvas.create_rectangle(box3.x, box3.y, box3.x+box3.width, box3.y+box3.height, fill=box3.color, outline='black')

root.mainloop()
