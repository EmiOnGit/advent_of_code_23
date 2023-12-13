#!/usr/bin/env python

# import utils
import os, sys
sys.path.append(os.path.abspath(os.path.join('..')))
from utils import *

import time
import numpy as np
from multiprocessing.pool import Pool

def parse(input_blocks):
    blocks = []
    for block in input_blocks:
        lines = [line for line in filter(lambda line: line != "", block.splitlines())]
        matrix = []
        for line in lines:
            matrix.append(np.array([0 if c == '.' else 1 for c in line]))
        matrix = np.array(matrix)
        blocks.append(matrix)
    return blocks


def check_mirror_row(row: int, matrix, is_part1: bool):
    row += 1
    height = min(row, len(matrix) - row)
    wildcard_is_used = is_part1
    if height <= 0:
        return False
    for i in range(height):
        upper = row - i - 1
        lower = row + i
        equals = matrix[upper] == matrix[lower]
        if not all(equals):
            if np.count_nonzero(equals == False) == 1:
                if wildcard_is_used:
                    return False
                else:
                    wildcard_is_used = True
            else:
                return False
    return wildcard_is_used
def find_mirror(matrix, is_part1):

    n = len(matrix)
    for i in range(n):
        is_mirror = check_mirror_row(i,matrix,is_part1)
        if is_mirror:
            return 100 * (i+1)
    
    matrix = np.transpose(matrix)
    n = len(matrix)
    for i in range(n):
        is_mirror = check_mirror_row(i,matrix, is_part1)
        if is_mirror:
            return (i+1)
    assert False, "matrix has no mirror"
def part1(matrix):
    return find_mirror(matrix,True)
def part2(matrix):
    return find_mirror(matrix,False)
@stop_time(1)
def part1_full(blocks):
    return sum(map(part1, blocks))
@stop_time(2)
def part2_full(blocks):
    return sum(map(part2, blocks))
if __name__ == '__main__':
    input = input(splitter = "\n\n")
    blocks = parse(input)
    blocks = blocks * 200
    # without multithreading
    part1_full(blocks)
    part2_full(blocks)

    # with multithreading
    with Pool() as p:
        start_time = time.time()
        res = sum(p.map(part1,blocks))
        print(f"solution part1: {res} \n completed in {(time.time() - start_time)} seconds")

        start_time = time.time()
        res = sum(p.map(part2,blocks))
        print(f"solution part2: {res} \n completed in {(time.time() - start_time)} seconds")
