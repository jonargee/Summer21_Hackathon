import pygame
import pygame.freetype
from pygame.sprite import Sprite
from music import play_title_scr_music, play_level_music, play_meow_fx
from enum import Enum
from pygame.rect import Rect

GREEN = (78, 245, 56)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """creates menu surface"""
    font = pygame.freetype.SysFont("Impact", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1


class UIElement(Sprite):
    """UI for menu buttons"""
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        self.mouse_over = False
        default_image = create_surface_with_text(text, font_size, text_rgb, bg_rgb)
        highlighted_image = create_surface_with_text(text, font_size * 1.2, text_rgb, bg_rgb)
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position)]
        self.action = action
        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos: object, mouse_up: object) -> object:
        """updates the button appearance and returns button's action if clicked"""
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)



def title_screen(screen):
    play_title_scr_music()
    start_btn = UIElement(
        center_position=(300, 130),
        font_size=40,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="START",
        action=GameState.NEWGAME,
    )

    quit_btn = UIElement(
        center_position=(300, 260),
        font_size=40,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="QUIT",
        action=GameState.QUIT,
    )

    fly_1 = pygame.image.load("fly_1.png")
    fly_1 = pygame.transform.scale(fly_1, (600, 400))
    fly_2 = pygame.image.load("fly_2.png")
    fly_2 = pygame.transform.scale(fly_2, (600, 400))
    bg_image = pygame.image.load("fish_title_bg_2.JPG")
    buttons = [start_btn, quit_btn]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                play_meow_fx()
                mouse_up = True
        screen.blit(bg_image, (0, 0))
        screen.blit(fly_1, (10, 64))
        screen.blit(fly_2, (200, 150))
        credits_game_design = create_surface_with_text("Game Design:", 20, BLACK, WHITE)
        credits_gen = create_surface_with_text("Gen Will", 20, BLACK, WHITE)
        credits_larry = create_surface_with_text("Larry Kwok", 20, BLACK, WHITE)
        credits_jon = create_surface_with_text("Jon Ramm", 20, BLACK, WHITE)
        screen.blit(credits_game_design, (0, 300))
        screen.blit(credits_gen, (0, 320))
        screen.blit(credits_larry, (0, 340))
        screen.blit(credits_jon, (0, 360))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)


        pygame.display.flip()


# def play_level(screen):
#     play_level_music()
#     return_btn = UIElement(
#         center_position=(150, 350),
#         font_size=20,
#         bg_rgb=GREEN,
#         text_rgb=BLACK,
#         text="RETURN TO MAIN MENU",
#         action=GameState.TITLE,
#     )
#
#     while True:
#         mouse_up = False
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
#                 play_meow_fx()
#                 mouse_up = True
#         screen.fill(GREEN)
#
#         ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
#         if ui_action is not None:
#             return ui_action
#         return_btn.draw(screen)
#
#         pygame.display.flip()

#
#     run = True
#     while run is True:
#         mouse_up = False
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
#                 mouse_up = True
#             screen.fill(GREEN)
#             ui_action = quit_uielement.update(pygame.mouse.get_pos(), mouse_up)
#             if ui_action is not None:
#                 return
#             quit_uielement.update(pygame.mouse.get_pos(), mouse_up)
#             quit_uielement.draw(screen)
#             # uielement.update(pygame.mouse.get_pos())
#             # uielement.draw(screen)
#             pygame.display.flip()
#
#     pygame.quit()
#
# main()









