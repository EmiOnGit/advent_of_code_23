import math
import time

def parse(input):
    row_reports = []
    for line in input.splitlines():
        damaged_count = [int(x) for x in line.split(" ")[1].split(",")]
        # -1 = ?, 1 = ., 0 = #
        new_line = line.split(" ")[0].replace("?","2").replace(".","1").replace("#","0")
        arrangement = [int(char) for char in new_line]
        arrangement = [-1 if x==2 else x for x in arrangement]
        row_reports.append([arrangement,damaged_count])

    return row_reports

    
def counts_consecutive_zeroes(combination):
    counts = []
    current_count = 0
    for num in combination:
        if num == 0:
            current_count += 1
        elif current_count > 0:
            counts.append(current_count)
            current_count = 0
    if current_count > 0:
        counts.append(current_count)
    return counts


def get_valid_combinations_the_smart_way(combinations,report_row):
    valid_combinations = 0
    for combination in combinations:
        combination_counts = counts_consecutive_zeroes(combination)
        if combination_counts == report_row[1]:
            valid_combinations += 1
    return valid_combinations


def check_if_valid_combination(combination, damaged_contigous):
    current_count = 0
    damaged_count_iter = iter(damaged_contigous)
    for num in combination:
        if num == 0:
            current_count += 1
        elif current_count > 0:
            current_damaged_count = next(damaged_count_iter)

            if current_count != current_damaged_count:
                return False
            current_count = 0
    try:
        current_damaged_count = next(damaged_count_iter)
        return current_damaged_count == current_count
    except:
        return True

def get_valid_combinations_the_maybe_faster_way(combinations,report_row):
    valid_combinations = 0
    for combination in combinations:
        if check_if_valid_combination(combination,report_row[1]):
            valid_combinations += 1
    return valid_combinations


def get_combinations(report_row):
    combinations = []
    spring_arrangement = report_row[0].copy()
    unknown_values = [i for i,x in enumerate(spring_arrangement) if x==-1]
    binary_len = len(unknown_values)
    max_number = int(math.pow(2,binary_len)-1)
    missing_number_damaged = sum(report_row[1]) - sum([1 for x in spring_arrangement if x == 0])

    for i in range(max_number+1):
        if i.bit_count()==missing_number_damaged:
            for nth_unkown, unknown_index in enumerate(unknown_values):
                bit_is_one = i&1<<nth_unkown != 0
                spring_arrangement[unknown_index] = 0 if bit_is_one else 1
            combinations.append([x for x in spring_arrangement])
    return combinations


def check_all_rows(parsed_input,way="easy"):
    total_number_valid = []
    for row in parsed_input:
        combinations = get_combinations(row)
        if way=="easy":
            valid_combinations = get_valid_combinations_the_smart_way(combinations,row)
        elif way=="fast":
            valid_combinations = get_valid_combinations_the_maybe_faster_way(combinations,row)
        else:
            raise Exception("No such way known: " + way)
        total_number_valid.append(valid_combinations)
    return total_number_valid


def check_combinations_one_by_one(report_row):
    spring_arrangement = report_row[0].copy()
    unknown_values = [i for i,x in enumerate(spring_arrangement) if x==-1]
    max_number = int(math.pow(2,len(unknown_values))-1)
    missing_number_damaged = sum(report_row[1]) - sum([1 for x in spring_arrangement if x == 0])
    number_combinations = 0

    for i in range(max_number+1):
        if i.bit_count()==missing_number_damaged:
            for nth_unkown, unknown_index in enumerate(unknown_values):
                bit_is_one = i&1<<nth_unkown != 0
                spring_arrangement[unknown_index] = 0 if bit_is_one else 1
            if check_if_valid_combination(spring_arrangement,report_row[1]):
                number_combinations += 1
    return number_combinations
 

def check_all_rows_in_place(parsed_input):
    total_combinations = 0
    for row in parsed_input:
        total_combinations += check_combinations_one_by_one(row)
    return total_combinations


#print(parsed_input)
input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

f = open("input_viki.txt","r")
input = f.read()
parsed_input = parse(input)

# calculates all combinations 
# stores them in lists 
# checks if all contigous damaged springs fulfill the restrictions
start_time = time.time()
c = check_all_rows(parsed_input,way='easy')
print(f"solution part1 (easy way): {sum(c)} \n completed in {(time.time() - start_time)} seconds")

# calculates all combinations
# stores them in lists 
# checks if all contigous damaged springs fulfill the restrictions 
# (stops as soon as one restriction is violated)
start_time = time.time()
c = check_all_rows(parsed_input,way='fast')
print(f"solution part1 (fast way): {sum(c)} \n completed in {(time.time() - start_time)} seconds")

# while calculating all combinations: 
# checks if all contigous damaged springs fulfill the restrictions 
# (stops as soon as one restriction is violated)
start_time = time.time()
c = check_all_rows_in_place(parsed_input)
print(f"solution part1 (even faster way): {c} \n completed in {(time.time() - start_time)} seconds")


