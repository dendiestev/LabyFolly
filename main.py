import pygame

from Map import *
from Player import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
        pygame.init()
        cell_size = 30
        num_rows = 25
        num_cols = 25
        screen_width = cell_size * num_cols
        screen_height = cell_size * num_rows
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Labyrinthe")
        map = Map(num_cols, num_rows)
        map.generate()
        running = True

        while running:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              running = False

          screen.fill(WHITE)

          # Affichage de la map grace à Map.py

          map.draw(screen, cell_size)

          # Initialisation du joueur grace à Player.py

          p = Player(screen, screen_height, 0)
          p.draw()

          # Déplacement vers le haut, bas, gauche, droite du joueur définit précedement

          keys = pygame.key.get_pressed()
          if keys[pygame.K_UP]:
              p.top()
              pygame.display.update()
          elif keys[pygame.K_DOWN]:
              p.down()
              pygame.display.update()
          elif keys[pygame.K_RIGHT]:
              p.right()
              pygame.display.update()
          elif keys[pygame.K_LEFT]:
              p.left()
              pygame.display.update()
              
          p.direction() # Faire un if pour chaque direction et vérifier dans le main
          pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    main()
