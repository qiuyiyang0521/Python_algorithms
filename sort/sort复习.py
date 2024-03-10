from random import randint


def select_sort(input_list):
    sorted_list = input_list
    # 遍历一遍需要排序的值
    for x in range(0, len(sorted_list) - 1):
        min_index = x
        # 遍历未排序区
        for y in range(x + 1, len(sorted_list)):
            # 如果未排序区的某一个值小于已知的最小值，那么更新下标
            if sorted_list[y] < sorted_list[min_index]:
                min_index = y
        # 把正在排序的值与未排序区最小值替换
        sorted_list[x], sorted_list[min_index] = sorted_list[min_index], sorted_list[x]

    # 输出排序后的列表
    return sorted_list


def bubble_sort(input_list):
    sorted_list = input_list
    # 确定排序区的范围
    for x in range(len(sorted_list) - 2, -1, -1):
        # 遍历一遍需要排序的值
        for y in range(0, x + 1):
            # 判断排序的值与下一个数的值哪一个大
            if sorted_list[y] > sorted_list[y + 1]:
                # 如果排序的值后一个数大，则交换两数位置
                sorted_list[y], sorted_list[y + 1] = sorted_list[y + 1], sorted_list[y]

    # 返回排序好的列表
    return sorted_list


def insert_sort(input_list):
    sorted_list = input_list
    # 遍历一遍需要排序的值的下标
    for sort_number_index in range(len(sorted_list)):
        tmp = sorted_list[sort_number_index]
        tmp_index = sort_number_index - 1
        # 向前找到合适的插入位置
        while tmp_index >= 0 and sorted_list[tmp_index] > tmp:
            # 把大于正在排序的值的数往后移
            sorted_list[tmp_index + 1] = sorted_list[tmp_index]
            tmp_index -= 1
        # 把正在排序的数放在合适的位置
        sorted_list[tmp_index + 1] = tmp

    # 返回排序好的列表
    return sorted_list
