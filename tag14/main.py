#!/usr/bin/env python

# import utils
import copy
from itertools import cycle
import os, sys
sys.path.append(os.path.abspath(os.path.join('..')))
from utils import *
from typing import List, Tuple
from enum import Enum

class Rocks(Enum):
    Round = 0
    Square = 1
    Empty = 2

    def from_char_to_type(char):
        if char == ".":
            return Rocks.Empty
        elif char == "#":
            return Rocks.Square
        else:
            return Rocks.Round
        
    def to_char(self):
        if self == Rocks.Round:
            return 'O'
        elif self == Rocks.Square:
            return '#'
        else:
            return '.'
        
    def __repr__(self) -> str:
        return self.to_char()
    
class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3

def parse(input_lines):
    column_list = [[] for x in range(len(input_lines[0]))]
    for line in input_lines:
        for i,char in enumerate(line):
            column_list[i].append(Rocks.from_char_to_type(char))
    return column_list

def keep_rolling(input_columns):
    for column in input_columns:
        place_to_roll = 0
        for i in range(len(column)):
            if column[i] == Rocks.Empty: 
                continue
            if column[i] == Rocks.Round:
                column[i], column[place_to_roll] = column[place_to_roll], column[i]
                place_to_roll += 1
            if column[i] == Rocks.Square:
                place_to_roll = i+1

def rotate_90_degrees_counter_clockwise(input_matix):
    return [list(row) for row in reversed(list((zip(*input_matix))))]


def rotate_90_degrees_clockwise(input_matix):
    return [list(row) for row in (zip(*reversed(input_matix)))]


def circle(matrix):
    for dir in ["North","West","South","East"]:
        keep_rolling(matrix)
        matrix = rotate_90_degrees_counter_clockwise(matrix)
    return matrix

def calculate_load(input_columns):
    return sum([sum([len(l)-i for i,x in enumerate(l) if x==Rocks.Round]) for l in input_columns])


def get_hashed_matrix(input_columns):
    return hash(str(input_columns))

@stop_time
def part1(input_columns):
    print("Part 1")
    keep_rolling(input_columns)
    return calculate_load(input_columns)


def find_cycle(org_matrix):
    matrix = copy.deepcopy(org_matrix)
    hash_values_list = [get_hashed_matrix(matrix)]
    i = 1 
    while i < 100_000:
        matrix = circle(matrix)
        new_hash = get_hashed_matrix(matrix) 
        if new_hash in hash_values_list:
            cycle_start = hash_values_list.index(new_hash)
            return i, cycle_start+1
        hash_values_list.append(new_hash)
        i += 1
    raise Exception("No circle found :(")


@stop_time
def part2(matrix):
    print("Part 2")
    i,cycle_start = find_cycle(matrix)
    remaining_circles = (1_000_000_000-cycle_start) % (i-(cycle_start-1))
    for _ in range(cycle_start+remaining_circles):
        matrix = circle(matrix)
    return calculate_load(matrix)
    


print_matrix = lambda matrix: print(']\n'.join([row[::-1] for row in str(rotate_90_degrees_clockwise(matrix)).replace(",","").split("]")]).replace("[","").replace("]",""))

input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

input_lines = split_input()
part1(parse(input_lines))
part2(parse(input_lines))

    

