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
