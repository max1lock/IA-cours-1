class Dog:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def bark(self):
        return f"{self.name} says Woof!"


my_dog = Dog(name="Buddy", age=3)
