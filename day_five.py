def read_input():
    with open("..\inputs\input_d5.txt") as f:
        return f.read().splitlines()


# Maps Dictionary
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


# Sort the src_to_dst by seed
def sort_src_to_dst(unsorted_src_to_dst, last_seed):
    unsorted_src_to_dst = swap_sources(unsorted_src_to_dst, True)
    src_to_dst = {}
    i = 0
    # Sort the sources
    while i <= last_seed:
        src_to_dst[i] = unsorted_src_to_dst[i]
        i += 1
    unsorted_src_to_dst.clear()

    return src_to_dst


# Make original src_to_dst with just seeds
def make_src_to_dst(maps):
    src_to_dst = {}
    for map in maps:
        destination_range = map[0]
        source_range = map[1]
        range_len = map[2]
        i = 0
        while i < range_len:
            source = source_range + i
            destination = destination_range + i
            # Just initializing Dictionary with Seeds
            src_to_dst[source] = [source]
            i += 1

    sources = list(src_to_dst.keys())
    sources.sort()
    last_seed = sources[-1]
    i = 0
    while i <= last_seed:
        # Initializing Dictionary with Seeds
        if not i in src_to_dst:
            src_to_dst[i] = [i]
        i += 1

    return src_to_dst, last_seed


# Swap original source with newest source
def swap_sources(original_src_to_dst, seed_swap):
    src_to_dst = {}
    for destinations in original_src_to_dst.values():
        # Make the new source the seed
        if seed_swap:
            new_source = destinations[0]
        # Make the new source the last destination
        else:
            new_source = destinations[-1]
        src_to_dst[new_source] = destinations
    original_src_to_dst.clear()
    return src_to_dst


# Map the seeds
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
            destination.append(source)

    return src_to_dst


def part_one(maps):
    # Make original src_to_dst with just seeds
    src_to_dst, last_seed = make_src_to_dst(maps[1])
    # Apply the maps
    i = 1
    while i < len(maps):
        map_the_seeds(maps[i], i, src_to_dst)
        src_to_dst = swap_sources(src_to_dst, False)
        i += 1
    # Sort the src_to_dst by seed
    src_to_dst = swap_sources(src_to_dst, True)

    # Get the lowest location number from given seeds
    min_location = 2**63 - 1
    for seed in maps[0]:
        mapped_seed = src_to_dst[seed]
        location = mapped_seed[-1]
        min_location = min(min_location, location)

    print(min_location)
    return src_to_dst


def main():
    lines = read_input()
    # Make the maps
    maps = make_maps_dictionary(lines)
    # Run Part One
    part_one(maps)


if __name__ == "__main__":
    main()
