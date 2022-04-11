# Tetris game with python

This is the base repository you can use to follow the process of
developing a python tetris game. It contains various branches of the steps
I will take during my presentation.

We shall use poetry to install python dependencies, but you can also just install
pygame manually.

## Getting started

1. [Install poetry](https://python-poetry.org/docs/#installation)
2. Install dependencies with `poetry install`
3. Start adding code to `main.py`

## Play the game:

1. [Install poetry](https://python-poetry.org/docs/#installation)
2. Install dependencies with `poetry install`
3. Run the game with `poetry run python main.py`

> Note: To actually play the game without developing it check out the `final` branch - `git checkout final`.

## Branches:

- `main`: the default branch without any code
- `step-0`: Code outline, piece types
- `step-1-grid`: Basic grid
- `step-2-falling-pieces`: Adding pieces that fall and freezing them when they reach bottom
- `step-3-controls`: Adding keyboard controls to pieces
- `step-4-scoring`: Adding scoring logic and displaying score
- `final`: Final game with leveling and combos
