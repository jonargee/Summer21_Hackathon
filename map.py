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


def draw_map(game_map):
    for row in game_map:
        #filling out game map
        y = 0
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
            if tile == '5':
                display.blit(grey_image, (x * GREY_TILE - scroll[0], y  * GREY_TILE - scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * SHELF_TILE, y * SHELF_TILE, SHELF_TILE, SHELF_TILE))

            x += 1

        y += 1
