import pygame
import webbrowser
import time

from Classes.Button import *
from Classes.Leaderboard import *
from Classes.NewGame import * 
from Classes.MultiGame import *

class MenuManager:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.bleaderborad = Button(screen=self.screen, pos=(540,590), path_img_down="assets/buttons/leaderboard/lead_new_down.png", path_img_up="assets/buttons/leaderboard/lead_new_up.png")
        self.bnew = Button(screen=self.screen, pos=(540,250), path_img_down="assets/buttons/new/newgame_new_down.png", path_img_up="assets/buttons/new/newgame_new.png")
        self.bmulti = Button(screen=self.screen, pos=(540,420), path_img_down="assets/buttons/multi/1v1_new_down.png", path_img_up="assets/buttons/multi/1v1_new.png")
        self.bback = Button(screen=self.screen, pos=(590,700), path_img_down="assets/buttons/go_back/down.png", path_img_up="assets/buttons/go_back/up.png")
        self.bsite = Button(screen=self.screen, pos=(540,760), path_img_down="assets/buttons/site_web/our_site_btn.png", path_img_up="assets/buttons/site_web/our_site_btn.png")
        self.logo = pygame.image.load("assets/logo/main.png").convert()
        self.site = pygame.image.load("assets/buttons/site_web/our_site_btn.png").convert()
        self.l = Leaderboard(screen=self.screen)
        self.newgame = NewGame(self.screen)
        self.multigame = MultiGame(self.screen)
        self.etat = "menu"
        self.start_the_game = False

    def update(self):
        if self.etat == "menu":
            self.screen.fill((43, 43, 43))
            self.screen.blit(self.logo, (290, 50))
            self.bsite.update()
            self.bleaderborad.update()
            self.bmulti.update()
            self.bnew.update()
        if self.etat == "leaderboard":
            self.screen.fill((238,238,238))
            self.l.draw_leaderboard()
            self.bback.update()
        if self.etat == "new game":
            self.screen.fill("red")
            self.newgame.update()
            self.bback.update()
        if self.etat == "multi":
            self.screen.fill("yellow")
            self.multigame.update()
            self.bback.update()
        if time.time() < self.newgame.cooldown+1:
            self.newgame.affiche_error(self.newgame.error)

    def ouvrir_site_web(self, link:str):
        webbrowser.open(link)