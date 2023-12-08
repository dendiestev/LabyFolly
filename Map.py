import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_LIGHT = (245, 66, 66)

class Map:

    ### Initialisation ###

    def __init__(self, collision_list=[]):
        self.collision_list = collision_list

    ### Dessin ###

    def draw(self, screen, screen_width, screen_height):
        # TEST ->
        num_col = screen_height // 30
        num_row = screen_width // 30
        for x in range(num_row):
            pygame.draw.rect(screen, BLACK, (screen_width))
        # A CONTINUER MAIS ON VA PARTIR SUR UNE GENERATION COMME SUR WIKIPEDIA
        # num_col = screen_height // 30
        # self.collision_list = []
        # for i in range(num_col):
        #     pygame.draw.rect(screen, BLACK, (screen_width - 30, screen_height - 30*i, 30, 30))
        #     mur_col_pos = [screen_width - 30, screen_height - 30*i]
        #     self.collision_list.append(mur_col_pos)
        # return self.collision_list


    # def draw(self, screen, cell_size):
    #     for row in range(self.height):
    #         for col in range(self.width):
    #             if self.cells[row][col]:
    #                 pygame.draw.rect(screen, BLACK, (col * cell_size, row * cell_size, cell_size, cell_size))

    # def find_set(self, sets, cell):
    #     for i, s in enumerate(sets):
    #         if cell in s:
    #             return i
    #     return None
    
    # def find_set(self, sets, cell):
    #     for i, s in enumerate(sets):
    #         if cell in s:
    #             return i
    #     return None

    # def generate(self):
    #     sets = [{(row, col)} for row in range(self.height) for col in range(self.width)]

    #     for wall in self.walls:
    #         (cell1, cell2) = wall
    #         (row1, col1), (row2, col2) = cell1, cell2
    #         set1_index = self.find_set(sets, (row1, col1))
    #         set2_index = self.find_set(sets, (row2, col2))

    #         if set1_index != set2_index:
    #             self.cells[row1][col1] = False
    #             sets[set1_index] |= sets[set2_index]
    #             sets.pop(set2_index)
