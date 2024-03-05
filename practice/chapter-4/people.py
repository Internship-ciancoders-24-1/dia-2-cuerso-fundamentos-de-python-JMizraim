class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age}")
        
        
if __name__ == "__main__":
    person1 = Person("Ana", 21)
    person1.say_hello()
    