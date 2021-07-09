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

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(CAT, (50, 50))
    pygame.display.update()


def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()
