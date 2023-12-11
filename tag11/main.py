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
            shift += (x-last- 1) * expansion_rate
        dimension[i] += shift
        last = x

def dimension_distance(dim):
    sum = 0
    n = len(dim)
    print(dim)
    
    for i in range(n):
        x = dim[i]
        y = dim[n-i-1]
        d = x-y
        sum += d * i
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
# input = f.read()
(dim_x, dim_y) = parse(input)
expand(dim_x,1)
expand(dim_y,1)
d = distance(dim_x, dim_y)
print("distance is", d)

(dim_x, dim_y) = parse(input)
expand(dim_x, 1_0)
expand(dim_y, 1_0)
d = distance(dim_x, dim_y)
print("distance is", d-82)
