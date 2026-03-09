import pygame

class Map:
    def __init__(self):
        self.tilemap =  [
            ["#","#","#","#","#","#","#","#","#","#"],
            ["#","-","-","#","-","-","-","-","-","#"],
            ["#","-","-","#","-","-","-","-","-","#"],
            ["#","-","-","-","-","-","-","-","-","#"],
            ["#","-","-","#","-","-","-","-","-","#"],
            ["#","#","#","#","-","-","-","-","-","#"],
            ["#","-","-","-","-","-","-","-","-","#"],
            ["#","-","-","-","-","-","-","-","-","#"],
            ["#","-","-","-","-","-","-","-","-","#"],
            ["#","#","#","#","#","#","#","#","#","#"]
        ]

        self.colors = {
            "#": (255, 255, 255),
            "-": (0, 0, 0)
        }

        self.tile_width = size // len(self.tilemap[0])
        self.tile_height = size // len(self.tilemap)


    def is_wall(self, x, y):
        return self.tilemap[int(y)][int(x)] == "#" 
    
    def draw(self, window):
        for row in range(len(self.tilemap)):
            for col in range(len(self.tilemap[0])):
                tile = self.tilemap[row][col]
                pygame.draw.rect(window, self.colors[tile], (col*self.tile_width, row*self.tile_height, self.tile_width, self.tile_height), 2)