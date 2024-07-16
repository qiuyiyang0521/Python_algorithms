def swap(li: list, value1_index: int, value2_index: int) -> None:
    """
    交换列表中两个值
    :param li: 列表
    :param value1_index: 第一个值的索引
    :param value2_index: 第二个值的索引
    :return: 没有返回值
    """
    li[value1_index], li[value2_index] = li[value2_index], li[value1_index]


def partition(data: list, start: int, end: int) -> None:
    """
    快速排序中的分区函数
    :param data: 需要分区的列表
    :param start: 分区范围开始的索引
    :param end: 分区范围结束的所引
    :return: 没有返回值
    """
    base_value = data[start]
    i, j = start, end

    while i < j:  # not i > 9
        while data[i] <= base_value and i < j:
            i += 1
        while data[j] >= base_value and i < j:
            j -= 1
        swap(data, i, j)

    else:
        # 此时i正确，即data[i]>base_value，而j=i，所以li[j-1]<base_value
        j -= 1  # 将j-1，使j符合条件
        swap(data, start, j)
