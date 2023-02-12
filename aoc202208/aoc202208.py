# aoc202208.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""

    rows = puzzle_input.split("\n")
    grid = [list(map(int,row)) for row in rows]
    return grid

def part1(grid):
    """Solve part 1."""
    visible_trees = 0
    for row_idx,row in enumerate(grid):
        for column_idx,column in enumerate(row):
            # Check left and right
            if column_idx > 0 and grid[row_idx][column_idx] > grid[row_idx][column_idx-1]:
                visible_trees += 1
            elif column_idx < 4 and grid[row_idx][column_idx] > grid[row_idx][column_idx+1]:
                visible_trees += 1
            # Check up and down

            if row_idx > 0 and grid[row_idx][column_idx] > grid[row_idx-1][column_idx]:
                visible_trees += 1
            elif row_idx < 4 and grid[row_idx][column_idx] > grid[row_idx+1][column_idx]:
                visible_trees += 1
    return visible_trees



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
