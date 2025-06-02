import pygame, sys
from init import init_game
from logic import game_loop_logic
from config import DIMENSIONS, WHITE
from corazones import extra_life_manager

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.bg = pygame.image.load("data/menu_background.prueba.png")
        self.bg = pygame.transform.scale(self.bg, DIMENSIONS)
        self.logo = pygame.image.load("data/menu_title.png")
        self.logo = pygame.transform.scale(self.logo, (DIMENSIONS[0], 300))
        self.logo.set_colorkey(WHITE)
        self.play_bttn = pygame.image.load("data/play_button.png")
        self.play_bttn = pygame.transform.scale(self.play_bttn, (200, 100))
        self.logo_rect = self.logo.get_rect(center = (400, 150))
        self.play_rect = self.play_bttn.get_rect(center = (DIMENSIONS[0] // 2, 400))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_rect.collidepoint(event.pos):
                return "play"
        return None
    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.logo, (0, 0))
        self.screen.blit(self.play_bttn, self.play_rect)
    

def run_game(screen):
    from init import init_game
    from logic import game_loop_logic
    import pygame


    menu = Menu(screen)
    clock = pygame.time.Clock()

    all_sprites_list, cat_final_x, cat_final_x2, cat_pos_y, cat_pos_y_actual, cat_visible, rat, platform_general, trap_general, bg_manager, cat, extra_life_manager.extralife_list = init_game()

    while True:
        in_menu = True
        while in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if menu.handle_event(event) == "play":
                    in_menu = False

            pygame.mixer.init()
            pygame.mixer.music.load("data/musica.mp3")  
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)

            menu.draw()
            pygame.display.flip()
            clock.tick(60)

        all_sprites_list, cat_final_x, cat_final_x2, cat_pos_y, cat_pos_y_actual, cat_visible, rat, platform_general, trap_general, bg_manager, cat, extra_life_manager.extralife_list = init_game()
        game_over = False
        main_menu_button_rect = None

        in_game = True
        while in_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                    if main_menu_button_rect and main_menu_button_rect.collidepoint(event.pos):
                        in_game = False

            result = game_loop_logic(
                game_over, all_sprites_list, platform_general, trap_general, bg_manager, rat, cat,
                cat_final_x, cat_final_x2, cat_pos_y, cat_pos_y_actual, cat_visible, extra_life_manager
            )
            if len(result) == 7:
                game_over, cat_pos_y, cat_pos_y_actual, cat_visible, rat.speed_y, rat.is_jumping, main_menu_button_rect = result
            else:
                game_over, cat_pos_y, cat_pos_y_actual, cat_visible, rat.speed_y, rat.is_jumping = result

            pygame.display.flip()
            clock.tick(60)
 