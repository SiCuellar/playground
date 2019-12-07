class Car:
    def __init__(self, color, milage):
        self.color = color
        self.milage = milage

    def __str__(self):
        return 'a {self.color} car'.format(self=self)


# print(my_car)
# print(my_car.color, my_car.milage)  #incorrect
