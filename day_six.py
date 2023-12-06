def read_input():
    with open("..\inputs\input_d6.txt") as f:
        return f.read().splitlines()


def race_time(race_time, record):
    # Speed = time holding down button
    speed = 0
    wins = 0
    while speed <= race_time:
        # Time left in the race
        time_left = race_time - speed
        # Distance
        distance = speed * time_left

        speed += 1

        if distance > record:
            wins += 1

    return wins


def calculate_num_ways_to_win(times, records):
    times = times[times.index(":") + 1 :].split()
    records = records[records.index(":") + 1 :].split()
    # Part One
    part_one = 1
    # Part Two
    time = ""
    record = ""

    for i in range(len(times)):
        # Part One
        part_one *= race_time(int(times[i]), int(records[i]))
        # Part Two
        time += times[i]
        record += records[i]

    part_two = race_time(int(time), int(record))

    return part_one, part_two


def main():
    lines = read_input()
    times = lines[0]
    records = lines[1]
    part_one, part_two = calculate_num_ways_to_win(times, records)
    print(part_one)
    print(part_two)


if __name__ == "__main__":
    main()
