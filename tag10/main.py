from enum import Enum
import numpy as np
from typing import Tuple
from typing import List
class Dir(Enum):
    North = 0
    East = 1
    South = 2
    West = 3
    def move(self, row: int, column: int):
        if self == self.North:
            return [row-1,column]
        if self == self.East:
            return [row,column+1]
        if self == self.South:
            return [row+1,column]
        if self == self.West:
            return [row,column-1]
    def rotate_right(self):
        return Dir((self.value + 1) % 4)
    def rotate_left(self):
        return Dir((self.value - 1) % 4)
def direction_from_delta(delta: List[int]):
    if all(delta == [-1,0]):
        return Dir.South
    if all(delta == [0, 1]):
        return Dir.West
    if all(delta == [1,0]):
        return Dir.North
    if all(delta == [0,-1]):
        return Dir.East
class Cluster(Enum):
    Unknown = 0
    One = 1
    Two = 2
    Path = 3
    


class Matrix:
    def __init__(self, input):
        self.inner = [[char for char in line] for line in input.splitlines()]
    def __getitem__(self, position):
        return self.inner[position[0]][position[1]]
    def __repr__(self):
        inner = '\n'.join(str(line) for line in self.inner)
        clusters = '\n'.join(' '.join(str(cluster.value) for cluster in cluster_row) for cluster_row in self.clusters)
        return inner +"\n"+ clusters

    # find start position which is indicated with a 'S' character 
    def start_position(self):
        for line_index, line in enumerate(self.inner):
            try:
                char_index = line.index('S')
                return [line_index, char_index]
            except:
                continue
        assert False, ("Oh no, we no found start on point in matrix list kappa")
    
    def adjacent_tiles(self, current_tile):
        character = self[current_tile]
        if character == '|':
            adjs = (Dir.North, Dir.South)
        elif character == '-':
            adjs = (Dir.West, Dir.East)
        elif character == 'L':
            adjs = (Dir.North, Dir.East)
        elif character == 'J':
            adjs = (Dir.North, Dir.West)
        elif character == '7':
            adjs = (Dir.South, Dir.West)
        elif character == 'F':
            adjs = (Dir.East, Dir.South)
        elif character == '.':
            panic("oh no bad character")
        elif character == 'S':
            adjs = []
            # north
            temp = Dir.North.move(*current_tile)
            if self[temp] in ['|', '7','F']:
                adjs.append(Dir.North)
            # east
            temp = Dir.East.move(*current_tile)
            if self[temp] in ['-', 'J','7']:
                adjs.append(Dir.East)
            # south
            temp = Dir.South.move(*current_tile)
            if self[temp] in ['|', 'L','J']:
                adjs.append(Dir.South)
            # west
            temp = Dir.West.move(*current_tile)
            if self[temp] in ['-', 'F','L']:
                adjs.append(Dir.West)
            assert(len(adjs) == 2)
            adjs = (adjs[0], adjs[1])

        return (adjs[0].move(*current_tile), adjs[1].move(*current_tile))
    

    def find_next(self, position, last_position):
        adjacent_tiles = self.adjacent_tiles(position)
        if last_position is None:
            return adjacent_tiles[0]
        return adjacent_tiles[(adjacent_tiles.index(last_position) + 1) % 2]

    def simplify_matrix_representation(self, path: List[Tuple[int,int]]):
        for row in range(len(self.inner)):
            for column in range(len(self.inner[row])):
                if [row, column] not in path and self.inner[row][column] != '.':
                    self.inner[row][column] = 'x'
                    

    def is_in_bounds(self, row,column):
        if row < 0 or column < 0:
            return False
        return len(self.inner) > row and len(self.inner[0]) > column
    def init_clusters(self, path: List[List[int]]):
        self.clusters = [[Cluster.Unknown] * len(row) for row in self.inner]
        for point in path:
            self.clusters[point[0]][point[1]] = Cluster.Path

            
    def grow_clusters(self):
        has_changed = False
        for row in range(len(self.clusters)):
            for column in range(len(self.clusters[0])):
                cluster = self.clusters[row][column]
                if cluster != Cluster.Unknown:
                    continue
                for dir in [Dir.North, Dir.East, Dir.South, Dir.West]:
                    position = dir.move(row,column)
                    if not self.is_in_bounds(*position):
                        continue
                    tile = self.clusters[position[0]][position[1]]
                    if tile == Cluster.One or tile == Cluster.Two:
                        self.clusters[row][column] = tile
                        has_changed = True
                        break
        return has_changed


    def romantic_walk_around(self, path: List[List[int]]):
        previous_index = -1
        for current, next in zip(path, path[1:]):
            if previous_index != -1:
                previous = path[previous_index]

                delta = (np.array(current) - np.array(previous))
                direction = direction_from_delta(delta)
                left_direction = direction.rotate_left()
                right_direction = direction.rotate_right()
                left_tile = left_direction.move(*current)
                right_tile = right_direction.move(*current)
                if self.is_in_bounds(*left_tile):
                    if self.clusters[left_tile[0]][left_tile[1]] != Cluster.Path:
                        self.clusters[left_tile[0]][left_tile[1]] = Cluster.One
                if self.is_in_bounds(*right_tile):
                    if self.clusters[right_tile[0]][right_tile[1]] != Cluster.Path:
                        self.clusters[right_tile[0]][right_tile[1]] = Cluster.Two
                
            delta = (np.array(next) - np.array(current))
            previous_index += 1
            direction = direction_from_delta(delta)
            left_direction = direction.rotate_left()
            right_direction = direction.rotate_right()
            left_tile = left_direction.move(*current)
            right_tile = right_direction.move(*current)
            if self.is_in_bounds(*left_tile):
                if self.clusters[left_tile[0]][left_tile[1]] != Cluster.Path:
                    self.clusters[left_tile[0]][left_tile[1]] = Cluster.One
            if self.is_in_bounds(*right_tile):
                if self.clusters[right_tile[0]][right_tile[1]] != Cluster.Path:
                    self.clusters[right_tile[0]][right_tile[1]] = Cluster.Two
    def find_enclosed_cluster(self):
        row = self.clusters[0]
        if any([cluster == Cluster.One for cluster in row]):
            return Cluster.Two
        if any([cluster == Cluster.Two for cluster in row]):
            return Cluster.One
        row = self.clusters[-1]
        if any([cluster == Cluster.One for cluster in row]):
            return Cluster.Two
        if any([cluster == Cluster.Two for cluster in row]):
            return Cluster.One
        for cluster_pair in [[row[0],row[-1]] for row in self.clusters]:
            if any([cluster == Cluster.One for cluster in cluster_pair]):
                return Cluster.Two
            if any([cluster == Cluster.Two for cluster in cluster_pair]):
                return Cluster.One
    def count_enclosed(self):
        sum = 0
        enclosed_cluster = self.find_enclosed_cluster()
        for row in range(len(self.inner)):
            for column in range(len(self.inner[0])):
                if self.clusters[row][column] ==Cluster.Unknown:
                    sum += 1
                if self.clusters[row][column] == enclosed_cluster:
                    # if self.inner[row][column] == '.':
                    sum += 1
        return sum
            
        

def parse(input_matrix):
    start_pos = input_matrix.start_position()

    path = [start_pos]
    current = input_matrix.find_next(start_pos, None)
    last = start_pos
    
    while current != start_pos:
        path.append(current)
        next_temp = input_matrix.find_next(current, last)
        last = current
        current = next_temp
    return path

    


input = """.....
.S-7.
.|.|.
.L-J.
....."""
input = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""
f = open("input_emi.txt", 'r')
input = f.read()
import math
input_matrix = Matrix(input)
path = parse(input_matrix)
max_length = math.ceil(len(path) / 2)
print("path1 result:", max_length)

input_matrix.simplify_matrix_representation(path)
input_matrix.init_clusters(path)
input_matrix.romantic_walk_around(path)
can_grow = True
while can_grow:
    can_grow = input_matrix.grow_clusters()

print(input_matrix.count_enclosed())
