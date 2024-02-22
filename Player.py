import pygame
import time
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_LIGHT = (245, 66, 66)
BROWN = (110, 70, 2)
GREEN_LIGHT = (61, 255, 168)
HIT_BOX_BLOCK = 30
HIT_BOX_PLAYER = 20

class Player():
    """
    All the differents player mecanics
    """
    
    def __init__(self, screen, map, cell_size):
        self.screen = screen
        self.map = map
        self.position_x = self.map.start[0]
        self.position_y = self.map.start[1]
        self.player = pygame.Rect(0, 0, 0, 0)
        self.player = pygame.Rect(0, 0, 0, 0)
        self.life = 3
        self.nextLevel = False
        self.cell_size = cell_size

    def top(self, main_liste):
        if self.canMoveTop(main_liste):
            main_liste[self.position_x][self.position_y] = 0
            self.position_y -=1
            main_liste[self.position_x][self.position_y] = 7
    

    def down(self, main_liste):
        if self.canMoveDown(main_liste):
            main_liste[self.position_x][ self.position_y] = 0
            self.position_y += 1
            main_liste[self.position_x][ self.position_y] = 7
     

    def right(self, main_liste):
        if self.canMoveRight(main_liste):
            main_liste[self.position_x][self.position_y] = 0
            self.position_x += 1
            main_liste[self.position_x][self.position_y] = 7
     
    
    def left(self, main_liste):
        if self.canMoveLeft(main_liste):
            main_liste[self.position_x][self.position_y] = 0
            self.position_x -= 1
            main_liste[self.position_x][self.position_y] = 7
    

    def canMoveTop(self, main_liste):
        if self.position_x == 1 and self.position_y-1 == 1:
            self.nextLevel = True
        if main_liste[self.position_x][self.position_y-1] in [-1,-2,-3,-4]:
            return False
        else:
            return True
        
    def canMoveDown(self, main_liste):
        if self.position_x == 1 and self.position_y+1 == 1:
            self.nextLevel = True
        if main_liste[self.position_x][self.position_y+1] in [-1,-2,-3,-4]:
            return False
        else:
            return True
        
    def canMoveLeft(self, main_liste):
        if self.position_x-1 == 1 and self.position_y == 1:
            self.nextLevel = True
        if main_liste[self.position_x-1][self.position_y] in [-1,-2,-3,-4]:
            return False
        else:
            return True
    
    def canMoveRight(self, main_liste):
        if self.position_x+1 == 1 and self.position_y == 1:
            self.nextLevel = True
        if main_liste[self.position_x +1][self.position_y] in [-1,-2,-3,-4]:
            return False
        else:
            return True