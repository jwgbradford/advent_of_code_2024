'''
supposed to find two MAS in the shape of an X

S.M.A.S.M

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
    count += len(re.findall("M.S.A.M.S", line))
    count += len(re.findall("S.M.A.S.M", line))
    count += len(re.findall("M.M.A.S.S", line))
    count += len(re.findall("S.S.A.M.M", line))
    return count

def chunk_grid(data : list[str]) -> int:
    chunk_count : int = 0
    line : str = ''
    for row in range(len(data) - 2):
        for col in range(len(data[0]) - 2):
            line = data[row][col:col+3] + data[row+1][col:col+3] + data[row+2][col:col+3]
            chunk_count += xmas_search(line)
    return chunk_count

def count_xmas(file_name : str) -> int:
    my_data : list[str] = get_data(file_name)
    return chunk_grid(my_data)

def run(file_name):
    print(count_xmas(file_name))

if __name__ == "__main__":
    run("input4.txt")
