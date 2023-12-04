
from itertools import product


path = "input_emi.txt"
file = open(path,"r")
input = file.read()
# contains array with tupel (index,number) for every line
num_arr = []
# contains array of index of chars for every line
char_arr = []
star_arr = []

def parse():
    for line in input.splitlines():
        num_line_arr = []
        char_line_arr = []
        star_line_arr = []
        new_number = ""
        for i,c in enumerate(line):
            if c.isnumeric():
                new_number += c
            elif (c == ".") | (c == " ") | (c == "\n"):
                if new_number!="":
                    n = int(new_number)
                    num_line_arr.append((i-len(new_number),n))
                    new_number = ""  
            else:
                char_line_arr.append(i)
                if c == "*":
                    star_line_arr.append(i)
                if new_number!="":
                    n = int(new_number)
                    num_line_arr.append((i-len(new_number),n))
                    new_number = ""
        if new_number != "":
            n = int(new_number)
            num_line_arr.append((i-len(new_number),n))
        num_arr.append(num_line_arr)
        char_arr.append(char_line_arr)
        star_arr.append(star_line_arr)

def part1():
    sum = 0
    for line_number, tuples in enumerate(num_arr):
        for number_entry in tuples:
            start = max(number_entry[0]-1,0)
            end = number_entry[0] + len(str(number_entry[1])) + 1

            for i in [max(line_number-1,0), line_number, min(line_number+1,len(num_arr)-1)]:
                if any([True for x in char_arr[i] if x in range(start,end)]):
                        sum += number_entry[1]
                        break
    return sum

def part2():
    sum = 0
    for line_number, star_line in enumerate(star_arr):
        for star_index in star_line:
            start = max(star_index -1,0)
            end = star_index + 1

            numbers_hit = []
            
            """
            for i in [max(line_number-1,0), line_number, min(line_number+1,len(num_arr)-1)]:
                for num in num_arr[i]:
                    if (num[0] < end) & (num[0]+len(str(num[1])) > start):
                        numbers_hit.append(num[0])
            """        
        
            for i in [line_number-1, line_number, line_number+1]:
                if (i < 0) | (i > len(num_arr)): continue
                line_hits = [n[1] for n in num_arr[i] if (n[0] < end + 1) & (n[0] + len(str(n[1])) > start )]
                numbers_hit.extend(line_hits)
            if len(numbers_hit) == 2:
                ratio = numbers_hit[0]*numbers_hit[1]
                sum += ratio
    return sum


parse()
print("Part 1 solution:",part1())
print("Part 2 solution:",part2())
