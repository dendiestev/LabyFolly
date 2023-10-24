import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player:

    ### Initialisation ###
    def __init__(self, row, col):
        self.row = row
        self.col = col

    ### Mouvements ###

    def move(self, dx, dy):
        # Ici, vous pouvez mettre votre logique de déplacement du joueur
        pass

    ### Skin Du Joueur ###

    def draw(self, screen, cell_size):
        # Ici, vous pouvez dessiner le joueur
        pass