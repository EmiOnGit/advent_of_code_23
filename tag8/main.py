#!/bin/env python
from typing import List, Tuple
def binary_search(list: List[Tuple[str, Tuple[str,...]]], key: str, l = 0, r = -1):
    if r == -1:
        r = len(list)
    middle_index = int((l + r) / 2)
    middle = list[middle_index]
    if middle[0] == key:
        return middle
    if middle[0] > key:
        return binary_search(list, key, l=l, r=middle_index-1)
    if middle[0] < key:
        return binary_search(list, key, l=middle_index+1 , r=r)

def parse(file_path):
    import os
    if os.path.isfile(file_path):
        f = open(file_path, "r")
        input = f.read()
    else:
        input = file_path
    lines = input.splitlines()
    steps = lines[0]

    map_list = []
    for line in lines[2:]:
        [key, rest] = line.replace(' ','').split('=')
        value = tuple(rest.replace('(','').replace(')','').split(','))
        key = key[::-1]
        value = (value[0][::-1], value[1][::-1])
        map_list.append((key,value))

    map_list.sort(key = lambda x: x[0])
    return(steps, map_list)

def part1(steps, map_list, start_point="AAA"):
    current = start_point
    end_point = "ZZZ"
    steps_count = 0
    while True:
        for direction in steps:
            steps_count += 1
            element = binary_search(map_list, current)
            if direction == "R":
                current = element[1][1]
            else:
                current = element[1][0]
            if current == end_point:
                return steps_count

def part2(steps, map_list):
    points = []
    for value in map_list:
        if value[0][0] == 'A':
            points.append(value[0])
        else:
            break
    steps_count = 0
    while True:
        for direction in steps:
            steps_count += 1

            entries = [binary_search(map_list,point) for point in points]
            if direction == "R":
                points = [entry[1][1] for entry in entries]
            else:
                points = [entry[1][0] for entry in entries]
            if all([point[0] == 'Z' for point in points]):
                return steps_count
            if steps_count % 1_000_000 == 0:
                print(steps_count)

input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
result = part1(*parse("input_viki.txt"))
print(f"part1 result: {result}")
result = part2(*parse("input_viki.txt"))
print(f"part2 result: {result}")
            
        

        
