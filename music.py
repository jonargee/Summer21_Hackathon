import pygame
from pygame import mixer
pygame.init()
mixer.init()


def play_level_music():
    """plays level one music"""
    mixer.music.load("toaf_remix.mp3")
    mixer.music.play(-1)


def play_title_scr_music():
    """plays title screen music"""
    mixer.music.load("toaf_menu_screen.mp3")
    mixer.music.play(-1)

def play_meow_fx():
    """meow effect for various things"""
    fx = pygame.mixer.Sound("meow_fx.mp3")
    pygame.mixer.Sound.play(fx)

def jump_fx():
    """silly jump sound"""
    fx = pygame.mixer.Sound("jump.mp3")
    pygame.mixer.Sound.play(fx)

def good_thing():
    """happy sound"""
    fx = pygame.mixer.Sound("good_thing.mp3")
    pygame.mixer.Sound.play(fx)

def bad_thing():
    """sad sound"""
    fx = pygame.mixer.Sound("bad_thing.mp3")
    pygame.mixer.Sound.play(fx)

def cat_death():
    """you have died"""
    fx = pygame.mixer.Sound("cat_death.mp3")
    pygame.mixer.Sound.play(fx)







