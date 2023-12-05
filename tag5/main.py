import numpy


f = open("tag5/input_emi.txt", "r")
input = f.read()

def seeds_part1():
    return list(map(int,input.split("seeds:")[1].split("\n")[0].split()))

# seed tuples (start, range)
def seeds_part2():
    seed_input = input.splitlines()[0].split(':')[1].split()
    zipped = [(int(x), int(y)) for (x,y) in zip(seed_input[::2], seed_input[1::2]) if (x != " ") and (y != " ")] 
    return zipped

def location_calculation(seeds):
    locations = []
    for seed in seeds:
        current_value = seed
        for block in input.split(":"):
            content = block.splitlines()[1:-1]
            for map_entry in content:
                if map_entry == "": continue
                [d,s,r] = list(map(int,map_entry.split()))
                if current_value in range(s,s+r):
                    current_value = current_value-s + d
                    break
        locations.append(current_value)
    return min(locations)

def get_blocks():
    blocks = []
    for b in input.split(":")[2:]:
        s = b.splitlines()[1:-1]
        # filter empty stings
        s = list(filter(lambda x: x, s))
        blocks.append(s)
    return [[list(map(int,line.split())) for line in block] for block in blocks]


def reverse_location_calulation():
    loc = 0
    current_source = loc
    blocks = get_blocks()
    seeds = seeds_part2()
    while True:
        for block in blocks[::-1]:
            for line in block:
                [d,s,r] = line
                if d <= current_source < d+r:
                    current_source = current_source + (s-d)
                    break
        for seed in seeds:
            if seed[0] <= current_source < seed[0]+seed[1]:
                return loc
        loc += 1
        current_source = loc
        if current_source%1_000_000 == 0:
            print(current_source)




print("solution part 1:", location_calculation(seeds_part1()))
#print("solution part 2:",location_calculation(seeds_part2()))
#print(len(seeds_part2()))
print(reverse_location_calulation())