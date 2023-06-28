# -*- coding:utf-8 -*-

from random import randint


def linear_search(li, value):
    for index, val in enumerate(li):
        if val == value:
            return index
    else:
        return None


def search(li, value):
    li.sort()
    lens = len(li)
    start = 0
    mid = len(li) // 2
    end = len(li) - 1
    num = 1
    while num != 0 and 0 <= start < end <= lens - 1:
        if li[mid] > value:
            end = mid - 1
            mid = (start + end) // 2
        elif li[mid] < value:
            start = mid + 1
            mid = (start + end) // 2
        else:
            return mid
    else:
        return None


# 随机生成一组数
numbers = []
for x in range(100):
    numbers.append(x)

# 打印随机数组
for x in range(10):
    for y in range(10):
        print("%3d[%2d]" % (x * 10 + y, numbers[x * 10 + y]), end="")
    print("")

print(search(numbers, 56))
