from random import shuffle
from timer import timer


@timer
def select_sort_simple(lst):
    lst = lst  # 定义一个局部变量，以免影响全局变量
    sorted_lst = []
    for i in range(len(lst)):
        min_val = min(lst)
        sorted_lst.append(min_val)
        lst.remove(min_val)

    return sorted_lst


@timer
def select_sort(lst):
    for i in range(len(lst) - 1):
        min_loc = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_loc]:
                min_loc = j

        lst[i], lst[min_loc] = lst[min_loc], lst[i]

    return lst
