import pygame
from config import screen, WHITE, DIMENSIONS

pygame.init()

heart_0 = pygame.image.load("data/hp_0.png").convert()
heart_0 = pygame.transform.scale(heart_0, (50, 50))
heart_0.set_colorkey(WHITE)
heart_1 = pygame.image.load("data/hp_1.png").convert()
heart_1 = pygame.transform.scale(heart_1, (50, 50))
heart_1.set_colorkey(WHITE)
hp_counter = 3

def draw_hp_bar(game_over, enemy_visible, player_rect, enemy_rect, speed_y, jump_strength, is_jumping, extralife_list):
    global hp_counter, heart_0, heart_1

    screen.blit(heart_0, (10, 10))
    screen.blit(heart_0, (70, 10))
    screen.blit(heart_0, (130, 10))
 
    hearth_collision = False

    for hearth in list(extralife_list):  
        if player_rect.colliderect(hearth.rect):
            extralife_list.remove(hearth)
            hearth_collision = True

    if enemy_visible and player_rect.colliderect(enemy_rect):
        hp_counter -= 1
        speed_y = -jump_strength * 1.5
        is_jumping = True
    
    if hearth_collision and hp_counter < 3:
        hp_counter += 1 

    for i in range(3):
        screen.blit(heart_0, (10 + 60 * i, 10))
    for i in range(hp_counter):
        screen.blit(heart_1, (10 + 60 * i, 10))
    if hp_counter <= 0:
        game_over = True
    return game_over, speed_y, is_jumping