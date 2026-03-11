import math

class Player:
    def __init__(self, x , y, angle):
        self.x = x
        self.y = y
        self.angle = angle

        self.speed = 0.05
        self.rotation_speed = 0.03

        self.hitbox_size = 0.1

    def move(self, direction, map):
        # direction: 1 for forward, -1 for backward
        new_x = self.x + math.cos(self.angle) * direction * self.speed
        new_y = self.y + math.sin(self.angle) * direction * self.speed

        if not map.is_wall(int(new_x + self.hitbox_size), int(self.y)) \
            and not map.is_wall(int(new_x - self.hitbox_size), int(self.y)):
            self.x = new_x
            
        if not map.is_wall(int(self.x), int(new_y + self.hitbox_size)) \
            and not map.is_wall(int(self.x), int(new_y - self.hitbox_size)):
            self.y = new_y

    def rotate(self, direction):
        # direction: 1 for right, -1 for left
        self.angle += direction * self.rotation_speed