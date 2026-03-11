import pygame

from .player import Player
from .map import Map
from .raycaster import Raycaster  

from settings import fov, ray_count, max_depth

class Game:
    def __init__(self):
        self.player = Player(1.5, 1.5, 0)
        self.map = Map()
        
        self.raycaster = Raycaster(self, fov, ray_count, max_depth)
        self.rays = []

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(1, self.map)
        if keys[pygame.K_s]:
            self.player.move(-1, self.map)
        if keys[pygame.K_a]:
            self.player.rotate(-1)
        if keys[pygame.K_d]:
            self.player.rotate(1)
        
        self.rays = self.raycaster.cast_all_rays()
        

    