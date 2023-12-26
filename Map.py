import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_LIGHT = (245, 66, 66)
BROWN = (110, 70, 2)
GREEN_LIGHT = (61, 255, 168)

class Map:

    ### Initialisation ###

    def __init__(self, screen, screen_width, screen_height, collision_list=[]):
        self.collision_list = collision_list
        self.main_liste = []
        self.screen_width = screen_width//30
        self.screen_height = screen_height//30
        self.screen = screen
        self.player_collision = []
        self.liste_enemy_collision = []
        self.liste_enemies = []

    ### Dessin ###

    ## -1 => bords
    ## -2 => modifiable (colone)
    ## -3 => modifiable (ligne)
    ## -4 => non-modifiable

    def generer_matrice(self):
        a=1
        for row in range(0, self.screen_width):
            liste = []
            for col in range(0, self.screen_height):
                if col == 0 or row == 0 or row == (self.screen_width - 1) or col == (self.screen_height - 1):
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
        print(self.screen_width, self.screen_height)

    def select_random(self):
        column = 0
        ligne = self.select_line()
        if ligne % 2 == 0:
            column = random.randrange(1, self.screen_height - 1, 2)
        else:
            column = random.randrange(2, self.screen_height - 2, 2)
        return (ligne, column)
    
    def select_line(self):
        return random.randint(1, self.screen_height - 2)

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

    def afficher(self):
        for sous_liste in self.main_liste:
            print(sous_liste)
    
    def afficher2pointzero(self):
        for x in range(len(self.main_liste)):
            for y in range(len(self.main_liste[x])):
                if self.main_liste[x][y] in [-1, -2, -3, -4]:
                    print("#", end="")
                    # pygame.draw.rect(self.screen, BLACK, ((x + 1)*30, (y + 1)*30, 30, 30))
                else:
                    print(" ", end="")
                    # pygame.draw.rect(self.screen, WHITE, ((x + 1)*30, (y + 1)*30, 30, 30))
            print("")

    def afficher_graphique(self):
        liste = []
        for x in range(len(self.main_liste)):
            for y in range(len(self.main_liste[x])):
                if self.main_liste[x][y] in [-1, -2, -3, -4]:
                    colliding_block = pygame.Rect(x*30, y*30, 30, 30)
                    self.player_collision.append(colliding_block)
                    pygame.draw.rect(self.screen, BLACK, colliding_block)
                else:
                    pygame.draw.rect(self.screen, WHITE, ((x)*30, (y)*30, 30, 30))
                    liste.append(x*30)
                    liste.append(y*30)
                    self.liste_enemy_collision.append(liste)
                    liste = []
        for element in self.liste_enemy_collision:
            index = self.liste_enemy_collision.index(element)
            if element in self.liste_enemy_collision[0:index]:
                self.liste_enemy_collision.remove(element)
    
    def set_collider(self, player_rect):
        for obstacle_rect in self.player_collision:
            if player_rect.colliderect(obstacle_rect):
                print("Collision")
    
    def spawn_enemies(self, nombre_enemies, taille_joueur):
        for i in range(nombre_enemies):
            r = random.randint(0, len(self.liste_enemy_collision))
            liste = []
            if random not in liste:
                enemy = pygame.Rect(self.liste_enemy_collision[r][0] + taille_joueur/2, self.liste_enemy_collision[r][1] + taille_joueur/2, taille_joueur, taille_joueur)
                self.liste_enemies.append(enemy)
                liste.append(r)

    def afficher_enemies(self):
        for enemy in self.liste_enemies:
            pygame.draw.rect(self.screen, GREEN_LIGHT, enemy)
