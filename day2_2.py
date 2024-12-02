''' count where all of the following are true:
1) The levels are either all increasing or all decreasing.
2) Any two adjacent levels differ by at least one and at most three.
3) If removing a single level from an unsafe report would make it safe, the report instead counts as safe
'''

from aoc_common import get_data

def count_safe(data : list[list[int]]) -> int:
    safe_count : int = 0
    for report in data:
        if check_safe(report):
            safe_count += 1
        elif problem_dampener(report):
            safe_count += 1
    return safe_count

def check_safe(data : list[int]) -> bool:
    if (data[0] - data[1]) == 0:
        return False
    else:
        direction : int = (data[0] - data[1]) / abs(data[0] - data[1])
    for index in range(1, len(data)):
        if data[index-1] - data[index] == 0:
            return False
        elif ( 
            (data[index-1] - data[index]) / abs(data[index-1] - data[index]) == direction
            and 
            abs(data[index-1] - data[index]) < 4
            ):
            pass
        else:
            return False
    return True

def problem_dampener(data : list[int]) -> bool:
    for index in range(len(data)):
        # if you do test_level = data 
        # it creates a pointer to data
        # not a new list test_level
        test_level = [l for l in data]
        del test_level[index]
        if check_safe(test_level):
            return True
    return False

my_data = get_data('test2.txt')
print(count_safe(my_data))