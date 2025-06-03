import pygame, random
from config import DIMENSIONS, WHITE, screen

class Trap(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/trap.png").convert()
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
trap_properties = Trap()

class TrapManager:
    def __init__(self):
        self.trap_list = pygame.sprite.Group()

    def trap_procedural_generation(self, plat_list):
        self.trap_list.empty()
        for platform in plat_list:
            trap = Trap()
            generation_number = random.randrange(1, 10)
            if generation_number == 1:
                trap_y = platform.rect.top - 40
                trap_x = platform.rect.x + 125
                trap.rect.topleft = (trap_x, trap_y)
                self.trap_list.add(trap)

trap_general = TrapManager()

            
