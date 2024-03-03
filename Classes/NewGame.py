import pygame
from Classes.Button import *
from bdd.requests_bdd import *
import time

class NewGame():
    def __init__(self, screen) -> None:
        self.cooldown = 0
        self.error = None

        self.screen = screen
        self.liste_perso = ["assets/characters/jonesy.png","assets/characters/jonesy_du_bunker.png","assets/characters/jonesy_sombre.png","assets/characters/jonesy_le_noir.png","assets/characters/jonesy_le_lgbtqia2+.png"]
        self.perso_index = 0

        self.BDD = Bdd("./bdd/BDD.db")
        
        self.baleft =Button(screen=self.screen, pos=(880,100), path_img_down="assets/buttons/arrow_left/down.png", path_img_up="assets/buttons/arrow_left/up.png")
        self.baright =Button(screen=self.screen, pos=(1030,100), path_img_down="assets/buttons/arrow_right/down.png", path_img_up="assets/buttons/arrow_right/up.png")
        self.bmapcod = Button(screen=self.screen, pos=(300,200), path_img_down="assets/pp/pp_cod.png", path_img_up="assets/pp/pp_cod.png")
        self.bmapftn = Button(screen=self.screen, pos=(550,200), path_img_down="assets/pp/pp_ftn.png", path_img_up="assets/pp/pp_ftn.png")
        self.bmaphp = Button(screen=self.screen, pos=(800,200), path_img_down="assets/pp/pp_hp.png", path_img_up="assets/pp/pp_hp.png")
        self.bmapmk = Button(screen=self.screen, pos=(300,430), path_img_down="assets/pp/pp_mk.png", path_img_up="assets/pp/pp_mk.png")
        self.bmapvalo = Button(screen=self.screen, pos=(550,430), path_img_down="assets/pp/pp_valo.png", path_img_up="assets/pp/pp_valo.png")

        self.bstart =Button(screen=self.screen, pos=(825,455), path_img_down="assets/buttons/start/down.png", path_img_up="assets/buttons/start/up.png")
        
        self.list_map = [(self.bmapcod.pos[0]-5, self.bmapcod.pos[1]-5, 210,210), (self.bmapftn.pos[0]-5, self.bmapftn.pos[1]-5, 210,210),(self.bmaphp.pos[0]-5, self.bmaphp.pos[1]-5, 210,210),(self.bmapmk.pos[0]-5, self.bmapmk.pos[1]-5, 210,210),(self.bmapvalo.pos[0]-5, self.bmapvalo.pos[1]-5, 210,210)]
        self.map_index = 0

        self.base_font2 = pygame.font.SysFont("Monaco", 32)
        self.base_font = pygame.font.SysFont("Monaco", 32)
        self.user_text = 'Your pseudo'

        self.input_rect = pygame.Rect(160, 100, 300, 50)

        self.color_active = pygame.Color((120, 120, 120))
        
        self.color_passive = pygame.Color((100, 100, 100))
        self.color = self.color_passive
        
        self.active = False
    
    def affiche_error(self, error):
        pygame.draw.rect(self.screen, (209,30,30), (50,0, 950, 50))
        if error == 1:
            text_surface2 = self.base_font2.render("Pseudo invalid", True, (255, 255, 255))
        if error == 2:
            text_surface2 = self.base_font2.render("Pseudo invalid", True, (255, 255, 255))
        self.screen.blit(text_surface2, ((525)-(14*5), 15))
    
    def check_space(self):
        if " " in self.user_text:
            return True
        return False
    
    def check(self):
        data = self.BDD.get_all()
        if self.user_text in ["", "Max 15 charactere",'Your pseudo']:
            self.error = 1
            self.cooldown = time.time()
            return False
        if self.check_space():
            self.error = 2
            self.cooldown = time.time()
            return False
        for i in data:
            if i["pseudo"] == self.user_text:
                self.cooldown = time.time()
                self.error = 1
                return False
        return True

    def start(self):
        print("start")
        self.BDD.create_player(pseudo=self.user_text, character=self.perso_index)
        self.BDD.create_party(player=self.user_text, timer="00:00:00",level=1,map=self.map_index)
        print(self.user_text, self.perso_index, self.map_index)
        return (self.BDD.get_player, self.BDD.get_party)

    def draw_perso(self):
        b = pygame.image.load(self.liste_perso[self.perso_index]).convert_alpha()
        self.screen.blit(b, (930,70))

    def update(self):
        pygame.draw.rect(self.screen, (255,255,255), self.list_map[self.map_index])

        self.bstart.update()
        self.draw_perso()
        self.baright.update()
        self.baleft.update()
        self.bmapvalo.update()
        self.bmapcod.update()
        self.bmapftn.update()
        self.bmaphp.update()
        self.bmapmk.update()

        

        if self.active:
            self.color = self.color_active
        else:
            if self.user_text == "Max 15 charactères":
                self.user_text = 'Your pseudo'
            self.color = self.color_passive
            
        pygame.draw.rect(self.screen, self.color, self.input_rect)
    
        text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
        
        self.screen.blit(text_surface, ((270)-(len(self.user_text)*2), self.input_rect.y+15))
