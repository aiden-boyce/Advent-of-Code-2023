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


# Follow from
def follow_paths(source, end_goal, choices, paths, steps):
    if source == end_goal:
        return source, steps
    if choices == "":
        return source, steps

    choice = choices[0]

    destinations = paths[source]
    if choice == "L":
        return follow_paths(destinations[0], end_goal, choices[1:], paths, steps + 1)
    elif choice == "R":
        return follow_paths(destinations[1], end_goal, choices[1:], paths, steps + 1)


def main():
    lines = read_input()
    choices, paths = get_paths(lines)
    source = "AAA"
    end_goal = "ZZZ"
    steps = 0
    while source != end_goal:
        source, steps = follow_paths(source, end_goal, choices, paths, steps)

    print(source, steps)


if __name__ == "__main__":
    main()
