import pygame

from Classes.Button import *

class MultiGame:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.AleftJ1 = Button(screen=self.screen, pos=(120,100), path_img_down="assets/buttons/arrow_left/down.png", path_img_up="assets/buttons/arrow_left/up.png")
        self.Aright1 = Button(screen=self.screen, pos=(270,100), path_img_down="assets/buttons/arrow_right/down.png", path_img_up="assets/buttons/arrow_right/up.png")
        self.AleftJ2 = Button(screen=self.screen, pos=(980,100), path_img_down="assets/buttons/arrow_left/down.png", path_img_up="assets/buttons/arrow_left/up.png")
        self.Aright2 = Button(screen=self.screen, pos=(1130,100), path_img_down="assets/buttons/arrow_right/down.png", path_img_up="assets/buttons/arrow_right/up.png")
        
        self.liste_perso = ["assets/characters/jonesy.png","assets/characters/jonesy_du_bunker.png","assets/characters/jonesy_sombre.png","assets/characters/jonesy_le_noir.png","assets/characters/jonesy_le_lgbtqia2+.png"]
        self.p1 = 0
        self.p2 = 1

        self.bmapcod = Button(screen=self.screen, pos=(300,200), path_img_down="assets/pp/pp_cod.png", path_img_up="assets/pp/pp_cod.png")
        self.bmapftn = Button(screen=self.screen, pos=(550,200), path_img_down="assets/pp/pp_ftn.png", path_img_up="assets/pp/pp_ftn.png")
        self.bmaphp = Button(screen=self.screen, pos=(800,200), path_img_down="assets/pp/pp_hp.png", path_img_up="assets/pp/pp_hp.png")
        self.bmapmk = Button(screen=self.screen, pos=(300,430), path_img_down="assets/pp/pp_mk.png", path_img_up="assets/pp/pp_mk.png")
        self.bmapvalo = Button(screen=self.screen, pos=(550,430), path_img_down="assets/pp/pp_valo.png", path_img_up="assets/pp/pp_valo.png")

        self.list_map = [(self.bmapcod.pos[0]-5, self.bmapcod.pos[1]-5, 210,210), (self.bmapftn.pos[0]-5, self.bmapftn.pos[1]-5, 210,210),(self.bmaphp.pos[0]-5, self.bmaphp.pos[1]-5, 210,210),(self.bmapmk.pos[0]-5, self.bmapmk.pos[1]-5, 210,210),(self.bmapvalo.pos[0]-5, self.bmapvalo.pos[1]-5, 210,210)]
        self.map_choice = 0

        self.base_font = pygame.font.SysFont("Monaco", 64)

        self.bstart =Button(screen=self.screen, pos=(825,455), path_img_down="assets/buttons/start/down.png", path_img_up="assets/buttons/start/up.png")

    def draw_perso1(self):
        b = pygame.image.load(self.liste_perso[self.p1]).convert_alpha()
        self.screen.blit(b, (170,70))
        text_surface = self.base_font.render("Player 1", True, (0, 0, 0))
        self.screen.blit(text_surface, (140, 30))

    def draw_perso2(self):
        b = pygame.image.load(self.liste_perso[self.p2]).convert_alpha()
        self.screen.blit(b, (1030,70))
        text_surface = self.base_font.render("Player 2", True, (0, 0, 0))
        self.screen.blit(text_surface, (1000, 30))
    
    def draw_persos(self):
        self.draw_perso1()
        self.draw_perso2()
    
    def draw_buttons(self):
        self.draw_map_choice()
        self.AleftJ1.update()
        self.AleftJ2.update()
        self.Aright1.update()
        self.Aright2.update()
        self.bmapcod.update()
        self.bmapftn.update()
        self.bmapmk.update()
        self.bmaphp.update()
        self.bmapvalo.update()
        self.bstart.update()

    def draw_map_choice(self):
        pygame.draw.rect(self.screen, (255,255,255), self.list_map[self.map_choice])

    def update(self):
        self.draw_buttons()
        self.draw_persos()