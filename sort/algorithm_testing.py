from random import randint
from time import time

import bubble_sort
import heap_sort_review
import insert_sort
import quick_sort_review
import select_sort
import sys

sys.setrecursionlimit(1000000)

def timer(func, *args, **kwargs):
    start_time = time()
    func(*args, **kwargs)
    end_time = time()

    return end_time - start_time


testing_list = [randint(0, 1000000) for _ in range(10000)]
print("Testing list:", testing_list)

print("-" * 600)

bubble_sort_list = testing_list
bubble_sort_run_time = timer(bubble_sort.bubble_sort, bubble_sort_list)
print("The result of bubble sort:", bubble_sort_list)
print("The run time of bubble sort:", bubble_sort_run_time)

print("-" * 600)

select_sort_list = testing_list
select_sort_run_time = (timer(select_sort.select_sort, select_sort_list))
print("The result of select sort:", select_sort_list)
print("The run time of select sort:", select_sort_run_time)

print("-" * 600)

insert_sort_list = testing_list
insert_sort_run_time = (timer(insert_sort.insert_sort, insert_sort_list))
print("The result of insert sort:", insert_sort_list)
print("The run time of insert sort:", insert_sort_run_time)

print("-" * 600)

quick_sort_list = testing_list
quick_sort_run_time = (timer(quick_sort_review.quick_sort, quick_sort_list, 0, len(quick_sort_list) - 1))
print("The result of quick sort:", quick_sort_list)
print("The run time of quick sort:", quick_sort_run_time)

print("-" * 600)

heap_sort_list = testing_list
heap_sort_run_time = (timer(heap_sort_review.heap_sort, heap_sort_list))
print("The result of heap sort:", heap_sort_list)
print("The run time of heap sort:", heap_sort_run_time)
