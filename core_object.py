# def greet():
#     print("Привет, мир!")
#
# # Сохранение функции в переменную
# hello = greet
# print(hello)  # <function greet at 0x000001D641FBE8C0>
# # Вызов функции через переменную

def say_hello():
    return "Hello, World!"+'22'

print(say_hello())  # Выведет: Hello, World!

say_hello_lambda = lambda: "Hello, World!"+'11'
print(say_hello_lambda())  # Выведет: Hello, World!
print(say_hello_lambda)  # Выведет: Hello, World!
