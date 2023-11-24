import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Map:

    ### Création ###

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[False] * width for _ in range(height)]
        self.walls = []  # Liste des murs

        # Initialisez les murs et les cellules
        for row in range(height):
            for col in range(width):
                if row % 2 == 0 and col % 2 == 0:
                    continue
                self.cells[row][col] = True

                # Ajoutez les murs verticaux
                if col > 0:
                    self.walls.append(((row, col), (row, col - 1)))
                if col < width - 1:
                    self.walls.append(((row, col), (row, col + 1)))

                # Ajoutez les murs horizontaux
                if row > 0:
                    self.walls.append(((row, col), (row - 1, col)))
                if row < height - 1:
                    self.walls.append(((row, col), (row + 1, col)))

        random.shuffle(self.walls)  # Mélangez la liste des murs

    

    def find_set(self, sets, cell):
        for i, s in enumerate(sets):
            if cell in s:
                return i
        return None



    """
    ### Génaration ###

    def generate(self):
        sets = [{(row, col)} for row in range(self.height) for col in range(self.width)]

        for wall in self.walls:
            (cell1, cell2) = wall
            set1_index = self.find_set(sets, cell1)
            set2_index = self.find_set(sets, cell2)

            if set1_index != set2_index:
                self.cells[cell1[0]][cell1[1]] = False
                sets[set1_index] |= sets[set2_index]
                sets.pop(set2_index)

    def generate(self):
    # Ici, vous pouvez mettre votre logique de génération de labyrinthe
        pass
    """
    
    def find_set(self, sets, cell):
        for i, s in enumerate(sets):
            if cell in s:
                return i
        return None

    def generate(self):
        sets = [{(row, col)} for row in range(self.height) for col in range(self.width)]

        for wall in self.walls:
            (cell1, cell2) = wall
            (row1, col1), (row2, col2) = cell1, cell2
            set1_index = self.find_set(sets, (row1, col1))
            set2_index = self.find_set(sets, (row2, col2))

            if set1_index != set2_index:
                self.cells[row1][col1] = False
                sets[set1_index] |= sets[set2_index]
                sets.pop(set2_index)


    ### Dessin ###
    def draw(self, screen, screen_width, screen_height): 
        pygame.draw.rect(screen, BLACK, (screen_width - 50, screen_height - 50, 50, 50))
    # def draw(self, screen, cell_size):
    #     for row in range(self.height):
    #         for col in range(self.width):
    #             if self.cells[row][col]:
    #                 pygame.draw.rect(screen, BLACK, (col * cell_size, row * cell_size, cell_size, cell_size))
