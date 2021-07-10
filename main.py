import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

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

#creating scroll variable
scroll = [0,0]



def load_map(path):
    """
    function to load text file game map
    :param path: game map as text file
    :return: game map read out
    """
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map
game_map = load_map('map')


#old game map that I didn't want to erase because I spent a lot of time writing it
game_map2 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','2','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]



def collision_test(rect, tiles):
    """
    Function that determines when player collides with a tile
    """
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect,movement,tiles):
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
            collision_types['right']= True
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

#Establishing moving right and left variable
moving_right = False
moving_left = False

#Defining player location, momentum and air time variable
player_location = [50,300]
player_y_momentum = 0
air_timer = 0

#Defining player rectangle
player_rect = pygame.Rect(player_location[0],player_location[1],player_image.get_width(),player_image.get_height())

#Game loop
while True:
    #fills display with color
    display.fill((146,244,255))

    #defining scroll value based on character location
    scroll[0] += (player_rect.x - scroll[0]- 315)
    scroll[1] += (player_rect.y - scroll[1] - 300)

    #defining list of tile rectangles for map
    tile_rects = []
    y = 0
    for row in game_map:
        #filling out game map
        x = 0
        for tile in row:
            if tile == '1':
                display.blit(floor_image, (x * FLOOR_TILE - scroll[0], y * FLOOR_TILE - scroll[1]))
            if tile == '2':
                display.blit(shelf_image, (x * SHELF_TILE - scroll[0], y * SHELF_TILE - scroll[1]))
            if tile == '3':
                display.blit(white_image, (x * WHITE_TILE - scroll[0], y * WHITE_TILE - scroll[1]))
            if tile == '4':
                display.blit(black_image, (x * BLACK_TILE - scroll[0], y  * BLACK_TILE - scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * SHELF_TILE, y * SHELF_TILE, SHELF_TILE, SHELF_TILE))

            x += 1

        y += 1




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
                    player_y_momentum = -6
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