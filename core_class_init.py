class Car:
    make, model, year = "Honda", "Civic", 2000
    def __init__(self):

        #Initialize the Car with default attributes
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

# Creating an instance using the default constructor
car = Car()
print(car.make)
print(car.model)
print(car.year)
car = Car
print(car.make)
print(car.model)
print(car.year)