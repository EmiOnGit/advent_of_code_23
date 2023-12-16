#!/usr/bin/env python

# import utils
import os, sys
sys.path.append(os.path.abspath(os.path.join('..')))
from utils import *
from typing import List, Tuple
import copy
from enum import Enum


class Direction(Enum):
    right = 0,
    down = 1,
    left = 2,
    up = 3,

    def __str__(self) -> str:
        return super().__str__().replace("Direction.","")

class Object(Enum):
    vert_splitter = 0,
    hor_splitter = 1,
    right_mirror = 2,
    left_mirror = 3,
    empty_space = 4

    def from_str(label: str):
        if label == '|': return Object.vert_splitter
        if label == '-': return Object.hor_splitter
        if label == '/': return Object.right_mirror
        if label == '\\': return Object.left_mirror
        if label == '.': return Object.empty_space
        raise Exception("Could not parse character: ", label)
    
    def __str__(self) -> str:
        if self == Object.vert_splitter: return '|'
        if self == Object.hor_splitter: return '-'
        if self == Object.right_mirror: return '/'
        if self == Object.left_mirror: return '\\'
        if self == Object.empty_space: return '.' 



class Beam:
    def __init__(self, direction:Direction, x:int, y:int) -> None:
        self.direction = direction
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x},{self.y},{self.direction})"


class Tile:
    def __init__(self, x:int, y:int, direction: Direction) -> None:
        self.x = x
        self.y = y
        self.energized_from = [direction]

    def add_direction(self, direction:Direction):
        self.energized_from.append(direction)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __repr__(self) -> str:
        return f"({self.x},{self.y})"


def append_energized_tile(energized_tiles,current_tile):
    """Works inplace (hopefully); returns True if energized_tiles was modified, else False"""
    if current_tile not in energized_tiles:
        energized_tiles.append(current_tile)
    else:
        tile = energized_tiles[energized_tiles.index(current_tile)]
        # we already passed here from the same direction -> cycle found
        if current_tile.energized_from in tile.energized_from:
            # out of bounds beams will be removed later
            return False
            # haven't passed from this direction yet -> might energize new tiles
        else:
            tile.add_direction(current_tile.energized_from)
    return True



def move_beams(beams:List[Beam], matrix: List[List[Object]], energized_tiles: List[Tile]) -> Tuple[List[Beam],List[Tile],bool]:
    """Iterates through list of beams and moves every beam by one tile. Updates beams and energized tiles"""
    new_beams = []
    for beam in beams:
        direction = beam.direction
        x = beam.x
        y = beam.y
        try:
            obj = matrix[y][x]
        # sollte man wohl besser debuggen, versteh ich aber nicht
        except:
            beam.x = -1
            continue
        current_tile = Tile(x,y,direction)
        if not append_energized_tile(energized_tiles,current_tile):
            beam.x = -1
            break
        
        # / and \ can be simplified by changing the sign of 1 / -1 
        change_factor = 1 if obj == Object.right_mirror else -1
        # plus and minus are chosen as if it would be right_mirror, but get corrected by change_factor if it is left_mirror
        if obj == Object.right_mirror or obj == Object.left_mirror:
            if direction == Direction.right:
                beam.y = y - (1 * change_factor)
                beam.direction = Direction.up if change_factor == 1 else Direction.down
            elif direction == Direction.left:
                beam.y = y + (1 * change_factor)
                beam.direction = Direction.down if change_factor == 1 else Direction.up
            elif direction == Direction.up:
                beam.x = x + (1 * change_factor)
                beam.direction = Direction.right if change_factor == 1 else Direction.left
            elif direction == Direction.down:
                beam.x = x - (1 * change_factor)
                beam.direction = Direction.left if change_factor == 1 else Direction.right
        # -
        elif obj == Object.hor_splitter:
            if direction == Direction.right:
                beam.x = x + 1
            elif direction == Direction.left:
                beam.x = x - 1
            elif direction == Direction.up or direction == Direction.down:
                beam.x = x + 1
                beam.direction = Direction.right
                new_beams.append(Beam(Direction.left,x-1,y))
        # |
        elif obj == Object.vert_splitter:
            if direction == Direction.right or direction == Direction.left:
                beam.y = y + 1
                beam.direction = Direction.down
                new_beams.append(Beam(Direction.up, x, y-1))
            elif direction == Direction.up:
                beam.y = y - 1
            elif direction == Direction.down:
                beam.y = y + 1
        # .
        elif  obj == Object.empty_space:
            if direction == Direction.right:
                beam.x += 1
            elif direction == Direction.left:
                beam.x -= 1
            elif direction == Direction.up:
                beam.y -= 1
            elif direction == Direction.down:
                beam.y += 1
    # remove out of bound beams
    beams = [beam for beam in beams if 0<=beam.y<len(matrix) and 0<=beam.x<len(matrix[0])]
    new_beams = [beam for beam in new_beams if 0<=beam.y<len(matrix) and 0<=beam.x<len(matrix[0])]
    # add new beams
    beams.extend(new_beams)
    return beams, energized_tiles
        
@stop_time        
def get_energized(matrix:List[Object]) -> int:
    energized_tiles = []
    beams = [Beam(Direction.right,0,0)]
    while beams != []:
        beams, energized_tiles = move_beams(beams,matrix,energized_tiles)
    print_energized_fields(energized_tiles,matrix)
    return len(energized_tiles)

def print_energized_fields(energized_tiles,matrix):
    s = ""
    for i in range(len(matrix)):
        s+=str(i)
        for j in range(len(matrix[0])):
            if Tile(j,i,Direction.down) in energized_tiles:
                s+='#'
            else:
                s+='.'
        s+='\n'
    print(s)

def parse_tiles(input_lines: List[str]):
    return [[Object.from_str(c) for c in row] for row in input_lines]



input = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""
split_input = split_input()
matrix = parse_tiles(split_input)
# way too slow for part 2 :(
get_energized(matrix)








