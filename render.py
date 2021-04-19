from image import Image
from coloring import Color


def render():
    width = 3
    height = 1
    image = Image(width, height)
    red = Color.read_hex('#AA0000')
    green = Color.read_hex('#00AA00')
    blue = Color.read_hex('#0000AA')
    image.set_pixel_to_map(0, 0, red)
    image.set_pixel_to_map(0, 1, green)
    image.set_pixel_to_map(0, 2, blue)
    image.convert_to_ppm(filename='rgb_test')

if __name__ == '__main__':
    render()
