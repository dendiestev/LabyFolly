import pygame

from Map import *
from Player import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
        pygame.init()
        cell_size = 75
        num_rows = 14
        num_cols = 26
        screen_width = cell_size * num_cols
        screen_height = cell_size * num_rows
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Labyrinthe")
        map = Map(num_cols, num_rows)
        map.generate()
        player = Player(0, 0)
        running = True

        while running:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              running = False
          # Ici, vous pouvez gérer les événements de déplacement du joueur
          screen.fill(WHITE)
          map.draw(screen, cell_size)
          player.draw(screen, cell_size)
          pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    main()