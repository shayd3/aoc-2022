# aoc202203.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split()]

def part1(data):
    """Solve part 1."""
    priorities = {
        # 97 -> 123 is the ASCII representation of the lowercase letters a->z
        chr(i): i - 96 for i in range(97, 123)
    }
    priorities.update({
        # 65 -> 91 is the ASCII representation of the uppercase letters A->Z
        chr(i): i - 38 for i in range(65, 91)
    })

    total = 0
    for rucksack in data:
        # Split the rucksack into the first and second compartments
        first_compartment = rucksack[:len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2:]

        first_compartment_no_dupe = "".join(set(first_compartment))
        second_compartment_no_dupe = "".join(set(second_compartment))

        for c1 in first_compartment_no_dupe:
            if c1 in second_compartment_no_dupe:
                total += priorities[c1]
    return total

def part2(data):
    """Solve part 2.

    Split input to groups of 3
    Find common item between all three in a single group -> This is their badge
    Find the priority of the badge
    """
    priorities = {
        # 97 -> 123 is the ASCII representation of the lowercase letters a->z
        chr(i): i - 96 for i in range(97, 123)
    }
    priorities.update({
        # 65 -> 91 is the ASCII representation of the uppercase letters A->Z
        chr(i): i - 38 for i in range(65, 91)
    })

    total = 0
    groups = list(chunk(data,3))
    # Count the number of times each item appears in the group
    # If item_count for a particular item = 3, it appears in all 3 groups

    # @SPDene -> Can also find the common items with something like:
    # c = list(set(b1).intersection(set(b2)).intersection(set(b3)))[0]
    for group in groups:
        item_counts = {}
        for rucksack in group:
            # Remove duplicates in each rucksack
            rucksack = "".join(set(rucksack))
            for item in rucksack:
                item_counts[item] = item_counts.get(item,0) + 1

        badge = None
        for item, count in item_counts.items():
            if count == 3:
                badge = item
                break
        priority = priorities[badge]
        total += priority
    return total

def chunk(list: list, chunk_size: int):
    for i in range(0, len(list), chunk_size):
        yield list[i:i + chunk_size]

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
