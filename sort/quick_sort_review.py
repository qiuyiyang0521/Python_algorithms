from random import shuffle


def swap(li: list, value1_index: int, value2_index: int) -> None:
    """
    交换列表中两个值
    :param li: 列表
    :param value1_index: 第一个值的索引
    :param value2_index: 第二个值的索引
    :return: 没有返回值
    """
    li[value1_index], li[value2_index] = li[value2_index], li[value1_index]


def partition(data: list, start: int, end: int) -> int:
    """
    快速排序中的分区函数
    :param data: 需要分区的列表
    :param start: 分区范围开始的索引
    :param end: 分区范围结束的所引
    :return: 返回基准值的下标
    """
    base_value = data[start]
    i, j = start, end

    while i < j:  # not i > 9
        while data[j] >= base_value and i < j:
            j -= 1
        while data[i] <= base_value and i < j:
            i += 1
        if i < j:
            swap(data, i, j)

    swap(data, start, i)

    return i  # 返回基准值的下标


def quick_sort(li: list, left: int, right: int) -> None:
    """
    快速排序
    :param li: 被排序的列表
    :return: 没有返回值
    """

    if left < right:
        base_index = partition(li, left, right)
        quick_sort(li, left, base_index - 1)
        quick_sort(li, base_index + 1, right)

if __name__ == '__main__':
    li = list(range(1, 21))
    shuffle(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
