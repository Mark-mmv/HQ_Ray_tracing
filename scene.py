from image import Image
from camera import Camera
from primitives import *
from texture import *


class Scene:
    def __init__(self):
        width = 2560
        height = 1440
        self.image = Image(width, height)
        self.camera = Camera(position=(0.0, 0.0, -1.0), direction=(0.0, 0.0, 0.0))
        self.objects = [Sphere(position=(2.0, -0.4, 1.5), radius=1.0, material=MonoMaterial(color="#662222")),
                        Sphere(position=(0.0, 0.0, 1.0), radius=0.5, material=MonoMaterial(color="#116611", reflect_cof=0.75)),
                        Sphere(position=(1.0, 1.0, 5.0), radius=1.5, material=MonoMaterial(color="#555533")),
                        Sphere(position=(0.0, 0.0, 0.0), radius=3000.0, material=SkyBox(color="#AABBFF")),
                        Sphere(position=(0.0, 31.0, 0.0), radius=30.0,
                               material=ChessMaterial(color1="#335555", color2="#552233", reflect_cof=0.1))]
