from coloring import Color
from image import Image
import math


class MonoMaterial:
    def __init__(self, color, reflect_cof=0.4):
        self.type_recursive = 1
        self.color = Color.read_hex(str(color))
        self.reflect_cof = reflect_cof

    def color_at(self, position):
        return self.color


class ChessMaterial:
    def __init__(self, color1, color2, reflect_cof=0.2):
        self.type_recursive = 1
        self.color1 = Color.read_hex(str(color1))
        self.color2 = Color.read_hex(str(color2))
        self.reflect_cof = reflect_cof

    def color_at(self, position):
        if int((position.v0 + 5.0) * 3.0) % 2 == int(position.v2 * 3.0) % 2:
            return self.color1
        return self.color2

class SkyBox:
    def __init__(self, color, reflect_cof=0.4):
        self.texture = Image(2048, 1024)
        self.set_texture_map()
        self.type_recursive = 0
        self.color = Color.read_hex(str(color))
        self.reflect_cof = reflect_cof

    def set_texture_map(self):
        px = []
        with open('pictures/texture/Panorama2k.txt', 'r') as img_file:
            i = 0
            j = 0
            rgb = 0
            for line in img_file:
                px.append(float(line)/255)
                rgb += 1
                if j == self.texture.width:
                    i += 1
                    j = 0
                if rgb == 3:
                    rgb = 0
                    self.texture.set_pixel_to_map(i, j, Color(v0=px[0], v1=px[1], v2=px[2]))
                    j += 1
                    px = []

    def color_at(self, position):
        position = position.normalization()
        u = round((0.5 + math.atan2(position.v2, position.v0) / math.pi / 2) * 2047)
        v = round((0.5 - math.asin(-position.v1) / math.pi) * 1023)
        return self.texture.pixel_map[v][u]
