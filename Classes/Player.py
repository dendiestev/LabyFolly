import pygame
import time
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_LIGHT = (245, 66, 66)
BROWN = (110, 70, 2)
GREEN_LIGHT = (61, 255, 168)
PINK_LIGHT = (196, 59, 244)
HIT_BOX_BLOCK = 30
HIT_BOX_PLAYER = 20

class Player():
    """
    All the differents player mecanics
    """
    
    def __init__(self, screen, cell_size, num_cols, num_row):
        self.screen = screen
        self.position_x = num_cols-2
        self.position_y = num_row-2
        self.player = pygame.Rect(0, 0, 0, 0)
        self.player = pygame.Rect(0, 0, 0, 0)
        self.life = 3
        self.shard = 0
        self.power = False
        self.power_step = 0
        self.nextLevel = False
        self.cell_size = cell_size

    def check_colison(self, enemie:dict, shard:dict, map):
        if [self.position_x, self.position_y] in [element[0] for element in enemie.values()]:
            element_del = []
            for cle,val in enemie.items():
                if val[0] == [self.position_x, self.position_y]:
                    element_del.append(cle)
                    if self.power == False:
                        self.life -=1
            for i in element_del:
                del enemie[i]
            map.afficher_update(enemie, shard)
        if [self.position_x, self.position_y] in shard.values():
            element_del = []
            for cle,val in shard.items():
                if val == [self.position_x, self.position_y]:
                    element_del.append(cle)
                    self.shard += 1
            for i in element_del:
                del shard[i]
            map.afficher_update(enemie, shard)

    def update_shard(self):
        if self.power != False:
            self.power_step -= 1
        if self.power_step <= 0:
            self.power = False

    def top(self, main_liste):
        if self.canMoveTop(main_liste):
            main_liste[self.position_x][self.position_y] = 0
            self.position_y -=1
            main_liste[self.position_x][self.position_y] = 7
            self.update_shard()
    
    def down(self, main_liste):
        if self.canMoveDown(main_liste):
            main_liste[self.position_x][ self.position_y] = 0
            self.position_y += 1
            main_liste[self.position_x][ self.position_y] = 7
            self.update_shard()
     
    def right(self, main_liste):
        if self.canMoveRight(main_liste):
            main_liste[self.position_x][self.position_y] = 0
            self.position_x += 1
            main_liste[self.position_x][self.position_y] = 7   
            self.update_shard()
    
    def left(self, main_liste):
        if self.canMoveLeft(main_liste):
            main_liste[self.position_x][self.position_y] = 0
            self.position_x -= 1
            main_liste[self.position_x][self.position_y] = 7  
            self.update_shard()

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