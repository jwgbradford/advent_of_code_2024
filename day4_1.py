'''
She only has to find one word: XMAS.

This word search allows words to be:
- horizontal, 
- vertical, 
- diagonal, 
- written backwards, or even 
- overlapping other words.
'''

from aoc_common import read_file
import re

def get_data(file : str) -> list[str]:
    file_data : str = read_file(file)
    data_list : list[str] = file_data.split("\n")
    del data_list[-1]
    return data_list

def xmas_search(line : str) -> int:
    count = 0
    count += len(re.findall("XMAS", line))
    count += len(re.findall("SAMX", line))

    return count
    
def count_hor(data : list[str]) -> int:
    fwd_count = 0
    for line in data:
        fwd_count += xmas_search(line)
    return fwd_count

def count_vert(data : list[str]) -> int:
    vert_count = 0
    length : int= len(data[0])
    for i in range(length):
        vert_slice : str = ''
        for line in data:
            vert_slice += line[i]
        vert_count += xmas_search(vert_slice)
    return vert_count

def count_diag(data : list[str], direction : int = 1) -> int:
    diag_count : int = 0
    rows : int = len(data)
    cols : int = len(data[0])
    loop : int = rows + cols - 7
    row : int = rows - 4
    if direction > 0:
        col : int = 0
    else:
        col : int = cols - 1
    for _ in range(loop):
        line : str = ''
        index : int = 0
        while (
                (row + index < rows and col + index < cols) 
                and 
                (row + abs(index) < rows and col + index > -1) 
                ):
            line += data[row + abs(index)][col + index]
            index += direction
        diag_count += xmas_search(line)
        if row > 0:
            row -= 1
        else:
            col += direction
    return diag_count

def count_xmas(file_name : str) -> int:
    xmas_count : int = 0
    my_data : list[str] = get_data(file_name)
    xmas_count += count_hor(my_data)
    xmas_count += count_vert(my_data)
    xmas_count += count_diag(my_data, -1)
    xmas_count += count_diag(my_data, 1)
    #too high = 20, should be 18
    return xmas_count

def run(file_name):
    print(count_xmas(file_name))

if __name__ == "__main__":
    run("input4.txt")
