''' count where both of the following are true:
1) The levels are either all increasing or all decreasing.
2) Any two adjacent levels differ by at least one and at most three.
'''
from aoc_common import get_data

def count_safe(data : list[list[int]]) -> int:
    safe_count : int = 0
    for report in data:
        if check_safe(report):
            safe_count += 1
    return safe_count

def check_safe(data : list[int]) -> bool:
    if (data[0] - data[1]) == 0:
        return False
    else:
        direction : int = (data[0] - data[1]) / abs(data[0] - data[1])
    for index in range(len(data)):
        if index == 0:
            pass
        elif data[index-1] - data[index] == 0:
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

my_data = get_data('input2.txt')
print(count_safe(my_data))