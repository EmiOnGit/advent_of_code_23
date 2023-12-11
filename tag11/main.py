#!/usr/bin/python

def parse(input: str):
    galaxies_x = []
    galaxies_y = []
    for row, line in enumerate(input.splitlines()):
        for column, char in enumerate(line):
            if char == '#':
                galaxies_x.append(column)
                galaxies_y.append(row)
    galaxies_x.sort()
    galaxies_y.sort()
    return [galaxies_x, galaxies_y]

def expand(dimension, expansion_rate):
    shift = 0
    last = 0
    for i in range(len(dimension)):
        x = dimension[i]
        if x-last > 1:
            shift += (x-last - 1) * expansion_rate - 1
        dimension[i] += shift
        last = x

def dimension_distance(dim):
    sum = 0
    n = len(dim)
    n_half = int(n/2) + 1
    for i in range(n_half):
        x = dim[i]
        y = dim[n-i-1]
        d = y-x
        factor = n - (i*2) - 1
        sum += d * factor
    return sum

def distance(dim_x, dim_y):
    return dimension_distance(dim_x) + dimension_distance(dim_y)

f = open("input_emi.txt",'r')
input="""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
input = f.read()
(dim_x, dim_y) = parse(input)
expand(dim_x,2)
expand(dim_y,2)
# dimension_distance(dim_x)
d = distance(dim_x, dim_y)
print("distance is", d)

(dim_x, dim_y) = parse(input)
# expand(dim_x, 1_00)
# expand(dim_y, 1_00)
expand(dim_x, 1_000_000)
expand(dim_y, 1_000_000)
d = distance(dim_x, dim_y)
print("distance is", d)
