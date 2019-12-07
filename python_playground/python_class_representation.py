#__str__ vs __repr__

#__str__ -----> is used to give an easy, human consumption
#__repr__ -----> unanbiguous, valid python, more developers

import datetime
today = datetime.date.today()

print(str(today))     #---> 2019-12-07
print(repr(today))    #---> datetime.date(2019, 12, 7)



# class Car:
#     def __init__(self, color, milage):
#         self.color = color
#         self.milage = milage
#
#     def __repr__(self):
#         return '__repr__ for Car'
#
#     def __str__(self):
#         return '__str__ for Car'
#


#__repr__ ----> shows this when the object is inspected
# repr(my_car)


# dunder str or __str__ converts objects into strings -- pythonic way of doing this
# str(my_car) # will call the str method
# {}.format(my_car)

# print(my_car)
# print(my_car.color, my_car.milage)  #incorrect
