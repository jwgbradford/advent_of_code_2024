''' count where both of the following are true:
1) The levels are either all increasing or all decreasing.
2) Any two adjacent levels differ by at least one and at most three.
'''

def read_file(file : str) -> str:
    with open(file) as my_file:
        return my_file.read()

def get_data(file : str) -> list[list[int]]:
    file_data : str = read_file(file)
    data_list : list[str] = file_data.split("\n")
    del data_list[-1]
    data_list_split : list[list[int]] = split_list(data_list)
    return data_list_split

def split_list(data : list[str]) -> list[list[int]]:
    for index, item in enumerate(data):
        sub_list : list[str]= item.split(" ")
        sub_list = str_to_int(sub_list)
        data[index] = sub_list
    return data

def str_to_int(data : list[str]) -> list[int]:
    for index, item in enumerate(data):
        data[index] = int(item)
    return data

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