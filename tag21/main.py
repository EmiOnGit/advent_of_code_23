#!/usr/bin/env python

# import utils
import os, sys
sys.path.append(os.path.abspath(os.path.join('..')))
from utils import *
from typing import List, Tuple, Dict

@stop_time
def bfs_graph(matrix:List[List[int]],
              s:Tuple[int],
              max_step:int)->List[Tuple[int]]:

    if max_step%2 == 0:
        result[s] = 1
        matrix[s[0]][s[1]] = 1
        step = 0
    else:
        result = {}
        matrix[s[0]][s[1]] = 1
        step = 0
    search = [s]
    while step<max_step:
        neighbours = []
        if search == []: break
        while search != []:
            s = search.pop()
            x = s[1]
            y = s[0]
            if y+1<len(matrix) and matrix[y+1][x] == 0:
                neighbours.append((y+1,x))
                matrix[y+1][x] = 1
            
            if x+1 < len(matrix[0]) and matrix[y][x+1] == 0:
                neighbours.append((y,x+1))
                matrix[y][x+1] = 1
            
            if y-1>0 and matrix[y-1][x] == 0:
                neighbours.append((y-1,x))
                matrix[y-1][x] = 1
            
            if x-1>0 and matrix[y][x-1] == 0:
                neighbours.append((y,x-1))
                matrix[y][x-1] = 1
        step += 1
        search = neighbours
        if step%2 == 0:
            result.extend(neighbours)
    return len(result)


def parse(lines):
    matrix = [[0 for _ in range(len(lines))] for _ in range(len(lines[0]))]
    for y,line in enumerate(lines):
        for x,char in enumerate(line):
            if char == "#":
                matrix[y][x] = 1
            if char == "S": 
                start = (y,x)
    return start,matrix

input = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

input_lines = split_input()
start,matrix = parse(input_lines)
print("Part 1")
bfs_graph(matrix,start,64)
print("Part 2")
