import math
from vector3d import Vector


class Sphere:
    def __init__(self, position, radius, material):
        self.position = Vector(position[0], position[1], position[2])
        self.radius = radius
        self.material = material

    def interception(self, ray):
        delta_origin_position = ray.origin - self.position
        b = ray.basis.dot(delta_origin_position)
        c = delta_origin_position.dot(delta_origin_position) - self.radius * self.radius
        discriminant = b * b - c
        if discriminant >= 0:
            distance_cof = -b - math.sqrt(discriminant)
            if distance_cof > 0:
                return distance_cof
            else:
                distance_cof = -b + math.sqrt(discriminant)
                if distance_cof > 0:
                    return distance_cof
        return 10001.0

    def normal(self, surf_point):
        """Return surface normal of sphere"""
        return (surf_point - self.position).normalization()
