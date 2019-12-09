class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.legth * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inhereits from the Rectangle class
class Square(Rectangle)
    def __init__(self, length):
        super().__init__(length, length)


# Square is a special instance of a Rectangle - we can use the super class to reduce the code
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * self.length + 2 * self.width
#
#
# class Square:
#     def __init__(self, length):
#         self.length = length
#
#     def area(self):
#         return self.length * self.length
#
#     def perimeter(self):
#         return 4 * self.length
#

square = Square(4)
print(square.area())

rectangle = Rectangle(2,4)
print(rectangle.area())
