import pygame
import os

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Cat Will One Day Eat Me")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)

CAT_WIDTH, CAT_HEIGHT = 100, 150

CAT_IMAGE = pygame.image.load(os.path.join("assets", "cat.png"))
CAT = pygame.transform.scale(CAT_IMAGE, (CAT_WIDTH, CAT_HEIGHT))

VEL = 5
FPS = 60


def draw_window(cat):
    WIN.fill(WHITE)
    WIN.blit(CAT, (cat.x, cat.y))
    pygame.display.update()


def handle_cat_movement(keys_pressed, cat):
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
