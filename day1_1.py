#imported old basic functions from 2022
def read_file(file : str) -> list:
    with open(file) as my_file:
        return my_file.read()

def get_data(file : str) -> list[list]:
    file_data = read_file(file)
    data_list = file_data.split("\n")
    data_list_split = split_list(data_list)
    return data_list_split

def split_list(data : list) -> list[list]:
    for index, item in enumerate(data):
        sub_list = item.split(" ")
        sub_list = clear_spaces(sub_list)
        data[index] = sub_list
    return data

def clear_spaces(data : list) -> list:
    temp_list = []
    temp_int = 0
    temp_dec = 1
    for item in data:
        if item == "" and temp_int > 0:
            temp_list.append(temp_int)
            temp_int = 0
            temp_dec = 1
        elif item == "" and temp_int == 0:
            pass
        else:
            temp_int += int(item) * temp_dec
            temp_dec *= 10
    temp_list.append(temp_int)
    return temp_list

def sort_lists(data : list[list]) -> list:
    list_1, list_2 = [], []
    for item in data:
        list_1.append(item[0])
        list_2.append(item[1])
    list_1.sort()
    list_2.sort()
    return list_1, list_2

def find_dist(data : list[list]) -> int:
    list_1, list_2 = sort_lists(data)
    dist = 0
    for i in range(len(list_1)):
        dist += abs(list_1[i] - list_2[i])
    return dist

my_data = get_data('test1.txt')
print(find_dist(my_data))