# aoc202207.py

import pathlib
import sys
from collections import defaultdict

def parse(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data):
    """Solve part 1."""
    file_sizes = get_sizes(data)
    directories_file_sizes_below_threshold_total = 0
    for file_dir, file_size in file_sizes.items():
        if file_size <= 100000:
            directories_file_sizes_below_threshold_total += file_size
    return directories_file_sizes_below_threshold_total

def part2(data):
    """Solve part 2."""
    file_sizes = get_sizes(data)
    total_disk_space = 70000000
    needed_disk_space = 30000000
    space_needed_to_free = file_sizes['/'] + needed_disk_space - total_disk_space

    directories_above_threshold = {}
    for file_dir, file_size in file_sizes.items():
        if file_size >= space_needed_to_free:
            directories_above_threshold[file_dir] = file_size
    return(min(directories_above_threshold.values()))

def get_sizes(data):
    file_struct = []
    file_sizes = defaultdict(int)
    for line in data.split("\n"):
        # Build directory tree
        if line.startswith('$'):
            line = line.replace("$", " ").strip()
            cmd, *cmd_args = line.split(" ")
            if cmd == "cd":
                if cmd_args[0] == "/":
                    file_struct.clear()
                    file_struct.append("/")
                elif cmd_args[0] == "..":
                    file_struct.pop()
                else:
                    directory = cmd_args[-1]
                    file_struct.append(directory)
        # Listing file, add size to current directory + parent dirs
        else:
            filesize = line.split()[0]
            if(filesize.isdigit()):
                filesize = int(filesize)
                for i in range(len(file_struct)):
                    directory = '/'.join(file_struct[:i+1]).replace("//","/")
                    file_sizes[directory] += filesize
    return file_sizes

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
