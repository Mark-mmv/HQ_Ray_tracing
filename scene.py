from image import Image
from camera import Camera
from primitives import *
from texture import *


class Scene:
    def __init__(self):
        width = 400
        height = 300
        self.image = Image(width, height)
        self.camera = Camera(position=(0.0, 0.0, -1.0), direction=(0.0, 0.0, 0.0))
        self.objects = [Sphere(position=(-1.0, 0.0, 1.5), radius=1.0, material=MonoMaterial(color="#AA0000")),
                        Sphere(position=(0.0, 0.0, 1.0), radius=0.5, material=MonoMaterial(color="#00AA00")),
                        Sphere(position=(1.0, 1.0, 5.0), radius=1.5, material=MonoMaterial(color="#AAAA00")),
                        Sphere(position=(0.0, 10001.0, 0.0), radius=10000, material=MonoMaterial(color="#335555"))]
