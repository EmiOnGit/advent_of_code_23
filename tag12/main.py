import math

#first example: ???.### 1,1,3
def get_valid_combinations_pls_dont_look_at_me(combinations,report_row):
    valid_combinations = 0
    for org_combination in combinations:
        # neccesary to check last
        combination = org_combination.copy()
        combination.append(1)
        
        damaged_count_iter = iter(report_row[1])
        current_damaged_count = next(damaged_count_iter)
        damaged_contiguous = -1
        print("combinatino:", combination)
        invalid_combination = False
        for spring in combination:
            print("spring:",spring)
            print("current_damaged_count:",current_damaged_count)
            if spring == 1 and damaged_contiguous!=-1:
                if current_damaged_count != damaged_contiguous:
                    invalid_combination = True
                    print("Found invalid combination")
                    break
                else:
                    try:
                        current_damaged_count = next(damaged_count_iter)
                    except:
                        print("no more segments left")
                        ()
                    print("valid segment")
                damaged_contiguous = -1
            if spring == 0:
                if damaged_contiguous == -1:
                    damaged_contiguous = 0
                damaged_contiguous += 1
                print("damaged_contigous:",damaged_contiguous)
        if not invalid_combination: 
            print("Valid combination")
            valid_combinations+=1
    return valid_combinations
 

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

def count_set_bits(n):
    count = 0
    while n != 0:
        count += n&1
        n = n>>1
    return count

def get_combinations(report_row):
    combinations = []
    unknown_values = [i for i,x in enumerate(report_row[0]) if x==-1]
    binary_len = len(unknown_values)
    max_number = int(math.pow(2,binary_len)-1)
    missing_number_damaged = sum(report_row[1]) - sum([1 for x in report_row[0] if x == 0])

    for i in range(max_number+1):
        if count_set_bits(i)==missing_number_damaged:
            for nth_unkown, unknown_index in enumerate(unknown_values):
                bit_is_one = i&int(math.pow(2,nth_unkown)) != 0
                report_row[0][unknown_index] = 0 if bit_is_one else 1
            combinations.append([x for x in report_row[0]])
    return combinations

       
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

#first example: ???.### 1,1,3
def get_valid_combinations_the_smart_way(combinations,report_row):
    valid_combinations = 0
    for combination in combinations:
        combination_counts = counts_consecutive_zeroes(combination)
        if combination_counts == report_row[1]:
            valid_combinations += 1
    return valid_combinations

def check_all_rows(parsed_input):
    total_number_valid = []
    for row in parsed_input:
        combinations = get_combinations(row)
        valid_combinations = get_valid_combinations_the_smart_way(combinations,row)
        total_number_valid.append(valid_combinations)
    return total_number_valid


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
print("solution part1: ",sum(check_all_rows(parsed_input)))

# ???.### 1,1,3
# ???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3


