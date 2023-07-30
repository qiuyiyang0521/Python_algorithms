from bubble_sort import *
from cal_time import *


@cal_time
def insert_sort(li):
    for i in range(1, len(li)):  # i:摸到的牌的下标
        tmp = li[i]
        j = i - 1
        while li[j] > tmp or j >= 0:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        return li


li = [5, 6, 9, 8, 7, 3, 2, 1, 4]
li_bubble_sort = bubble_sort(li)
print(li_bubble_sort)
li_insert_sort = insert_sort(li)
print(li_insert_sort)
