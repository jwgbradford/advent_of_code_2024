'''
page ordering rules, one per line. 
The first rule, 47|53, means that if an update includes both page number 47 and page number 53, then page number 47 must be printed at some point before page number 53.

For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order.
'''

from aoc_common import read_file

def make_prt_order_list(data : str) -> list[list[int]]:
    prt_list = data.split("\n")
    del prt_list[-1]
    prt_list = [prt.split(",") for prt in prt_list]
    prt_list = [[int(page) for page in update] for update in prt_list]
    return prt_list

def make_rule_list(data : str) -> list[(int, int)]:
    rule_list = data.split("\n")
    rule_list = [rule.split("|") for rule in rule_list]
    rule_list = [(int(rule[0]), int(rule[1])) for rule in rule_list]
    return rule_list

def check_correct(rules, prt_order) -> list[list[int]]:
    wrong_pages : list = []
    for printing in prt_order:
        for index in range(len(printing) - 1):
            correct_order : bool = False
            for rule in rules:
                if (printing[index] == rule[0] 
                    and
                    printing[index + 1] == rule[1] 
                    ):
                    correct_order = True
            if not correct_order:
                break
        if not correct_order:
            wrong_pages.append(printing)
    return wrong_pages

def sort_pages(start_loc : int, update : list[int], rules : list[(int, int)]) -> list[int]:
    for index in range(start_loc, len(update) - 1):
        correct_order : bool = False
        for rule in rules:
            if (update[index] == rule[0] 
                and
                update[index + 1] == rule[1] 
                ):
                correct_order = True
        if not correct_order:
            update[index], update[index + 1] = update[index + 1], update[index]
            if index > 0:
                update = sort_pages(index - 1, update, rules)
            else:
                update = sort_pages(index, update, rules)
    return update

def reorder_pages(rules : list[(int, int)], wrong_order : list[int]) -> int:
    page_count : int = 0
    for printing in wrong_order:
        printing = sort_pages(0, printing, rules)
        page_count += printing[len(printing)//2]
    return page_count

def separate_data(file_name : str) -> None:
    my_data = read_file(file_name)
    rules, prt_order = my_data.split("\n\n")
    prt_order = make_prt_order_list(prt_order)
    rules = make_rule_list(rules)
    wrong_updates = check_correct(rules, prt_order)
    print(reorder_pages(rules, wrong_updates))

def run(file_name : str) -> None:
    separate_data(file_name)

if __name__ == "__main__":
    run("input5.txt")