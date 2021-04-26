from ray import Ray
from vector3d import Vector
from coloring import Color


class Engine:
    def __init__(self, scene):
        self.image = scene.image
        self.camera = scene.camera
        self.objects = scene.objects
        self.max_depth = 4

    def render_scene(self):
        for j in range(self.image.height):
            y = self.image.y0 + j * self.image.y_step
            for i in range(self.image.width):
                x = self.image.x0 + i * self.image.x_step
                ray = Ray(self.camera.position, Vector(x, y, 0) - self.camera.position)
                px = self.ray_trace(ray=ray, depth=0, color=Color.read_hex('#000000'))
                self.image.set_pixel_to_map(j, i, px=px)
        return self.image

    def ray_trace(self, ray, depth=0, color=Color.read_hex('#000000')):
        distance_cof_min = 10000.0
        obj_near = None

        for obj in self.objects:
            distance_cof = obj.interception(ray)
            if distance_cof < distance_cof_min:
                distance_cof_min = distance_cof
                obj_near = obj

        if obj_near is None:
            return color

        near_position = ray.origin + ray.basis * distance_cof_min
        color = obj_near.material.color_at(near_position)

        if depth < self.max_depth and obj_near.material.type_recursive != 0:
            hit_normal = obj_near.normal(near_position)
            color += self.reflection(ray, near_position, hit_normal, depth+1, color) * obj_near.material.reflect_cof

        return color

    def light(self):
        pass

    def reflection(self, ray, hit_position, hit_normal, depth, color):
        reflect_ray_position = hit_position + hit_normal * 0.001
        reflect_ray_basis = ray.basis - 2 * hit_normal * ray.basis.dot(hit_normal)
        reflect_ray = Ray(reflect_ray_position, reflect_ray_basis)

        color += self.ray_trace(ray=reflect_ray, depth=depth, color=color)
        return color


