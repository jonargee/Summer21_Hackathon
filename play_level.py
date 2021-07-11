import pygame, sys
import random

clock = pygame.time.Clock()
from music import play_level_music, play_meow_fx, jump_fx, good_thing, bad_thing, cat_death
from home_screen import UIElement, GameState

from pygame.locals import *

pygame.init()

GREEN = (78, 245, 56)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def play_level(screen):
    level_select = 1  # placeholder for various levels
    pygame.display.set_caption('Level 1')
    play_level_music()
    # Window and display size
    WINDOW_SIZE = (600, 400)
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    display = pygame.Surface((600, 400))

    # Images for game
    player_image = pygame.image.load('cat.png')
    player_image_right = player_image
    player_image_left = pygame.transform.flip(player_image, True, False)
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
    roach_image = pygame.image.load('roach.png')
    # fish_img = pygame.image.load('fishbone.png')

    # creating scroll variable
    scroll = [0, 0]
    direction = 1

    class collectable():

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.fish_img = pygame.image.load('fishbone.png')
            self.fly_img = pygame.image.load('fly_2.png')
            self.hitbox = (self.x, self.y, 25, 30)

        def draw_fish(self, win):
            display.blit(self.fish_img, (self.x - scroll[0], self.y - scroll[1]))

        def draw_fly(self, win):
            display.blit(self.fly_img, (self.x - scroll[0], self.y - scroll[1]))

        def get_rect(self):
            return pygame.Rect(self.x, self.y, 32, 32)

        def hit(self):
            font1 = pygame.font.SysFont('comicsans', 100)
            text = font1.render('Score +1', True, (255, 255, 255))
            display.blit(text, (300 - (text.get_width() / 2), 175))
            pygame.display.update()

        def collision_test(self, rect):
            collect_rect = self.get_rect()
            if collect_rect.colliderect(rect):
                self.hit()
                good_thing()

    class enemy(object):

        def __init__(self, x, y, width, height, end):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end = end
            self.path = [self.x, self.end]
            self.walk_count = 0
            self.vel = 2
            self.roach_img = pygame.image.load('roach.png')
            self.hitbox = (self.x, self.y, 25, 30)

        def draw(self, win):
            self.move()
            if self.walk_count + 1 <= 33:
                self.walk_count = 0
            if self.vel > 0:
                display.blit(self.roach_img, (self.x - scroll[0], self.y - scroll[1]))
                self.walk_count += 1
            else:
                display.blit(self.roach_img, (self.x - scroll[0], self.y - scroll[1]))
                self.walk_count += 1

        def hit(self):
            font1 = pygame.font.SysFont('comicsans', 100)
            text = font1.render('Life - 1', True, (255, 255, 255))
            display.blit(text, (300 - (text.get_width() / 2), 175))
            player_rect.x = 50
            pygame.display.update()

        def move(self):
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walk_count = 0
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walk_count = 0

        def get_rect(self):
            return pygame.Rect(self.x, self.y, self.roach_img.get_width(), self.roach_img.get_height())

        def collision_test(self, rect):
            collect_rect = self.get_rect()
            if collect_rect.colliderect(rect):
                self.hit()
                bad_thing()

    def load_map(path):
        """
        function to load text file game map
        :param path: game map as text file
        :return: game map read out
        """
        f = open(path + '.txt', 'r')
        data = f.read()
        f.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map

    game_map = load_map('map')

    def collision_test(rect, tiles):
        """
        Function that determines when player collides with a tile
        """
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(rect, movement, tiles):
        """
        Function to define movement
        :param rect:
        :param movement:
        :param tiles:
        :return:
        """
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types

    # Establishing moving right and left variable
    moving_right = False
    moving_left = False

    # Defining player location, momentum and air time variable
    player_location = [50, 300]
    player_y_momentum = 0
    air_timer = 0

    # Defining player rectangle
    player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(),
                              player_image.get_height())

    enemy_location = [700, 285]
    enemy_rect = pygame.Rect(enemy_location[0], enemy_location[1], roach_image.get_width(), roach_image.get_height())
    roach1 = enemy(200, 295, 16, 16, 230)
    roach2 = enemy(400, 295, 16, 16, 1040)
    roach3 = enemy(800, 140, 16, 16, 880)
    roach4 = enemy(1280, 295, 16, 16, 2500)
    roach5 = enemy(1320, 295, 16, 16, 1400)
    roach6 = enemy(1738, 72, 16, 16, 1970)
    roach7 = enemy(2844, 106, 16, 16, 2980)
    roach8 = enemy(2646, 170, 16, 16, 2646)
    fish1 = collectable(305, 190)
    fish2 = collectable(600, 95)
    fish3 = collectable(1155, 190)
    fish4 = collectable(1970, 64)
    fish5 = collectable(2398, 128)
    fish6 = collectable(3582, 30)

    collectable_fish = [fish1, fish2, fish3, fish4, fish5, fish6]
    enemies = [roach1, roach2, roach3, roach4, roach5, roach6, roach7, roach8]

    score = 0
    lives = 9

    background = pygame.image.load("fish_bg_2.JPG")

    while True:

        return_btn = UIElement(
            center_position=(460, 10),
            font_size=20,
            bg_rgb=WHITE,
            text_rgb=BLACK,
            text="RETURN TO MAIN MENU",
            action=GameState.TITLE,
        )
        # fills display with color
        # display.fill((146,244,255))
        display.fill((0, 0, 0))
        display.blit(background, (0, 0))

        # defining scroll value based on character location
        scroll[0] += (player_rect.x - scroll[0] - 50)

        # defining list of tile rectangles for map
        tile_rects = []
        y = 0
        for row in game_map:
            # filling out game map
            x = 0
            for tile in row:
                if tile == '1':
                    display.blit(floor_image, (x * FLOOR_TILE - scroll[0], y * FLOOR_TILE - scroll[1]))
                if tile == '2':
                    display.blit(shelf_image, (x * SHELF_TILE - scroll[0], y * SHELF_TILE - scroll[1]))
                if tile == '3':
                    display.blit(white_image, (x * WHITE_TILE - scroll[0], y * WHITE_TILE - scroll[1]))
                if tile == '4':
                    display.blit(black_image, (x * BLACK_TILE - scroll[0], y * BLACK_TILE - scroll[1]))
                if tile == '5':
                    display.blit(grey_image, (x * GREY_TILE - scroll[0], y * GREY_TILE - scroll[1]))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x * SHELF_TILE, y * SHELF_TILE, SHELF_TILE, SHELF_TILE))

                x += 1

            y += 1

        # defining character movement variable
        player_movement = [0, 0]
        # Establing how player moves based on moving variable
        if moving_right:
            player_movement[0] += 2
            direction = 1
        if moving_left:
            player_movement[0] -= 2
            direction = 0
        player_movement[1] += player_y_momentum
        player_y_momentum += 0.2
        if player_y_momentum > 3:
            player_y_momentum = 3

        player_rect, collisions = move(player_rect, player_movement, tile_rects)
        # Checking if character collides with bottom or top of platform and establishes a jump time
        if collisions['bottom']:
            player_y_momentum = 0
            air_timer = 0
        else:
            air_timer += 1

        if collisions['top']:
            player_y_momentum = 0

        # displaying of player
        if direction == 1:
            display.blit(player_image_right, (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        elif direction == 0:
            display.blit(player_image_left, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

        for roach in enemies:
            roach.draw(display)
            if roach.collision_test(player_rect):
                lives -= 1
                roach.hit()


        font2 = pygame.font.SysFont('comicsans', 20)
        lives_text = font2.render('Lives: ' + str(lives), True, (255,255,255))
        display.blit(lives_text, (10,10))

        for fish in collectable_fish:
            fish.draw_fish(display)
            if fish.collision_test(player_rect):
                score += 1
                fish.hit()

        print(player_rect.x, player_rect.y)

        # Establishes movement by keystroke and Quiting of game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            mouse_up = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                play_meow_fx()
                mouse_up = True
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moving_right = True
                if event.key == K_LEFT:
                    moving_left = True
                if event.key == K_UP:
                    jump_fx()
                    if air_timer < 6:
                        player_y_momentum = -6.25
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False
        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action

        # scaling of game window
        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))
        return_btn.draw(screen)
        # updating display
        pygame.display.update()
        # game clock
        clock.tick(60)