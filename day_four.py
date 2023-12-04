def part_one(line):
    # Split the winning numbers from the pulled numbers
    line = line[line.index(':')+2:]
    winning_nums, pulled_nums = line.split(' | ')
    winning_nums = winning_nums.split()
    pulled_nums = pulled_nums.split()
    for i, num in enumerate(winning_nums):
        winning_nums[i] = int(num)
    for i, num in enumerate(pulled_nums):
        pulled_nums[i] = int(num)
    
    count = 0
    for num in pulled_nums:
        if num in winning_nums:
            count += 1
    if count == 0:
        return 0
    points = 2 ** (count-1)
    return points

card_copies = {}
def initialize_card_copies(lines):
    for line in lines:
        card_num = line[line.index(' '):line.index(':')]
        card_num = int(card_num.split()[0])
        card_copies[card_num] = 1

def part_two(line):
    # Split the winning numbers from the pulled numbers
    card_num = line[line.index(' '):line.index(':')]
    card_num = int(card_num.split()[0])

    line = line[line.index(':')+2:]
    winning_nums, pulled_nums = line.split(' | ')
    winning_nums = winning_nums.split()
    pulled_nums = pulled_nums.split()
    for i, num in enumerate(winning_nums):
        winning_nums[i] = int(num)
    for i, num in enumerate(pulled_nums):
        pulled_nums[i] = int(num)

    count = 0
    for num in pulled_nums:
        if num in winning_nums:
            count += 1

    return card_num, count

def add_copies(card_num, count):
    i = 1
    current_copies = card_copies[card_num]
    while i <= count:
        next_card_copies = card_copies[card_num+i]
        next_card_copies += current_copies
        card_copies[card_num+i] = next_card_copies
        i += 1

def read_input():
    with open("inputs\input_d4.txt") as f:
        return f.read().splitlines()
    
# Really easy but I overcomplicated the second part by trying recursion :(    
# Part One: 00:14:34   5418
# Part Two: 01:36:54  12755
def main():
    lines = read_input()
    sum = 0
    #for line in lines:
        #sum += part_one(line)
    #print(sum)
    initialize_card_copies(lines)
    for line in lines:
        card_num, count = part_two(line)
        add_copies(card_num, count)
    for value in card_copies.values():
        sum += value
    
    print(sum)
    
if __name__ == "__main__":
    main()