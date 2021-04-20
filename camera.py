from vector3d import Vector
import math

class Camera:
    def __init__(self, position=(0.0, 0.0, -1.0), direction=(0.0, 0.0, 0.0)):
        self.position = Vector(position[0], position[1], position[2])
        self.direction = Vector(direction[0], direction[1], direction[2]).normalization() + self.position


if __name__ == '__main__':
    Camera()