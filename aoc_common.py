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