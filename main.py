import pygame

from settings import *
from player import Player
from map import Map

pygame.init()
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

m = Map()
p = Player(width/ 2, height / 2)

### Main loop ###
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p.forward()
    
    if keys[pygame.K_s]:
        p.backward()
    
    if keys[pygame.K_a]:
        p.left()
    
    if keys[pygame.K_d]:
        p.right()
                

    win.fill((0, 0, 0))

    m.draw(win)
    p.draw(win, (255, 255, 255))

    pygame.display.update()