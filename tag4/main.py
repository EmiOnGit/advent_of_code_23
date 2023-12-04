#!/usr/bin/env python
def part1(input):
    res = 0
    for line in input.splitlines():
        if len(line) == 0:
            continue
        # remove 'Card [n]'
        line = line.split(':')[1]
        # split at '|' symbol
        [left, right] = line.split('|')
        left = [int(x) for x in left.split()]
        right = [int(x) for x in right.split()]
        left.sort()
        right.sort()
        l_index = 0
        r_index = 0
        sum = 0
        while l_index != len(left) and r_index != len(right):
            l_current = left[l_index]
            r_current = right[r_index]
            if l_current > r_current:
                r_index += 1
            elif l_current < r_current:
                l_index += 1
            else:
                sum = max(2 * sum, 1)
                r_index += 1
                l_index += 1
        res += sum
    return res


def part2(input):
    matches = []
    for line in input.splitlines():
        if len(line) == 0:
            continue
        # remove 'Card [n]'
        line = line.split(':')[1]
        # split at '|' symbol
        [left, right] = line.split('|')
        left = [int(x) for x in left.split()]
        right = [int(x) for x in right.split()]
        left.sort()
        right.sort()
        l_index = 0
        r_index = 0
        sum = 0
        while l_index != len(left) and r_index != len(right):
            l_current = left[l_index]
            r_current = right[r_index]
            if l_current > r_current:
                r_index += 1
            elif l_current < r_current:
                l_index += 1
            else:
                sum += 1
                r_index += 1
                l_index += 1
        matches.append(sum)
    card_count = [1 for x in range(len(matches))]
    for i in range(len(matches)):
        count = card_count[i]
        match = matches[i]
        for x in range(i+1,i+match+1):
            if x > len(matches):
                break
            card_count[x] += count
    sum2 = 0
    for count in card_count:
        sum2 += count
    return(sum2)
    

f = open("input_emi.txt", "r")
# f = open("input_viki.txt", "r")

input = f.read()
print("part1 solution: ", part1(input))
print("part2 solution: ", part2(input))
