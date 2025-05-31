import pygame
from config import WHITE, screen, DIMENSIONS
pygame.init()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_right = pygame.image.load("data/rat.png").convert()
        self.image_right = pygame.transform.scale(self.image_right, (75, 60))
        self.image_right.set_colorkey(WHITE)
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right
        self.rect = self.image.get_rect()
        self.x = 700
        self.y = 415
        self.speed = 10
        self.is_jumping = False 
        self.gravity = 1
        self.jump_strength = 20
        self.speed_y = 0
        self.facing_right = True
    
    def move(self, keys, platforms, over_floor, bg_s):
        self.y += bg_s
        if keys[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= self.speed
            if self.facing_right:
                self.image = self.image_left
                self.facing_right = False
        if keys[pygame.K_RIGHT]:
            if self.x < DIMENSIONS[0] - 50:
                self.x += self.speed
            if not self.facing_right:
                self.image = self.image_right
                self.facing_right = True

        if not self.is_jumping and keys[pygame.K_SPACE]:
            self.is_jumping = True
            self.speed_y = -self.jump_strength

        landed = False
        for platform in platforms:
            if self.speed_y >= 0 and self.rect.colliderect(platform.rect):
                prev_bottom = self.rect.bottom - self.speed_y
                if prev_bottom <= platform.rect.top and 0 <= self.rect.bottom - platform.rect.top < max(self.speed_y, 5):
                    self.y = platform.rect.top - self.rect.height + 1
                    self.is_jumping = False
                    self.speed_y = 0
                    landed = True
                    break

        if not landed and self.y < over_floor:
            self.is_jumping = True

        if self.is_jumping:
            self.y += self.speed_y
            self.speed_y += self.gravity

        if self.y >= over_floor:
            self.y = over_floor
            self.is_jumping = False
            self.speed_y = 0

        self.rect.topleft = (self.x, self.y)

rat = Player()



