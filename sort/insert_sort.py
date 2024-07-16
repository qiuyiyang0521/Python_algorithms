from random import shuffle
from timer import timer


@timer
def insert_sort(li):
    """
    插入排序算法

    :param li: 待排序的列表
    :return: 排序后的列表
    """
    for i in range(1, len(li)):  # 遍历列表索引
        tmp = li[i]  # 临时变量用于存储当前元素的值
        j = i - 1  # 设定一个索引变量，用于比较当前元素和之前元素的大小
        while j >= 0 and li[j] > tmp:  # 当索引大于等于0且当前元素比之前元素小
            li[j + 1] = li[j]  # 将之前元素的值放在当前元素的位置上
            j -= 1  # 减小索引变量的值
        li[j + 1] = tmp  # 将当前元素的值放在正确的位置上

    return li  # 返回排序后的列表


li = list(range(10000))
shuffle(li)
#
# li_insert_sort = insert_sort(li)
# print("插入排序:", li_insert_sort)
#
# li_select_sort_simple = select_sort_simple(li)
# print("选择排序简单版: ", li_select_sort_simple)
#
# li_select_sort = select_sort(li)
# print("选择排序: ", li_select_sort)
#
# li_bubble_sort = bubble_sort(li)
# print("冒泡排序: ", li_bubble_sort)




print(insert_sort(li))
