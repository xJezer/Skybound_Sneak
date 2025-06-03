import pygame
from config import screen, DIMENSIONS
from game_over import game_over_screen
from hp_bar import draw_hp_bar
def game_loop_logic(game_over, all_sprites_list, platform_general, trap_general, bg_manager, rat, cat, cat_final_x, cat_final_x2, cat_pos_y, cat_pos_y_actual, cat_visible, extra_life_manager):
    if not game_over:
        bg_manager.move()

        for hearth in extra_life_manager.extralife_list:
            hearth.rect.y += bg_manager.bg_speed
        for platform in platform_general.platforms_list:
            platform.rect.y += bg_manager.bg_speed
        for trap in trap_general.trap_list:
            trap.rect.y += bg_manager.bg_speed
        bg_manager.draw()

        all_sprites_list.draw(screen)
        extra_life_manager.extralife_list.draw(screen)
        keys = pygame.key.get_pressed()
        rat.move(keys, platform_general.platforms_list, bg_manager.over_floor, bg_manager.bg_speed)
        rat.update_effects()
        rat.rect.topleft = (rat.x, rat.y)

        if bg_manager.floor_y > 875:
            bg_manager.bg_speed = 2
            cat_visible = True
            cat_pos_y = 450
            if cat_pos_y_actual > cat_pos_y:
                cat_pos_y_actual -= bg_manager.bg_speed
            else:
                cat_pos_y_actual = cat_pos_y
        else:
            cat_visible = False
            cat_pos_y_actual = DIMENSIONS[1] + 300
        cat.update_position(cat_final_x, cat_pos_y_actual, cat_final_x2)
        cat.draw(screen, cat_visible)

        game_over, rat.speed_y, rat.is_jumping = draw_hp_bar(
            game_over, cat_visible, rat.rect, rat, cat.rect2, trap_general.trap_list, rat.speed_y, rat.jump_strength, rat.is_jumping, extra_life_manager.extralife_list
        )
        return game_over, cat_pos_y, cat_pos_y_actual, cat_visible, rat.speed_y, rat.is_jumping
    else:
        bg_manager.draw()
        all_sprites_list.draw(screen)
        screen.blit(cat.image, cat.rect)
        main_menu_button_rect = game_over_screen(game_over, bg_manager.bg_speed)
        return game_over, cat_pos_y, cat_pos_y_actual, cat_visible, rat.speed_y, rat.is_jumping, main_menu_button_rect