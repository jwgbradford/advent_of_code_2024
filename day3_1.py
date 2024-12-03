'''
What do you get if you add up all of the results of the multiplications?
'''

import re
from aoc_common import read_file

def calc_mul(data : str) -> int:
    # you have a problem, you use regex
    mul_list = re.findall("mul\(([0-9]+),([0-9]+)\)", data)
    # now you have two problems
    mul_calc = 0
    for calc in mul_list:
        mul_calc += int(calc[0]) * int(calc[1])
    print(mul_calc)

my_data = read_file('input3.txt')
calc_mul(my_data)