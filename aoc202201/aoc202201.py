# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    split_double_new_line = [line for line in puzzle_input.split('\n\n')]
    elf_calorie_groups = [group.split() for group in split_double_new_line]
    for idx,group in enumerate(elf_calorie_groups):
        elf_calorie_groups[idx] = [eval(i) for i in group]
    return elf_calorie_groups

def part1(data):
    """Solve part 1."""
    max = 0
    for elf in data:
        total = 0
        for calories in elf:
            total += calories
        if total > max:
            max = total
    return max

def part2(data):
    """Solve part 2."""
    calorie_totals_by_elf = []
    for elf in data:
        total = 0
        for calories in elf:
            total += calories
        calorie_totals_by_elf.append(total)
    calorie_totals_by_elf.sort(reverse=True)
    return calorie_totals_by_elf[0] + calorie_totals_by_elf[1] + calorie_totals_by_elf[2]

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
