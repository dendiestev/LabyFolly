import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_LIGHT = (245, 66, 66)

class Player():
    """
    Spawn a player
    """
    
    def __init__(self, screen, position_x, position_y):
        self.screen = screen
        self.position_x = position_x
        self.position_y = position_y

    def draw(self):
        width = 20
        height = 20
        pygame.draw.rect(self.screen, RED_LIGHT, (self.position_x, self.position_y, width, height))

    def top(self):
        self.position_y -= 5

    def down(self):
        self.position_y += 5

    def right(self):
        self.position_x += 5
    
    def left(self):
        self.position_x -= 5
