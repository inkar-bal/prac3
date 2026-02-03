class Car:
    wheels = 4  # Class variable (shared by all cars)
    def __init__(self, color, brand):
        self.color = color  # Instance variable
        self.brand = brand  # Instance variable
# Create objects
car1 = Car("Red", "Toyota")
car2 = Car("Blue", "Honda")
# Access instance variables
print(car1.color)  # Red
print(car2.color)  # Blue
# Access class variable
print(car1.wheels)  # 4
print(car2.wheels)  # 4
# Changing class variable
Car.wheels = 6
print(car1.wheels)  # 6
print(car2.wheels)  # 6
# Changing instance variable
car1.color = "Green"
print(car1.color)  # Green
print(car2.color)  # Blue
