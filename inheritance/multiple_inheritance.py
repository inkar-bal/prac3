class Person:
    def greet(self):
        print("Hello!")
class Employee:
    def work(self):
        print("Working hard...")
# Child inherits from both Person and Employee
class Manager(Person, Employee):
    def manage(self):
        print("Managing team")
# Create object
mgr = Manager()
mgr.greet()   # Hello! (from Person)
mgr.work()    # Working hard... (from Employee)
mgr.manage()  # Managing team (own method)
