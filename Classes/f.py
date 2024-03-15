import pygame
import pygame.freetype
import time

from bdd.requests_bdd import *
from Classes.Map import *
from Classes.Player import *
from Classes.Enemie import *

class GameManager:
    def __init__(self, screen, screen_width, screen_height, cell_size, num_rows, num_cols, lvl, user_and_party_info, nemuManager) -> None:
        self.screen = screen
        self.BDD = Bdd("./bdd/BDD.db")
        self.menu_manager = nemuManager
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.lvl = lvl
        self.user_and_party_info = user_and_party_info
        self.map = Map(screen, cell_size, num_rows, num_cols, None, None, None)
        self.player = Player(self.screen, cell_size, self.num_cols, self.num_rows)
        self.enemie = Enemie(self.num_cols, self.num_rows)
        self.start = False
        self.clock = pygame.time.Clock()
        self.font = pygame.freetype.SysFont("Monaco", 34)
        self.perso_index = 0
        self.map_index = 0
        self.path_liste = ["assets/textures/cod/route_cod.png", "assets/textures/fortnite/herbe_fortnite.png", "assets/textures/hp/brume_hp.png", "assets/textures/mk/terre_mk.png", "assets/textures/valo/neige_valo.png"]
        self.perso_liste = ["assets/characters/jonesy.png","assets/characters/jonesy_du_bunker.png","assets/characters/jonesy_sombre.png","assets/characters/jonesy_le_noir.png","assets/characters/jonesy_le_lgbtqia2+.png"]
        self.dead_perso_liste = ["assets/characters/dead_jonesy.png","assets/characters/dead_jonesy_du_bunker.png","assets/characters/dead_jonesy_sombre.png","assets/characters/dead_jonesy_le_noir.png","assets/characters/dead_jonesy_le_lgbtqia2+.png"]
        self.liste_map = ["assets/textures/cod/mur_cod.png", "assets/textures/fortnite/mur_fortnite.png", "assets/textures/hp/brume_hp.png", "assets/textures/mk/lave_mk.png", "assets/textures/valo/mur_valo.png"]
        self.liste_music = ["assets/textures/cod/cod.mp3", "assets/textures/fortnite/fortnite.mp3", "assets/textures/hp/hp.mp3", "assets/textures/mk/mk.mp3", "assets/textures/valo/valo.mp3"]
        self.life = pygame.image.load("assets/life/life.png")
        self.slime = pygame.image.load("assets/mob/slime.png")
        self.slime2 = pygame.image.load("assets/mob/slime2.png")
        self.Over = False

    def play_music(self):
        pygame.mixer.music.load(self.liste_music[self.map_index])
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

    def gameOver(self):
        self.menu_manager.etat = "game over"
        self.menu_manager.bback.update()
        s = pygame.Surface((1350,1050))
        s.set_alpha(128)
        s.fill((0,0,0)) 
        self.screen.blit(s, (0,0)) 
        font = pygame.freetype.SysFont("Monaco", 128)
        font.render_to(self.screen, (350, 100), "Game Over", pygame.Color('white'))
        perso = pygame.image.load(self.dead_perso_liste[self.perso_index]).convert_alpha()
        perso = pygame.transform.scale(perso, (300, 300))
        self.screen.blit(perso, (500, 200))
    def reset(self):
        self.lvl = 0
        self.cell_size = 60
        self.num_rows = 5
        self.num_cols = 5
        self.player = Player(self.screen, self.cell_size, self.num_cols, self.num_rows)

    def next_lvl(self):
        print(self.liste_map[self.map_index])
        self.screen.fill(BLACK)
        self.player.nextLevel = False
        self.lvl += 1
        pygame.display.set_caption(f"Labyrinthe - Niveau {self.lvl}")
        if self.lvl % 2 == 0:
            self.num_cols += (self.lvl)
            self.num_rows += (self.lvl)
        else:
            self.num_cols += (self.lvl+1)
            self.num_rows += (self.lvl+1)

        if self.screen_width < self.cell_size * self.num_rows or self.screen_height < self.cell_size * self.num_cols:
            if self.cell_size >= 50:
                self.cell_size -= 20
            elif self.cell_size >= 20:
                self.cell_size -= 5
            elif self.cell_size >= 10:
                self.cell_size -= 3
        self.map = Map(self.screen, self.cell_size, self.num_rows, self.num_cols, pygame.image.load(self.perso_liste[self.perso_index]).convert_alpha(), pygame.image.load(self.liste_map[self.map_index]).convert_alpha(), pygame.image.load(self.path_liste[self.map_index]).convert_alpha())
        
        self.play_music()
        
        # Initialisation de la map grace à Map.py
        self.map.generer_matrice()
        self.map.matrice_finale()
        #map.afficher2pointzero()
        # Initialisation du joueur grace à Player.py
        # Set la velocite du joueur proportionnellement à la taille de la fenêtre
        self.screen.fill(BLACK)


        # Affichage de la map grace à Map.py
        self.map.centre()
        self.map.afficher_graphique()
        self.player.cell_size = self.cell_size
        self.player.position_x = self.num_cols-2
        self.player.position_y = self.num_rows-2
        self.enemie = Enemie(self.num_cols, self.num_rows)
        self.enemie.create_enemies(self.lvl+3)
        self.enemie.create_shards(self.lvl*3)
        self.map.afficher_update(self.enemie.enemie, self.enemie.shard)

    def affichage_update(self):
        self.map.afficher_update(self.enemie.enemie, self.enemie.shard)
    
    def update(self):
        if self.Over == False:
            self.showTimer()
            self.showShard()
            self.showLife()
            if self.player.nextLevel == True:
                self.next_lvl()
            if not self.start:
                self.next_lvl()
                self.start = True
            if self.player.power:
                self.map.slime = self.slime2
            else:
                self.map.slime = self.slime
            if self.player.life <= 0:
                self.Over = True
                self.save()
                self.gameOver()
            
    def top(self):
        if self.Over == False:
            self.enemie.move_enemie(self.map.main_liste)
            self.player.top(self.map.main_liste)
            self.player.check_colison(self.enemie.enemie, self.enemie.shard, self.map)
            self.map.afficher_update(self.enemie.enemie, self.enemie.shard)

    def down(self):
        if self.Over == False:
            self.enemie.move_enemie(self.map.main_liste)
            self.player.down(self.map.main_liste)
            self.player.check_colison(self.enemie.enemie, self.enemie.shard, self.map)
            self.map.afficher_update(self.enemie.enemie, self.enemie.shard)

    def right(self):
        if self.Over == False:
            self.enemie.move_enemie(self.map.main_liste)
            self.player.right(self.map.main_liste)
            self.player.check_colison(self.enemie.enemie, self.enemie.shard, self.map)
            self.map.afficher_update(self.enemie.enemie, self.enemie.shard)
        
    def left(self):
        if self.Over == False:
            self.enemie.move_enemie(self.map.main_liste)
            self.player.left(self.map.main_liste)
            self.player.check_colison(self.enemie.enemie, self.enemie.shard, self.map)
            self.map.afficher_update(self.enemie.enemie, self.enemie.shard)

    def save(self):
        if self.user_and_party_info != None:
            ticks = pygame.time.get_ticks()
            millis = ticks%1000
            seconds = int(ticks/1000 % 60)
            minutes = int(ticks/60000 % 24)
            print(self.user_and_party_info)
            self.BDD.update_party(level=self.lvl, timer=f"{minutes}:{seconds}:{millis}", pseudo=self.user_and_party_info[0]["pseudo"])

    def showTimer(self):
        outEnd = pygame.rect.Rect(1150, 150, 175, 300)
        pygame.draw.rect(self.screen, (133, 133, 133), outEnd)
        ticks = pygame.time.get_ticks()
        millis = ticks%1000
        seconds = int(ticks/1000 % 60)
        minutes = int(ticks/60000 % 24)
        out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        self.font.render_to(self.screen, (1160, 188), out, pygame.Color('white'))

    def showShard(self):
        b = pygame.transform.scale(self.map.shard, (80,80))
        self.screen.blit(b, (1140,250))
        self.font.render_to(self.screen, (1220, 275), f"{self.player.shard}", pygame.Color('white'))

    def showLife(self):
        img = pygame.transform.scale(self.life, (40,40))
        if self.player.life >= 1:
            self.screen.blit(img, (1165,350))
        if self.player.life >= 2:
            self.screen.blit(img, (1215,350))
        if self.player.life >= 3:
            self.screen.blit(img, (1265,350))
        pygame.display.flip()

