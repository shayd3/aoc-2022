from enum import Enum

class Player1Action(Enum):
    A = 1 # Rock
    B = 2 # Paper
    C = 3 # Scissors

class Player2Action(Enum):
    X = 1 # Rock
    Y = 2 # Paper
    Z = 3 # Scissors

class RPSResultPoints(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

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
