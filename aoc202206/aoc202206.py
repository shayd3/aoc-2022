# aoc202206.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    return puzzle_input

def part1(data):
    """Solve part 1."""
    # Keep track of window of 4 characters
    sequence_window = []
    for i, char in enumerate(data):
        sequence_window.append(char)
        if len(sequence_window) == 4:
            if len(set(sequence_window)) == 4:
                return i + 1
            else:
                sequence_window.pop(0)


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
