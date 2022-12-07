# aoc202202.py

import pathlib
import sys
import RPS

def parse(puzzle_input):
    """Parse input."""
    rounds = [line for line in puzzle_input.split("\n")]
    round_guesses = [round.split() for round in rounds]
    return round_guesses

def part1(data):
    """Solve part 1.

    A/B/C => Opponent
    X/Y/Z => You

    A / X => Rock (1 point)
    B / Y => Paper (2 points)
    C / Z => Scissors (3 points)

    Loss => 0 Points
    Draw => 3 Points
    Win => 6 Points
    """
    total_points = 0
    for game_actions in data:
        # Player 1 = Opponent, Player 2 = You
        winner = RPS.find_winner(RPS.Player1Action[game_actions[0]].value, RPS.Player2Action[game_actions[1]].value)
        if winner == 0:
            total_points += RPS.RPSResultPoints["DRAW"].value
        if winner == 1:
            total_points += RPS.RPSResultPoints["LOSS"].value
        if winner == 2:
            total_points += RPS.RPSResultPoints["WIN"].value
        total_points += RPS.Player2Action[game_actions[1]].value
    return total_points

def part2(data):
    """Solve part 2."""

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
