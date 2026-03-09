import numpy as np
import pygame

class Player:
    def __init__(self, x, y):
        self.position = np.array([x, y])

        self.moveSpeed = 1
        self.rotationSpeed = 2

        self.size = 15

        self.angle = np.radians(90) 

    def forward(self):
        self.position += np.array([np.cos(self.angle), -np.sin(self.angle)]) * self.moveSpeed

    def backward(self):
        self.position -= np.array([np.cos(self.angle), -np.sin(self.angle)]) * self.moveSpeed

    def right(self):
        self.angle -= np.radians(self.rotationSpeed) 
        
    def left(self):
        self.angle += np.radians(self.rotationSpeed)
    
    def draw(self, window, color):

        direction = np.array([np.cos(self.angle), -np.sin(self.angle)])

        front = self.position + direction #* self.size
        back = self.position - direction #* self.size * 0.2
        left = np.array([-direction[1], direction[0]]) #* self.size * 0.4

        points = [(front), (back + left), (self.position), (back - left)]
        pygame.draw.polygon(window, color, points)  