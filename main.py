import pygame
import time
from pygame import mixer

from Classes.MenuManager import *
from Classes.GameManager import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    # mixer.init()
    # m_valo = "textures/valo/valoMusic.mp3"
    # mixer.music.load(m_valo)
    lvl = 0
    cell_size = 60
    num_rows = 5
    num_cols = 5
    screen_width = 1350 #taille de chemin -> 20 * 30 (le nombre de case de chemin + 5 (taille de mur) * 29 (nombre de mur)
    screen_height = 1050
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"Labyrinthe")
    
    running = True
    menuManager = MenuManager(screen)
    user_and_party_info = None

    game_manager = GameManager(screen, screen_width, screen_height, cell_size, num_rows, num_cols, lvl, user_and_party_info)
    
    while running:
        menuManager.update()
        if menuManager.etat == "game":
            game_manager.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_manager.save()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menuManager.etat == "menu":
                        if menuManager.bleaderborad.over():
                            menuManager.etat = "leaderboard"
                        if menuManager.bnew.over():
                            menuManager.etat = "new game"
                        if menuManager.bmulti.over():
                            menuManager.etat = "multi"
                    if menuManager.etat == "leaderboard":
                        if menuManager.l.breload.over():
                            menuManager.l.reload()
                    if menuManager.etat == "new game":
                        if menuManager.newgame.baright.over():
                            if menuManager.newgame.perso < len(menuManager.newgame.liste_perso)-1:
                                menuManager.newgame.perso +=1
                            else:
                                menuManager.newgame.perso = 0
                        if menuManager.newgame.baleft.over():
                            if menuManager.newgame.perso > 0:
                                menuManager.newgame.perso -= 1
                            else:
                                menuManager.newgame.perso = len(menuManager.newgame.liste_perso)-1
                        if menuManager.newgame.bmapcod.over():
                            menuManager.newgame.map = 0
                        if menuManager.newgame.bmapftn.over():
                            menuManager.newgame.map = 1
                        if menuManager.newgame.bmaphp.over():
                            menuManager.newgame.map = 2
                        if menuManager.newgame.bmapmk.over():
                            menuManager.newgame.map = 3
                        if menuManager.newgame.bmapvalo.over():
                            menuManager.newgame.map = 4
                        if menuManager.newgame.bstart.over():
                            check = menuManager.newgame.check()
                            if check == True:
                                user_and_party_info = menuManager.newgame.start()
                                game_manager.user_and_party_info = user_and_party_info
                                menuManager.etat = "game"
                                menuManager.start_the_game == True
                    if menuManager.etat == "multi":
                        if menuManager.multigame.Aright1.over():
                            if menuManager.multigame.p1 < len(menuManager.multigame.liste_perso)-1:
                                menuManager.multigame.p1 +=1
                            else:
                                menuManager.multigame.p1 = 0
                        if menuManager.multigame.AleftJ1.over():
                            if menuManager.multigame.p1 > 0:
                                menuManager.multigame.p1 -= 1
                            else:
                                menuManager.multigame.p1 = len(menuManager.multigame.liste_perso)-1
                        if menuManager.multigame.Aright2.over():
                            if menuManager.multigame.p2 < len(menuManager.multigame.liste_perso)-1:
                                menuManager.multigame.p2 +=1
                            else:
                                menuManager.multigame.p2 = 0
                        if menuManager.multigame.AleftJ2.over():
                            if menuManager.multigame.p2 > 0:
                                menuManager.multigame.p2 -= 1
                            else:
                                menuManager.multigame.p2 = len(menuManager.multigame.liste_perso)-1
                        if menuManager.multigame.bmapcod.over():
                            menuManager.multigame.map_choice = 0
                        if menuManager.multigame.bmapftn.over():
                            menuManager.multigame.map_choice = 1
                        if menuManager.multigame.bmaphp.over():
                            menuManager.multigame.map_choice = 2
                        if menuManager.multigame.bmapmk.over():
                            menuManager.multigame.map_choice = 3
                        if menuManager.multigame.bmapvalo.over():
                            menuManager.multigame.map_choice = 4
                        if menuManager.multigame.bstart.over():
                            check = menuManager.multigame.check()
                if menuManager.etat in ["new game","leaderboard","multi"]:             
                    if menuManager.bback.over():
                        menuManager.etat = "menu"
            if menuManager.etat == "new game":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menuManager.newgame.input_rect.collidepoint(event.pos):
                        menuManager.newgame.active = True
                    else:
                        menuManager.newgame.active = False
        
                if event.type == pygame.KEYDOWN:
        
                    if menuManager.newgame.active:
                        if event.key == pygame.K_BACKSPACE:
                            menuManager.newgame.user_text = menuManager.newgame.user_text[:-1]

                        elif len(menuManager.newgame.user_text)+2 > 15:
                            menuManager.newgame.user_text = "Max 15 charactere"
                        else:
                            menuManager.newgame.user_text += event.unicode
                
        # Déplacement vers le haut, bas, gauche, droite du joueur définit précedement

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_manager.top()
                    pygame.display.update()
                elif event.key == pygame.K_DOWN:
                    game_manager.down()
                    pygame.display.update()
                elif event.key == pygame.K_RIGHT:
                    game_manager.right()
                    pygame.display.update()
                elif event.key == pygame.K_LEFT:
                    game_manager.left()
                    pygame.display.update()
            
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
