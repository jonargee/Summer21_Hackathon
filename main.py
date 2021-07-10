import os
import pygame
from pygame import mixer


mixer.init() # start music 

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Cat Will One Day Eat Me") # caption of project name

WHITE = (255, 255, 255)  # initialize default coloring
BLACK = (0, 0, 0, 0)

CAT_WIDTH, CAT_HEIGHT = 100, 150  # dimension of cat photo

CAT_IMAGE = pygame.image.load(os.path.join("assets", "cat.png"))  # load in picture
CAT_ORIGINAL = pygame.transform.scale(CAT_IMAGE, (CAT_WIDTH, CAT_HEIGHT))  # apply cat photo dimensions to asset
CAT = CAT_ORIGINAL  # created a second image to avoid depreciation of original asset when applying


background_music = mixer.music.load(os.path.join("assets", "toaf.mp3"))  # set music to TOAF written by Jon
mixer.music.play(-1)                                                     # play music indefinitely

VEL = 5     # speed of cat
FPS = 60    # frames per second


def draw_window(cat):
    """
    The initial setup of the window and player cat character
    :param cat: player object controlled by user
    """
    WIN.fill(WHITE)
    WIN.blit(CAT, (cat.x, cat.y))
    pygame.display.update()


def handle_cat_movement(keys_pressed, cat):
    """
    Control for the player cat character using WASD keys for the 4 cardinal directions
    :param keys_pressed: controls for moving
    :param cat: player object
    """
    if keys_pressed[pygame.K_a] and cat.x - VEL > 0:  # left
        cat.x -= VEL

    if keys_pressed[pygame.K_d] and cat.x + VEL < WIDTH - CAT_WIDTH:  # right
        cat.x += VEL
    if keys_pressed[pygame.K_w] and cat.y - VEL > 0:  # up
        cat.y -= VEL
    if keys_pressed[pygame.K_s] and cat.y + VEL < cat.height - CAT_HEIGHT:  # down
        cat.y += VEL


def main():
    cat = pygame.Rect(100, 300, WIDTH, HEIGHT)
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        handle_cat_movement(keys_pressed, cat)
        draw_window(cat)
    pygame.quit()


if __name__ == "__main__":
    main()