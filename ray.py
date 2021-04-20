from vector3d import Vector


class Ray:
    def __init__(self, origin, basis):
        self.origin = origin
        self.basis = basis.normalization()
