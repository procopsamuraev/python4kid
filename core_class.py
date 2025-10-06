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
# from tkinter import Canvas, Tk
# 
# # Создаем окно
# root = Tk()
# root.title("Три коробки на Canvas")
# 
# # Создаем холст
# canvas_width = 400
# canvas_height = 300
# canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
# canvas.pack()
# 
# # Параметры коробок
# # Коробка 1
# x, y = 50, 50
# width, height = 100, 60
# canvas.create_rectangle(x, y, x + width, y + height, fill="lightblue", outline="black")
# 
# # Коробка 2
# x, y = 200, 70
# width, height = 80, 120
# canvas.create_rectangle(x, y, x + width, y + height, fill="lightgreen", outline="black")
# 
# # Коробка 3
# x, y = 120, 180
# width, height = 140, 50
# canvas.create_rectangle(x, y, x + width, y + height, fill="salmon", outline="black")
# 
# 
# # Запуск главного цикла
# root.mainloop()


# """
# Используя библиотеку tkinter и Canvas. Нарисовать 3 коробки на холсте
# с помощью задания координат и размеров через список.
# """
#import tkinter as tk
#root = tk.Tk()
#root.title('3 box_list')
#
#canvas = tk.Canvas(root, width=400, height=300, bg="lightgrey")
#canvas.pack()
## x, y , w , h 
#boxes = [
#[10, 20, 30, 30, 'salmon'], 
#[70, 100, 100, 20, 'red'], 
#[100, 200, 34, 70, 'yellow']
#]
#for box in boxes:
#    x, y, width, height, color = box
#    canvas.create_rectangle(x, y, x+width, y+height, fill=color, outline='black')
#
#root.mainloop()

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
#     {'x':10, 'y':20, 'width':30, 'height':30, 'color':'salmon'},
#     {'x':70, 'y':100, 'width':100, 'height':20, 'color':'red'},
#     {'x':100, 'y':200, 'width':34, 'height':70, 'color':'yellow'},
# ]
# 
# for box in boxes:
#     x, y, width, height, color = box
#     x = box.get('x')
#     y = box.get('y')
#     width = box.get('width')
#     height = box.get('height')
#     color = box.get('color')
#     canvas.create_rectangle(x, y, x+width, y+height, fill=color, outline='black')
# 
# root.mainloop()

"""
Используя библиотеку tkinter и Canvas. Нарисовать 3 коробки на холсте c 
помощью задания координат и размеров через класс.
"""

import tkinter as tk


class Box:
    x : int = 10
    y = 20
    width = 30
    height = 30
    color = 'salmon'
    outline = 'grey'


root = tk.Tk()
root.title('3 box_list')

canvas = tk.Canvas(root, width=400, height=300, bg="lightgrey")
canvas.pack()

box = Box()
canvas.create_rectangle(box.x, box.y, box.x+box.width, box.y+box.height, fill=box.color, outline=box.outline)

box = Box()
box.x, box.y, box.width, box.height, box.color = 70, 100, 100, 20, 'red'
canvas.create_rectangle(box.x, box.y, box.x+box.width, box.y+box.height, fill=box.color, outline=box.outline)

box = Box()
box.x, box.y, box.width, box.height, box.color = 100, 200, 34, 70, 'yellow'
canvas.create_rectangle(box.x, box.y, box.x+box.width, box.y+box.height, fill=box.color, outline=box.outline)

root.mainloop()
