#!/usr/bin/env python3

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(lst):
    lst.extend([6, 7, 8])
    return lst

def remove_items_from_list(lst, items):
    for i in items:
        if i in lst:
            lst.remove(i)
    return lst

if __name__ == "__main__":
    print(add_item_to_list(my_list))
    print(remove_items_from_list(my_list, [1, 5, 6]))
