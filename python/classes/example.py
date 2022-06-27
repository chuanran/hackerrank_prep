class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age =age
    def print_person(self):
        print(f"name is {self.name}, and age is {self.age}")

p1 = Person("chuan", 34)
p1.print_person()