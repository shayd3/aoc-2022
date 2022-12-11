# aoc202204.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    lines = [line.split(",") for line in puzzle_input.split()]
    return lines

def part1(data):
    """Solve part 1.

    # Split each range into start + end points
    # Compare each pair of ranges to see if one fully contains the other
    """
    count = 0
    for pairs in data:
        pair1_start, pair1_end = split_range(pairs[0])
        pair2_start, pair2_end = split_range(pairs[1])
        if((pair2_start >= pair1_start and pair2_end <= pair1_end) or
           (pair2_start <= pair1_start and pair2_end >=pair1_end)):
            count += 1
    return count

def part2(data):
    """Solve part 2."""
    count = 0
    for pairs in data:
        pair1_start, pair1_end = split_range(pairs[0])
        pair2_start, pair2_end = split_range(pairs[1])
        pair1 = range(pair1_start, pair1_end+1)
        pair2 = range(pair2_start, pair2_end+1)

        pair1set = set(pair1)
        pair2set = set(pair2)
        intersection = pair1set.intersection(pair2set)
        if(len(intersection) != 0):
            count += 1
    return count

def split_range(range_str):
    start, end = range_str.split("-")
    return int(start), int(end)

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
