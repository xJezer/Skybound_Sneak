import pygame
from config import DIMENSIONS, screen

class BackgroundManager:
    def __init__(self):
        self.background = pygame.image.load("data/bg.png").convert()
        self.bg_width = DIMENSIONS[0]
        self.bg_height = int(self.background.get_height() * (self.bg_width / self.background.get_width()) * 1.5)
        self.background = pygame.transform.scale(self.background, (self.bg_width, self.bg_height))
        self.bg_y = -(self.bg_height - DIMENSIONS[1])
        self.bg_speed = 1

        self.floor = pygame.image.load("data/floor.prueba.png").convert()
        self.floor = pygame.transform.scale(self.floor, (1375, 400))
        self.floor_y = 475
        self.over_floor = self.floor_y - 50

    def move(self):
        self.bg_y += self.bg_speed
        self.floor_y += self.bg_speed
        self.over_floor = self.floor_y - 50
        if self.bg_y > self.bg_height * 0.3:
            self.bg_speed = 4
        elif self.bg_y > 0:
            self.bg_speed = 0



    def draw(self):
        screen.blit(self.background, (0, self.bg_y))
        screen.blit(self.floor, (0, self.floor_y))

bg_manager = BackgroundManager()