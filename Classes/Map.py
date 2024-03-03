import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_LIGHT = (245, 66, 66)
BROWN = (110, 70, 2)
GREEN_LIGHT = (61, 255, 168)
YELLOW = (240, 191, 31)
PINK_LIGHT = (196, 59, 244)

class Map:

    ### Initialisation ###

    def __init__(self, screen, cell_size, num_rows, num_cols, jonesy, mur, player_collision=[], collision_list=[]):
        self.collision_list = collision_list
        self.main_liste = []
        self.cell_size = cell_size
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.screen_width = self.num_cols * self.cell_size
        self.screen_height = self.num_rows * self.cell_size
        self.screen = screen
        self.player_collision = player_collision
        self.start = (0,0)
        self.jonesy = jonesy
        self.slime = pygame.image.load("assets/mob/slime.png")
        self.shard = pygame.image.load("assets/shard/shard.png")
        self.mur = mur

    def centre(self):
        screen_size = self.screen.get_size()
        self.pas_droite = ((screen_size[0]-self.screen_width)/2)
        self.pas_bas = ((screen_size[1]-self.screen_height)/2)

    ### Dessin ###

    ## -1 => bords
    ## -2 => modifiable (colone)
    ## -3 => modifiable (ligne)
    ## -4 => non-modifiable

    def generer_matrice(self):
        a=1
        for row in range(0, self.num_cols):
            liste = []
            for col in range(0, self.num_rows):
                if col == 0 or row == 0 or row == (self.num_cols - 1) or col == (self.num_rows - 1):
                    liste.append(-1)
                elif row % 2 == 1:
                    if col%2==1:
                        liste.append(a) 
                        a+=1
                    else:
                        liste.append(-3)
                elif row%2==0 and col%2 ==0:
                    liste.append(-4)
                else:
                    liste.append(-2)
            self.main_liste.append(liste)

    def select_random(self):
        column = 0
        ligne = self.select_line()
        if ligne % 2 == 0:
            column = random.randrange(1, self.num_rows - 1, 2)
        else:
            column = random.randrange(2, self.num_rows - 2, 2)
        return (ligne, column)
    
    def select_line(self):
        return random.randint(1, self.num_rows - 2)

    def casser(self):
        l, c = self.select_random() 
        var = 0
        supp = 0
        # print(l, c)
        if self.main_liste[l][c] == -2:
            if self.main_liste[l - 1][c] != self.main_liste[l + 1][c]:
                if self.main_liste[l - 1][c] < self.main_liste[l + 1][c]:
                    supp = self.main_liste[l + 1][c]
                    var = self.main_liste[l - 1][c]
                    self.main_liste[l][c] = var
                    self.main_liste[l + 1][c] = var
                else:
                    var = self.main_liste[l + 1][c]
                    supp = self.main_liste[l - 1][c]
                    self.main_liste[l][c] = var
                    self.main_liste[l - 1][c] = var
        elif self.main_liste[l][c] == -3:
            if self.main_liste[l][c - 1] != self.main_liste[l][c + 1]:
                if self.main_liste[l][c - 1] < self.main_liste[l][c + 1]:
                    supp = self.main_liste[l][c + 1]
                    var = self.main_liste[l][c - 1]
                    self.main_liste[l][c] = var
                    self.main_liste[l][c + 1] = var
                else:
                    supp = self.main_liste[l][c - 1]
                    var = self.main_liste[l][c + 1]
                    self.main_liste[l][c] = var
                    self.main_liste[l][c - 1] = var
        for x in range(len(self.main_liste)):
            for y in range(len(self.main_liste[x])):
                if self.main_liste[x][y] == supp:
                    self.main_liste[x][y] = var
    
    def labyrinthe_complet(self) -> bool:
        for sous_liste in self.main_liste:
            for i in sous_liste:
                if not i in [-1, -2, -3, -4, 1]:
                    return False
        return True
    
    def matrice_finale(self):
        while self.labyrinthe_complet() == False:
            self.casser()
        self.main_liste[len(self.main_liste) - 2][len(self.main_liste) - 2] = 7
    

    def afficher(self):
        for sous_liste in self.main_liste:
            print(sous_liste)
    
    def afficher2pointzero(self):
        for x in range(len(self.main_liste)):
            for y in range(len(self.main_liste[x])):
                if self.main_liste[x][y] in [-1, -2, -3, -4]:
                    print(self.main_liste[x][y], end="")
                    # pygame.draw.rect(self.screen, BLACK, ((x + 1)*30, (y + 1)*30, 30, 30))
                else:
                    print(self.main_liste[x][y], end="")
                    # pygame.draw.rect(self.screen, WHITE, ((x + 1)*30, (y + 1)*30, 30, 30))
            print("")

    def afficher_graphique(self):
        for x in range(len(self.main_liste)):
            for y in range(len(self.main_liste[x])):
                if self.main_liste[x][y] in [-1, -2, -3, -4]:
                    colliding_block = pygame.Rect(x*self.cell_size + self.pas_droite, y*self.cell_size + self.pas_bas, self.cell_size, self.cell_size)
                    self.player_collision.append(colliding_block)
                    self.mur = pygame.transform.scale(self.mur, (self.cell_size, self.cell_size))
                    self.screen.blit(self.mur, (x*self.cell_size + self.pas_droite, y*self.cell_size + self.pas_bas))
                    # pygame.draw.rect(self.screen, BLACK, colliding_block)
                else:
                    pygame.draw.rect(self.screen, WHITE, (x*self.cell_size+ self.pas_droite, y*self.cell_size + self.pas_bas, self.cell_size, self.cell_size))
    
    
    def afficher_update(self, dico_enemie:dict, dico_shard:dict):
        for x in range(len(self.main_liste)):
            for y in range(len(self.main_liste[x])):
                if self.main_liste[x][y] == 0:
                    pygame.draw.rect(self.screen, WHITE, (x*self.cell_size+ self.pas_droite, y*self.cell_size + self.pas_bas, self.cell_size, self.cell_size))
                    self.main_liste[x][y] = 1
                if [x,y] in [element[1] for element in dico_enemie.values()]:
                    pygame.draw.rect(self.screen, WHITE, (x*self.cell_size+ self.pas_droite, y*self.cell_size + self.pas_bas, self.cell_size, self.cell_size))
                if x == len(self.main_liste)-2 and y == len(self.main_liste[x])-2:
                    colliding_block = pygame.Rect(x*self.cell_size+ self.pas_droite, y*self.cell_size + self.pas_bas, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, YELLOW, colliding_block)
                if x == 1 and y == 1:
                    colliding_block = pygame.Rect(x*self.cell_size+ self.pas_droite, y*self.cell_size + self.pas_bas, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, YELLOW, colliding_block)
                    self.finish = (x,y)
                if [x,y] in [element[0] for element in dico_enemie.values()]:
                    # colliding_block = pygame.Rect(x*self.cell_size+ self.pas_droite + self.cell_size/4, y*self.cell_size + self.pas_bas + self.cell_size/4, self.cell_size/2, self.cell_size/2)
                    # pygame.draw.rect(self.screen, GREEN_LIGHT, colliding_block)
                    self.slime = pygame.transform.scale(self.slime, (self.cell_size/2, self.cell_size/2))
                    self.screen.blit(self.slime, (x*self.cell_size+ self.pas_droite + self.cell_size/4, y*self.cell_size + self.pas_bas + self.cell_size/4))
                if [x,y] in dico_shard.values():
                    # colliding_block = pygame.Rect(x*self.cell_size+ self.pas_droite + self.cell_size/4, y*self.cell_size + self.pas_bas + self.cell_size/4, self.cell_size/2, self.cell_size/2)
                    # pygame.draw.rect(self.screen, PINK_LIGHT, colliding_block)
                    self.shard = pygame.transform.scale(self.shard, (self.cell_size/2, self.cell_size/2))
                    self.screen.blit(self.shard, (x*self.cell_size+ self.pas_droite + self.cell_size/4, y*self.cell_size + self.pas_bas + self.cell_size/4))
                
                if self.main_liste[x][y] == 7:
                    self.jonesy = pygame.transform.scale(self.jonesy, (self.cell_size/2, self.cell_size/2))
                    self.screen.blit(self.jonesy, (x*self.cell_size+ self.pas_droite + self.cell_size/4, y*self.cell_size + self.pas_bas + self.cell_size/4))