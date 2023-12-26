import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_LIGHT = (245, 66, 66)

class Player():
    """
    Spawn a player
    """
    
    def __init__(self, screen, position_x, position_y, vel):
        self.screen = screen
        self.position_x = position_x
        self.position_y = position_y
        self.vel = vel
        self.player = pygame.Rect(0, 0, 0, 0)
        self.life = 3

    def draw(self):
        width = 15
        height = 15
        self.player = pygame.Rect(self.position_x, self.position_y, width, height)
        pygame.draw.rect(self.screen, RED_LIGHT, self.player)

    def top(self):
        self.position_y -= self.vel

    def down(self):
        self.position_y += self.vel

    def right(self):
        self.position_x += self.vel
    
    def left(self):
        self.position_x -= self.vel

    def clear_player(self):
        pygame.draw.rect(self.screen, WHITE, (self.position_x, self.position_y, 15, 15))
