import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

GREEN = (78, 245, 56)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """creates menu surface"""
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """UI for menu buttons"""


    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb):
        self.mouse_over = False
        super().__init__()
        default_image = create_surface_with_text(text, font_size, text_rgb, bg_rgb)
        highlighted_image = create_surface_with_text(text, font_size * 1.2, text_rgb, bg_rgb)
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position)]

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    uielement = UIElement(
        center_position=(400, 300),
        font_size=30,
        bg_rgb=GREEN,
        text_rgb=BLACK,
        text="Welcome to the Apo-cat-lypse"
    )

    run = True
    while run is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            screen.fill(GREEN)
            uielement.update(pygame.mouse.get_pos())
            uielement.draw(screen)
            pygame.display.flip()

    pygame.quit()

main()









