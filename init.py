import pygame
from config import DIMENSIONS
from background import bg_manager
from platforms import platform_general
from trap import trap_general, trap_properties
from player import rat
from enemy import cat
from corazones import extra_life_manager


def init_game():
    platform_general.procedural_generation(bg_manager.bg_height)
    extra_life_manager.procedural_generation(bg_manager.bg_height, platform_general.platforms_list)
    trap_general.trap_procedural_generation(platform_general.platforms_list)
    trap_properties.rect = trap_properties.image.get_rect()
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(rat)
    all_sprites_list.add(platform_general.platforms_list)
    all_sprites_list.add(trap_general.trap_list)
    cat_final_x = 400
    cat_final_x2 = 0
    cat_pos_y = DIMENSIONS[1] + 300
    cat_pos_y_actual = DIMENSIONS[1] + 300
    cat_visible = False

    return all_sprites_list, cat_final_x, cat_final_x2, cat_pos_y, cat_pos_y_actual, cat_visible, rat, platform_general, trap_general, bg_manager, cat, extra_life_manager.extralife_list
