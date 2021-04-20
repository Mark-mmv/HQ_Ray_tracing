import time
from image import Image
from scene import Scene
from engine import Engine


def render():
    scene_objects = Scene()
    engine = Engine(scene_objects)
    image = engine.render_scene()
    image.convert_to_ppm('pictures/Test3')


if __name__ == '__main__':
    start = time.perf_counter()
    render()
    end = time.perf_counter()
    print((end - start) * 1000, 'ms')
