class Animal:
    def sound(self):
        print("Some generic animal sound")
class Dog(Animal):
    # Method overriding
    def sound(self):
        print("Woof! Woof!")
class Cat(Animal):
    # Method overriding
    def sound(self):
        print("Meow!")
# Create objects
animal = Animal()
dog = Dog()
cat = Cat()
animal.sound()  # Some generic animal sound
dog.sound()     # Woof! Woof!
cat.sound()     # Meow!
