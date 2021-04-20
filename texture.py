from coloring import Color


class MonoMaterial:
    def __init__(self, color):
        self.color = Color.read_hex(str(color))

    def read_color(self):
        return self.color
