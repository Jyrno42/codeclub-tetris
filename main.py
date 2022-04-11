from typing import Dict, List

import pygame

from constants import (grid_area_width, screen_height, screen_padding_x,
                       screen_width)
from grid import Coordinate, Grid, create_grid
from pieces import Piece, get_shape
from util import draw_text_middle


def draw_grid(surface: pygame.Surface, grid: Grid):
    """This function should draw the filled cells of the grid (blocks that have already reached the ground)"""

    # Use: pygame.draw.rect(surface, color, (x1, y1, width, height), width=0) to draw each cell
    raise NotImplementedError


def draw_grid_borders(surface: pygame.Surface, rows: int, columns: int):
    """This function should draw the gray borders for each grid cell and a thick border
    around the entire play area"""

    # Use: pygame.draw.line(surface, border_color, (x1, y1), (x2, y2))
    raise NotImplementedError


def get_empty_cells(grid: Grid) -> List[Coordinate]:
    """This method returns all empty cells as a list of tuple coordinates"""
    raise NotImplementedError


def valid_space(piece: Piece, offset: Coordinate, grid: Grid):
    """Return true if piece with applied offset is a valid space for a piece

    Note: Parts of piece above screen are always valid
    """
    raise NotImplementedError


def game_over(locked_positions: Dict):
    """Return true if the game is over

    The method body should check all locked positions and return True if any of them are out
    of the screen (e.g. have negative y coordinates).
    """
    raise NotImplementedError


def draw_window(
    surface: pygame.Surface, score: int, high_score: int, next_piece: Piece
):
    """This method clears the background, writes Tetris title and draws current/high score and next piece"""

    # Make background black
    surface.fill((0, 0, 0))

    # Tetris Title
    font = pygame.font.Font(pygame.font.get_default_font(), 60)
    label = font.render("TETRIS", True, (255, 255, 255))
    surface.blit(
        label, (screen_padding_x + grid_area_width / 2 - (label.get_width() / 2), 30)
    )

    # TODO: draw current score
    # TODO: draw high score

    # TODO: draw next piece


def clear_rows(grid: Grid, locked_positions: Dict):
    """This method checks if any rows need clearing and clears them if they do

    After clearing, it shifts all pieces above the cleared lines down by N rows where N is the cleared row count.

    Finally, it returns the cleared row count which is used to update score.
    """
    raise NotImplementedError


def loop(surface: pygame.Surface):
    run = True

    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()

    score = 0
    high_score = 0

    # Repeat key events every 200 ms
    pygame.key.set_repeat(200)

    while run:
        grid = (
            []
        )  # create_grid(grid_size[1], grid_size[0], locked_positions={(1, 0): (255, 0, 0)})

        # TODO: measure fall time and move current piece down if needed. set flag to indicate piece change when ground reached

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            # keyboard handling goes here

        # TODO: Handle drawing current piece on the grid (use current_piece.get_shape_on_grid)

        # TODO: Handle when current piece reaches ground (add score / increase difficulty)

        # draw window
        draw_window(surface, score, high_score, next_piece)

        # draw grid and borders
        # TODO: draw_grid(surface, grid)
        # TODO: draw_grid_borders(surface, grid_size[1], grid_size[0])

        # tell pygame to update screen
        pygame.display.update()

    while True:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            break

    return True


def main_menu(win):
    run = True

    while run:
        # clear window
        win.fill((0, 0, 0))

        # write text
        draw_text_middle(win, "Press [space] To Play", 60, (255, 255, 255))

        # drawing done
        pygame.display.update()

        # wait for quit or keyboard/mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE
            ):
                # Start game loop
                if not loop(win):
                    run = False

    pygame.display.quit()


def main():
    # Important: init the engine
    pygame.init()

    # Create window and set title
    pygame.display.set_caption("Codeclub Tetris")
    win = pygame.display.set_mode((screen_width, screen_height))

    main_menu(win)


if __name__ == "__main__":
    main()
