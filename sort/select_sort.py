def select_sort_simple(lst):
    sorted_lst = []
    for i in range(len(lst)):
        min_val = min(lst)
        sorted_lst.append(min_val)
        lst.remove(min_val)


def select_sort(lst):
    for i in range(len(lst) - 1):
        min_loc = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_loc]:
                min_loc = j

        lst[i], lst[min_loc] = lst[min_loc], lst[i]
