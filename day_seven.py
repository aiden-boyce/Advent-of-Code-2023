def read_input():
    with open("..\inputs\input_d7.txt") as f:
        return f.read().splitlines()


# Get the hand
def hand_type(hand):
    cards_seen = {}
    for x in hand:
        try:
            cards_seen[x] += 1
        except:
            cards_seen[x] = 1
    matches = list(cards_seen.values())
    matches.sort()
    match len(matches):
        # 5 OF A KIND
        case 1:
            return 7
        case 2:
            match matches[1]:
                # 4 OF A KIND
                case 4:
                    return 6
                # FULL HOUSE
                case 3:
                    return 5
        case 3:
            match matches[2]:
                # 3 OF A KIND
                case 3:
                    return 4
                # TWO PAIR
                case 2:
                    return 3
        # ONE PAIR
        case 4:
            return 2
        # HIGH CARD
        case 5:
            return 1


def radix_sort_hands(hands):
    # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
    strength_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    unsorted = []
    max_cards = 5
    i = 0
    while i < max_cards:
        j = 0
        while j < len(hands):
            idk_bro = 0
    print(hands)


def rank_hands(hands_dict):
    ranked_hands = {}
    hand_strength = 1
    for strength in hands_dict:
        radix_sort_hands(hands_dict[strength])


def make_hands_dict():
    hands_dict = {}
    i = 1
    while i <= 7:
        hands_dict[i] = []
        i += 1
    return hands_dict


def part_one(lines):
    hands_dict = make_hands_dict()
    for line in lines:
        hand, bid = line.split()
        type_hand = hand_type(hand)
        hands_dict[type_hand].append(hand)
    ranked_hands = rank_hands(hands_dict)


def main():
    lines = read_input()
    part_one(lines)


if __name__ == "__main__":
    main()
