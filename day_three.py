def read_input():
    with open("inputs\input_d3.txt") as f:
        return f.read().splitlines()

# Part One
def find_special_indices(lines):
    sum = 0
    # Looking for the Special Indices
    for i, line in enumerate(lines):
        for j, symbol in enumerate(line):
            if symbol != '.' and not symbol.isdigit():
                sum += find_adj_nums(lines, i, j)
    
    return sum

def find_adj_nums(lines, sp_i, sp_j):
    adj_nums = []
    # Adj Top Row
    if lines[sp_i-1][sp_j-1].isdigit():
        adj_nums.append([sp_i-1,sp_j-1])
    if lines[sp_i-1][sp_j].isdigit():
        adj_nums.append([sp_i-1,sp_j])
    if lines[sp_i-1][sp_j+1].isdigit():
        adj_nums.append([sp_i-1,sp_j+1])
    
    # Adj Mid Row
    if lines[sp_i][sp_j-1].isdigit():
        adj_nums.append([sp_i,sp_j-1])
    if lines[sp_i][sp_j+1].isdigit():
        adj_nums.append([sp_i,sp_j+1])

    # Adj Bot Row
    if lines[sp_i+1][sp_j-1].isdigit():
        adj_nums.append([sp_i+1,sp_j-1])
    if lines[sp_i+1][sp_j].isdigit():
        adj_nums.append([sp_i+1,sp_j])
    if lines[sp_i+1][sp_j+1].isdigit():
        adj_nums.append([sp_i+1,sp_j+1])

    return sum_adj_nums(lines, sp_i, adj_nums)

# PAIN
def sum_adj_nums(lines, sp_i, adj_nums):
    sum = 0
    # Only go through rows directly above, equal to, or directly below it
    for i in range(sp_i-1, sp_i+2):
        j = 0
        # Iterate through each column
        while j < len(lines[i]):
            symbol = lines[i][j]
            # Reached a number
            if symbol.isdigit():
                is_adj = False
                num = ""
                num_j = j
                # Add the whole number to a string
                while symbol.isdigit():
                    num += symbol
                    # Check if the number is adjacent to a special character
                    if [i, num_j] in adj_nums:
                        is_adj = True
                    num_j += 1
                    try:
                        symbol = lines[i][num_j]
                    except IndexError:
                        break
                j = num_j
                # Add num to sum if it was adjacent
                if is_adj:
                    sum += int(num)
            j += 1
    
    return sum


# Part Two
def find_special_gears(lines):
    sum = 0
    # Looking for the Special Gears
    for i, line in enumerate(lines):
        for j, symbol in enumerate(line):
            if symbol == '*':
                sum += pt2_find_adj_nums(lines, i, j)
    
    return sum    
    
def pt2_find_adj_nums(lines, sp_i, sp_j):
    adj_nums = []
    # Adj Top Row
    if lines[sp_i-1][sp_j-1].isdigit():
        adj_nums.append([sp_i-1,sp_j-1])
    if lines[sp_i-1][sp_j].isdigit():
        adj_nums.append([sp_i-1,sp_j])
    if lines[sp_i-1][sp_j+1].isdigit():
        adj_nums.append([sp_i-1,sp_j+1])
    
    # Adj Mid Row
    if lines[sp_i][sp_j-1].isdigit():
        adj_nums.append([sp_i,sp_j-1])
    if lines[sp_i][sp_j+1].isdigit():
        adj_nums.append([sp_i,sp_j+1])

    # Adj Bot Row
    if lines[sp_i+1][sp_j-1].isdigit():
        adj_nums.append([sp_i+1,sp_j-1])
    if lines[sp_i+1][sp_j].isdigit():
        adj_nums.append([sp_i+1,sp_j])
    if lines[sp_i+1][sp_j+1].isdigit():
        adj_nums.append([sp_i+1,sp_j+1])
    
    return get_gear_ratio(lines, sp_i, adj_nums)

def get_gear_ratio(lines, sp_i, adj_nums):
    # List to hold all numbers adjacent to the gear
    nums = []
    gear_ratio = 0

    # Only go through rows directly above, equal to, or directly below it
    for i in range(sp_i-1, sp_i+2):
        j = 0
        # Iterate through each column
        while j < len(lines[i]):
            symbol = lines[i][j]
            # Reached a number
            if symbol.isdigit():
                is_adj = False
                num = ""
                num_j = j
                # Add the whole number to a string
                while symbol.isdigit():
                    num += symbol
                    # Check if the number is adjacent to a gear
                    if [i, num_j] in adj_nums:
                        is_adj = True
                    num_j += 1
                    try:
                        symbol = lines[i][num_j]
                    except IndexError:
                        break
                j = num_j
                # Add num to list if it was adjacent
                if is_adj:
                    nums.append(int(num))
            j += 1

    # Gear Ratio calculated with exactly two adjacent numbers
    if len(nums) == 2:
        gear_ratio = nums[0] * nums[1]
    
    return gear_ratio
    
    
# Part One: 01:35:27  10117
# Part Two: 01:47:26   8040
def main():
    lines = read_input()
    # Convert all lines to char arrays
    for i, line in enumerate(lines):
        lines[i] = list(line)

    part_one = find_special_indices(lines)
    print("Part One:", part_one)
    part_two = find_special_gears(lines)
    print("Part Two:", part_two)

    
if __name__ == "__main__":
    main()