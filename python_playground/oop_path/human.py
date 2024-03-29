class Person:
    description = "general person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("My name is {} and I am {} years old".format(self.name, self.age))

    def eat(self, food):
        print("{} eats {}".format(self.name, food))

    def action(self):
        print("{} jumps".format(self.name))

class Baby(Person):
    description = "baby"

    def speak(self):
        print("bah bah bah something")

    def nap(self):
        print("{} takes a nap".format(self.name))


person = Person("steve", 20)
person.speak()
person.eat("Pasta")
person.action()

baby = Baby("max", 2)
baby.speak()
baby.nap()

print(isinstance(baby, Person))
print(isinstance(baby, object))
print(isinstance(baby, Baby))
