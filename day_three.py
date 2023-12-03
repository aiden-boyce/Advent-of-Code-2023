def read_input():
    with open("inputs\input_d3.txt") as f:
        return f.read().splitlines()

# Find special indices and gears
def find_special_indices(lines):
    p1_sum = 0
    p2_sum = 0
    # Looking for the Special Indices
    for i, line in enumerate(lines):
        for j, symbol in enumerate(line):
            adj_nums = []
            # Found a Special Character
            if symbol != '.' and not symbol.isdigit():
                adj_nums = find_adj_nums(lines, i, j)
                sums = sum_adj_nums(lines, i, adj_nums, symbol)
                p1_sum += sums[0]
                p2_sum += sums[1]
            
    return p1_sum, p2_sum

# Find all adjacent number indices
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

    return adj_nums

# Get the final sums of adjacent numbers for Part One and Part Two
def sum_adj_nums(lines, sp_i, adj_nums, special_symbol):
    # Part 1 and Part 2 return values
    p1_sum = 0
    p2_gear_ratio = 0
    gear_nums = []

    # Only go through rows directly above, equal to, or directly below special row
    for i in range(sp_i-1, sp_i+2):
        j = 0
        # Iterate through each column
        while j < len(lines[i]):
            symbol = lines[i][j]
            is_adj = False
            num = ""
            # Reached a number
            if symbol.isdigit():
                # Extract the number from the line
                num, j, is_adj = extract_number(lines, i, j, adj_nums)
            # Add num to sum if it was adjacent
            if is_adj:
                p1_sum += int(num) 
            # Add num to gear_nums if it was a gear
            if is_adj and special_symbol == '*':
                gear_nums.append(int(num))

            j += 1

    # Gear Ratio calculated only if there are exactly two adjacent numbers
    if len(gear_nums) == 2:
        p2_gear_ratio = gear_nums[0] * gear_nums[1]

    return p1_sum, p2_gear_ratio

# Get the number in the line    
def extract_number(lines, i, j, adj_nums):
    is_adj = False
    symbol = lines[i][j]
    # Add the whole number to a string
    num = ""
    while symbol.isdigit():
        num += symbol
        # Check if the number is adjacent to a special symbol
        if [i, j] in adj_nums:
            is_adj = True 

        j += 1
        # Move to next symbol
        try:
            symbol = lines[i][j]
        except IndexError:
            break
    
    return num, j, is_adj

# Part One: 01:35:27  10117
# Part Two: 01:47:26   8040
def main():
    lines = read_input()
    
    part_one, part_two = find_special_indices(lines)
    print("Part One:", part_one)
    print("Part Two:", part_two)

    
if __name__ == "__main__":
    main()