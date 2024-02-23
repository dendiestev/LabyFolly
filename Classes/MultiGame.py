import pygame

from Button import *

class MultiGame:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.AleftJ1 = Button(screen=self.screen, pos=(880,100), path_img_down="assets/buttons/arrow_left/down.png", path_img_up="assets/buttons/arrow_left/up.png")
        self.Aright1 = Button(screen=self.screen, pos=(880,100), path_img_down="assets/buttons/arrow_left/down.png", path_img_up="assets/buttons/arrow_left/up.png")
        self.AleftJ2 = Button(screen=self.screen, pos=(1030,100), path_img_down="assets/buttons/arrow_right/down.png", path_img_up="assets/buttons/arrow_right/up.png")
        self.Aright2 = Button(screen=self.screen, pos=(1030,100), path_img_down="assets/buttons/arrow_right/down.png", path_img_up="assets/buttons/arrow_right/up.png")
        
        self.liste_perso = ["assets/characters/jonesy.png","assets/characters/jonesy_du_bunker.png","assets/characters/jonesy_sombre.png","assets/characters/jonesy_le_noir.png","assets/characters/jonesy_le_lgbtqia2+.png"]
        self.p1 = 0
        self.p2 = 1

        self.baleft =Button(screen=self.screen, pos=(880,100), path_img_down="assets/buttons/arrow_left/down.png", path_img_up="assets/buttons/arrow_left/up.png")
        self.baright =Button(screen=self.screen, pos=(1030,100), path_img_down="assets/buttons/arrow_right/down.png", path_img_up="assets/buttons/arrow_right/up.png")
        self.bmapcod = Button(screen=self.screen, pos=(300,200), path_img_down="assets/pp/pp_cod.png", path_img_up="assets/pp/pp_cod.png")
        self.bmapftn = Button(screen=self.screen, pos=(550,200), path_img_down="assets/pp/pp_ftn.png", path_img_up="assets/pp/pp_ftn.png")
        self.bmaphp = Button(screen=self.screen, pos=(800,200), path_img_down="assets/pp/pp_hp.png", path_img_up="assets/pp/pp_hp.png")
        self.bmapmk = Button(screen=self.screen, pos=(300,430), path_img_down="assets/pp/pp_mk.png", path_img_up="assets/pp/pp_mk.png")
        self.bmapvalo = Button(screen=self.screen, pos=(550,430), path_img_down="assets/pp/pp_valo.png", path_img_up="assets/pp/pp_valo.png")

        self.bstart =Button(screen=self.screen, pos=(825,455), path_img_down="assets/buttons/start/down.png", path_img_up="assets/buttons/start/up.png")

    def update(self):
        self.AleftJ1.update()
        self.AleftJ2.update()
        self.Aright1.update()
        self.Aright2.update()
        self.baleft.update()
        self.baright.update()
        self.bmapcod.update()
        self.bmapftn.update()
        self.bmaphp.update()
        self.bmapvalo.update()
        self.bstart.update()