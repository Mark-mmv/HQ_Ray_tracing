from coloring import Color
import math


class Image:
    """The image containing the rendering result"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixel_map = [[None for _ in range(width)] for _ in range(height)]
        self.x0 = -1.0
        self.y0 = -1.0 * height / width
        self.x_step = 2 / (width - 1)
        self.y_step = 2 / (height - 1) * height / width

    def set_pixel_to_map(self, x, y, px=Color(v0=0.0, v1=0.0, v2=0.0)):
        #px = self.gamma_correction(px)
        self.pixel_map[x][y] = px

    def gamma_correction(self, color):
        return color.log(2.0).normalization()

    def convert_to_ppm(self, filename=str('Non_name_img')):
        def to_int8(color):
            return round(max(min(color * 255, 255), 0))

        with open(str(filename + '.ppm'), 'w') as img_file:
            img_file.write('P3 {} {}\n255\n'.format(self.width, self.height))
            for row in self.pixel_map:
                for px in row:
                    img_file.write('{} {} {} '.format(to_int8(px.v0), to_int8(px.v1), to_int8(px.v2)))
                img_file.write('\n')