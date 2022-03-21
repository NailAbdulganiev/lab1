import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, right):
        return Point(self.x + right.x, self.y + right.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        if isinstance(number, int) or isinstance(number, float):
            return Point(number * self.x, number * self.y)
        else:
            return sum(self.x * number.x, self.y * number.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))
