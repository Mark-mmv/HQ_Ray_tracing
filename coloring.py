from vector3d import Vector


class Color(Vector):
    """Color as a vector"""
    @classmethod
    def read_hex(cls, hexcolor="#000000"):
        v0 = int(hexcolor[1:3], 16) / 255.0
        v1 = int(hexcolor[3:5], 16) / 255.0
        v2 = int(hexcolor[5:7], 16) / 255.0
        return cls(v0, v1, v2)
