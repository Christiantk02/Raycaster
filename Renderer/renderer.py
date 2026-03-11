import pygame
import math

class Renderer:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height

        self.colors = {
            0: (0, 0, 0),
            1: (255, 255, 255),
        }

        self.minimap_margin = height * 0.05

        self.minimap_scale = 0.3
        self.minimap_size = min(int(width * self.minimap_scale), int(height * self.minimap_scale))
        
        self.minimap_x = width - self.minimap_size - self.minimap_margin
        self.minimap_y = self.minimap_margin
    
    def render_game(self, game):
        self.render_3d_view(game)
        self.render_map(game)

    def render_map(self, game):
        
        w, h = game.map.get_size()
        tile_size = min(self.minimap_size // w, self.minimap_size // h)

        player = game.player

        player_x = int(player.x * tile_size + self.minimap_x)
        player_y = int(player.y * tile_size + self.minimap_y)

        for row in range(h):
            for col in range(w):
                tile = game.map.get_tile(col, row)
                pygame.draw.rect(self.window, self.colors[tile], (col*tile_size + self.minimap_x, row*tile_size + self.minimap_y, tile_size, tile_size))

        for ray in game.rays:
            ray_end_x = int(ray[1][0] * tile_size + self.minimap_x)
            ray_end_y = int(ray[1][1] * tile_size + self.minimap_y)
            pygame.draw.line(self.window, (200, 200, 200), (player_x, player_y), (ray_end_x, ray_end_y), 1)

        pygame.draw.circle(self.window, (255, 0, 0), (player_x, player_y), tile_size // 6)
    
    def render_3d_view(self, game):
        rays = 0

        for ray in game.rays:
            distance = ray[0]

            if distance is None:
                continue

            wall_height = int(self.height / (distance + 0.0001))
            wall_width = self.width / len(game.rays)

            strip_x = rays * wall_width
            strip_y = (self.height - wall_height) // 2

            rays += 1
            color_intensity = max(0, min(255, int(255 - distance * 20)))

            pygame.draw.rect(self.window, (color_intensity, color_intensity, color_intensity), (strip_x, strip_y, wall_width, wall_height))
            