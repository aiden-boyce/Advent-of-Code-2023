def read_input():
    with open("inputs\input_d4.txt") as f:
        return f.read().splitlines()

# Make a dictionary that adds 1 copy to each card number
def initialize_card_copies(lines):
    card_copies = {}
    for line in lines:
        card_num = line[line.index(' '):line.index(':')]
        card_num = int(card_num.split()[0])
        card_copies[card_num] = 1
    return card_copies

def card_num_and_wins(line):
    # Get the card number
    card_num = line[line.index(' '):line.index(':')]
    card_num = int(card_num.split()[0])
    # Split the winning numbers from the pulled numbers
    line = line[line.index(':')+1:]
    winning_nums, pulled_nums = line.split(' | ')
    winning_nums = winning_nums.split()
    pulled_nums = pulled_nums.split()

    # Get intersection of winning and pulled
    matches = list(set(winning_nums) & set(pulled_nums))

    wins = len(matches)

    return card_num, wins

# Add new cards
def add_copies(card_num, wins, card_copies):
    i = 1
    copies_of_card_num = card_copies[card_num]
    while i <= wins:
        copies_of_next_card = card_copies[card_num+i]
        copies_of_next_card += copies_of_card_num
        card_copies[card_num+i] = copies_of_next_card
        i += 1
    
def main():
    lines = read_input()
    part_one = 0
    part_two = 0
    card_copies = initialize_card_copies(lines)

    for line in lines:
        card_num, wins = card_num_and_wins(line)
        # Part 1
        if wins != 0:
            part_one += 2 ** (wins-1)
        # Part 2
        add_copies(card_num, wins, card_copies)
    
    # Count the number of cards pulled
    for value in card_copies.values():
        part_two += value
    
    print(f'Part One: {part_one}')
    print(f'Part Two: {part_two}')
    
if __name__ == "__main__":
    main()