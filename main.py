import pygame

from Game.game import Game         
from Renderer.renderer import Renderer

from settings import fps, width, height, fov, ray_count, max_depth

pygame.init()
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

game = Game()
renderer = Renderer(win, width, height)

running = True

while running:
    clock.tick(fps)
    win.fill((20, 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.update()

    renderer.render_game(game)

    pygame.display.update()