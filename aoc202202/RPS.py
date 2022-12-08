from enum import Enum

class PlayerAction(Enum):
    A = 1 # Rock
    B = 2 # Paper
    C = 3 # Scissors
    X = 1 # Rock
    Y = 2 # Paper
    Z = 3 # Scissors

class GameResults(Enum):
    X = "LOSS"
    Y = "DRAW"
    Z = "WIN"
class RPSResultPoints(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

# TODO: Rather than use single letters, its better to convert the input to human readible form
rules = {
    "A": {
        "X": "C",
        "Y": "A",
        "Z": "B"
    },
    "B": {
        "X": "A",
        "Y": "B",
        "Z": "C"
    },
    "C": {
        "X": "B",
        "Y": "C",
        "Z": "A"
    }
}

def find_move(player_action: int, game_outcome: str):
    """
    Returns 1 (Rock), 2 (Paper), 3 (Scissors) based on first move (:param: player_action) to have the given game outcome (:param: game_outcome)
    """
    if game_outcome == GameResults("DRAW").name:
        return player_action
    if player_action == 1:
        if game_outcome == GameResults("LOSS").name:
            return 2
        if game_outcome == GameResults("WIN").name:
            return 3
    if player_action == 2:
        if game_outcome == GameResults("LOSS").name:
            return 1
        if game_outcome == GameResults("WIN").name:
            return 3
    if player_action == 3:
        if game_outcome == GameResults("LOSS").name:
            return 2
        if game_outcome == GameResults("WIN").name:
            return 1

def find_winner(player1_action: int, player2_action: int):
    """
    Returns 0 (tie), 1 (player1), or 2 (player2) based on which player won

    Win Table (Based on RPSChoice)
    1 beats 3
    2 beats 1
    3 beats 2
    """
    if player1_action == player2_action:
        return 0
    # If Player1 Throws Rock
    if player1_action == 1:
        # Player 2 Throws Paper
        if player2_action == 2:
            return 2
        # Player 2 Throws Scissors
        else:
            return 1
    # If Player1 Throws Paper
    if player1_action == 2:
        # If Player 2 Thows Rock
        if player2_action == 1:
            return 1
        # IF Player 2 Throws Scissors:
        else:
            return 2
    # If Player1 Throws Scissors
    if player1_action == 3:
        if player2_action == 1:
            return 2
        if player2_action == 2:
            return 1
