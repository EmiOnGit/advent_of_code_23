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
    
f = open("input_emi.txt", "r")
input = f.read()
lines = input.splitlines()
steps = lines[0]

map_list = []
for line in lines[2:]:
    [key, rest] = line.replace(' ','').split('=')
    value = tuple(rest.replace('(','').replace(')','').split(','))
    map_list.append((key,value))
map_list.sort(key = lambda x: x[0])

current = "AAA"
end_point = "ZZZ"
steps_count = 0
found_end_point = False
while not found_end_point:
    for direction in steps:
        steps_count += 1
        element = binary_search(map_list, current)
        if direction == "R":
            current = element[1][1]
        else:
            current = element[1][0]
        if current == end_point:
            found_end_point = True
            break
print(f"steps {steps_count}")

            
        

        
