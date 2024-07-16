from random import shuffle, randint
from time import time
from heap_sort_review import heap_sort

li1 = list(range(1, 10001))
shuffle(li1)
li2 = []
for x in range(10000):
    li2.append(randint(1, 10000))
print(li1)
print(li2)

start_time = time()
li1 = heap_sort(li1)
end_time = time()
run_time = end_time - start_time
print("Run time: {}".format(run_time))
print(li1)

start_time = time()
li2 = heap_sort(li2)
end_time = time()
run_time = end_time - start_time
print("Run time: {}".format(run_time))
print(li2)

