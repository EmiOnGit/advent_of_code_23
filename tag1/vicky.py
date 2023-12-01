import re

f = open("input.txt","r")
sum = 0

for line in f.read().splitlines():
    numbers = re.findall("\d", line)
    first = int(numbers[0])
    last = int(numbers[-1])
    res = first*10 + last
    sum += res
print("puzzle 1 sum", sum)






    
