import re

f = open("viki_input.txt","r")
file = f.read()
sum = 0

#part 1 (only digits)
for line in file.splitlines():
    numbers = re.findall("\d", line)
    first = int(numbers[0])
    last = int(numbers[-1])
    res = first*10 + last
    sum += res
print("puzzle 1 sum", sum)

#part 2 (words and digits)

def word_at(line, index, word):
   if len(word)+index >= len(line):
       return False
   return word in line[index:index+len(word)]

sum = 0
for line in file.splitlines():
    first = -1
    last = -1
    for i in range (len(line)):
        for x, word in enumerate(["zero","one","two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            if word_at(line,i,word):
                if first == -1:
                    first = x
                last = x
        sum += first*10 * last
print("part 2 sum", sum)





    
