def read_input():
    with open("..\inputs\input_d15.txt") as f:
        return f.read()


# Part One Hashing Function
def hashing_function(str):
    current_value = 0
    for character in str:
        current_value += ord(character)
        current_value *= 17
        current_value = current_value % 256

    return current_value


# Make the Boxes Dictionary
def make_boxes_dictionary():
    boxes = {}
    for i in range(256):
        boxes[i] = []
    return boxes


# Remove an Element from a Box
def remove_from_box(str, boxes):
    box_num = hashing_function(str[:-1])
    lenses = boxes[box_num]
    for lens in lenses:
        if lens[0] == str[:-1]:
            lenses.remove(lens)
            return


# Add an element to the box
def add_to_box(str, boxes):
    box_num = hashing_function(str[:-2])
    lenses = boxes[box_num]
    new_lens = str.split("=")
    for lens in lenses:
        if lens[0] == new_lens[0]:
            i = lenses.index(lens)
            lenses.remove(lens)
            lenses.insert(i, new_lens)
            return
    lenses.append(new_lens)


# Part Two Hash Map
def hash_map(lines):
    # Initialize the Boxes
    boxes = make_boxes_dictionary()
    for line in lines:
        # Remove Element from Box
        if line[-1] == "-":
            remove_from_box(line, boxes)
        # Add Element to Box
        else:
            add_to_box(line, boxes)

    total_focusing_power = 0
    # Get the total_focusing_power from the hashmap
    for box, lenses in boxes.items():
        lens_index = 0
        for lens in lenses:
            # Get the box_num
            box_num = box + 1
            # Get the lens_num
            lens_num = lens_index + 1
            # Get the focal_length
            focal_length = int(lens[1])
            # Multiply them all together to get the focusing power
            focusing_power = box_num * lens_num * focal_length
            # Add to the total focusing power
            total_focusing_power += focusing_power

            lens_index += 1

    return total_focusing_power


def main():
    line = read_input()
    lines = line.split(",")
    part_one = 0
    for line in lines:
        part_one += hashing_function(line)
    print(part_one)

    part_two = hash_map(lines)
    print(part_two)


if __name__ == "__main__":
    main()
