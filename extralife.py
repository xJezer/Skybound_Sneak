import pygame, random
WHITE = (255, 255, 255)

class ExtraLife(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/hp_1.png").convert()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

class ExtraLifeManager:
    def __init__(self):
        self.extralife_list = pygame.sprite.Group()
        self.start_y = 2000
        self.spacing_y = 1000
    
    def procedural_generation(self, height, platform_list):
        self.extralife_list.empty()
        for y_pos in range(-self.start_y, -height, -self.spacing_y):
            x1 = random.randrange(350, 800)
            extra1 = ExtraLife()
           
            
            extra1.rect.topleft = (x1, y_pos)
            for platform in platform_list:
                if extra1.rect.colliderect(platform.rect):
                    y_pos -= 50
                    extra1.rect.topleft = (x1, y_pos)

            self.extralife_list.add(extra1)

extra_life_manager = ExtraLifeManager()
