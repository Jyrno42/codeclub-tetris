def load_high_score() -> int:
    """This method loads the previous high-score from score.txt and returns it as int

    Note: If file does not exist or is empty 0 should be returned
    """

    try:
        with open("score.txt", "r") as h:
            return int(h.read())

    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(score: int):
    """This method saves high-score into score.txt"""

    with open("score.txt", "w+") as h:
        h.write(f"{score}")
