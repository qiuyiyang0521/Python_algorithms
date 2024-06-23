# 顺序查找
def linear_search(li, value):
    # 遍历列表
    for val in li:
        # 找到值
        if val == value:
            # 返回值
            return val
    # 如果没有找到返回None
    return None


# 二分查找
def binary_search(li: list, value):
    # 定义开头下标
    start = 0
    # 定义结尾下标
    end = len(li) - 1
    # 判断条件：只要候选区中没有数字就退出
    while end >= start:
        # 获取中间数的下标
        mid = (start + end) // 2
        # 如果中间数大于要查找的值,向左查找
        if li[mid] > value:
            end = mid - 1
        # 如果中间数小于要查找的值，向右查找
        if li[mid] < value:
            start = mid + 1
        # 如果中间值等于要查找的值，返回中间值
        if li[mid] == value:
            return mid

    # 如果没有找到返回None
    return None

li = [0,1,2,3,4,5,6]
print(binary_search(li,6))
