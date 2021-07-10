import pygame
from pygame import mixer
pygame.init()
mixer.init()

def play_lv1_music():
    """plays level one music"""
    mixer.music.load("toaf_remix.mp3")
    mixer.music.play(-1)