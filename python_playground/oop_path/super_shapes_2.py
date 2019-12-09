class Square(Rectangel)
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square)
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length
