import pygame
import time

from Map import *
from Player import *
from Button import *
from Leaderboard import *
from NewGame import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



def main():
    # pygame setup
    screen_etat = 0
    etat = "menu"
    pygame.init()
    screen = pygame.display.set_mode((1050, 750))
    clock = pygame.time.Clock()
    running = True
    bleaderborad = Button(screen=screen, pos=(440,250), path_img_down="assets/buttons/leaderboard/down.png", path_img_up="assets/buttons/leaderboard/up.png")
    bnew = Button(screen=screen, pos=(440,320), path_img_down="assets/buttons/new/down.png", path_img_up="assets/buttons/new/up.png")
    bload = Button(screen=screen, pos=(440,390), path_img_down="assets/buttons/load/down.png", path_img_up="assets/buttons/load/up.png")
    bback = Button(screen=screen, pos=(465,650), path_img_down="assets/buttons/go_back/down.png", path_img_up="assets/buttons/go_back/up.png")
    l = Leaderboar(screen=screen)
    newgame = NewGame(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if etat == "menu":
                        if bleaderborad.over():
                            etat = "leaderboard"
                        if bnew.over():
                            etat = "new game"
                        if bload.over():
                            etat = "load game"
                    if etat == "leaderboard":
                        if l.breload.over():
                            l.reload()
                    if etat == "new game":
                        if newgame.baright.over():
                            if newgame.perso < len(newgame.liste_perso)-1:
                                newgame.perso +=1
                            else:
                                newgame.perso = 0
                        if newgame.baleft.over():
                            if newgame.perso > 0:
                                newgame.perso -= 1
                            else:
                                newgame.perso = len(newgame.liste_perso)-1
                        if newgame.bmapcod.over():
                            newgame.map = 0
                        if newgame.bmapftn.over():
                            newgame.map = 1
                        if newgame.bmaphp.over():
                            newgame.map = 2
                        if newgame.bmapmk.over():
                            newgame.map = 3
                        if newgame.bmapvalo.over():
                            newgame.map = 4
                        if newgame.bstart.over():
                            check = newgame.check()
                            print(newgame.error)
                            print(check)
                            print(newgame.cooldown)
                            print(newgame.error)
                            if check == True:
                                newgame.start()
                                etat = "game"
                if etat in ["new game","leaderboard"]:             
                    if bback.over():
                        etat = "menu"
            if etat == "new game":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if newgame.input_rect.collidepoint(event.pos):
                        newgame.active = True
                    else:
                        newgame.active = False
        
                if event.type == pygame.KEYDOWN:
        
                    if newgame.active:
                        if event.key == pygame.K_BACKSPACE:
                            newgame.user_text = newgame.user_text[:-1]

                        elif len(newgame.user_text)+2 > 15:
                            newgame.user_text = "Max 15 charactere"
                        else:
                            
                            newgame.user_text += event.unicode
        # to show buttons created
        if etat == "menu":
            screen.fill("purple")
            logo = pygame.image.load("assets/logo/main.png").convert()
            screen.blit(logo, (140, 50))
            bleaderborad.update()
            bload.update()
            bnew.update()
        if etat == "leaderboard":
            screen.fill("blue")
            l.draw_leaderboard()
            bback.update()
        if etat == "new game":
            screen.fill("red")
            newgame.update()
            bback.update()
        if time.time() < newgame.cooldown+1:
            newgame.affiche_error(newgame.error)
        if etat == "load game":
            screen.fill("green")
            bback.update()
        if etat == "game":
            screen.fill("yellow")

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

pygame.quit()

if __name__ == "__main__":
    main()
