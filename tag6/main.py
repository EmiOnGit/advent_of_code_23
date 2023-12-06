#!/usr/bin/env python

from typing import List

def parse1(input_string: str):
    [time_line, distance_line] = input_string.splitlines()
    times = [int(time_value) for time_value in time_line.split()[1:]]
    distances = [int(distance_value) for distance_value in distance_line.split()[1:]]
    return (times, distances)

def parse2(input_string: str):
    [time_line, distance_line] = input_string.splitlines()
    times = int(time_line.replace(' ', '').split(':')[1])
    distances = int(distance_line.replace(' ', '').split(':')[1])
    return (times, distances)
    
def calculate(times: List[int], records: List[int]):
    product = 1
    for time, last_record in zip(times,records):
        total = sum([travel_distance(wait_time, time) > last_record for wait_time in range(time)])
        product = product * total
    return product

def travel_distance(wait_time: int, total_time: int):
    race_time = total_time - wait_time
    return wait_time * race_time

f = open("input_emi.txt", 'r')
input = f.read()
(times, records) = parse1(input)
product = calculate(times, records)
print("result part 1:", product)
(time, record) = parse2(input)
sum = calculate([time], [record])
print("result part 2:", sum)
