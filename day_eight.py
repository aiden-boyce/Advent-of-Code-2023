def read_input():
    with open("..\inputs\input_d8.txt") as f:
        return f.read().splitlines()


# Choices = LRLRLR...
# Paths Dictionary: Source -> (Left, Right)
def get_paths(lines):
    choices = lines[0]
    lines.remove(choices)
    lines.remove(lines[0])
    paths = {}
    for line in lines:
        source, destinations = line.split(" = ")
        left, right = destinations[1:-1].split(", ")
        destinations = (left, right)
        paths[source] = destinations

    return choices, paths


# Given a source, follow the next direction choice
def follow_paths(source, end_goal, choices, paths, steps):
    # Base Cases
    if source == end_goal:
        return source, steps
    if choices == "":
        return source, steps

    choice = choices[0]

    destinations = paths[source]
    if choice == "L":
        return follow_paths(destinations[0], end_goal, choices[1:], paths, steps + 1)
    if choice == "R":
        return follow_paths(destinations[1], end_goal, choices[1:], paths, steps + 1)


# Just to run part one in its own function
def part_one(choices, paths):
    # Starting at "AAA"
    source = "AAA"
    # Ending at "ZZZ"
    end_goal = "ZZZ"

    steps = 0
    # Continue looping until landed in the final state
    while source != end_goal:
        source, steps = follow_paths(source, end_goal, choices, paths, steps)

    return steps


def main():
    lines = read_input()
    # Part One
    choices, paths = get_paths(lines)
    part_one_steps = part_one(choices, paths)
    print(f"Part One Steps: {part_one_steps}")


if __name__ == "__main__":
    main()
