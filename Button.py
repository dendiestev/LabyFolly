import pygame


class Button():
    def __init__(self, screen, path_img_up, path_img_down, pos):
        self.button_up = path_img_up
        self.button_down = path_img_down
        self.screen = screen
        self.button = self.button_up
        self.pos = pos
        self.button_size = pygame.image.load(self.button).convert().get_size()

    def draw(self):
        b = pygame.image.load(self.button).convert_alpha()
        self.screen.blit(b, self.pos)

    def over(self):
        if pygame.mouse.get_pos()[0] >= self.pos[0] and pygame.mouse.get_pos()[0] <= self.pos[0]+self.button_size[0] and pygame.mouse.get_pos()[1] >= self.pos[1] and pygame.mouse.get_pos()[1] <= self.pos[1]+self.button_size[1]:
            self.button = self.button_down
            return True
        else:
            self.button = self.button_up
            return False

    def update(self):
        self.over()
        self.draw()