import pygame
from config import screen, WHITE, DIMENSIONS, BLACK

game_over = False
game_over_background = pygame.image.load("data/game_over_background.png").convert()
game_over_background = pygame.transform.scale(game_over_background, DIMENSIONS)
game_over_background.set_alpha(175)
game_over_text = pygame.image.load("data/game_over_text.png").convert()
game_over_text = pygame.transform.scale(game_over_text, (700, 200))
game_over_text.set_colorkey(BLACK)
main_menu_button = pygame.image.load("data/main_menu_button.png").convert()
main_menu_button = pygame.transform.scale(main_menu_button, (300, 100))

def game_over_screen(game_over, bg_speed):
    global game_over_background, game_over_text, main_menu_button, main_menu_button_rect
    if game_over:
        
        game_over_background = pygame.transform.scale(game_over_background,DIMENSIONS)
        screen.blit(game_over_background, (0, 0))
        screen.blit(game_over_text, (DIMENSIONS[0] // 2 - 350, 100))
        #screen.blit(main_menu_button, (DIMENSIONS[0] // 2 - 150, 400))
        main_menu_button_rect = main_menu_button.get_rect(topleft=(DIMENSIONS[0] // 2 - 50, 400))
        pygame.display.flip()
        bg_speed = 0

