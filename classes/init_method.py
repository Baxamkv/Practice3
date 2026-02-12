class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Person name: {self.name}, Person age: {self.age}")
    
person1 = Person("Alex", 30)
person1.info()
print(person1.__dict__)