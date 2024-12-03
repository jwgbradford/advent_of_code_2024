'''
What do you get if you add up all of the results of the multiplications?

There are two new instructions you'll need to handle:
- The do() instruction enables future mul instructions.
- The don't() instruction disables future mul instructions.
'''

import re
from aoc_common import read_file

def calc_mul(data : str) -> int:
    # you have a problem, you use regex
    mul_list = re.findall("mul\\(([0-9]+),([0-9]+)\\)", data)
    # now you have two problems
    mul_calc = 0
    for calc in mul_list:
        mul_calc += int(calc[0]) * int(calc[1])
    print(mul_calc)

def remove_disabled(data : str) -> str:
    new_calc = re.sub("don't().*?do()", "", data)
    print(new_calc)
    return new_calc

my_data = read_file('test3_1.txt')
my_data = remove_disabled(my_data)
calc_mul(my_data)