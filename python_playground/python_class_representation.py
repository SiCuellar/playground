#__str__ vs __repr__

#__str__ -----> is used to give an easy, human consumption
#__repr__ -----> unanbiguous, valid python, more developers

# add __repr__ to any class that you define is good practice

class Car:
    def __init__(self, color, milage):
        self.color = color
        self.milage = milage

    def __repr__(self):
        return('{self.__class__.__name__}({self.color}, {self.milage})'.format(self=self))
        # return('Car({self.color}, {self.milage})'.format(self=self))


my_car = Car('red', 54324)
print(my_car)



#---------------------------------------------------------------------
# import datetime
# today = datetime.date.today()
#
# print(str(today))     #---> 2019-12-07
# print(repr(today))    #---> datetime.date(2019, 12, 7)
#-----------------------------------------------------------------------



#__repr__ ----> shows this when the object is inspected
# repr(my_car)


# dunder str or __str__ converts objects into strings -- pythonic way of doing this
# str(my_car) # will call the str method
# {}.format(my_car)

# print(my_car)
# print(my_car.color, my_car.milage)  #incorrect
