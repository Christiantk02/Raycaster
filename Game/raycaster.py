import math

class Raycaster:
    def __init__(self, game, fov, num_rays, max_depth):
        self.game = game
        self.map = game.map
        self.player = game.player

        self.fov = fov
        self.num_rays = num_rays
        self.max_depth = max_depth

        self.angle_step = self.fov / self.num_rays

    def cast_all_rays(self):
        start_angle = self.player.angle - self.fov / 2
        rays = []

        for ray in range(self.num_rays):
            ray_angle = start_angle + ray * self.angle_step
            distance ,ray_end = self.cast_ray(ray_angle)
            rays.append((distance, ray_end))

        return rays
    
    def cast_ray(self, angle):
        x, y = self.player.x, self.player.y
        step = 0.1
        
        while True:
            x += math.cos(angle) * step
            y += math.sin(angle) * step
            
            if self.map.is_wall(int(x), int(y)):
                distance = math.sqrt((x - self.player.x) ** 2 + (y - self.player.y) ** 2)
                return distance, (x, y)
            
            if math.sqrt((x - self.player.x) ** 2 + (y - self.player.y) ** 2) > self.max_depth:
                return None, (x, y)
                

