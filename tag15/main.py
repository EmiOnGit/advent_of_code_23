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
def parse(input = None):
    if input == None:
        f = open("input.txt", "r")
        input = f.read()
    input = input.replace("\n", "")
    return input.split(",")
    
# input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

parsed = parse()
print(hash_string(parsed))
