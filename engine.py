from ray import Ray
from vector3d import Vector
from coloring import Color


class Engine:
    def __init__(self, scene):
        self.image = scene.image
        self.camera = scene.camera
        self.objects = scene.objects

    def render_scene(self):
        for j in range(self.image.height):
            y = self.image.y0 + j * self.image.y_step
            for i in range(self.image.width):
                x = self.image.x0 + i * self.image.x_step
                ray = Ray(self.camera.position, Vector(x, y, 0) - self.camera.position)
                self.image.set_pixel_to_map(j, i, self.ray_trace(ray))
        return self.image

    def ray_trace(self, ray, depth=0):
        color = Color.read_hex('#AAAABB')
        distance_cof_min = 10000.0
        obj_near = None

        for obj in self.objects:
            distance_cof = obj.interception(ray)
            if distance_cof < distance_cof_min:
                distance_cof_min = distance_cof
                obj_near = obj

        if obj_near is not None:
            hit_position = ray.origin + ray.basis * distance_cof_min
            hit_normal = obj_near.normal(hit_position)
            #color = self.add_color(obj_near, hit_position, hit_normal)
            return obj_near.material.color
        return color
