#!/usr/bin/env python
def part1(input):
    max_r = 12
    max_g = 13
    max_b = 14
    sum = 0
    for i,line in enumerate(input.splitlines()):
        game = i+1
        for color in ["green","red","blue"]:
            for split in line.split(color)[:-1]:
                if len(split) == 0:
                    continue
                count = int(split.split(" ")[-2])
                if color == "green": 
                    max = max_g
                elif color == "red":
                    max = max_r
                elif color == "blue":
                    max = max_b
                if max < count:
                    game = 0
                    break;
        sum = sum + game
    return(sum)

def part2(input):
   
    sum = 0
    for line in input.splitlines():
        line_product = 1
        for color in ["green","red","blue"]:
            max = 0
            for split in line.split(color)[:-1]:
                if len(split) == 0:
                    continue
                count = int(split.split(" ")[-2])
                if max < count:
                    max = count
            line_product *= max
        sum = sum + line_product
    return(sum)

import sys
f = open("input_viki.txt", "r")
input = f.read()
print(f"part1 answer: {part1(input)}")
print(f"part2 answer: {part2(input)}")
