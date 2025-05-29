import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# -- Pantalla --
DIMENSIONS = (1375, 700)
screen = pygame.display.set_mode((DIMENSIONS))
pygame.display.set_caption("Skybound Sneak")
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)