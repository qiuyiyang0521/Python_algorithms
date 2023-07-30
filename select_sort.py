from random import randint
from cal_time import cal_time


@cal_time
def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)

    return li_new

@cal_time
def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j

        li[i], li[min_loc] = li[min_loc], li[i]

    return li


li = [randint(1, 1000) for x in range(10000)]
print(li)
li_new = select_sort(li)
print(li_new)
li_new_simple = select_sort_simple(li)
print(li_new_simple)

