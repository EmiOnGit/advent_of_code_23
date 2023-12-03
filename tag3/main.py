file = open("input_viki.txt","r")
input = file.read()


def part1():
    # contains array with tupel (index,number) for every line
    num_arr = []
    # contains array of index of chars for every line
    char_arr = []
    sum = 0
    for line in input.splitlines():
        num_line_arr = []
        char_line_arr = []
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
                if new_number!="":
                    n = int(new_number)
                    num_line_arr.append((i-len(new_number),n))
                    new_number = ""
        if new_number != "":
            n = int(new_number)
            num_line_arr.append((i-len(new_number),n))
        num_arr.append(num_line_arr)
        char_arr.append(char_line_arr)

    sum = 0
    for line_number, tuples in enumerate(num_arr):
        for number_entry in tuples:
            start = max(number_entry[0]-1,0)
            end = number_entry[0] + len(str(number_entry[1])) + 1

            for i in [max(line_number-1,0), line_number, min(line_number+1,len(num_arr)-1)]:
                if any([True for x in char_arr[i] if x in range(start,end)]):
                        sum += number_entry[1]
                        break

print(sum)