import pygame
import time
from pygame import mixer

from Classes.MenuManager import *
from Classes.GameManager import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    mixer.init()
    lvl = 0
    cell_size = 60
    num_rows = 5
    num_cols = 5
    screen_width = 1350 # Taille de chemin -> 20 * 30 (le nombre de case de chemin + 5 (taille de mur) * 29 (nombre de mur) (NORMALEMENT 1350)
    screen_height = 1050
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"LabyFunny - Départ")
    
    running = True
    menuManager = MenuManager(screen)
    user_and_party_info = None

    game_manager = GameManager(screen, screen_width, screen_height, cell_size, num_rows, num_cols, lvl, user_and_party_info, menuManager)
    
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
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.etat = "leaderboard"
                        if menuManager.bnew.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.etat = "new game"
                        if menuManager.bmulti.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.etat = "multi"
                        if menuManager.site.get_rect(topleft=(540,760)).collidepoint(event.pos):
                            menuManager.ouvrir_site_web("http://127.0.0.1:5000")
                    if menuManager.etat == "leaderboard":
                        if menuManager.l.breload.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.l.reload()
                    if menuManager.etat == "new game":
                        if menuManager.newgame.baright.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            if menuManager.newgame.perso_index < len(menuManager.newgame.liste_perso)-1:
                                menuManager.newgame.perso_index +=1
                            else:
                                menuManager.newgame.perso_index = 0
                        if menuManager.newgame.baleft.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            if menuManager.newgame.perso_index > 0:
                                menuManager.newgame.perso_index -= 1
                            else:
                                menuManager.newgame.perso_index = len(menuManager.newgame.liste_perso)-1
                        if menuManager.newgame.bmapcod.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.newgame.map_index = 0
                        if menuManager.newgame.bmapftn.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.newgame.map_index = 1
                        if menuManager.newgame.bmaphp.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.newgame.map_index = 2
                        if menuManager.newgame.bmapmk.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.newgame.map_index = 3
                        if menuManager.newgame.bmapvalo.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.newgame.map_index = 4
                        if menuManager.newgame.bstart.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            check = menuManager.newgame.check()
                            if check == True:
                                user_and_party_info = menuManager.newgame.start()
                                game_manager.user_and_party_info = user_and_party_info
                                menuManager.etat = "game"
                                menuManager.start_the_game == True
                                game_manager.perso_index = menuManager.newgame.perso_index
                                game_manager.map_index = menuManager.newgame.map_index
                    if menuManager.etat == "multi":
                        if menuManager.multigame.Aright1.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            if menuManager.multigame.p1 < len(menuManager.multigame.liste_perso)-1:
                                menuManager.multigame.p1 +=1
                            else:
                                menuManager.multigame.p1 = 0
                        if menuManager.multigame.AleftJ1.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            if menuManager.multigame.p1 > 0:
                                menuManager.multigame.p1 -= 1
                            else:
                                menuManager.multigame.p1 = len(menuManager.multigame.liste_perso)-1
                        if menuManager.multigame.Aright2.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            if menuManager.multigame.p2 < len(menuManager.multigame.liste_perso)-1:
                                menuManager.multigame.p2 +=1
                            else:
                                menuManager.multigame.p2 = 0
                        if menuManager.multigame.AleftJ2.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            if menuManager.multigame.p2 > 0:
                                menuManager.multigame.p2 -= 1
                            else:
                                menuManager.multigame.p2 = len(menuManager.multigame.liste_perso)-1
                        if menuManager.multigame.bmapcod.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.multigame.map_choice = 0
                        if menuManager.multigame.bmapftn.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.multigame.map_choice = 1
                        if menuManager.multigame.bmaphp.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.multigame.map_choice = 2
                        if menuManager.multigame.bmapmk.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.multigame.map_choice = 3
                        if menuManager.multigame.bmapvalo.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.multigame.map_choice = 4
                        if menuManager.multigame.bstart.over():
                            pygame.mixer.music.load("sound/click_sound.mp3")
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_volume(.2)
                            menuManager.multigame.soon()
                if menuManager.etat in ["new game","leaderboard","multi", "game over"]:             
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
                if event.key == pygame.K_SPACE:
                    if game_manager.player.shard > 0:
                        game_manager.player.power_step += 10
                        game_manager.player.power = True
                        game_manager.player.shard -= 1
                        game_manager.affichage_update()
                    pygame.display.update()
            
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
