import pygame
from config import screen, DIMENSIONS

pygame.init()

WHITE = (255, 255, 255)

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/cat.png").convert()
        self.image = pygame.transform.scale(self.image, (500, 300))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.image2 = pygame.image.load("data/cat_hitbox.png").convert()
        self.image2 = pygame.transform.scale(self.image2, (1365, 300))
        self.image2.set_colorkey(WHITE)
        self.rect2 = self.image2.get_rect()
    
    def draw(self, screen, visible):
        if visible:
            screen.blit(self.image, self.rect)
            screen.blit(self.image2, self.rect2)

    def update_position(self, final_x, pos_y, final_x2):
        self.rect.topleft = (final_x, pos_y)
        self.rect2.topleft = (final_x2, pos_y)

cat = Cat()