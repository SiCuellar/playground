class Car:
    def __init__(self, color, milage):
        self.color = color
        self.milage = milage

    def __str__(self):
        return 'a {self.color} car'.format(self=self)

my_car = Car('red', 5432)
print(my_car)








# dunder str or __str__ converts objects into strings -- pythonic way of doing this  
# str(my_car) # will call the str method
# {}.format(my_car)

# print(my_car)
# print(my_car.color, my_car.milage)  #incorrect
