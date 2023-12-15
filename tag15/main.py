#!/usr/bin/env python

# import utils
import os, sys
sys.path.append(os.path.abspath(os.path.join('..')))
from utils import *
from typing import List, Tuple


def hash(string):
    sum = 0
    for ascii in [ord(c) for c in string]:
        sum += ascii
        sum *= 17
        sum = sum % 256
    return sum

def hash_string(list):
    return sum(hash(string) for string in list)

class Operation:
    def __init__(self, string):
        if '=' in string:
            [hash_string, focal_length] = list(string.split("="))
            self.focal_length = int(focal_length)
            self.operation = '='
        elif '-' in string:
            hash_string = list(string.split("-"))[0]
            self.operation = '-'
        else:
            raise Exception("couldn't parse operation with ["+string+"]")
        self.hash = hash(hash_string)
        self.label = hash_string
    def __repr__(self):
        focal_length = f", focal_length: {self.focal_length}" if hasattr(self,"focal_length") else ""
        return f"[label: {self.label} ,hash:{self.hash}, op: {self.operation} {focal_length}]"
    def __eq__(self, other):
        return self.label == other.label
        


    
def parse(is_part_two, input= None ):
    if input == None:
        f = open("input.txt", "r")
        input = f.read()
    input = input.replace("\n", "")
    if is_part_two:
        return list(map(Operation, input.split(",")))
    else:
        return input.split(",")
class BoxManager:
    def __init__(self):
        # Hashmap<HASH, List[Operation]>
        self.boxes = {}
    def __repr__(self):
        return "\n".join([str(box[0].hash) +":"+ str(box) for box in self.boxes.values() if len(box) != 0])
    def apply(self, operation):
        if operation.operation == '=':
            self.push(operation)
        elif operation.operation == '-':
            self.remove(operation)
        else:
            raise Exception("bad operation")
    def sum(self):
        total_sum = 0
        for hash, operations in self.boxes.items():
            total_sum += (hash + 1) * sum([(i+1) * operation.focal_length for i, operation in enumerate(operations)])
        return total_sum

            
    def push(self, operation):
        if operation.hash not in self.boxes.keys():
            self.boxes[operation.hash] = [operation]
            return

        box = self.boxes[operation.hash]
        if operation in box:
            i = box.index(operation)
            self.boxes[operation.hash][i] = operation
        else:
            self.boxes[operation.hash].append(operation)
    def remove(self, operation):
        if operation.hash in self.boxes.keys():
            try:
                self.boxes[operation.hash].remove(operation)
            except:
                return
        
                
            

input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
# Part 1
# parsed = parse(is_part_two=False)
# print(hash_string(parsed))
# Part 2
operations = parse(is_part_two=True)
boxes = BoxManager()
for operation in operations:
    boxes.apply(operation)
print(boxes)
print("sum:", boxes.sum())
