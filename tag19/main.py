#!/usr/bin/env python

# import utils
import os, sys
sys.path.append(os.path.abspath(os.path.join('..')))
from utils import *
import os
import stat
import time


class Gear():
    def __init__(self,x:int,m:int,a:int,s:int) -> None:
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        self.gear_sum = x+m+a+s

    def __repr__(self) -> str:
        return f"x:{self.x},m:{self.m},a:{self.a},s:{self.s}\n"

#line : {x=787,m=2655,a=1222,s=2876}
def parse_gears(lines):
    gear_list = []
    for line in lines:
        if line == "": continue
        gear_list.append(Gear(*[int(val.split("=")[1].replace("}","")) for val in line.split(",")]))
    return gear_list



def parse_program(lines):
    file_name = "input_program.py"
    with open(file_name,"w+") as f:
        f.write("accepted_gears = []\n")
        for line in lines:
            split_line = line.split("{")
            func_name = split_line[0]
            if func_name=="in":
                func_name="first_workflow"
            f.write(f"def {func_name}(gear):\n")
            if_string = "if"
            for statement in split_line[1].split(","):
                if ":" not in statement:
                    func = statement.replace("}","")
                    f.write(f"\telse:\n")
                else:
                    func = statement.split(":")[1]
                    f.write(f"\t{if_string} gear.{statement.split(':')[0]}:\n")
                if func=="A":
                    f.write(f"\t\taccepted_gears.append(gear)\n\t\treturn\n")
                elif func=="R":
                    f.write(f"\t\treturn\n")
                else:
                    f.write(f"\t\t{func}(gear)\n")

                if if_string == "if":
                    if_string = "elif"
        f.write("def get_accepted_gears(gear_list):\n")
        f.write("\t[first_workflow(acc) for acc in gear_list]\n")
        f.write("\treturn accepted_gears")
        #f.write("\tres = [first_workflow(acc) for acc in gear_list]\n")
        #f.write("\treturn [x for x in res if x]\n")


    st = os.stat(file_name)
    os.chmod(file_name, st.st_mode | stat.S_IEXEC)

@stop_time
def part1(gear_lines):
    accepted_gears = get_accepted_gears(parse_gears(gear_lines))
    return sum([gear.gear_sum for gear in accepted_gears])

# only execute if you have time until the end of the universe
def part2():
    res = 0
    total = 4000*4000*4000*4000
    start_time = time.time()
    for x in range(1,4001):
        for m in range(1,4001):
            for a in range(1,4001):
                for s in range(1,4001):
                    gear = get_accepted_gears([Gear(x,m,a,s)])[0]
                    if gear:
                        res += gear.gear_sum
            print(f"Gears checked: {x*m*4000*4000}/{total}")
            s_per_gear = (time.time()-start_time)/x*m*4000*4000
            remaining_to_check = (4000-x)*(4000-m)*4000*4000
            print(f"You only need to wait {s_per_gear*remaining_to_check*60*60*24*365} years for the program to finish :^)")
    return res

input = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

lines = split_input()
split_index = lines.index("")
program_lines = lines[:split_index]
gear_lines = lines[split_index+1:]
parse_program(program_lines)

from input_program import *
print("Part 1")
part1(gear_lines)
print("Part 2")
part2()