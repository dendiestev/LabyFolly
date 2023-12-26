import pygame

from Map import *
from Player import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
        pygame.init()
        cell_size = 30
        num_rows = 25
        num_cols = 35
        screen_width = 21*30 #taille de chemin -> 20 * 30 (le nombre de case de chemin + 5 (taille de mur) * 29 (nombre de mur)
        screen_height = 21*30
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Labyrinthe")
        map = Map(screen, screen_width, screen_height)
        map.generer_matrice()
        map.matrice_finale()
        map.afficher2pointzero()
        # Initialisation du joueur grace à Player.py
        # Set la velocite du joueur proportionnellement à la taille de la fenêtre
        p = Player(screen, screen_width - 52.5, screen_height - 52.5, .1)
        map.set_collider(p.player)

        screen.fill(WHITE)

        # Affichage de la map grace à Map.py

        map.afficher_graphique()
        map.spawn_enemies(15, 15)
        map.afficher_enemies()
                
        # Affichage du player

        p.draw()
        
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            # Déplacement vers le haut, bas, gauche, droite du joueur définit précedement

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                p.clear_player()
                p.top()
                p.draw()
                pygame.display.update()
            elif keys[pygame.K_DOWN]:
                p.clear_player()
                p.down()
                p.draw()
                pygame.display.update()
            elif keys[pygame.K_RIGHT]:
                p.clear_player()
                p.right()
                p.draw()
                pygame.display.update()
            elif keys[pygame.K_LEFT]:
                p.clear_player()
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
            
            # for i in range(len(map.collision_list)):
            #     if p.position_x < map.collision_list[i][0]:
            #         p.position_x += p.vel
            # print(map.collision_list)

            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    main()

# TO DO:
# - Finir la fonction de collision
