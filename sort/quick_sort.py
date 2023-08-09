def quick_sort(data: list, right: int, left: int) -> list:
    """
    :param data: 需要排序的列表
    :param right: 最右边数值的下标
    :param left:  最左边数值的下标
    :return: 排序完成的列表
    """
    data = data
    if left < right:
        mid = partition(data, right, left)
        # 排序左半边部分
        data[left:mid - 1] = quick_sort(data, mid - 1, left)
        # 排序右半边部分
        data[mid + 1:right] = quick_sort(data, right, mid + 1)

    return data


def partition(data: list, right: int, left: int) -> int:
    pass
