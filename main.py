from typing import Dict, List

import pygame

from constants import (
    border_color,
    cell_height,
    cell_width,
    grid_area_height,
    grid_area_width,
    grid_size,
    screen_height,
    screen_padding_x,
    screen_padding_y,
    screen_width,
    levels,
)
from grid import Coordinate, Grid, create_grid
from pieces import Piece, get_shape
from util import draw_text_middle


def draw_grid(surface: pygame.Surface, grid: Grid):
    """This function should draw the cells of the grid"""

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            x1 = screen_padding_x + (cell_width * x)
            y1 = screen_padding_y + (cell_height * y)

            pygame.draw.rect(surface, cell, (x1, y1, cell_width, cell_height), width=0)


def draw_grid_borders(surface: pygame.Surface, rows: int, columns: int):
    """This function should draw the gray borders for each grid cell and a thick border
    around the entire play area"""

    sx = screen_padding_x
    sy = screen_padding_y

    for y in range(rows):
        y1 = sy + (cell_height * y)
        pygame.draw.line(surface, border_color, (sx, y1), (sx + grid_area_width, y1))

        for x in range(columns):
            x1 = sx + (cell_width * x)
            pygame.draw.line(
                surface, border_color, (x1, sy), (x1, sy + grid_area_height)
            )

    pygame.draw.rect(
        surface, (255, 255, 255), (sx, sy, grid_area_width, grid_area_height), 5
    )


def get_empty_cells(grid: Grid) -> List[Coordinate]:
    """This method returns all empty cells as a list of tuple coordinates"""
    empty_cells = []

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == (0, 0, 0):
                empty_cells.append((x, y))

    return empty_cells


def valid_space(piece: Piece, offset: Coordinate, grid: Grid):
    """Return true if piece with applied offset is a valid space for a piece

    Note: Parts of piece above screen are always valid
    """

    empty_cells = get_empty_cells(grid)

    for (x, y) in piece.get_shape_on_grid(offset=offset):
        if y < 0:
            continue

        if (x, y) not in empty_cells:
            return False

    return True


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

    locked_positions = {}

    current_piece = get_shape()
    next_piece = get_shape()
    change_piece = False

    clock = pygame.time.Clock()
    fall_time = 0

    score = 0
    high_score = 0

    # Repeat key events every 200 ms
    pygame.key.set_repeat(200)

    while run:
        grid = create_grid(
            grid_size[1], grid_size[0], locked_positions=locked_positions
        )

        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > levels[0]:
            fall_time = 0

            if valid_space(current_piece, (0, 1), grid):
                # move piece down
                current_piece.y += 1

            else:
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            # keyboard handling goes here

        shape_cells = current_piece.get_shape_on_grid()
        for (x, y) in shape_cells:
            if y >= 0 and x >= 0:
                grid[y][x] = current_piece.color

        if change_piece:
            for (x, y) in shape_cells:
                locked_positions[(x, y)] = current_piece.color

            current_piece = next_piece
            next_piece = get_shape()

            change_piece = False

            # TODO: check if score needs to be increased

        # draw window
        draw_window(surface, score, high_score, next_piece)

        # draw grid and borders
        draw_grid(surface, grid)
        draw_grid_borders(surface, grid_size[1], grid_size[0])

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
