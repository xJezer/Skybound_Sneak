import pygame, random
from config import screen, WHITE

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/platform.png").convert()
        self.image = pygame.transform.scale(self.image, (250, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

class PlatformManager:
    def __init__(self):
        self.platforms_list = pygame.sprite.Group()
        self.platform_y = 450
        self.pixels_each_platform = 150

    def procedural_generation(self, height):
        self.platforms_list.empty()
        for plat_y in range(self.platform_y + -self.pixels_each_platform, -height, -self.pixels_each_platform):
            plat_x1 = random.randrange(150, 1000)
            plat_x2 = random.randrange(150, 1000)
            platform1 = Platform()
            platform2 = Platform()
            platform1.rect.topleft = (plat_x1, plat_y)
            platform2.rect.topleft = (plat_x2, plat_y)
            self.platforms_list.add(platform1)
            self.platforms_list.add(platform2)

platform_general = PlatformManager()