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
        map = Map()

        # Initialisation du joueur grace à Player.py

        p = Player(screen, screen_width - 25, screen_height - 20)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
            screen.fill(WHITE)

            # Affichage de la map grace à Map.py

            map.draw(screen, screen_width, screen_height)
            
            # Affichage du player

            p.draw()

            # Déplacement vers le haut, bas, gauche, droite du joueur définit précedement

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                p.top()
                p.draw()
                pygame.display.update()
            elif keys[pygame.K_DOWN]:
                p.down()
                p.draw()
                pygame.display.update()
            elif keys[pygame.K_RIGHT]:
                p.right()
                p.draw()
                pygame.display.update()
            elif keys[pygame.K_LEFT]:
                p.left()
                p.draw()
                pygame.display.update()
            
            # Vérification pour les bors de la map

            if p.position_x <= 0:
                p.position_x = 0
            if p.position_x >= screen_width - 20:
                p.position_x = screen_width - 20
            if p.position_y <= 0:
                p.position_y = 0
            if p.position_y >= screen_height - 20:
                p.position_y = screen_height - 20
            # for i in range(1):
            #     print(p.position_x, map.collision_list[i])
            #     if p.position_x == map.collision_list[i][0]:
            #         print(p.position_x)
                    
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    main()
