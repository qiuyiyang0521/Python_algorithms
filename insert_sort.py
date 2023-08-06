from random import shuffle
from cal_time import cal_time
from bubble_sort import bubble_sort
from select_sort import select_sort, select_sort_simple


@cal_time
def insert_sort(li):
    for i in range(1, len(li)):  # i:摸到的牌的下标
        tmp = li[i]
        j = i - 1  # j:手里比较牌的下标
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp

    return li


li = list(range(3))
shuffle(li)

# li_insert_sort = insert_sort(li)
# print("插入排序:", li_insert_sort)

li_select_sort_simple = select_sort_simple(li)
print("选择排序简单版: ", li_select_sort_simple)

# li_select_sort = select_sort(li)
# print("选择排序: ", li_select_sort)
#
# li_bubble_sort = bubble_sort(li)
# print("冒泡排序: ", li_bubble_sort)
