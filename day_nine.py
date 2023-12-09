def read_input():
    with open("..\inputs\input_d9.txt") as f:
        return f.read().splitlines()


# Just convert line to int
def convert_line_to_int(line):
    for i, value in enumerate(line):
        line[i] = int(value)
    return line


# Check if all values are zero
def all_values_zero(values):
    all_zero = True
    for x in values:
        if x != 0:
            all_zero = False
            break
    return all_zero


# Find the differences of each value list
def find_differences(values, step, all_values):
    # Add most recent values to the all_values dictionary
    next_values = []
    all_values[step] = values

    # Base Case: When all differences are 0
    if all_values_zero(values):
        return all_values

    # Get the difference of each value
    i = 0
    while i < len(values) - 1:
        difference = values[i + 1] - values[i]
        next_values.append(difference)
        i += 1

    # Find differences from the next value list
    return find_differences(next_values, step + 1, all_values)


# Extrapolate both Part One and Part Two
def extrapolate(all_values):
    p1_diff = 0
    p2_diff = 0
    # Go through keys backwards
    for key in list(all_values.keys())[::-1]:
        diff_lst = all_values[key]
        # Part One
        last_value = diff_lst[-1]
        # Part Two
        first_value = diff_lst[0]

        # Get the Part One difference: p1_diff + last_value
        p1_diff = p1_diff + last_value
        # Get the Part Two difference: first_value - p2_diff
        p2_diff = first_value - p2_diff

        # Add the values to dictionary cuz why not
        all_values[key].append(p1_diff)
        all_values[key].insert(0, p2_diff)

    return p1_diff, p2_diff


def main():
    lines = read_input()
    p1_sum = 0
    p2_sum = 0
    for line in lines:
        line = convert_line_to_int(line.split())
        all_values = find_differences(line, 0, {})
        p1, p2 = extrapolate(all_values)
        p1_sum += p1
        p2_sum += p2

    print(f"Part One: {p1_sum}")
    print(f"Part Two: {p2_sum}")


if __name__ == "__main__":
    main()
