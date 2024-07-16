# -*- coding:utf-8 -*-
import timer
@cal_time
def linear_search(li, value):
    for index, val in enumerate(li):
        if val == value:
            return index
    else:
        return None


@cal_time
def binary_search(li, value):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == value:
            return mid
        elif li[mid] > value:
            right = mid -1
        else:
            left = mid + 1
    else:
        return None

# 随机生成一组数
numbers = []
for x in range(100000):
    numbers.append(x)
    print(x)

# 打印随机数组
# for x in range(10):
#     for y in range(10):
#         print("%3d[%2d]" % (x * 10 + y, numbers[x * 10 + y]), end="")
#     print("")

print(binary_search(numbers, 99999))
