#!/usr/bin/env python

# import utils
import os, sys
sys.path.append(os.path.abspath(os.path.join('..')))
from utils import *
import numpy as np


def parse_part1(split_input):
    instructions = []
    for line in split_input:
        split_line = line.split()
        char = split_line[0]
        length = int(split_line[1])
        instructions.append((char,length))
    return instructions

def parse_part2(split_input):
    inst_map = {0:'R',1:'D',2:'L',3:'U'}
    instructions = []
    for line in split_input:
        split_line = line.split("(")[1]
        char = inst_map[int(split_line[-2])]
        length = int(split_line[1:-2],16)
        instructions.append((char,length))
    return instructions

def get_polygon(instructions):
    x_list = []
    y_list = []
    x,y,x_min,y_min,trench_length = 0,0,0,0,0
    for inst in instructions:
        char,length = inst
        trench_length += length
        if char == 'R':
            x += length
            x_list.append(x)
            y_list.append(y)
        elif char == 'L':
            x -= length
            x_list.append(x)
            y_list.append(y)
        elif char == 'D':
            y += length
            x_list.append(x)
            y_list.append(y)
        elif char == 'U':
            y -= length
            x_list.append(x)
            y_list.append(y)
            
        else:
            raise Exception("Could not parse chararcter " + char)
    
        x_min = min(x_min,x)
        y_min = min(y_min,y)
    x_list = np.array(x_list,dtype='double')+abs(x_min)
    y_list = np.array(y_list,dtype='double')+abs(y_min)
    return x_list,y_list,trench_length


def polygon_area(x,y,trench_length):
    correction = x[-1] * y[0] - y[-1]* x[0]
    main_area = np.dot(x[:-1], y[1:]) - np.dot(y[:-1], x[1:])
    # + 1 because of Pick's Theorem (?)
    return 0.5*(np.abs(main_area + correction)+trench_length) + 1

@stop_time
def part1(split_input):
    return polygon_area(*get_polygon(parse_part1(s_input)))

@stop_time
def part2(split_input):
    return polygon_area(*get_polygon(parse_part2(s_input)))

input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

s_input = split_input(input,remove_empty=True)
print("Part 1:")
part1(s_input)
# part 1 correct, sample for part 2 correct, but not main input for part 2 (57196493937396 is too low)
#rigth solution:    57196493937398
#my solution:       57196493937396
print("Part 2:")
part2(s_input)

