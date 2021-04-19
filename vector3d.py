import math


class Vector:
    """3 dimensional vector used in graphics"""
    def __init__(self, v0=0.0, v1=0.0, v2=0.0):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2

    def __str__(self):
        return '({}, {}, {})'.format(self.v0, self.v1, self.v2)

    def __add__(self, other):
        return Vector(self.v0 + other.v0, self.v1 + other.v1, self.v2 + other.v2)

    def __sub__(self, other):
        return Vector(self.v0 - other.v0, self.v1 - other.v1, self.v2 - other.v2)

    def __mul__(self, other):
        """Vector-scalar multiplication"""
        assert not isinstance(other, Vector)
        return Vector(self.v0 * other, self.v1 * other, self.v2 * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        try:
            return Vector(self.v0 / other, self.v1 / other, self.v2 / other)
        except ZeroDivisionError:
            return Vector(math.inf, math.inf, math.inf)

    def dot(self, other):
        return self.v0 * other.v0 + self.v1 * other.v1 + self.v2 * other.v2

    def norma(self):
        return math.sqrt(self.dot(self))

    def normalization(self):
        return self/self.norma()
