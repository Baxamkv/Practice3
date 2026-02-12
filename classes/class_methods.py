class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self, surname):
        return {"name" : self.name, "surname" : surname, "age" : self.age}
    
p1 = Person("Alex", 30)
print(p1.info("Johnson"))