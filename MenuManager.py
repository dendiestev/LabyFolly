import pygame
import time

from Button import *
from Leaderboard import *
from NewGame import * 

class MenuManager:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.bleaderborad = Button(screen=self.screen, pos=(590,250), path_img_down="assets/buttons/leaderboard/down.png", path_img_up="assets/buttons/leaderboard/up.png")
        self.bnew = Button(screen=self.screen, pos=(590,320), path_img_down="assets/buttons/new/down.png", path_img_up="assets/buttons/new/up.png")
        self.bload = Button(screen=self.screen, pos=(590,390), path_img_down="assets/buttons/load/down.png", path_img_up="assets/buttons/load/up.png")
        self.bback = Button(screen=self.screen, pos=(590,650), path_img_down="assets/buttons/go_back/down.png", path_img_up="assets/buttons/go_back/up.png")
        self.logo = pygame.image.load("assets/logo/main.png").convert()
        self.l = Leaderboard(screen=self.screen)
        self.newgame = NewGame(self.screen)
        self.etat = "menu"
        self.start_the_game = False

    def update(self):
        if self.etat == "menu":
            self.screen.fill("purple")
            self.screen.blit(self.logo, (290, 50))
            self.bleaderborad.update()
            self.bload.update()
            self.bnew.update()
        if self.etat == "leaderboard":
            self.screen.fill("blue")
            self.l.draw_leaderboard()
            self.bback.update()
        if self.etat == "new game":
            self.screen.fill("red")
            self.newgame.update()
            self.bback.update()
        if time.time() < self.newgame.cooldown+1:
            self.newgame.affiche_error(self.newgame.error)