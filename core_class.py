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

class Car():
    brand = ''
    model = ''
    year = 2000
    color = ''
    def get_detail(self):
        return self.brand, self.model, self.year, self.color


car_one = Car()
car_one.brand = 'Toyota'
car_one.model = 'Supra'
car_one.color = 'black'

print(car_one.get_detail())