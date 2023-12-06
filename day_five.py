def read_input():
    with open("..\inputs\input_d5.txt") as f:
        return f.read().splitlines()


def make_maps_dictionary(lines):
    maps = {}
    seeds = lines[0]
    seeds = seeds[seeds.index(":") + 1 :].split()
    seeds = [int(x) for x in seeds]
    maps[0] = seeds
    i = 0
    for line in lines:
        # Increment i to next map
        if line == "":
            i += 1
            maps[i] = []
            continue

        if not line[0].isdigit():
            continue

        # Add numbers to their respective maps
        nums = [int(x) for x in line.split()]
        maps[i].append(nums)

    return maps


def make_src_to_dst(maps):
    unsorted_src_to_dst = {}
    for map in maps:
        destination_range = map[0]
        source_range = map[1]
        range_len = map[2]
        i = 0
        while i < range_len:
            source = source_range + i
            destination = destination_range + i
            unsorted_src_to_dst[source] = 0
            i += 1

    sources = list(unsorted_src_to_dst.keys())
    sources.sort()
    last_seed = sources[-1]

    src_to_dst = {}
    i = 0
    while i <= last_seed:
        src_to_dst[i] = [i]
        i += 1

    return src_to_dst


def map_the_seeds(maps, map_num, src_to_dst):
    for map in maps:
        destination_range = map[0]
        source_range = map[1]
        range_len = map[2]
        i = 0
        while i < range_len:
            source = source_range + i
            destination = destination_range + i
            src_to_dst[source].append(destination)
            i += 1

    for source, destination in src_to_dst.items():
        # No element mapped so use previous element
        if len(destination) != map_num + 1:
            destination.append(destination[-1])


def main():
    lines = read_input()
    maps = make_maps_dictionary(lines)
    src_to_dst = make_src_to_dst(maps[1])
    i = 1
    # Go through each map
    """
    while i <= 7:
        map_the_seeds(maps[i], i, src_to_dst)
        i += 1
    """
    # Seed #: [Seed, Soil, Fertilizer, Water, Light, Temperature, Humidity, Location]
    map_the_seeds(maps[1], 1, src_to_dst)
    print(f"Seed 79: {src_to_dst[79]}")
    print(f"Seed 14: {src_to_dst[14]}")
    print(f"Seed 55: {src_to_dst[55]}")
    print(f"Seed 13: {src_to_dst[13]}")
    print()
    map_the_seeds(maps[2], 2, src_to_dst)
    print(f"Seed 79: {src_to_dst[79]}")
    print(f"Seed 14: {src_to_dst[14]}")
    print(f"Seed 55: {src_to_dst[55]}")
    print(f"Seed 13: {src_to_dst[13]}")
    print()
    map_the_seeds(maps[3], 3, src_to_dst)
    print(f"Seed 79: {src_to_dst[79]}")
    print(f"Seed 14: {src_to_dst[14]}")  # SHOULD BE WATER = 49
    print(f"Seed 55: {src_to_dst[55]}")  # SHOULD BE WATER = 53
    print(f"Seed 13: {src_to_dst[13]}")  # SHOULD BE WATER = 41
    print()


if __name__ == "__main__":
    main()
