import pygame
import pygame.freetype
import time

from bdd.requests_bdd import *
from Classes.Map import *
from Classes.Player import *
from Classes.Enemie import *

class GameManager:
    def __init__(self, screen, screen_width, screen_height, cell_size, num_rows, num_cols, lvl, user_and_party_info) -> None:
        self.screen = screen
        self.BDD = Bdd("./bdd/BDD.db")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.lvl = lvl
        self.user_and_party_info = user_and_party_info
        self.map = Map(screen, cell_size, num_rows, num_cols, None, None)
        self.player = Player(self.screen, cell_size, self.num_cols, self.num_rows)
        self.enemie = Enemie(self.num_cols, self.num_rows)
        self.start = False
        self.clock = pygame.time.Clock()
        self.font = pygame.freetype.SysFont(None, 34)

    def next_lvl(self):
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
            if self.cell_size >= 60:
                self.cell_size -= 20
            elif self.cell_size >= 30:
                self.cell_size -= 5
            elif self.cell_size >= 10:
                self.cell_size -= 3
        self.map = Map(self.screen, self.cell_size, self.num_rows, self.num_cols, pygame.image.load("assets/characters/njonesy_topview.png").convert_alpha(), pygame.image.load("assets/textures/valo/mur_valo.png").convert_alpha())

        self.map.generer_matrice()
        self.map.matrice_finale()
        #map.afficher2pointzero()
        # Initialisation du joueur grace à Player.py
        # Set la velocite du joueur proportionnellement à la taille de la fenêtre
        self.screen.fill(BLACK)


        # Affichage de la map grace à Map.py
        self.map.centre()
        self.map.afficher_graphique()
        self.player = Player(self.screen, self.cell_size, self.num_cols, self.num_rows)
        self.enemie = Enemie(self.num_cols, self.num_rows)
        self.enemie.create_enemies(self.lvl+3)
        self.enemie.create_shards(self.lvl*3)
        self.map.afficher_update(self.enemie.enemie, self.enemie.shard)

    def update(self):
        self.showTimer()
        if self.player.nextLevel == True:
            self.next_lvl()
        if not self.start:
            self.next_lvl()
            self.start = True
    
    def top(self):
        self.enemie.move_enemie(self.map.main_liste)
        self.player.top(self.map.main_liste)
        self.map.afficher_update(self.enemie.enemie, self.enemie.shard)

    def down(self):
        self.enemie.move_enemie(self.map.main_liste)
        self.player.down(self.map.main_liste)
        self.map.afficher_update(self.enemie.enemie, self.enemie.shard)

    def right(self):
        self.enemie.move_enemie(self.map.main_liste)
        self.player.right(self.map.main_liste)
        self.map.afficher_update(self.enemie.enemie, self.enemie.shard)
        
    def left(self):
        self.enemie.move_enemie(self.map.main_liste)
        self.player.left(self.map.main_liste)
        self.map.afficher_update(self.enemie.enemie, self.enemie.shard)

    def save(self):
        self.BDD.update_party(level=self.lvl, timer=self.time)

    def showTimer(self):
        outEnd = pygame.rect.Rect(100, 100, 500, 100)
        pygame.draw.rect(self.screen, (0, 0, 0), outEnd)
        ticks = pygame.time.get_ticks()
        millis = ticks%1000
        seconds = int(ticks/1000 % 60)
        minutes = int(ticks/60000 % 24)
        out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        self.font.render_to(self.screen, (100, 100), out, pygame.Color('white'))
        pygame.display.flip()
        self.clock.tick(60)