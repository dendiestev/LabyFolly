import pygame
from bdd.requests_bdd import Bdd
from Classes.Button import *

class Leaderboard():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.bdd = Bdd("./bdd/BDD.db")
        self.leaderboar = self.bdd.get_all()[:10]
        self.font = pygame.font.SysFont("Times", 30)
        self.font2 = pygame.font.SysFont("Times", 20)
        self.font3 = pygame.font.SysFont("Times", 15)
        self.breload = Button(screen=self.screen, pos=(565,550), path_img_up="assets/buttons/reload/up.png", path_img_down="assets/buttons/reload/down.png")

    def reload(self):
        self.leaderboar = self.bdd.get_all()[:10]

    def draw_one(self, v):
        value = self.leaderboar[v]

        pygame.draw.rect(self.screen, (100,100,100), (200, (45*v)+50, 980, 45))

        p = self.font.render(f"{value['rank']}", 1, (255,255,255))
        self.screen.blit(p, (205, 45*v+55))

        p = self.font2.render(f"{value['pseudo']}", 1, (255,255,255))
        self.screen.blit(p, (255, 45*v+60))

        p = self.font2.render(f"{value['level']}", 1, (255,255,255))
        self.screen.blit(p, (475, 45*v+60))

        p = self.font2.render(f"{value['timer']}", 1, (255,255,255))
        self.screen.blit(p, (675, 45*v+60))

        p = self.font2.render(f"{value['map']}", 1, (255,255,255))
        self.screen.blit(p, (875, 45*v+60))

        p = self.font2.render(f"{value['character']}", 1, (255,255,255))
        self.screen.blit(p, (1075, 45*v+60))

    def draw_leaderboard(self):
        self.breload.update()
        pygame.draw.rect(self.screen, (0,0,0), (200, 25, 980, 25))
        p = self.font3.render(f"rank", 1, (255,255,255))
        self.screen.blit(p, (205, 30))

        p = self.font3.render(f"pseudo", 1, (255,255,255))
        self.screen.blit(p, (255, 30))

        p = self.font3.render(f"level", 1, (255,255,255))
        self.screen.blit(p, (475, 30))

        p = self.font3.render(f"timer", 1, (255,255,255))
        self.screen.blit(p, (675, 30))

        p = self.font3.render(f"map", 1, (255,255,255))
        self.screen.blit(p, (875, 30))

        p = self.font3.render(f"character", 1, (255,255,255))
        self.screen.blit(p, (1075, 30))
        for i in range(len(self.leaderboar)):
            self.draw_one(i)
