
from copy import deepcopy




class Matrix:
    def __init__(self, input):
        self.inner = [line for line in input.splitlines()]
    def __getitem__(self, position):
        return self.inner[position[0]][position[1]]

    # find start position which is indicated with a 'S' character 
    def start_position(self):
        for line_index, line in enumerate(self.inner):
            char_index = line.find('S')
            if char_index != -1:
                return [line_index, char_index]
        assert False, ("Oh no, we no found start on point in matrix list kappa")
    
    def adjacent_tiles(self, current_tile):
        character = self[current_tile]
        adj1 = current_tile.copy()
        adj2 = current_tile.copy()
        if character == '|':
            adj1[0] += 1
            adj2[0] -= 1
        elif character == '-':
            adj1[1] += 1
            adj2[1] -= 1
        elif character == 'L':
            adj1[0] -= 1
            adj2[1] += 1
        elif character == 'J':
            adj1[0] -= 1
            adj2[1] -= 1
        elif character == '7':
            adj1[0] += 1
            adj2[1] -= 1
        elif character == 'F':
            adj1[0] += 1
            adj2[1] += 1
        elif character == '.':
            panic("oh no bad character")
        elif character == 'S':
            adjs = []
            # north
            temp = current_tile.copy()
            temp[0] -= 1
            if self[temp] in ['|', '7','F']:
                adjs.append(temp)
            # east
            temp = current_tile.copy()
            temp[1] += 1
            if self[temp] in ['-', 'J','7']:
                adjs.append(temp)
            # south
            temp = current_tile.copy()
            temp[0] += 1
            if self[temp] in ['|', 'L','J']:
                adjs.append(temp)
            # west
            temp = current_tile.copy()
            temp[1] -= 1
            if self[temp] in ['-', 'F','L']:
                adjs.append(temp)
            assert(len(adjs) == 2)
            adj1 = adjs[0]
            adj2 = adjs[1]
        return (adj1, adj2)

    def find_next(self, position, last_position):
        adjacent_tiles = self.adjacent_tiles(position)
        if last_position is None:
            return adjacent_tiles[0]
        return adjacent_tiles[(adjacent_tiles.index(last_position) + 1) % 2]
        

def parse(input):
    path = []
    input_matrix = Matrix(input)
    start_pos = input_matrix.start_position()

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
input = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
f = open("input_emi.txt", 'r')
input = f.read()
import math
path = parse(input)
max_length = math.ceil(len(path) / 2)
print("path1 result:", max_length)
