import pygame
import random
from collections import deque

class Enemie:
    def __init__(self, num_cols, num_rows):
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.enemie = {}
        self.shard = {}

    def create_shard(self):
        random_x = None
        random_y = None
        while random_x is None or random_y is None or random_x == random_y or [random_x, random_y] in self.shard.values():
            random_x = random.randint(1, (self.num_cols-1)/2)*2-1
            random_y = random.randint(1, (self.num_rows-1)/2)*2-1
        self.shard[f"{len(self.shard)+1}"] = [random_x, random_y]

    def create_shards(self, number):
        for _ in range(number):
            self.create_shard()

    def create_enemie(self):
        random_x = None
        random_y = None
        while random_x is None or random_y is None or random_x == random_y or [random_x, random_y] in [element[0] for element in self.enemie.values()]:
            random_x = random.randint(1, (self.num_cols-1)/2)*2-1
            random_y = random.randint(1, (self.num_rows-1)/2)*2-1
        direction = ["top", "right", "down", "left"]
        random.shuffle(direction)
        self.enemie[f"{len(self.enemie)+1}"] = [[random_x, random_y], [None,None], direction]
    
    def create_enemies(self, number):
        for _ in range(number):
            self.create_enemie()

    def move_enemie(self, main_liste):
        for cle, val in self.enemie.items():
            direction = val[2]
            move = False
            while not move:
                if direction[0] == "top":
                    if self.canMoveTop(val, main_liste):
                        val[1] = [val[0][0], val[0][1]]
                        self.top(val)
                        move = True
                    else: 
                        direction = direction[1:] + ["top"]

                if direction[0] == "right":
                    if self.canMoveRight(val, main_liste):
                        val[1] = [val[0][0], val[0][1]]
                        self.right(val)
                        move = True
                    else: 
                        direction = direction[1:] + ["right"]

                if direction[0] == "down":
                    if self.canMoveDown(val, main_liste):
                        val[1] = [val[0][0], val[0][1]]
                        self.down(val)
                        move = True
                    else: 
                        direction = direction[1:] + ["down"]

                if direction[0] == "left":
                    if self.canMoveLeft(val, main_liste):
                        val[1] = [val[0][0], val[0][1]]
                        self.left(val)
                        move = True
                    else: 
                        direction = direction[1:] + ["left"]
            val[2] = direction

    """def direction(self):
        enemie = self.enemie["1"]
        parents = self.dico_parents((enemie[0], enemie[1]))
        player_position = (self.player.position_x, self.player.position_y)

        find = player_position
        chemain = []
        while find != (enemie[0], enemie[1]):
            for cle, val in parents.keys():
                if val == find:
                    find = cle
                    chemain.append(val)
        print(chemain)

    def dico_parents(self, depart):
        # Dictionnaire pour stocker le parent de chaque sommet
        parents = {depart: None}
        # Utilisation d'une file pour le parcours en largeur
        file = deque([depart])

        while file:
            sommet_actuel = file.popleft()
            # Parcourir tous les voisins du sommet actuel
            for voisin in self.enemie.get(sommet_actuel, []):
                # Si le voisin n'a pas encore été visité
                if voisin not in parents:
                    parents[voisin] = sommet_actuel  # Définir le parent du voisin
                    file.append(voisin)  # Ajouter le voisin à la file pour le visiter plus tard
        return parents"""

    def top(self, enemie):
        enemie[0][1] -=1

    def down(self, enemie):
        enemie[0][1] += 1

    def right(self, enemie):
        enemie[0][0] += 1
    
    def left(self, enemie):
        enemie[0][0] -= 1
    
    def canMoveTop(self, enemie, main_liste):
        if main_liste[enemie[0][0]][enemie[0][1]-1] in [-1,-2,-3,-4]:
            return False
        else:
            return True
        
    def canMoveDown(self, enemie, main_liste):
        if main_liste[enemie[0][0]][enemie[0][1]+1] in [-1,-2,-3,-4]:
            return False
        else:
            return True
        
    def canMoveLeft(self, enemie, main_liste):
        if main_liste[enemie[0][0]-1][enemie[0][1]] in [-1,-2,-3,-4]:
            return False
        else:
            return True
    
    def canMoveRight(self, enemie, main_liste):
        if main_liste[enemie[0][0]+1][enemie[0][1]] in [-1,-2,-3,-4]:
            return False
        else:
            return True