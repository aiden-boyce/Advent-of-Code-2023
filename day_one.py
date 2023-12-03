import time

def read_input():
    with open("inputs\input_d1.txt") as f:
        return f.read().splitlines()

# Part One
# Time: 00:17:16
# Rank: 7516
def get_calibration_value_digits(line):
    first_digit = 0
    last_digit = 0
    for symbol in line:
        if symbol.isdigit():
            first_digit = int(symbol)
            break
    for symbol in line[::-1]:
        if symbol.isdigit():
            last_digit = int(symbol)
            break
    
    calibration_value = (first_digit*10) + last_digit
    return calibration_value
            
def sum_of_calibration_values(lines):
    values_sum = 0
    for line in lines:
        values_sum += get_calibration_value_digits(line)
    return values_sum

# Part Two
# Time: 00:39:41
# Rank: 4524
def get_spelled_digit(line, index):
    letters = ['o', 't', 'f', 's', 'e', 'n']
    # Return if can't be spelled digit
    if line[index] not in letters:
        return
    # One
    if line[index:index+3] == 'one':
        return 1
    # Two
    if line[index:index+3] == 'two':
        return 2
    # Three
    if line[index:index+5] == 'three':
        return 3
    # Four
    if line[index:index+4] == 'four':
        return 4
    # Five
    if line[index:index+4] == 'five':
        return 5
    # Six
    if line[index:index+3] == 'six':
        return 6
    # Seven 
    if line[index:index+5] == 'seven':
        return 7
    # Eight
    if line[index:index+5] == 'eight':
        return 8
    # Nine
    if line[index:index+4] == 'nine':
        return 9

def part_two_get_calibration_value(line):
    first_digit = 0
    last_digit = 0
    for i, symbol in enumerate(line):
        if symbol.isdigit():
            first_digit = int(line[i])
            break
        if get_spelled_digit(line, i):
            first_digit = get_spelled_digit(line, i)
            break
    
    for i, symbol in reversed(list(enumerate(line))):
        if symbol.isdigit():
            last_digit = int(line[i])
            break
        if get_spelled_digit(line, i):
            last_digit = get_spelled_digit(line, i)
            break
    calibration_value = (first_digit*10) + last_digit
    return calibration_value

def part_two_sum_of_calibration_values(lines):
    values_sum = 0
    for line in lines:
        values_sum += part_two_get_calibration_value(line)
    return values_sum

# Jonathan Paulson - #4 on Leaderboard
def jonathan_paulson():
    D = open('inputs\input_d1.txt').read().strip()
    p1_sum = 0
    p2_sum = 0
    for line in D.split('\n'):
        p1_digits = []
        p2_digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                p1_digits.append(c)
                p2_digits.append(c)
            for j, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    p2_digits.append(str(j+1))
        p1_sum += int(p1_digits[0] + p1_digits[-1])
        p2_sum += int(p2_digits[0] + p2_digits[-1])
    return p1_sum, p2_sum

def main():
    # My code
    print("My Code!")
    my_start_time = time.time()
    lines = read_input()
    part_one_sum = sum_of_calibration_values(lines)
    print("Part One:", part_one_sum)
    part_two_sum = part_two_sum_of_calibration_values(lines)
    print("Part Two:", part_two_sum)
    my_time = time.time() - my_start_time
    print("%s seconds" % my_time)

    # Jonathan Paulson's Code
    print()
    print("Jonathan Paulson's Code!")
    optimized_start_time = time.time()
    p1_sum, p2_sum = jonathan_paulson()
    print("Part One:", p1_sum)
    print("Part Two:", p2_sum)
    optimized_time = time.time() - optimized_start_time
    print("%s seconds" % optimized_time)
    
    
if __name__ == "__main__":
    main()