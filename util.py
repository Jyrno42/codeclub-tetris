import pygame

from constants import (grid_area_height, grid_area_width, screen_height,
                       screen_padding_x, screen_padding_y, screen_width)


def draw_text_middle(surface, text, size, color, background=True):
    """This method draws text in the middle of the surface

    When background is True it should also draw a black transparent overlay
    on-top of the other parts of the screen.
    """

    font = pygame.font.Font(pygame.font.get_default_font(), size)
    font.set_bold(True)
    label = font.render(text, True, color)

    if background:
        bg = pygame.Surface((screen_width, screen_height))
        bg.set_alpha(240)
        bg.fill((0, 0, 0))
        surface.blit(bg, (0, 0))

    surface.blit(
        label,
        (
            screen_padding_x + grid_area_width / 2 - (label.get_width() / 2),
            screen_padding_y + grid_area_height / 2 - label.get_height() / 2,
        ),
    )


def draw_text_bottom(surface, text, size, color, offset=(0, 0)):
    """This method draws text in the bottom of the surface"""

    font = pygame.font.Font(pygame.font.get_default_font(), size)
    font.set_bold(True)
    label = font.render(text, True, color)

    surface.blit(
        label,
        (
            (
                screen_padding_x
                + grid_area_width / 2
                - (label.get_width() / 2)
                + offset[0]
            ),
            (
                screen_padding_y
                + grid_area_height
                - screen_padding_y
                - (label.get_height() / 2)
            )
            + offset[1],
        ),
    )
