# aoc202205.py

import pathlib
import sys

# Split stacks, split steps
def parse(puzzle_input):
    """Parse input."""
    stacks_str, procedures = puzzle_input.split("\n\n")

    *crates, num_stacks = stacks_str.split("\n")
    num_of_stacks = len(num_stacks.split())

    stacks = [[] for _ in range(num_of_stacks)]
    crates.reverse()
    for line in crates:
        for stack_idx, i in enumerate(range(1, len(line), 4)):
            if(line[i].strip()):
                stacks[stack_idx].append(line[i])

    procedure = []
    for line in procedures.strip().split("\n"):
        words = line.split()
        amount, source, target = int(words[1]), int(words[3]), int(words[5])
        source_idx = source - 1
        target_idx = target - 1
        procedure.append((amount, source_idx, target_idx))
    return stacks, procedure

def part1(stacks, procedure):
    """Solve part 1."""
    for step in procedure:
        amount, source_idx, target_idx = step
        for _ in range(amount):
            val = stacks[source_idx].pop()
            stacks[target_idx].insert(len(stacks[target_idx]),val)
    answer = [stack[-1] for stack in stacks]
    return "".join(answer)

def part2(stacks, procedure):
    """Solve part 2."""
    for step in procedure:
        amount, source_idx, target_idx = step
        stacks[target_idx].extend(stacks[source_idx][-amount:])
        stacks[source_idx] = stacks[source_idx][:-amount]

    answer = [stack[-1] for stack in stacks]
    return "".join(answer)

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    stacks1, procedure1 = parse(puzzle_input)
    stacks2, procedure2 = parse(puzzle_input)
    solution1 = part1(stacks1, procedure1)
    solution2 = part2(stacks2, procedure2)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
