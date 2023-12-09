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


def p1_extrapolate(all_values):
    last_diff = 0
    # Go through the keys backwards
    for key in list(all_values.keys())[::-1]:
        # Get the current difference list
        diff_lst = all_values[key]
        last_value = diff_lst[-1]
        # Get the next difference: last_diff + last_value
        next_diff = last_diff + last_value
        # Add it to the dictionary cuz why not
        all_values[key].append(next_diff)
        # Update last_diff
        last_diff = next_diff

    return last_diff


def p2_extrapolate(all_values):
    last_diff = 0
    # Go through the keys backwards
    for key in list(all_values.keys())[::-1]:
        # Get the current difference list
        diff_lst = all_values[key]
        first_value = diff_lst[0]
        # Get the next difference: first_value - last_diff
        next_diff = first_value - last_diff
        # Add it to dictionary cuz why not
        all_values[key].insert(0, next_diff)
        # Update last_diff
        last_diff = next_diff

    return last_diff


def main():
    lines = read_input()
    p1_sum = 0
    p2_sum = 0
    for line in lines:
        line = convert_line_to_int(line.split())
        all_values = find_differences(line, 0, {})
        p1_sum += p1_extrapolate(all_values)
        p2_sum += p2_extrapolate(all_values)

    print(f"Part One: {p1_sum}")
    print(f"Part Two: {p2_sum}")


if __name__ == "__main__":
    main()
