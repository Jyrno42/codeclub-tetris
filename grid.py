from typing import Dict, List, Tuple

from pieces import Cell

# Grid is a two-dimensional list of Cell's
#
#
Grid = List[List[Cell]]

# Represents a coordinate on the Grid E.g. `(x, y)` which means `grid[y][x]`
Coordinate = Tuple[int, int]


def create_grid(rows: int, columns: int, locked_positions: Dict) -> Grid:
    """
    Creates a grid of rows and columns

    All cells are empty by default unless they exist in the locked_positions Dict

    Note: The returned grid should be created in a fashion where `len(grid) == rows` and `len(grid[1]) == columns`
    """
    # TODO: Create grid
    raise NotImplementedError
