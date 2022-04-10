import pygame

from constants import screen_height, screen_width
from util import draw_text_middle


def main():
    # Important: init the engine
    pygame.init()

    # Create window and set title
    pygame.display.set_caption("Codeclub Tetris")
    win = pygame.display.set_mode((screen_width, screen_height))

    draw_text_middle(win, "Tetris", 60, (255, 255, 255))
    pygame.display.update()

    # Keep the window open for 5 seconds
    pygame.time.wait(5000)


if __name__ == "__main__":
    main()
