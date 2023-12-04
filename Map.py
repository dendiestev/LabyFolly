import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_LIGHT = (245, 66, 66)

class Map:

    ### Dessin ###

    def __init__(self) -> None:
        self.collision_list = []

    def draw(self, screen, screen_width, screen_height):
        # Ensuite il faut nommé avec X, y, 1(x, y), 1(y, x), 2(x, y), 2(y, x)
        num_col = screen_height // 30
        for i in range(num_col):
            pygame.draw.rect(screen, BLACK, (screen_width - 30, screen_height - 30*i, 30, 30))
            mur_col_pos = [screen_width - 30, screen_height - 30*i]
            self.collision_list.append(mur_col_pos)
        return(self.collision_list)
