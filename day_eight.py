from math import gcd


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


# Given a source, follow the next direction choice
def p2_follow_paths(source, choices, paths, steps):
    while not source.endswith("Z") or steps == 0:
        # Get the direction choice
        choice = choices[0]
        choices = choices[1:] + choice

        destinations = paths[source]
        if choice == "L":
            source = destinations[0]
        elif choice == "R":
            source = destinations[1]

        steps += 1

    return source, steps


def part_two(choices, paths):
    sources_XXA = []
    # Find all sources that end with "A"
    for source in paths.keys():
        if source.endswith("A"):
            sources_XXA.append(source)

    # Go through each source that ends with A
    # Find the cycles for each path
    cycles = []
    for source in sources_XXA:
        cycle = []
        steps = 0
        first_z = None

        # Find the length of each cycle
        while True:
            # Go to source that ends with Z
            source_z, steps = p2_follow_paths(source, choices, paths, steps)
            cycle.append(steps)
            # Save first source_z found
            if first_z is None:
                first_z = source_z
                steps = 0
            # Found first_z again so cycle found
            elif source_z == first_z:
                break

        cycles.append(cycle)

    # The cycle length is the same as A -> First_Z and First_Z -> First_Z
    cycle_lengths = [cycle[0] for cycle in cycles]

    # Get the least common multiple of all the cycle lengths
    lcm = cycle_lengths.pop()
    for num in cycle_lengths:
        lcm = (lcm * num) // gcd(lcm, num)

    return lcm


def main():
    lines = read_input()
    # Part One
    choices, paths = get_paths(lines)
    part_one_steps = part_one(choices, paths)
    print(f"Part One Steps: {part_one_steps}")
    part_two_steps = part_two(choices, paths)
    print(f"Part Two Steps: {part_two_steps}")


if __name__ == "__main__":
    main()
