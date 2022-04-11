import random
from typing import List, NamedTuple, Tuple

# fmt: off
S = [
    (
        ".....",
        ".....",
        "..**.",
        ".**..",
    ),
    (
        ".....",
        "..*..",
        "..**.",
        "...*.",
    ),
]

Z = [
    (
        ".....",
        ".....",
        ".**..",
        "..**."
    ),
    (
        ".....",
        "..*..",
        ".**..",
        ".*...",
    ),
]

I = [
    (
        "..*..",
        "..*..",
        "..*..",
        "..*..",
    ),
    (
        ".....",
        ".....",
        ".....",
        "****."
    ),
]

O = [
    (
        ".....",
        ".....",
        ".**..",
        ".**..",
    )
]

J = [
    (
        ".....",
        ".....",
        ".*...",
        ".***.",
    ),
    (
        ".....",
        "..**.",
        "..*..",
        "..*..",
    ),
    (
        ".....",
        ".....",
        ".***.",
        "...*."
    ),
    (
        ".....",
        "..*..",
        "..*..",
        ".**.."
    ),
]

L = [
    (
        ".....",
        ".....",
        "...*.",
        ".***.",
    ),
    (
        ".....",
        "..*..",
        "..*..",
        "..**.",
    ),
    (
        ".....",
        ".....",
        ".***.",
        ".*...",
    ),
    (
        ".....",
        ".**..",
        "..*..",
        "..*..",
    ),
]

T = [
    (
        ".....",
        ".....",
        "..*..",
        ".***.",
    ),
    (
        ".....",
        "..*..",
        "..**.",
        "..*..",
    ),
    (
        ".....",
        ".....",
        ".***.",
        "..*.."),
    (
        ".....",
        "..*..",
        ".**..",
        "..*..",
    ),
]
# fmt: on


# Each integer represents a color value. For example `(0, 0, 0)` is an empty
#  cell while (255, 0, 0) is a red one.
Cell = Tuple[int, int, int]


class ShapeInfo(NamedTuple):
    shape: List[Tuple[str, str, str, str]]
    color: Cell


shapes = (
    ShapeInfo(S, (0, 255, 0)),
    ShapeInfo(Z, (255, 0, 0)),
    ShapeInfo(I, (0, 255, 255)),
    ShapeInfo(O, (255, 255, 0)),
    ShapeInfo(J, (255, 165, 0)),
    ShapeInfo(L, (0, 0, 255)),
    ShapeInfo(T, (128, 0, 128)),
)


class Piece(object):
    def __init__(self, column: int, row: int, shape: ShapeInfo):
        self.x = column
        self.y = row
        self.shape = shape.shape
        self.color = shape.color
        self.rotation = 0  # number from 0-3

    def get_shape_on_grid(self, offset=(0, 0)):
        """This method should return grid coordinates of the current Piece with applied offset
        while taking into account current rotation.
        """
        raise NotImplementedError


def get_shape():
    """This method should return a Piece instance with a random shape

    Note: The default position should be top middle
    """
    return Piece(5, 0, shape=random.choice(shapes))
