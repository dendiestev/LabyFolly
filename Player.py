import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player():
    """
    Spawn a player
    """
    
    def __init__(self, screen, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.screen = screen

    def draw(self):
        position_x = 10
        position_y = 10
        width = 10
        height = 10
        pygame.draw.rect(self.screen, (255,0,0), (position_x, position_y, width, height))

    def top(self):
        self.position_y -= self.vel

    def down(self):
        self.position_y += self.vel

    def right(self):
        self.position_x += self.vel
    
    def left(self):
        self.position_x -= self.vel

    def direction(self):
        x = 50
        y = 50
        width = 10
        height = 10
        vel = 10

        pygame.time.delay(100)
        
    

# class Player:

#     ### Initialisation ###
#     def __init__(self, row, col):
#         self.row = row
#         self.col = col

#     ### Mouvements ###

#     def move(self, dx, dy):
#         # Ici, vous pouvez mettre votre logique de déplacement du joueur
#         pass

#     ### Skin Du Joueur ###

#     def draw(self, screen):
#         # Ici, vous pouvez dessiner le joueur
#         pass
