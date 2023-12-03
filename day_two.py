def read_input():
    with open("inputs\input_d2.txt") as f:
        return f.read().splitlines()


def compare_pulled_to_max(num, color):
    max_red = 12
    max_green = 13
    max_blue = 14
    
    if color == 'r':
        return num <= max_red
    if color == 'g':
        return num <= max_green
    if color == 'b':
        return num <= max_blue

def get_num_color(line, digit_index):
    line = line[digit_index:]
    space_index = 0
    for i, elem in enumerate(line):
        if elem == ' ':
            space_index = i
            break
    num = line[:space_index]
    num = int(num)
    color = line[space_index+1]
    space_index = digit_index + space_index
    return num, color, space_index

def is_valid_game(line):
    line = line[line.index(':'):]
    is_valid = True
    i = 0
    while i < len(line):
        if line[i].isdigit():
            num, color, space_index = get_num_color(line, i)
            is_valid = compare_pulled_to_max(num, color)
            i = space_index
        if not is_valid:
            return is_valid
        i += 1
    return is_valid

def get_game_number(line):
    digit_index = 0
    colon_index = 0
    seen_first_digit = False
    for i, symbol in enumerate(line):
        if symbol.isdigit() and not seen_first_digit:
            digit_index = i
            seen_first_digit = True
        if symbol == ':':
            colon_index = i
            break
    game_num = line[digit_index:colon_index]
    return int(game_num)

def sum_possible_games(lines):
    sum = 0
    for line in lines:
        is_valid = is_valid_game(line)
        if is_valid:
            sum += get_game_number(line)
    return sum

# Compare current number to current max
def get_max_color(num, color, max_colors):
    if color == 'r':
        max_colors[0] = max(max_colors[0], num)
        return
    if color == 'g':
        max_colors[1] = max(max_colors[1], num)
        return
    if color == 'b':
        max_colors[2] = max(max_colors[2], num)
        return
    
    
# BRO COLOR DOES NOT LOOK LIKE A REAL WORD
def p2_get_num_color(line):
    line = line[line.index(':'):]
    # RED GREEN BLUE
    max_colors = [0, 0, 0]
    i = 0
    while i < len(line):
        if line[i].isdigit():
            num, color, space_index = get_num_color(line, i)
            i = space_index
            get_max_color(num, color, max_colors)
        i += 1
    return max_colors

def p2_get_power(line):
    max_colors = p2_get_num_color(line)
    return max_colors[0] * max_colors[1] * max_colors[2]

def p2_sum_powers(lines):
    sum = 0
    for line in lines:
        sum += p2_get_power(line)
    return sum
    
# Part One: 00:54:43  10859
# Part Two: 01:16:06  11659
def main():
    lines = read_input()
    part_one = sum_possible_games(lines)
    print("Part One:", part_one)
    part_two = p2_sum_powers(lines)
    print("Part Two:", part_two)

    
if __name__ == "__main__":
    main()