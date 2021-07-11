import pygame, sys
from pygame import mixer
from home_screen import create_surface_with_text, UIElement, title_screen, GameState
import pygame.freetype
from play_level import play_level
from pygame.sprite import Sprite
from enum import Enum
from music import play_level_music, play_title_scr_music, play_meow_fx, jump_fx, good_thing, bad_thing, cat_death
from pygame.locals import *
from map import load_map, draw_map
from movement import collision_test, move

clock = pygame.time.Clock()
mixer.init()

pygame.display.set_caption('Pygame Window')

GREEN = (78, 245, 56)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main_loop():
    pygame.init()

    screen = pygame.display.set_mode((600, 400))
    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            game_state = play_level(screen)

        if game_state == GameState.QUIT:
            pygame.quit()
            return
main_loop()
