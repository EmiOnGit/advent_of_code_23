"""input = 0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

f = open("input_viki.txt","r")
input = f.read()

def part1():
    final_sum = 0
    for line in input.splitlines():
        splitline = line.split()
        difference_lists = [[int(x) for x in splitline]]
        while any(difference_lists[-1]):
            differences = []
            for current, next in zip(difference_lists[-1],difference_lists[-1][1:]):
                differences.append(next-current)
            difference_lists.append(differences)

        value_before = 0
        for value in difference_lists[::-1]:
            value_before += value[-1]
        final_sum += value_before
    return final_sum

def part2():
    final_sum = 0
    for line in input.splitlines():
        splitline = line.split()
        difference_lists = [[int(x) for x in splitline]]
        while any(difference_lists[-1]):
            differences = []
            for current, next in zip(difference_lists[-1],difference_lists[-1][1:]):
                differences.append(next-current)
            difference_lists.append(differences)

        value_before = 0
        for value in difference_lists[::-1]:
            value_before = value[0] - value_before
        print(value_before)
        final_sum += value_before
    return final_sum

print("result part1:",part1())
print("result part2:",part2())