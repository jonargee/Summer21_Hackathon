import pygame, sys
from pygame import mixer
from home_screen import create_surface_with_text, UIElement
import pygame.freetype
from pygame.sprite import Sprite
from music import play_title_scr_music
from enum import Enum
from music import play_level_music
from pygame.locals import *
from map import load_map, draw_map
from movement import collision_test, move

clock = pygame.time.Clock()

pygame.init()
mixer.init()

play_level_music()

pygame.display.set_caption('Pygame Window')

#Window and display size
WINDOW_SIZE = (600,400)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
display = pygame.Surface((600,400))

#Images for game
player_image = pygame.image.load('cat.png')
floor_image = pygame.image.load('check.png')
FLOOR_TILE = floor_image.get_width()
shelf_image = pygame.image.load('shelf.png')
SHELF_TILE = shelf_image.get_width()
white_image = pygame.image.load('white.png')
WHITE_TILE = floor_image.get_width()
black_image = pygame.image.load('black.png')
BLACK_TILE = shelf_image.get_width()
grey_image = pygame.image.load('grey.png')
GREY_TILE = shelf_image.get_width()

game_map = load_map('map')

# background = pygame.image.load('some_image.png')
# background = pygame.transform.scale(background, (600, 400))

#creating scroll variable
scroll = [0,0]

#Establishing moving right and left variable
moving_right = False
moving_left = False

#Defining player location, momentum and air time variable
player_location = [50,300]
player_y_momentum = 0
air_timer = 0

#Defining player rectangle
player_rect = pygame.Rect(player_location[0],player_location[1],player_image.get_width(),player_image.get_height())


def main_loop():
    while True:
        #fills display with color
        display.fill((146,244,255))
        #defining scroll value based on character location
        scroll[0] += (player_rect.x - scroll[0]- 50)
        scroll[1] += (player_rect.y - scroll[1] - 300)
        #defining list of tile rectangles for map
        tile_rects = []

        draw_map(game_map)

        #defining character movement variable
        player_movement = [0,0]
        #Establing how player moves based on moving variable
        if moving_right:
            player_movement[0] += 2
        if moving_left:
            player_movement[0] -= 2
        player_movement[1] += player_y_momentum
        player_y_momentum += 0.2
        if player_y_momentum > 3:
            player_y_momentum = 3


        player_rect, collisions = move(player_rect, player_movement, tile_rects)
        #Checking if character collides with bottom or top of platform and establishes a jump time
        if collisions['bottom']:
            player_y_momentum = 0
            air_timer = 0
        else:
            air_timer += 1

        if collisions['top']:
            player_y_momentum = 0

        #displaying of player
        display.blit(player_image, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

        #Establishes movement by keystroke and Quiting of game loop
        for event in pygame.event.get():
            if event.type == QUIT:

                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moving_right = True
                if event.key == K_LEFT:
                    moving_left = True
                if event.key == K_UP:
                    if air_timer < 6:
                        player_y_momentum = -6.25
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False



        #scaling of game window
        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf,(0,0))
        #updating display
        pygame.display.update()
        #game clock
        clock.tick(60)